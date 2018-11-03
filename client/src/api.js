// import Vue from "vue";
import axios from "axios";

const client = axios.create({
  baseURL: process.env.VUE_APP_API_BASE_URL,
  json: true
});

export default {
  async execute(method, resource, data) {
    return client({
      method,
      url: resource,
      data,
      headers: { "Access-Control-Allow-Origin": "*" }
    }).then(req => {
      return req.data;
    });
  },
  getChallenges() {
    return this.execute("get", "/api/challenges");
  },
  getChallenge(id) {
    return this.execute("get", `/api/challenges/${id}`);
  },
  getChallengeRank(id) {
    return this.execute("get", `/api/challenges/${id}/rank`);
  },
  checkChallenge(id, data) {
    return this.execute("post", `/api/challenges/${id}`, data);
  },
  getRank() {
    return this.execute("get", "/api/rank");
  }
};
