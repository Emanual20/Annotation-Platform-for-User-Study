from flask import Flask, jsonify, request
from books import Book
import json
from settings import RSA_1024_PRIV_KEY, REQUSET_LISTS
import re
import rsa
import base64
import time
import random

def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin')
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization,Accept,Origin,Referer,User-Agent'
    response.headers['Access-Control-Allow-Credentials'] = 'true'
    return response


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.after_request(after_request)


# 检查是否含有特殊字符
def is_string_validate(str):
    sub_str = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])","",str)
    if len(str) == len(sub_str):
        # 说明合法
        return False
    else:
        # 不合法
        return True


# 解密函数
def get_secret_key(cryptdata):
    # print("cryptdata = ", cryptdata)
    privkey = rsa.PrivateKey.load_pkcs1(RSA_1024_PRIV_KEY)
    msg = rsa.decrypt(base64.b64decode(cryptdata), privkey)
    # msg = rsa.decrypt(base64.b64decode(cryptdata), RSA_1024_PRIV_KEY)
    # print("str(msg) = ", msg)
    # print("str(msg) = ", msg.decode().split(":")[1])
    try:
        result = {
            "request_time":msg.decode().split(":")[0],  # 防止爬虫利用这个反复爬取
            "request_url":msg.decode().split(":")[1],
            "request_infos": msg.decode().split(":")[2]
        }
    except:
        result = {
            "request_time":'',  # 防止爬虫利用这个反复爬取
            "request_url":'',
            "request_infos": ''
        }
    # print("result = ", result)
    return result


@app.errorhandler(404)
def handler_404_error(err):
    resData = {
        "resCode": 404, # 非0即错误 1
        "data": [],# 数据位置，一般为数组
        "message": err
    }
    return jsonify(resData)


@app.route('/user_stuinfos', methods=['GET', 'POST'])
def get_specific_stuinfos(stu_uuid):
    book = Book()
    sql_data = book.get_stu_infos(stu_uuid)
    print(stu_uuid, " request specific stuinfos")
    print(sql_data)
    resData = {
        "resCode": 0, 
        "data": sql_data,
        "message": "request successful" 
    }
    return jsonify(resData)


@app.route('/get_stuinfos', methods=['GET', 'POST'])
def get_all_stuinfos():
    book = Book()
    res = book.get_allstu_infos()
    resData = {
        "resCode": 0,
        "data": res,
        "message": 'Successful get all student infos'
    }
    return jsonify(resData)


@app.route('/fetchdisplaylist', methods=['GET', 'POST'])
def get_displaylist():
    data = json.loads(request.get_data(as_text=True))
    book = Book()
    if 'username' not in data.keys() or 'displaynum' not in data.keys():
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'No username in post params'
        }
        return jsonify(resData)
    nusername = data['username']
    displaynum = data['displaynum']
    if displaynum >= 10:
        displaynum = 10
    else:
        displaynum = 5
    ret_data = book.fetch_displaylist(nusername, displaynum)
    resData = {
        "resCode": 0,
        "data": [ret_data[0], ret_data[1], ret_data[2]],
        "message": 'Successful require display list'
    }
    return jsonify(resData)


@app.route('/fetchdisplaycombinationlist', methods=['GET', 'POST'])
def get_displaycombinationlist():
    data = json.loads(request.get_data(as_text=True))
    book = Book()
    if 'username' not in data.keys() or 'displaynum' not in data.keys():
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'No username in post params'
        }
        return jsonify(resData)
    nusername = data['username']
    displaynum = data['displaynum']
    if displaynum >= 10:
        displaynum = 10
    else:
        displaynum = 5
    ret_data = book.fetch_displaylist_combination(nusername, displaynum)
    print(nusername, " is noting: ", ret_data[2], " ranking policy for property usefulness..")
    resData = {
        "resCode": 0,
        "data": [ret_data[0], ret_data[1], ret_data[2]],
        "message": 'Successful require display list'
    }
    return jsonify(resData)


@app.route('/fetchdisplayfidelitylist', methods=['GET', 'POST'])
def get_displayfidelitylist():
    data = json.loads(request.get_data(as_text=True))
    book = Book()
    if 'username' not in data.keys():
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'No username in post params'
        }
        return jsonify(resData)
    nusername = data['username']
    displaynum = 5
    ret_data = book.fetch_displaylist_fidelity(nusername, displaynum)
    print(nusername, " is noting: ", ret_data[2], " ranking policy for property fidelity..")
    resData = {
        "resCode": 0,
        "data": [ret_data[0], ret_data[1], ret_data[2]],
        "message": 'Successful require display list'
    }
    return jsonify(resData)


