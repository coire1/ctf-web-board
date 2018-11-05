<template>
  <div class="challenge">
    <ChallengeEl :challenge="challenge" @updateRank="refreshRank()" />
    <Rank :users="users" />
  </div>
</template>

<script>
// @ is an alias to /src
import api from "@/api";
import ChallengeEl from "@/components/ChallengeEl.vue";
import Rank from "@/components/Rank.vue";

export default {
  name: "challenge",
  components: {
    ChallengeEl,
    Rank
  },
  data() {
    return {
      loading: false,
      challenge: [],
      users: []
    };
  },
  async created() {
    this.refreshChallenge();
    this.refreshRank();
  },
  methods: {
    async refreshChallenge() {
      this.loading = true;
      this.challenge = await api.getChallenge(this.$route.params.id);
      this.loading = false;
    },
    async refreshRank() {
      this.loading = true;
      this.users = await api.getChallengeRank(this.$route.params.id);
      this.loading = false;
    }
  }
};
</script>

<style scoped lang="scss">
.challenge {
  width: 100%;
  float: left;
  margin-top: 80px;
}
</style>
