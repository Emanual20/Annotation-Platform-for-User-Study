<template>
    <div class="displaycombination">
      <Header />
  
      <div class="ifloginview" v-if="$store.state.user.is_login">
          <br>
          <h2 style="text-align: center;">Evaluate this ranking list!</h2>
  
          <div class="choosedisplaynum_then">
              <div class="container">
                <div class="row" style="text-align: center;">
                    <div class="col">
                    <h3 style="text-align: center;"> Round {{ Math.floor((this.nlist.idx - 1) / 5) + 1 }}, Scene {{ this.nlist.idx % 5 + (this.nlist.idx % 5 == 0 ? 5 : 0)}} </h3><br>
                    </div>
                </div>
              </div>

              <!-- <div class="container">
                <div id="myCarousel" class="carousel slide">
                    <ol class="carousel-indicators">
                        <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                        <li data-target="#myCarousel" data-slide-to="1"></li>
                        <li data-target="#myCarousel" data-slide-to="2"></li>
                    </ol>   
                    <div class="carousel-inner">
                        <div class="item active">
                            <img src="../assets/1.png" alt="First slide">
                        </div>
                        <div class="item">
                            <img src="../assets/2.png" alt="Second slide">
                        </div>
                        <div class="item">
                            <img src="../assets/3.png" alt="Third slide">
                        </div>
                    </div>
                    <a class="carousel-control left" href="#myCarousel" 
                    data-slide="prev"> <span _ngcontent-c3="" aria-hidden="true" class="glyphicon glyphicon-chevron-right"></span></a>
                    <a class="carousel-control right" href="#myCarousel" 
                    data-slide="next">›</a>
                </div>
              </div> -->
  
              <div class="container">
              <div class="row">
                  <div class="col-3">
                  </div>

                  <div class="col-6">
                  <div class="container">
                      <div v-for="(niter, index) in nlist.left_list[nlist.idx - 1]" :key="index">
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
  
                  <div class="col-3">
                </div>
                  
              </div>
              </div>
              
              <div class="container">
                
              <div v-if="nlist.idx <= 40">
              <!-- <h5>1. 您认为，该列表中的推荐解释在"帮助您<b>更有效地准确选择</b>外卖商家"的方面表现如何？</h5> -->
              <h5>1. What's the performance of explanations in this list assisting you to determine which online delivery customers to buy more effectively?</h5>
              <div class="row">
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="effectiveness_degree" name="inlineRadioOptions" id="inlineRadio1" value="1">
                    <label class="form-check-label" for="inlineRadio1">1（No assistance at all）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="effectiveness_degree" name="inlineRadioOptions" id="inlineRadio2" value="2">
                    <label class="form-check-label" for="inlineRadio2">2</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="effectiveness_degree" name="inlineRadioOptions" id="inlineRadio3" value="3">
                    <label class="form-check-label" for="inlineRadio3">3</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="effectiveness_degree" name="inlineRadioOptions" id="inlineRadio4" value="4">
                    <label class="form-check-label" for="inlineRadio3">4</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="effectiveness_degree" name="inlineRadioOptions" id="inlineRadio5" value="5">
                    <label class="form-check-label" for="inlineRadio3">5（Perfectly confirm my mental decision）</label>
                </div>
              </div>

              <!-- <h5>2. 您认为，该列表中的推荐解释在"影响您选择外卖商家<b>做出更快的选择</b>"的方面表现如何？（主要是决策时间）</h5> -->
              <h5>2. What's the performance of explanations in this list helping you to decide faster if you like customers in this impression list? </h5>
              <div class="row">
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio1" value="1">
                    <label class="form-check-label" for="inlineRadio1">1（Significantly increasing my decision time）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio2" value="2">
                    <label class="form-check-label" for="inlineRadio2">2</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio3" value="3">
                    <label class="form-check-label" for="inlineRadio3">3</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio4" value="4">
                    <label class="form-check-label" for="inlineRadio3">4</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="efficiency_degree" name="inlineRadioOptions1" id="inlineRadio5" value="5">
                    <label class="form-check-label" for="inlineRadio3">5（Significantly decreasing my decision time）</label>
                </div>
              </div>      

              <!-- <h5>3. 您认为，该列表中的推荐解释在"<b>促使您点击外卖商家，以进一步了解</b>"的方面表现如何？</h5> -->
              <h5> 3. What's the performance of explanations making you more willing to click the customer boxes in this impression list for further exploring?</h5>
              <div class="row">
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio1" value="1">
                    <label class="form-check-label" for="inlineRadio1">1（make me hate to click）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio2" value="2">
                    <label class="form-check-label" for="inlineRadio2">2</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio3" value="3">
                    <label class="form-check-label" for="inlineRadio3">3</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio4" value="4">
                    <label class="form-check-label" for="inlineRadio3">4</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="persuasiveness_degree" name="inlineRadioOptions2" id="inlineRadio5" value="5">
                    <label class="form-check-label" for="inlineRadio3">5（appeal me to click）</label>
                </div>
              </div>

  
              <!-- <h5>4. 您认为，该列表中的推荐解释在"<b>帮助您理解给您推荐这些外卖商家的原因</b>"的方面表现如何？</h5> -->
              <h5> 4. What's the performance of explanations in this list helping you to understand what the recommendation is based on? </h5>
              <div class="row">
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="transparency_degree" name="inlineRadioOptions3" id="inlineRadio1" value="1">
                    <label class="form-check-label" for="inlineRadio1">1（Completely no help for me to understand）</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="transparency_degree" name="inlineRadioOptions3" id="inlineRadio2" value="2">
                    <label class="form-check-label" for="inlineRadio2">2</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="transparency_degree" name="inlineRadioOptions3" id="inlineRadio3" value="3">
                    <label class="form-check-label" for="inlineRadio3">3</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="transparency_degree" name="inlineRadioOptions3" id="inlineRadio4" value="4">
                    <label class="form-check-label" for="inlineRadio3">4</label>
                </div>
                <div class="col form-check form-check-inline">
                    <input class="form-check-input" type="radio" v-model="transparency_degree" name="inlineRadioOptions3" id="inlineRadio5" value="5">
                    <label class="form-check-label" for="inlineRadio3">5（Help me to understand very well）</label>
                </div>
              </div>
              </div>
            
              <div v-if="nlist.idx % 5 == 0">
                <!-- <h5>Ex1. 看完上述之前由<b>同种生成方式</b>生成的5个带有解释的推荐列表，您认为该轮(Round)5个场景(Scene)的推荐解释在"<b>帮助您信任该生成方式给您的个性化推荐结果</b>"的方面表现如何？</h5> -->
                <h5> Ex1. What's the performance of explanations displayed on these five pages that help you to trust the generated personalized recommendation?</h5>
                <div class="row">
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="trust_degree" name="inlineRadioOptionsex1" id="inlineRadio1" value="1">
                        <label class="form-check-label" for="inlineRadio1">1（Cannot make me trust at all）</label>
                    </div>
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="trust_degree" name="inlineRadioOptionsex1" id="inlineRadio2" value="2">
                        <label class="form-check-label" for="inlineRadio2">2</label>
                    </div>
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="trust_degree" name="inlineRadioOptionsex1" id="inlineRadio3" value="3">
                        <label class="form-check-label" for="inlineRadio3">3</label>
                    </div>
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="trust_degree" name="inlineRadioOptionsex1" id="inlineRadio4" value="4">
                        <label class="form-check-label" for="inlineRadio3">4</label>
                    </div>
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="trust_degree" name="inlineRadioOptionsex1" id="inlineRadio5" value="5">
                        <label class="form-check-label" for="inlineRadio3">5（Make me trust very well）</label>
                    </div>
                </div>


                <!-- <h5>Ex2. 看完上述之前由<b>同种生成方式</b>生成的5个带有解释的推荐列表，您对该轮(Round)5个场景(Scene)的推荐解释<b>满意程度</b>如何？</h5> -->
                <h5> Ex2. How do you satisfy with the explanations displayed on these five pages in terms of picking a recommendation?</h5>
                <div class="row">
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="satisfaction_degree" name="inlineRadioOptionsex2" id="inlineRadio1" value="1">
                        <label class="form-check-label" for="inlineRadio1">1（Very Unsatisfied）</label>
                    </div>
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="satisfaction_degree" name="inlineRadioOptionsex2" id="inlineRadio2" value="2">
                        <label class="form-check-label" for="inlineRadio2">2</label>
                    </div>
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="satisfaction_degree" name="inlineRadioOptionsex2" id="inlineRadio3" value="3">
                        <label class="form-check-label" for="inlineRadio3">3</label>
                    </div>
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="satisfaction_degree" name="inlineRadioOptionsex2" id="inlineRadio4" value="4">
                        <label class="form-check-label" for="inlineRadio3">4</label>
                    </div>
                    <div class="col form-check form-check-inline">
                        <input class="form-check-input" type="radio" v-model="satisfaction_degree" name="inlineRadioOptionsex2" id="inlineRadio5" value="5">
                        <label class="form-check-label" for="inlineRadio3">5（Very Satisfied）</label>
                    </div>
                </div>
              </div>

              <div v-if="nlist.idx > 40">
                <br>
                <b-container>
                <div class="container">
                    <div class="card-body">
                    <h4><b>最后两个问题了!</b></h4>
                    
                    <form @submit.prevent="updatespitslot()">
                        <div class="form-group">
                            经过四十次标注之后，想必您对这些问题形成了自己的评价标准。
                            <br><br>
                            请问您对每个场景(scene)下的四个问题的评价标准是怎样的(帮助您有效准确选择外卖商家、做出更快决策、促使您点击外卖商家、帮助您理解推荐这些外卖商家的原因)？
                        <textarea
                            class="form-control"
                            rows="4"
                            v-model="textinfo1"
                            placeholder="畅所欲言！"
                        >
                        </textarea>
                        <br>
                            请问您对每轮(round)后的两个问题(Ex1, Ex2)的评价标准是怎样的(帮助您信任该生成方式给您的个性化推荐结果、对推荐解释的满意程度)？
                        <textarea
                            class="form-control"
                            rows="2"
                            v-model="textinfo2"
                            placeholder="畅所欲言！"
                        >
                        </textarea>
                        </div>
                    </form>
                    </div>
                </div>
                </b-container>
              </div>
              
  
              <div class="col" style="text-align:center;" v-if="nlist.idx <= 40">
                  <button type="button" @click.prevent="clicktosubmit()" class="btn btn-primary btn-lg">Next Group</button>
              </div>

              <div class="col" style="text-align:center;" v-if="nlist.idx > 40">
                  <br>
                  <button type="button" @click.prevent="clicktosubmit(), logout()" class="btn btn-primary btn-lg">Submit and Finish</button>
              </div>

              </div>
  
          </div>
      </div>
      <div class="nologinview" v-else>
          <div class="container">
              <h3> please login first.. </h3>
          </div>
      </div>
  
      <Footer />
    </div>
  
  
  </template>
  
  <script>
  import Header from "../components/HeaderComp.vue";
  import Footer from "../components/FooterComp.vue";
  import { FetchDisplayinfoPost } from "../apis/read.js";
  import { FetchDisplayNewPost } from "../apis/read.js";
  import { SubmitClicklogPost } from "../apis/update.js";
  import { ref, reactive, onMounted } from "@vue/composition-api";
  import { Store, useStore } from 'vuex';
  import Axios from "axios";
  import router from "../router";
  import store from "../store";
  
  
  export default {
    inject: ['reload'],
    name: "DisplayNewView",
    components: {
      Header,
      Footer
    },
    setup(props, context){
      let displaynums = 5;
      const nlist = reactive({
        idx: 1,
        left_list: [],
        description: ""
      });
      let effectiveness_degree = 0;
      let efficiency_degree = 0;
      let persuasiveness_degree = 0;
      let transparency_degree = 0;

      let trust_degree = 0;
      let satisfaction_degree = 0;
      let textinfo1 = "";
      let textinfo2 = "";
  
      onMounted(()=>{
        console.log(context.root.$route.path)
      });

      const FetchInfoParams = reactive({
            url: 'fetchdisplaynewlist',
            key: 'fetchinfo',
            username: store.state.user.username,
            displaynum: displaynums,
        });
        FetchDisplayNewPost(FetchInfoParams).then(resp => {
          nlist.left_list = resp.data.data[0];
          nlist.description = resp.data.data[1];
        });
      
      return{
        displaynums,
        nlist,
        effectiveness_degree, efficiency_degree, persuasiveness_degree, transparency_degree,
        trust_degree, satisfaction_degree,
        textinfo1, textinfo2
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
        alert("衷心感谢您的参与，谢谢！");
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
        this.nlist.idx = this.nlist.idx + 1;
        const FetchInfoParams = reactive({
            url: 'fetchdisplaycombinationlist',
            key: 'fetchinfo',
            username: store.state.user.username,
            displaynum: this.displaynums,
        });
        FetchDisplayNewPost(FetchInfoParams).then(resp => {
          this.text = resp.data.message;
          this.nlist.left_list = resp.data.data[0];
          this.nlist.description = resp.data.data[1];
          this.$store.dispatch("UpdateNlistAction", {
            nlist1: this.nlist.left_list,
            nlist2: []
          });
        })
        .catch(err => {
          this.text = 'error' + err;
          alert(this.text);
        })
      },
      clicktosubmit(){
        if(this.nlist.idx <= 40 && this.nlist.idx % 5 == 0 && (this.trust_degree == 0 || this.satisfaction_degree == 0)){
            alert("please select your extra questions' choices and submit your answer..");
        }
        else if(this.nlist.idx <= 40 && (this.effectiveness_degree == 0 || this.efficiency_degree == 0 || this.persuasiveness_degree == 0 || this.transparency_degree == 0)){
            alert("please select your questions' choices and submit your answer..");
        }
        else
        {
            const Params = reactive({
                url: 'submitclicklog',
                key: 'submitlog',
                username: store.state.user.username,
                infos: {
                nlist_leftpolicy: this.nlist.left_list[this.nlist.idx - 1],
                nlist_rightpolicy: [],
                certainty_degree: "not defined", 
                diversity_degree: "not defined",
                attrs: {
                    property: "tintarev",
                    ranking_policy: this.nlist.description.split(';;')[Math.floor((this.nlist.idx - 1) / 5)],
                    round: this.nlist.idx, 
                    effectiveness_degree: this.effectiveness_degree,
                    efficiency_degree: this.efficiency_degree,
                    persuasiveness_degree: this.persuasiveness_degree,
                    transparency_degree: this.transparency_degree,
                    trust_degree: this.trust_degree,
                    satisfaction_degree: this.satisfaction_degree,
                    textinfo1: this.textinfo1,
                    textinfo2: this.textinfo2,
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
            this.nlist.idx = this.nlist.idx + 1;
            console.log(this.nlist.idx);
            
            this.effectiveness_degree = 0;
            this.efficiency_degree = 0;
            this.transparency_degree = 0;
            this.persuasiveness_degree = 0;

            this.trust_degree = 0;
            this.satisfaction_degree = 0;
            document.documentElement.scrollTop = 0;
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