<template>
    <b-container id="header">
      <b-navbar toggleable="lg" type="dark" variant="info">
        <b-navbar-brand href="/">DefaultGroup</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <ul  class="navbar-nav ml-auto" v-if="!$store.state.user.is_login">
            <a class="nav-link" href="/login/">登录</a>
            <a class="nav-link" href="/register/">注册</a>
          </ul>
          <ul  class="navbar-nav ml-auto" v-else>
            <a class="nav-link" @click="checknew()"> Annotating Page </a>
            <!-- <a class="nav-link" @click="checkcombination()"> 正式实验-U </a> -->
            <!-- <a class="nav-link" @click="checkfidelity()"> 正式实验-F </a> -->
            <a class="nav-link" @click="checkselfinfo()"> {{ $store.state.user.username }} </a>
            <a class="nav-link" @click="checkstuinfo()"> Selfinfos </a>
            <a class="nav-link" @click="logout()"> Logout </a>
          </ul>
        </b-collapse>
      </b-navbar>
    </b-container>
</template>

<script>
import { ref } from "@vue/composition-api";
import { store } from "../store";
import { router } from "../router" ;
import { useStore } from 'vuex';

export default {
    name: "Header",
    setup(props, context){
      const now_url = ref(context.root.$route.path);
      return {
        now_url,
      };
    },
    methods:{
      checknew(){
        this.$router.push({name: 'Displaynew'});
      },
      checkcombination(){
        this.$router.push({name: 'DisplayCombination'});
      },
      checkfidelity(){
        this.$router.push({name: 'DisplayFidelity'});
      },
      checkselfinfo(){
        this.$router.push({name: 'Selfinfo'});
      },
      checkstuinfo(){
        this.$router.push({name: 'DisplaySimulator'});
      },
      logout(){
        console.log("Log out begin..!");
        this.$store.dispatch("LogoutAction",{
        });
        console.log("Log out finish..!");
        this.$router.push({name: 'Home'});
      }
    }
}
</script>

<style lang="scss" scoped>
@media (max-width:500px) {
  #Header{
    margin-top:90px
  }
}
</style>