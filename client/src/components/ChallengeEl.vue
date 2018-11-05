<template>
  <div class="wrapper">
    <div class="single-challenge">
      <div class="name">
        <router-link :to="{ name: 'challenge', params: { id: challenge.id }}">
          {{ challenge.name }}
        </router-link>
      </div>
      <div class="description">{{ challenge.description }}</div>
      <div class="address">{{ challenge.address }}</div>
      <div class="base-points">Flag points: {{ challenge.base_points }}</div>
      <div class="blood-points">Blood points: {{ challenge.blood_points }}</div>
      <div class="button" @click="showModal = true">Submit flag</div>
      <check-challenge :challenge="challenge" v-if="showModal" @close="showModal = false" @updateRank="updateRank()" />
    </div>
  </div>
</template>

<script>
import CheckChallenge from "@/components/CheckChallenge.vue";

export default {
  name: "ChallengeEl",
  components: {
    CheckChallenge
  },
  props: {
    challenge: {}
  },
  data() {
    return {
      showModal: false
    };
  },
  methods: {
    updateRank() {
      this.$emit("updateRank");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.single-challenge {
  width: 100%;
  float: left;
  margin-bottom: 80px;
  a,
  a:visited {
    color: #fff;
  }
  & > div:not(.modal-mask) {
    width: 100%;
    float: left;
    margin-bottom: 20px;
  }
  .name {
    font-size: 30px;
    margin-bottom: 30px !important;
    text-transform: uppercase;
  }
  .description {
    font-size: 22px;
    line-height: 25px;
  }
  .address {
    float: left;
    width: auto !important;
    padding: 20px;
    font-family: Monaco, courier, monospace;
    background: #424040;
  }
  .blood-points {
    margin-bottom: 30px !important;
    color: red;
  }
  .button {
    width: auto !important;
    // text-decoration: underline;
    text-transform: uppercase;
    font-size: 20px;
    cursor: pointer;
    border: 5px solid white;
    padding: 10px;
    &:hover {
      color: black;
      background: white;
    }
  }
}
</style>
