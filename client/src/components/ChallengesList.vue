<template>
  <div class="board">
    <h2>Challenges</h2>
    <div class="challenges-list">
      <div v-for="challenge in challenges" class="single-challenge" :key="challenge.id">
        <challenge-el :challenge="challenge" />
      </div>
    </div>
  </div>
</template>

<script>
import api from "@/api";
import ChallengeEl from "@/components/ChallengeEl.vue";

export default {
  name: "ChallengesList",
  components: {
    ChallengeEl
  },
  data() {
    return {
      loading: false,
      challenges: []
    };
  },
  async created() {
    this.refreshChallenges();
  },
  methods: {
    async refreshChallenges() {
      this.loading = true;
      this.challenges = await api.getChallenges();
      this.loading = false;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h2 {
  margin-top: 80px;
  margin-bottom: 80px;
  font-size: 40px;
}
</style>
