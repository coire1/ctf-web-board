import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/challenges",
      name: "challenges",
      component: () => import("./views/Challenges.vue")
    },
    {
      path: "/challenge/:id",
      name: "challenge",
      component: () => import("./views/Challenge.vue")
    }
  ]
});
