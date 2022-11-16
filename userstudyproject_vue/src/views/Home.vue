<template>

  <div class="home">
    <Header />
    <div class="container">
      <p class="lead"> 
        登陆前请阅读如下注意事项，感谢！
      </p>
      <ul class="list-unstyled">
        <li>登录相关:
          <ul>
            <li>您第一次使用本网站的时候，请按照流程先注册新账号。</li>
              <ul>
                <li> 输入邮箱(Email address)、密码(Password)、邀请码(Invitation Code, 本次实验为defaultstr)；</li>
                <li> 输入手机号(支付宝绑定的手机号，用于发放被试费)、姓名、年级、专业；</li>
                <li> 点击蓝色按钮Submit即可成功注册。</li>
              </ul>
            <li>如已注册，则可以使用原账号登录。</li>
            <li>如需修改密码，您可以在登陆后，点击页面上方自己的邮箱以修改密码。</li>
          </ul>
        </li>
        <li>实验相关(<b>由于本实验均在线上完成，请您先阅读如下实验须知</b>):
          <ul>
            <li>我们是来自中国人民大学高瓴人工智能学院defaultGroup的研究生，所有的标注任务数据只用于科学研究，不会影响任何您的隐私信息。</li>
            <!-- <li><b>用户实验每次会展出推荐列表，这两个列表展出商家的顺序是相同的，但是每个商家内部提供的解释是不同的，我们需要您就每个列表的满意程度给这两个列表分别打分(1-5)，并就您此次打分确定程度打分(1-5)。整个流程重复十次。</b></li> -->
            <li>用户实验共分为八轮(Round):</li>
              <ul>
                <li>每轮中会展出五个推荐列表(Scene)，这五个推荐列表都对应着同样的一种展出策略(Policy)。</li>
                <li>对于每个推荐列表，您需要就四个问题打分(1-5, 1分表示该问题上的最差表现, 5分表示该问题上的最好表现)。</li>
                <li>在每轮最后，您还需要就有关本轮展出的这五个推荐列表的两个问题打分(1-5)。</li>
              </ul>
            <li>当出现Round9时，标注结束，您可以退出页面。无需保留截图，我们在后台自动核验数据完整性。</li>
            <li>被试费为50元人民币，被试费可能会根据您标注数据的质量上浮(最多20%)或下调(如数据完整性有问题, 最多50%)，将会在您参与实验后的5个工作日内通过支付宝发放。</li>
            <li>实验数据直接应用于科学研究和商用推荐系统的改进，若参与实验请务必认真完成。</li>
            <li><b>注意：该实验具有连续性和完整性，如标注到中途因为网络原因中断，需要从最开始(Round1)重新标注，<b>所以请尽量在稳定的网络环境下在一段连续的时间内完成实验</b>。否则如数据完整性受损将扣减一定比例的被试费。</b></li>
          </ul>
        </li>
        <li>实验指导视频<b>（请务必观看后再标注）</b>：
          <br>
          可以<a target="_blank" href="https://www.bilibili.com/video/BV14N4y1A7fa">b站链接</a>看也可以在网站内看。
          <video width="960" height="540" controls>
          <source src="../assets/meeting_01.mp4" type="video/mp4">
          </video>
        </li>
        <li>Bug反馈相关：
          <ul>
            <li>请不要做SQL注入等安全测试、DDOS等压力测试，避免服务器和服务宕机。</li>
            <li>您可以随时通过<a href="mailto:emanual20@foxmail.com">邮件</a>联系的方式向我反馈bug。</li>
          </ul>
        </li>
      </ul>
    </div>
    <Footer />
  </div>

</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { ref, reactive, onMounted } from "@vue/composition-api";


export default {
  name: "Home",
  components: {
    Header,
    Footer
  },
  setup(props, context){
    const poicard = reactive({
      PoiName: "Poi-Name", 
      DianpingPoint: "xxx",
      MonthlySale: "xxx", 
      CostEachPerson: "xxx", 
      MinimalDelivery: "xxx",
      CostDelivery: "xxx",
      MinutesDelivery: "xx",
      DistanceDelivery: "xx",
      Explanations: ["解释1", "解释2"], 
      Discounts: ["满减1", "满减2"],
    })

    onMounted(()=>{
      console.log(context.root.$route.path);
    });

    return{
      poicard,
    };
  }

};
</script>

<style scoped>
.single-explanation{
    padding-left: 20px;
    padding-right: 20px;
    background-color: rgb(251, 249, 224);
    text-emphasis-color: rgb(230, 129, 21);
    border-color: white;
    outline-color: white;
    margin-bottom: 3px;
    /* size: 5rem; */
}

</style>