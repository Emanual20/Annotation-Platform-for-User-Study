<template>
    <div class="displaycombination">
      <Header />
  
      <div class="ifloginview" v-if="$store.state.user.is_login">
          <br>
          <h2 style="text-align: center;">Which is better?</h2>
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
                      <div v-for="(niter, index) in nlist.left_list" :key="index">
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
                                          月售{{ niter['log_monthly_sale'] }} 人均 ¥{{ niter['log_cost_eachperson'] }}
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
                                          起送 ¥{{ niter['log_minimal_delivery'] }}
                                      </div>
                                      <div class="col-3" style="text-align: left; color:#8b898a">
                                          配送 约¥{{ niter['log_cost_delivery'] }}
                                      </div>
                                      <div class="col" style="text-align: right; color:#8b898a">
                                          {{ niter['log_minutes_delivery'] }}分钟 {{ niter['log_distance_delivery'] }}km
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
                      <div v-for="(niter, index) in nlist.right_list" :key="index">
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
                                          月售{{ niter['log_monthly_sale'] }} 人均 ¥{{ niter['log_cost_eachperson'] }}
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
                                        起送 ¥{{ niter['log_minimal_delivery'] }}
                                      </div>
                                      <div class="col-3" style="text-align: left; color:#8b898a">
                                        配送 约¥{{ niter['log_cost_delivery'] }}
                                      </div>
                                      <div class="col" style="text-align: right; color:#8b898a">
                                          {{ niter['log_minutes_delivery'] }}分钟 {{ niter['log_distance_delivery'] }}km
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
                              </div>
                          </div>
                      </div>
                      </div>
                  </div>
                  </div>
              </div>
              </div>
              <br>
  
              <!-- <div class="container">
              <div class="row">
                  <div class="col" style="text-align:center;">
                  <button type="button" class="btn btn-primary btn-lg">Left Better</button>
                  </div>
                  <div class="col" style="text-align:center;">
                  <button type="button" class="btn btn-primary btn-lg">Right Better</button>
                  </div>
              </div>
              </div> -->
              <br><br>
              
              <div class="container">
              <!-- <h5>1. 如果需要您给左边列表推荐解释的满意程度按1-5分打分，您的选择是？</h5>
              <select id="leftpolicy_score" v-model="leftpolicy_score" class="form-select">
                  <option value="0" selected>请选择</option>
                  <option value="1">1分 我非常不满意</option>
                  <option value="2">2分</option>
                  <option value="3">3分</option>
                  <option value="4">4分</option>
                  <option value="5">5分 我非常满意</option>
              </select><br>
  
              <h5>2. 如果需要您给右边列表推荐解释的满意程度按1-5分打分，您的选择是？</h5>
              <select id="rightpolicy_score" v-model="rightpolicy_score" class="form-select">
                  <option value="0" selected>请选择</option>
                  <option value="1">1分 我非常不满意</option>
                  <option value="2">2分</option>
                  <option value="3">3分</option>
                  <option value="4">4分</option>
                  <option value="5">5分 我非常满意</option>
              </select><br> -->
            
              <h5>1. 您认为左右两个列表的推荐解释哪个对您选择外卖商家更有用？</h5>
              <div class="row">
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="usefulness_degree" name="inlineRadioOptions" id="inlineRadio1" value="-2">
                    <label class="form-check-label" for="inlineRadio1">-2（左侧列表更有用）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="usefulness_degree" name="inlineRadioOptions" id="inlineRadio2" value="-1">
                    <label class="form-check-label" for="inlineRadio2">-1</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="usefulness_degree" name="inlineRadioOptions" id="inlineRadio3" value="0">
                    <label class="form-check-label" for="inlineRadio3">0（基本没有差异）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="usefulness_degree" name="inlineRadioOptions" id="inlineRadio4" value="1">
                    <label class="form-check-label" for="inlineRadio3">+1</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="usefulness_degree" name="inlineRadioOptions" id="inlineRadio5" value="2">
                    <label class="form-check-label" for="inlineRadio3">+2（右侧列表更有用）</label>
                </div>
              </div>

              <h5>2. 您认为左右两个列表的推荐解释哪个能帮助您选择外卖商家做出更快的选择？</h5>
              <div class="row">
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio1" value="-2">
                    <label class="form-check-label" for="inlineRadio1">-2（左侧列表更能帮助）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio2" value="-1">
                    <label class="form-check-label" for="inlineRadio2">-1</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio3" value="0">
                    <label class="form-check-label" for="inlineRadio3">0（基本没有差异）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio4" value="1">
                    <label class="form-check-label" for="inlineRadio3">+1</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio5" value="2">
                    <label class="form-check-label" for="inlineRadio3">+2（右侧列表更能帮助）</label>
                </div>
              </div>              

              <h5>3. 您认为左右两个列表的推荐解释哪个更能促使您点击外卖商家，以进一步了解？</h5>
              <div class="row">
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio1" value="-2">
                    <label class="form-check-label" for="inlineRadio1">-2（左侧列表更能促使）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio2" value="-1">
                    <label class="form-check-label" for="inlineRadio2">-1</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio3" value="0">
                    <label class="form-check-label" for="inlineRadio3">0（基本没有差异）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio4" value="1">
                    <label class="form-check-label" for="inlineRadio3">+1</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio5" value="2">
                    <label class="form-check-label" for="inlineRadio3">+2（右侧列表更能促使）</label>
                </div>
              </div>  

              <!-- <h5>3. 请问您做出上两个问题决策的确定程度如何，按1-5分打分？</h5>
              <select id="certainty_degree" v-model="certainty_degree" class="form-select">
                  <option value="0" selected>请选择</option>
                  <option value="1">1分，我非常不确定我的判断</option>
                  <option value="2">2分</option>
                  <option value="3">3分</option>
                  <option value="4">4分</option>
                  <option value="5">5分，我非常确定我的判断</option>
              </select><br> -->
  
              <h5>4. 如果需要您为上述两种推荐解释展出的差异度按1-5分打分，您的选择是？</h5>
              <select id="diversity_degree" v-model="diversity_degree" class="form-select">
                  <option value="0" selected>请选择</option>
                  <option value="1">1分，两个列表无法让我感受出明显差异</option>
                  <option value="2">2分</option>
                  <option value="3">3分</option>
                  <option value="4">4分</option>
                  <option value="5">5分，两个列表能让我感受出明显差异</option>
              </select><br>
  
              <div class="col" style="text-align:center;">
                  <button type="button" @click.prevent="clicktosubmit()" class="btn btn-primary btn-lg">下一组</button>
              </div>

              <div class="col" style="text-align:center;" v-if="displaytimes > 40">
                  <br>
                  <button type="button" @click.prevent="logout()" class="btn btn-primary btn-lg">我累了，不想标了</button>
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
  import { FetchDisplayCombinationinfoPost } from "../apis/read.js";
  import { SubmitClicklogPost } from "../apis/update.js";
  import { ref, reactive, onMounted } from "@vue/composition-api";
  import { Store, useStore } from 'vuex';
  import Axios from "axios";
  import router from "../router";
  import store from "../store";
  
  
  export default {
    inject: ['reload'],
    name: "DisplayCombinationView",
    components: {
      Header,
      Footer
    },
    setup(props, context){
      let displaynums = 5;
      let displaytimes = 1;
      const nlist = reactive({
        left_list: [],
        right_list: [],
        description: ""
      });
      let certainty_degree = 0;
      let diversity_degree = 0;
      let usefulness_degree = 0;
      let efficiency_degree = 0;
      let persuasiveness_degree = 0;
  
      onMounted(()=>{
        console.log(context.root.$route.path)
      });

      const FetchInfoParams = reactive({
            url: 'fetchdisplaycombinationlist',
            key: 'fetchinfo',
            username: store.state.user.username,
            displaynum: displaynums,
        });
        FetchDisplayCombinationinfoPost(FetchInfoParams).then(resp => {
          nlist.left_list = resp.data.data[0];
          nlist.right_list = resp.data.data[1];
          nlist.description = resp.data.data[2];
        });
      
      return{
        displaynums, displaytimes,
        nlist,
        certainty_degree, diversity_degree,
        usefulness_degree, efficiency_degree, persuasiveness_degree
      }
    },
  
    data(){
      return{
        text: 'hello world',
        description: "usefulness-evaluation",
      }
    },
  
    methods:{
      logout(){
        alert("感谢你的参与，请通知主试，谢谢！");
        console.log("Log out begin..!");
        this.$store.dispatch("LogoutAction",{
        });
        console.log("Log out finish..!");
        this.$router.push({name: 'Home'});
      },
      click5item(){
          this.displaynums = 5;
      },
      click10item(){
          this.displaynums = 10;
      },
      fetchinfolist(){
        this.displaytimes = this.displaytimes + 1;
        const FetchInfoParams = reactive({
            url: 'fetchdisplaycombinationlist',
            key: 'fetchinfo',
            username: store.state.user.username,
            displaynum: this.displaynums,
        });
        FetchDisplayCombinationinfoPost(FetchInfoParams).then(resp => {
          this.text = resp.data.message;
          this.nlist.left_list = resp.data.data[0];
          this.nlist.right_list = resp.data.data[1];
          this.nlist.description = resp.data.data[2];
          this.$store.dispatch("UpdateNlistAction", {
            nlist1: this.nlist.left_list,
            nlist2: this.nlist.right_list
          });
        })
        .catch(err => {
          this.text = 'error' + err;
          alert(this.text);
        })
      },
      clicktosubmit(){
        // if(this.usefulness_degree == -2048 || this.efficiency_degree == -2048 || this.persuasiveness_degree == -2048){
        //     alert("please select your choice and submit your answer..");
        // }
        // else
        {
            const Params = reactive({
                url: 'submitclicklog',
                key: 'submitlog',
                username: store.state.user.username,
                infos: {
                nlist_leftpolicy: this.nlist.left_list,
                nlist_rightpolicy: this.nlist.right_list,
                certainty_degree: this.certainty_degree, 
                diversity_degree: this.diversity_degree,
                attrs: {
                    property: "usefulness",
                    usefulness_degree: this.usefulness_degree,
                    efficiency_degree: this.efficiency_degree,
                    persuasiveness_degree: this.persuasiveness_degree,
                    diversity_degree: this.diversity_degree,
                },
                description: this.nlist.description,
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
            });
            this.certainty_degree = 0;
            this.diversity_degree = 0;
            // this.usefulness_degree = -2048;
            // this.efficiency_degree = -2048;
            // this.persuasiveness_degree = -2048;
            this.fetchinfolist();
        }
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