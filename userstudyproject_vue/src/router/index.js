import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import DisplaySimulatorView from "../views/DisplaySimulatorView.vue";
import DisplayCombinationView from "../views/DisplayCombinationView.vue";
import DisplayFidelityView from "../views/DisplayFidelityView.vue";
import DisplayNewView from "../views/DisplaynewView.vue";
import SelfinfoView from "../views/SelfinfoView.vue";

Vue.use(VueRouter);

const routes = [
  // 网站首页
  {
    path: "/",
    name: "Home",
    component: Home
  },

  // 登陆页面
  {
    path: "/login/",
    name: "LoginView",
    component: LoginView
  },

  // 注册页面
  {
    path: "/register/",
    name: "RegisterView",
    component: RegisterView
  },

  // 展示online-random列表详情页
  {
    path: "/displaysimulator/",
    name: "DisplaySimulator",
    component: DisplaySimulatorView,
  },

  // 展示所有策略列表usefulness详情页
  {
    path: "/displaycombination/",
    name: "DisplayCombination",
    component: DisplayCombinationView,
  },

  // 展示fidelity详情页
  {
    path: "/displayfidelity/",
    name: "DisplayFidelity",
    component: DisplayFidelityView,
  },

  // 新标注页面, 2022.9.28
  {
    path: "/displaynew/",
    name: "Displaynew",
    component: DisplayNewView,
  },

  // 个人信息详情页
  {
    path: '/selfinfo/',
    name: "Selfinfo",
    component: SelfinfoView,
  },

  // 404 NotFoundPage
  {
    path: "/404/",
    name: "404",
    component: NotFoundView
  },

  {
    path: "/:catchAll(.*)",
    redirect: "/404/"
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
