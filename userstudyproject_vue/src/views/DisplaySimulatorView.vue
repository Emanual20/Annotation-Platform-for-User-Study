<template>
  <div class="displaysimulator">
    <Header />

    <div class="ifloginview" v-if="$store.state.user.is_login">
        <br>
        <h2 style="text-align: center;">操作示例：Which is better?</h2>
        <br>

        <div class="choosedisplaynum_then">
            <div class="container">
            <div class="row" style="text-align: center;">
                <div class="col">
                <h3 style="text-align: center;"> Scene {{ this.displaytimes }} </h3>
                </div>
            </div>
            <div class="row">
                <div class="col">
                <h4 style="text-align: center;">Group1</h4>
                </div>
                <div class="col-1"></div>
                <div class="col">
                <h4 style="text-align: center;">Group2</h4>
                </div>
                </div>
            </div>

            <div class="container">
            <div class="row">
                <div class="col">
                <div class="container">
                    <div class="row">
                    <div v-for="(niter, index) in display_data.left_list" :key="index">
                        <div class="card text-center" style="width: 30rem; margin-bottom: 5px;">
                            <div class="card-body">
                                <!-- first row -->
                                <div class="row">
                                    <div class="col-3" >
                                        <img src="../assets/shenquan.png" width="40" height="22" align="left" />
                                    </div>
                                    <div class="col" style="text-align: left;">
                                        <b> {{ niter['log_poi_name'] }} </b>
                                    </div>
                                </div>
                                <!-- second row -->
                                <div class="row">
                                    <div class="col-3" style="text-align: left; color:#fe5d0d;">
                                        <b> {{ niter['log_dianping_point'] }}分 </b>
                                    </div>
                                    <div class="col" style="text-align: left; color:#8b898a">
                                        {{ niter['log_monthly_sale'] }} {{ niter['log_cost_eachperson'] }}
                                    </div>
                                    <div class="col-3" style="text-align: center;">
                                        <div class="card">
                                            美团专送
                                        </div>
                                    </div>

                                </div>
                                <!-- third row -->
                                <div class="row">
                                    <div class="col-3" style="text-align: left; color:#8b898a">
                                        {{ niter['log_minimal_delivery'] }}
                                    </div>
                                    <div class="col-3" style="text-align: left; color:#8b898a">
                                        {{ niter['log_cost_delivery'] }}
                                    </div>
                                    <div class="col" style="text-align: right; color:#8b898a">
                                        {{ niter['log_minutes_delivery'] }} {{ niter['log_distance_delivery'] }}
                                    </div>
                                </div>
                                <!-- fourth row, explanation row-->
                                <div class="row" style="text-align:left">
                                    <div v-for="(explanation, index) in niter['log_explanations']" :key="index">
                                        <div class="col">
                                            <div class="card border-white">
                                                <div class="card-body text-dark single-explanation" style="text-align: center; vertical-align: center;">
                                                    <p class="card-text text-dark">
                                                    {{ explanation }}
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- fifth row, discount-->
                                <!-- <div class="row" style="text-align: left;">
                                    <div v-for="(discount, index) in niter['log_discounts']" :key="index">
                                        <div class="col">
                                            <div class="card border-danger" >
                                                <div class="card-body single-discount" style="text-align: center; vertical-align: center;">
                                                    {{ discount }}
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div> -->

                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>

                <div class="col-1">
                </div>
                
                <div class="col">
                <div class="container">
                    <div class="row">
                    <div v-for="(niter, index) in display_data.right_list" :key="index">
                        <div class="card text-center" style="width: 30rem; margin-bottom: 5px;">
                            <div class="card-body">
                                <!-- first row -->
                                <div class="row">
                                    <div class="col-3" >
                                        <img src="../assets/shenquan.png" width="40" height="22" align="left" />
                                    </div>
                                    <div class="col" style="text-align: left;">
                                        <b> {{ niter['log_poi_name'] }} </b>
                                    </div>
                                </div>
                                <!-- second row -->
                                <div class="row">
                                    <div class="col-3" style="text-align: left; color:#fe5d0d;">
                                        <b> {{ niter['log_dianping_point'] }}分 </b>
                                    </div>
                                    <div class="col" style="text-align: left; color:#8b898a">
                                        {{ niter['log_monthly_sale'] }} {{ niter['log_cost_eachperson'] }}
                                    </div>
                                    <div class="col-3" style="text-align: center;">
                                        <div class="card">
                                            美团专送
                                        </div>
                                    </div>

                                </div>
                                <!-- third row -->
                                <div class="row">
                                    <div class="col-3" style="text-align: left; color:#8b898a">
                                        {{ niter['log_minimal_delivery'] }}
                                    </div>
                                    <div class="col-3" style="text-align: left; color:#8b898a">
                                        {{ niter['log_cost_delivery'] }}
                                    </div>
                                    <div class="col" style="text-align: right; color:#8b898a">
                                        {{ niter['log_minutes_delivery'] }} {{ niter['log_distance_delivery'] }}
                                    </div>
                                </div>
                                <!-- fourth row, explanation row-->
                                <div class="row" style="text-align:left">
                                    <div v-for="(explanation, index) in niter['log_explanations']" :key="index">
                                        <div class="col">
                                            <div class="card border-white">
                                                <div class="card-body text-dark single-explanation" style="text-align: center; vertical-align: center;">
                                                    {{ explanation }}
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <!-- fifth row, discount
                                <div class="row" style="text-align: left;">
                                    <div v-for="(discount, index) in niter['log_discounts']" :key="index">
                                        <div class="col">
                                            <div class="card border-danger" >
                                                <div class="card-body single-discount" style="text-align: center; vertical-align: center;">
                                                    <div class="text-red"> {{ discount }} </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div> -->

                            </div>
                        </div>
                    </div>
                    </div>
                </div>
                </div>
            </div>
            </div>
            <br><br>
            
            <div class="container">
            <h5>1. 如果需要您给左边列表推荐解释的满意程度按1-5分打分，您的选择是？</h5>
            <select id="leftpolicy_score" v-model="leftpolicy_score" class="form-select">
                <option value="1" selected>1分 我非常不满意</option>
                <option value="2">2分</option>
                <option value="3">3分</option>
                <option value="4">4分</option>
                <option value="5">5分 我非常满意</option>
            </select><br>

            <h5>2. 如果需要您给右边列表推荐解释的满意程度按1-5分打分，您的选择是？</h5>
            <select id="rightpolicy_score" v-model="rightpolicy_score" class="form-select">
                <option value="1" selected>1分 我非常不满意</option>
                <option value="2">2分</option>
                <option value="3">3分</option>
                <option value="4">4分</option>
                <option value="5">5分 我非常满意</option>
            </select><br>

            <h5>3. 请问您做出上两个问题决策的确定程度如何，按1-5分打分？</h5>
            <select id="certainty_degree" v-model="certainty_degree" class="form-select">
                <option value="1" selected>1分，我非常不确定我的判断</option>
                <option value="2">2分</option>
                <option value="3">3分</option>
                <option value="4">4分</option>
                <option value="5">5分，我非常确定我的判断</option>
            </select><br>

            <h5>4. 如果需要您为上述两种推荐解释展出策略的差异度按1-5分打分，您的选择是？</h5>
            <select id="diversity_degree" v-model="diversity_degree" class="form-select">
                <option value="1" selected>1分，两个列表无法让我感受出明显差异</option>
                <option value="2">2分</option>
                <option value="3">3分</option>
                <option value="4">4分</option>
                <option value="5">5分，两个列表能让我感受出明显差异</option>
            </select><br>

            <div class="col" style="text-align:center;">
                <button type="button" @click.prevent="switchtodisplaycombinationview()" class="btn btn-primary btn-lg">进入正式实验</button>
            </div>

            </div>

        </div>
    </div>
    <div class="nologinview" v-else>
        <div class="container">
            <h3> please login first.. </h3>
        </div>
    </div>

    <br><br>

    <Footer />
  </div>


