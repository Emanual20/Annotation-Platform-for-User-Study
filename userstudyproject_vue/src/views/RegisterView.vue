<template>
  <div class="login">
    <Header />

    <div class="container">
      <div class="card-body">
        <!-- If you wanna make register function available, change blockedregister() into tryregister() method -->
        <!-- <form @submit.prevent="tryregister()"> -->
        <form @submit.prevent="blockedregister()">
        <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">注册邮箱(Email address)</label>
            <input v-model="emailaddress" type="email" class="form-control" id="emailaddress" aria-describedby="emailHelp">
            <div id="emailHelp" class="form-text"><b>The email address will be set as your login username.</b></div>
        </div>
        <!-- <div class="mb-3">
            <label for="exampleInputNickname1" class="form-label">Nickname</label>
            <input v-model="username" type="text" class="form-control" id="username" aria-describedby="NicknameHelp">
        </div> -->
        <div class="mb-3">
            <label for="exampleInputPassword1" class="form-label">密码(Password)</label>
            <input v-model="password" type="password" class="form-control" id="password"> 
            <div id="PasswordHelp" class="form-text"><b>The Password shall pass automatically security check.</b></div>
        </div>
        <div class="mb-3">
            <label for="exampleInputPassword" class="form-label">邀请码(Invitation Code)</label>
            <input v-model="invitation_code" type="password" class="form-control" id="invitation_code"> 
            <div id="InvitationCodeHelp" class="form-text"><b>An invitation code for checking user resources.</b></div>
        </div>
        <div class="mb-3">
            <label for="exampleInputPhoneNumber1" class="form-label">手机号码(Mobile phone Number)</label>
            <input v-model="mobilephonenumber" type="text" class="form-control" id="mobilephonenumber">
        </div>
        <div class="mb-3">
            <label for="exampleInputRealname1" class="form-label">姓名(Real name)</label>
            <input v-model="realname" type="text" class="form-control" id="realname">
        </div>
        <div class="mb-3">
            <label for="exampleInputSex1" class="form-label">性别(Sex)</label>
            <input v-model="sex" type="text" class="form-control" id="sex">
        </div>
        <div class="mb-3">
            <label for="exampleInputGrade1" class="form-label">年级(Grade)</label>
            <input v-model="grade" type="text" class="form-control" id="grade">
        </div>
        <div class="mb-3">
            <label for="exampleInputMajor1" class="form-label">专业(Major or College)</label>
            <input v-model="major" type="text" class="form-control" id="major">
        </div>
        <!-- <div class="mb-3 form-check">
            <input type="checkbox" class="form-check-input" id="exampleCheck1">
            <label class="form-check-label" for="exampleCheck1">我同意将我的信息用于网站建设。</label>
        </div> -->
        <button type="submit" class="btn btn-primary">Submit</button>
        </form>

      </div>
    </div>
 
    <Footer />
  </div>


</template>

<script>
import Header from "../components/HeaderComp.vue";
import Footer from "../components/FooterComp.vue";
import { RegisterUserPost } from "../apis/update.js";
import { ref, reactive, onMounted } from "@vue/composition-api";
import { useStore } from 'vuex';
import Axios from "axios";
import router from "../router";
import store from "../store";


export default {
  name: "LoginView",
  components: {
    Header,
    Footer
  },
  setup(props, context){
    let emailaddress = "";
    let password = "";
    let invitation_code = "";
    let mobilephonenumber = "";
    let realname = "";
    let sex = "";
    let grade = "";
    let major = "";
    let error_message = ref('');
    onMounted(()=>{
      console.log(context.root.$route.path)
    });

    return{
      emailaddress,
      password,
      invitation_code,
      mobilephonenumber, realname, sex, grade, major,
      error_message,
    }
  },

  data(){
    return{
      text: 'some log',
      retCode: -1,
    }
  },

  methods:{
    blockedregister(){
      let text = "Register service is not available for users now.";
      console.log(text);
      alert(text);
    },
    tryregister(){
      console.log("In Register View:", "email:", emailaddress.value);
      const testParams = reactive({
        url: 'registernewuser', 
        key: 'register',
        emailaddress: emailaddress.value,
        // username: username.value,
        password: password.value,
        invitation_code: invitation_code.value,
        attrs: {
          mobilephonenumber: mobilephonenumber.value, 
          realname: realname.value,
          sex: sex.value,
          grade: grade.value, 
          major: major.value,
        }
      });
      RegisterUserPost(testParams).then(resp=>{
        this.text = resp.data.message;
        alert(this.text);
        router.push({name: 'LoginView'});
      })
      .catch(err=>{
        this.text = 'error' + err.message;
        let error_message = "Internal server error or this email already exists or invitation code error..";
        alert(error_message);
      })
    },
  }

};
</script>