@app.route('/fetchdisplaynewlist', methods=['GET', 'POST'])
def get_displaynewlist():
    data = json.loads(request.get_data(as_text=True))
    book = Book()
    if 'username' not in data.keys():
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'No username in post params'
        }
        return jsonify(resData)
    nusername = data['username']
    displaynum = 5
    ret_data = book.fetch_displaylist_new(nusername, displaynum)
    ret_data_another = book.fetch_displaylist_new(nusername, displaynum)
    print(nusername, " is noting: ", ret_data[1], " ranking policy for Tintarev's 7 goals..")
    resData = {
        "resCode": 0,
        "data": [ret_data[0] + ret_data_another[0], ret_data[1] + ';;' + ret_data_another[1]],
        "message": 'Successful require display list'
    }
    return jsonify(resData)


@app.route('/submitclicklog', methods=['GET', 'POST'])
def insert_clicklog():
    data = json.loads(request.get_data(as_text=True))
    book = Book()
    if 'infos' not in data.keys() or 'username' not in data.keys():
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'No username or infos in post params'
        }
        return jsonify(resData)
    nusername = data['username']
    infos = data['infos']
    retCode = book.insert_clicklog(nusername, infos)
    print("inserting clicklog for user ", nusername)
    resData = {
        "resCode": 0,
        "data": retCode,
        "message": 'Update user clicklog successfully'
    }
    return jsonify(resData)


@app.route('/registernewuser', methods=['GET', 'POST'])
def register_newuser():
    data = json.loads(request.get_data(as_text=True))
    book = Book()
    if 'emailaddress' not in data.keys():
        print("There is no emailaddress in data")
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no emailaddress'
        }
        return jsonify(resData)

    emailaddress = data['emailaddress']
    res_matchusername = book.get_matchemail(emailaddress)
    if res_matchusername is not None:
        print("In register_newuser: Email already exists ", emailaddress)
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'Email already exists ' + emailaddress
        }
        return jsonify(resData)

    if 'password' not in data.keys() or 'invitation_code' not in data.keys():
        print("There is no password or invitation_code in data")
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no password or invitation_code'
        }
        return jsonify(resData)
    password = data['password']
    print(data)
    attrs = data['attrs']
    invitation_code = data['invitation_code']
    print(emailaddress, " registering an new account, using password: ", password, " ,using invitation_code: ", invitation_code)
    if invitation_code == "defaultstr":
        retCode = book.insert_stuifonewuser(emailaddress, password, attrs)
    else:
        retCode = 1
    resData = {
        "resCode": retCode,
        "data": [],
        "message": 'Successfully register a new account.'
    }
    return jsonify(resData)


def is_allow_domain_time(request_time, request_url):
    if(int(time.time() * 1000) - int(request_time) > 300000):
        return True
    if request_url not in REQUSET_LISTS:
        # 只有指定的域名才能访问
        # resData = {
        #     "resCode": 1, # 非0即错误 1
        #     "data": [],# 数据位置，一般为数组
        #     "message": '你猜，你使劲猜'
        # }
        # return jsonify(resData)
        return True
    return False


@app.route('/checknamepw', methods=['GET', 'POST'])
def check_namepw():
    # data = request.get_json()
    data = json.loads(request.get_data(as_text=True))
    if 'username' not in data.keys():
        print('no username in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no username'
        }
        return jsonify(resData)
    if 'password' not in data.keys():
        print('no password in data, fxxk!')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because no password'
        }
        return jsonify(resData)
    book = Book()
    nusername = data['username']
    npassword = data['password']
    res_nuserinfo = book.get_user_password(nusername, npassword)
    print(nusername, "request login", ", matching record: ", res_nuserinfo)
    flag = res_nuserinfo is None
    resData = {
        "resCode": int(flag),
        "data": [res_nuserinfo],
        "message": "Password verified finished."
    }
    return jsonify(resData)


@app.route('/updatepassword', methods=['GET', 'POST'])
def update_password():
    data = json.loads(request.get_data(as_text=True))
    if 'username' not in data.keys() or 'npassword' not in data.keys():
        print('Missing username or npassword in data')
        resData = {
            "resCode": 1,
            "data": [],
            "message": 'failed because missing username or npassword in data'
        }
        return jsonify(resData)
    username = data['username']
    new_password = data['npassword']
    book = Book()
    RetCode = book.update_userpassword(username, new_password)
    print(username, " request update password, new password: ", new_password)
    resData = {
        "resCode": 0,
        "data": [],
        "message": 'successful update your password, please login again..!'
    }
    return jsonify(resData)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    book = Book()
    arrData = "Please do not hack this database."
    return jsonify(arrData)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1943, debug=True)
    # app.run(host='0.0.0.0', port=8889, debug=True)
    # from waitress import serve
    # serve(app, host='0.0.0.0', port=8889)