import datetime
import random
import copy
import numpy as npy
from pymysql import connect
from pymysql.cursors import DictCursor
from pymysql.converters import escape_string
from scipy.stats import kendalltau
from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

DISPLAY_MAXIMUM_COUNT = 5

class Book(object):
    def __init__(self):  # 创建对象同时要执行的代码
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8'
        )
        self.cursor=self.conn.cursor(DictCursor)  # 这个可以让他返回字典的形式

    def __del__(self):  # 释放对象同时要执行的代码
        self.cursor.close()
        self.conn.close()

    def get_stu_infos_limit(self):
        sql = 'SELECT * FROM user_info WHERE user_permission = 3;'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    # 查询和当前请求邮箱(登陆主键)相同的记录
    def get_matchemail(self, stu_name):
        sql = "select * from user_info where user_name = '{}'".format(stu_name)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查询当前用户信息
    def get_stu_infos(self, stu_uuid):
        sql = "select * from user_info where user_uuid = '{}';".format(stu_uuid)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查询所有学生信息
    def get_allstu_infos(self):
        sql = "SELECT ui.user_uuid, ui.user_name FROM user_info as ui WHERE ui.user_permission = 3;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 查询当前用户名密码是否正确
    def get_user_password(self, username, password):
        sql = "select user_uuid, user_name, user_idcid from user_info where user_name = '{}' and user_idcid = '{}';".format(username, password)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查询学生姓名和uuid对应的json
    def get_uuid2stuname(self):
        sql = "SELECT user_uuid, user_name FROM user_info;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 修改用户密码
    def update_userpassword(self, emailaddress, stu_npassword):
        sql = "UPDATE user_info SET user_idcid = '{}' WHERE user_name = '{}';".format(stu_npassword, emailaddress)
        self.cursor.execute(sql)
        return self.conn.commit()

    # 注册新用户信息
    def insert_stuifonewuser(self, emailaddress, stu_password, stu_attrs):
        stu_attrs = escape_string(str(stu_attrs))
        sql = "INSERT INTO user_info (user_name, user_idcid, user_attrs) VALUES ('{}', '{}', '{}')".format(emailaddress, stu_password, stu_attrs)
        self.cursor.execute(sql)
        self.conn.commit()
        return 0

    # 修改所有学生查看权限：
    def update_allpermission(self, stu_uuid, nvalue, params):
        for param in params:
            stu_touuid = param['stu_uuid']
            sql = "UPDATE user_masterpermission as sium SET sium.user_permissiontype = {} WHERE " \
                  "sium.user_fmuuid = '{}' and sium.user_touuid = '{}';".format(nvalue, stu_touuid, stu_uuid)
            self.cursor.execute(sql)
            self.conn.commit()
        return 1

    # 随机获取一个待展示的历史列表，再根据获取的这个历史列表的商家候选解释集随机获取解释
    def fetch_displaylist(self, stu_uuid, display_num):
        sql = "SELECT * FROM traceuuid_info WHERE log_length >= '{}' ORDER BY RAND() LIMIT 1;".format(display_num)
        self.cursor.execute(sql)
        data_res = self.cursor.fetchone()
        # uuid_res = data_res['user_uuid']
        trace_res = data_res['user_trace_id']

        # 从history click log中随机选取
        sql = "SELECT * FROM log_for_display WHERE log_trace_id = '{}' order by log_poi_position LIMIT {};".format(trace_res, display_num)
        history_explanations_cnt_list = []
        self.cursor.execute(sql)
        data_for_display_history = self.cursor.fetchall()
        for item in data_for_display_history:
            item['log_discounts'] = item['log_discounts'].split(',')
            explanations_for_display_history = []
            eaches_for_explanations_history = item['log_explanations'].split(';;;')
            cnt_tmp = 0
            for each in eaches_for_explanations_history:
                try:
                    tmp_dict = eval(each)
                    explanations_for_display_history.append(tmp_dict['text'])
                    cnt_tmp += 1
                except SyntaxError or NameError:
                    print("Catch SyntaxError or NameError in fetch_displaylist function")
                    continue
            history_explanations_cnt_list.append(cnt_tmp)
            item['log_explanations'] = explanations_for_display_history

        # 从random log中随机选取
        sql = "SELECT * FROM log_for_display_random WHERE log_trace_id = '{}' order by log_poi_position LIMIT {};".format(trace_res, display_num)
        self.cursor.execute(sql)
        data_for_display_random = self.cursor.fetchall()
        idx = 0
        for item in data_for_display_random:
            item['log_discounts'] = item['log_discounts'].split(',')
            # explanations_for_display_random = []
            explanations_for_display_random = {}
            eaches_for_explanations_random = item['log_explanations'].split(';;;')
            for each in eaches_for_explanations_random:
                try:
                    tmp_dict = eval(each)
                    ntype = tmp_dict['type']
                    ntext = tmp_dict['text']
                    # explanations_for_display_random.append(ntext)
                    if ntype not in explanations_for_display_random.keys():
                        explanations_for_display_random[ntype] = [ntext]
                    else:
                        explanations_for_display_random[ntype].append(ntext)
                except SyntaxError:
                    continue
            # /* completely random by text */
            # selected_explanations_for_display_random = npy.random.choice(explanations_for_display_random, size=min(len(explanations_for_display_random), 3),replace=False)
            # item['log_explanations'] = list(selected_explanations_for_display_random)

            # /* first random by type, then for each random selected type random by text */
            selected_explanations_for_display_random = npy.random.choice(list(explanations_for_display_random.keys()), size=min(len(list(explanations_for_display_random.keys())), min(4, history_explanations_cnt_list[idx])), replace=False)
            selected_explanations_for_display_random = list(selected_explanations_for_display_random)
            selected_list_tmp = []
            for each in selected_explanations_for_display_random:
                tmp = explanations_for_display_random[each]
                random_item_tmp = npy.random.choice(tmp, size=1, replace=False)
                selected_list_tmp.append(list(random_item_tmp)[0])
            item['log_explanations'] = selected_list_tmp
            idx += 1

        # 随机打乱两个list的顺序并写入description中
        description = ["history", "random"]
        npy.random.seed()
        rand_seed1 = npy.random.rand()
        npy.random.seed()
        rand_seed2 = npy.random.rand()
        if rand_seed1 > rand_seed2:
            description[0], description[1] = description[1], description[0]
            data_for_display_history, data_for_display_random = data_for_display_random, data_for_display_history
        description = ":-:".join(description)

        return [data_for_display_history, data_for_display_random, description]

    # 从log_for_display_combination表中任意获取两种（其中一种一定是bper），用来评价usefulness
    def fetch_displaylist_combination(self, stu_uuid, display_num):
        DISPLAY_EXPLANATION_NUM = 1
        sql = "SELECT DISTINCT uuid, trace_id FROM (SELECT uuid, trace_id, count(*) as log_length FROM " \
              "log_for_display_combination WHERE is_nearby = 1 GROUP BY uuid, trace_id) as tab WHERE log_length >= {} " \
              "ORDER BY RAND() LIMIT 1;".format(display_num)
        self.cursor.execute(sql)
        data_res = self.cursor.fetchone()
        uuid = data_res['uuid']
        traceid = data_res['trace_id']

        policy_names = ["random", "online", "lime", "proxy_model"]
        policy_names_in_db = {"random": "random_list", "online": "online_selected_tag_list", "bper": "bper_list", "lime": "lime_list", "proxy_model": "proxy_list"}
        selected_policy = list(npy.random.choice(policy_names, size=1, replace=False))
        policy_left, policy_right = selected_policy[0], "bper"
        if npy.random.rand() > npy.random.rand():
            policy_left, policy_right = policy_right, policy_left

        sql = "SELECT * FROM log_for_display_combination WHERE trace_id = '{}' and is_nearby = 1 order by log_poi_position LIMIT {};".format(traceid, display_num)
        self.cursor.execute(sql)
        data_res = self.cursor.fetchall()
        left_policy_data = copy.deepcopy(data_res)
        right_policy_data = copy.deepcopy(data_res)
        description = policy_left + ":-:" + policy_right

        for each in left_policy_data:
            left_display_explanations_list = each[policy_names_in_db[policy_left]].split(';')
            if policy_left != "random":
                left_display_explanations_list = left_display_explanations_list[0:min(len(left_display_explanations_list), DISPLAY_EXPLANATION_NUM)]
            else:
                left_display_explanations_list = list(npy.random.choice(left_display_explanations_list, size=min(len(left_display_explanations_list), DISPLAY_EXPLANATION_NUM)))
            each["log_explanations"] = left_display_explanations_list
        for each in right_policy_data:
            right_display_explanations_list = each[policy_names_in_db[policy_right]].split(';')
            if policy_right != "random":
                right_display_explanations_list = right_display_explanations_list[0:min(len(right_display_explanations_list), DISPLAY_EXPLANATION_NUM)]
            else:
                right_display_explanations_list = list(npy.random.choice(right_display_explanations_list, size=min(len(right_display_explanations_list), DISPLAY_EXPLANATION_NUM)))
            each["log_explanations"] = right_display_explanations_list
        # print(data_res[0][policy_names_in_db[policy_left]], data_res[0][policy_names_in_db[policy_right]])
        # print(left_policy_data[0]["log_explanations"], right_policy_data[0]["log_explanations"])
        return [left_policy_data, right_policy_data, description]

    # 从log_for_display_combination表中随机获取一个online列表和它的lime解释，再返回一个随机打乱顺序的list，用来评价fidelity
    def fetch_displaylist_fidelity(self, stu_uuid, display_num):
        DISPLAY_EXPLANATION_NUM = 1
        sql = "SELECT DISTINCT uuid, trace_id FROM (SELECT uuid, trace_id, count(*) as log_length FROM " \
              "log_for_display_combination WHERE is_nearby = 1 GROUP BY uuid, trace_id) as tab WHERE log_length >= {} " \
              "ORDER BY RAND() LIMIT 1;".format(display_num)
        self.cursor.execute(sql)
        data_res = self.cursor.fetchone()
        uuid = data_res['uuid']
        traceid = data_res['trace_id']

        policy_names = ["random", "online", "bper", "lime", "proxy_model"]
        policy_names_in_db = {"random": "random_list", "online": "online_selected_tag_list", "bper": "bper_list", "lime": "lime_list", "proxy_model": "proxy_list"}
        selected_policy_name = list(npy.random.choice(policy_names, size=1, replace=False))[0]
        policy_col = policy_names_in_db[selected_policy_name]
        policy_left = selected_policy_name + "_" + "onlinelogseq"
        policy_right = selected_policy_name + "_" + "randomseq"

        sql = "SELECT * FROM log_for_display_combination WHERE trace_id = '{}' and is_nearby = 1 order by log_poi_position LIMIT {};".format(traceid, display_num)
        self.cursor.execute(sql)
        data_res = self.cursor.fetchall()
        list_len = len(data_res)
        selected_list = npy.floor(npy.multiply([0.2, 0.4, 0.6, 0.8, 1], list_len)) - 1
        left_policy_data = []
        for each in selected_list:
            left_policy_data.append(data_res[int(each)])
        for each in left_policy_data:
            explanation_list = each[policy_col].split(";")
            if selected_policy_name != "random":
                each["log_explanations"] = explanation_list[0:min(len(explanation_list), DISPLAY_EXPLANATION_NUM)]
            else:
                each["log_explanations"] = list(npy.random.choice(explanation_list, size=min(len(explanation_list), DISPLAY_EXPLANATION_NUM)))
        right_policy_data = copy.deepcopy(left_policy_data)
        right_policy_data = list(npy.random.choice(right_policy_data, size=len(right_policy_data), replace=False))
        left_exp_data = []
        for each in left_policy_data:
            left_exp_data.append(each['log_explanations'])
        right_exp_data = []
        for each in right_policy_data:
            right_exp_data.append(each['log_explanations'])
        while kendalltau(left_exp_data, right_exp_data).correlation > 0:
            right_policy_data = list(npy.random.choice(right_policy_data, size=len(right_policy_data), replace=False))
            left_exp_data = []
            for each in left_policy_data:
                left_exp_data.append(each['log_explanations'])
            right_exp_data = []
            for each in right_policy_data:
                right_exp_data.append(each['log_explanations'])

        if npy.random.rand() > npy.random.rand():
            left_policy_data, right_policy_data = right_policy_data, left_policy_data
            policy_left, policy_right = policy_right, policy_left
        description = policy_left + ":-:" + policy_right
        # print(left_policy_data, right_policy_data, description)
        return [left_policy_data, right_policy_data, description]

    # 2022-10-06 update
    # 从 filtered_processed_data_20221004 表中随机获取一个用户的20个impression ranking list, 分别从4个ranking_policy中选择五个ranking list
    def fetch_displaylist_new(self, stu_uuid, display_num):
        SCENE_NUM_IN_AN_ROUND = 5
        DISPLAY_EXPLANATION_NUM = 1
        sql = "SELECT uuid, count(*) as candidate_len FROM ( SELECT uuid, trace_id FROM filtered_processed_data_20221004 " \
              "GROUP BY uuid, trace_id ) as tab1 GROUP BY uuid HAVING count(*) >= {}; ".format(SCENE_NUM_IN_AN_ROUND)
        self.cursor.execute(sql)
        # data_res is a list, each element in list is a dict,
        # key "uuid" for uuid,
        # key "candidate_len" for length of candidate list for specific user
        data_res = self.cursor.fetchall()
        selected_user = list(npy.random.choice(data_res, size=1))[0]
        selected_user = selected_user['uuid']
        sql = "SELECT DISTINCT trace_id FROM filtered_processed_data_20221004 WHERE uuid = '{}';".format(selected_user)
        self.cursor.execute(sql)
        data_res = self.cursor.fetchall()
        data_res = [int(x['trace_id']) for x in data_res]
        # print(data_res)
        selected_traceid = list(npy.random.choice(data_res, size=SCENE_NUM_IN_AN_ROUND, replace=False))
        selected_traceid.sort()
        print(selected_traceid)
        candidate_datas = []
        for each in selected_traceid:
            sql = "SELECT * FROM filtered_processed_data_20221004 WHERE trace_id = '{}' and is_nearby = 1 order by log_poi_position LIMIT {};".format(each, display_num)
            self.cursor.execute(sql)
            now_data = self.cursor.fetchall()
            candidate_datas.append(now_data)

        policy_names = ["random", "bper", "lime", "proxy_model"]
        policy_names_in_db = {"random": "random_list", "bper": "bper_list", "lime": "lime_list", "proxy_model": "proxy_list"}

        policy_seq = list(npy.random.choice(policy_names, size=len(policy_names), replace=False))
        ret = []
        for policy_now in policy_seq:
            for each in candidate_datas:
                for each_poi in each:
                    explanations_res = each_poi[policy_names_in_db[policy_now]]
                    explanations_res = explanations_res.split(';')
                    if policy_now == "random":
                        candidate_tags = list(npy.random.choice(explanations_res, size=min(DISPLAY_EXPLANATION_NUM, len(explanations_res)), replace=False))
                    else:
                        candidate_tags = explanations_res[0: min(DISPLAY_EXPLANATION_NUM, len(explanations_res))]
                    each_poi['log_explanations'] = candidate_tags
                ret.append(each)
        description = ";;".join(policy_seq)
        return [ret, description]

    # 将用户的clicklog写回数据库里
    def insert_clicklog(self, nusername, infos):
        sql = "SELECT user_uuid, user_name FROM user_info WHERE user_name = '{}';".format(nusername)
        self.cursor.execute(sql)
        user_uuid = self.cursor.fetchone()['user_uuid']
        try:
            nlist_leftpolicy = escape_string(str(infos['nlist_leftpolicy']))
        except KeyError:
            nlist_leftpolicy = []
        try:
            nlist_rightpolicy = escape_string(str(infos['nlist_rightpolicy']))
        except KeyError:
            nlist_rightpolicy = []
        # leftpolicy_score = infos['leftpolicy_score']
        # rightpolicy_score = infos['rightpolicy_score']
        # certainty_degree = infos['certainty_degree']
        # diversity_degree = infos['diversity_degree']
        try:
            attrs = escape_string(str(infos['attrs']))
        except KeyError:
            attrs = ""
        # print(infos)
        try:
            description = infos['description']
        except KeyError:
            description = ""
        sql = "INSERT INTO user_clicklog (user_uuid, display_list_left, display_list_right, click_timestamp, scene_type, attrs) VALUES (" \
              "'{}', '{}', '{}', now(), '{}', '{}');".format(user_uuid, nlist_leftpolicy, nlist_rightpolicy, description, attrs)
        self.cursor.execute(sql)
        return self.conn.commit()

    def initialize_traceuuid_info(self):
        sql = "TRUNCATE traceuuid_info;"
        self.cursor.execute(sql)
        self.conn.commit()
        sql = "SELECT tab1.log_trace_id, GREATEST(tab1.cnt, tab2.cnt) as cnt FROM (SELECT log_trace_id, count(*) as " \
              "cnt FROM log_for_display GROUP BY log_trace_id) tab1 INNER JOIN (SELECT log_trace_id, count(*) as cnt " \
              "FROM log_for_display_random GROUP BY log_trace_id) tab2 ON tab1.log_trace_id = tab2.log_trace_id"
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        for each in datas:
            trace_id = each['log_trace_id']
            cnt = each['cnt']
            sql = "INSERT INTO traceuuid_info (user_trace_id, log_length) VALUES ('{}', '{}');".format(trace_id, cnt)
            self.cursor.execute(sql)
            self.conn.commit()

    def calc_average_displaylen(self):
        sql = "SELECT * FROM log_for_display_random;"
        self.cursor.execute(sql)
        datas = self.cursor.fetchall()
        tmp_lst = []
        tmp_typelst = []
        for each in datas:
            explanations = each['log_explanations'].split(';;;')
            tmp_st = set()
            for explanation in explanations:
                try:
                    explanation = eval(explanation)
                except:
                    continue
                tmp_st.add(explanation['type'])
            tmp_lst.append(len(explanations))
            tmp_typelst.append(len(tmp_st))
        print(npy.average(tmp_lst), len(tmp_lst))
        print(npy.average(tmp_typelst), len(tmp_typelst))

# book = Book()
# book.fetch_displaylist_new(stu_uuid=111, display_num=5)
# book.calc_average_displaylen()
# book.initialize_traceuuid_info()
