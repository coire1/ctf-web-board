<template>
  <div class="home">
    <Rank :users="users" />
  </div>
</template>

<script>
import api from "@/api";
import Rank from "@/components/Rank.vue";

export default {
  name: "home",
  components: {
    Rank
  },
  data() {
    return {
      loading: false,
      users: []
    };
  },
  async created() {
    this.refreshRank();
  },
  methods: {
    async refreshRank() {
      this.loading = true;
      this.users = await api.getRank();
      this.loading = false;
    }
  }
};
</script>