</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { FetchDisplayinfoPost } from "../apis/read.js";
import { SubmitClicklogPost } from "../apis/update.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { Store, useStore } from 'vuex';
import Axios from "axios";
import router from "../router";
import store from "../store";


export default {
  inject: ['reload'],
  name: "DisplaySimulatorView",
  components: {
    Header,
    Footer
  },
  setup(props, context){
    let displaynums = 5;
    let displaytimes = 0;
    let nlist_history = ref('');
    let nlist_random = ref('');
    let description = ref('');
    let leftpolicy_score = ref('');
    let rightpolicy_score = ref('');
    let certainty_degree = ref('');
    let diversity_degree = ref('');

    const display_data = reactive({
        left_list: [],
        right_list: []
    });

    onMounted(()=>{
      console.log(context.root.$route.path)
    });

    const FetchInfoParams = reactive({
          url: 'fetchdisplaylist',
          key: 'fetchinfo',
          username: store.state.user.username,
          displaynum: displaynums,
    });
    FetchDisplayinfoPost(FetchInfoParams).then(resp => {
        display_data.left_list = resp.data.data[0];
        display_data.right_list = resp.data.data[1];
        description = resp.data.data[2];
        console.log(nlist_history);
      })
      .catch(err => {
        text = 'error' + err;
        alert(text);
    });

    return{
      display_data,
      displaynums, displaytimes,
      nlist_history,
      nlist_random,
      description,
      leftpolicy_score, rightpolicy_score, certainty_degree, diversity_degree,
    }
  },

  data(){
    return{
      text: 'hello world to check test() function',
      nlist_history: [],
      nlist_random: [],
      description: "",
    }
  },

  methods:{
    switchtodisplaycombinationview(){
        router.push({name: 'DisplayCombination'});
    },
    click5item(){
        this.displaynums = 5;
    },
    click10item(){
        this.displaynums = 10;
    },
    fetchinfolist(){
      this.displaytimes = this.displaytimes + 1;
      console.log("??:, ", this.displaynums);
      const FetchInfoParams = reactive({
          url: 'fetchdisplaylist',
          key: 'fetchinfo',
          username: store.state.user.username,
          displaynum: this.displaynums,
      });
      FetchDisplayinfoPost(FetchInfoParams).then(resp => {
        this.text = resp.data.message;
        this.nlist_history = resp.data.data[0];
        this.nlist_random = resp.data.data[1];
        this.description = resp.data.data[2];
        this.$store.dispatch("UpdateNlistAction", {
          nlist1: this.nlist_history,
          nlist2: this.nlist_random,
        });
      })
      .catch(err => {
        this.text = 'error' + err;
        alert(this.text);
      })
    },
    clicktosubmit(){
      const Params = reactive({
          url: 'submitclicklog',
          key: 'submitlog',
          username: store.state.user.username,
          infos: {
            nlist_leftpolicy: this.nlist_history,
            nlist_rightpolicy: this.nlist_random,
            leftpolicy_score: this.leftpolicy_score, 
            rightpolicy_score: this.rightpolicy_score, 
            certainty_degree: this.certainty_degree, 
            diversity_degree: this.diversity_degree,
            description: this.description,
          },
      });
      console.log(Params);
      alert("submit successfully");
      SubmitClicklogPost(Params).then(resp => {
        this.text = resp.data.message;
        console.log(this.text);
      })
      .catch(err => {
        this.text = 'error' + err;
        alert(this.text);
      })
    },
  }

};
</script>

<style scoped>
.single-explanation{
    padding-left: 5px;
    padding-right: 5px;
    color: #967540;
    background-color: #fcf7e4;
    /* text-emphasis-color: rgb(230, 129, 21); */
    border-color: white;
    outline-color: white;
    margin-bottom: 5px;
    font-size: small;
    /* block-size: auto; */
    height: fit-content;
    max-height: max-content;
    padding: 5px;
    padding-bottom: 5px;
}

.single-discount{
    padding-left: 5px;
    padding-right: 5px;
    color: #ef5e43;
    background-color: white;
    border-color: #e3d0d6;
    outline-color: white;
    margin-bottom: 3px;
    font-size: small;
    /* size: 5rem; */
    height: fit-content;
    max-height: max-content;
    padding: 5px;
    padding-bottom: 5px;
}

</style>