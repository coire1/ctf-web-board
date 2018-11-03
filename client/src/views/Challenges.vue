<template>
  <div class="challenges">
    <ChallengesList />
  </div>
</template>

<script>
// @ is an alias to /src
import ChallengesList from "@/components/ChallengesList.vue";

export default {
  name: "challenges",
  components: {
    ChallengesList
  }
};
</script>
