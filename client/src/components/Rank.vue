<template>
  <div class="rank">
    <h2>Rank</h2>
    <div class="standing-wrapper">
      <div class="heading row">
        <div class="pos">#</div>
        <div class="name">Name</div>
        <div class="points">Points</div>
        <div class="bloods">Bloods</div>
      </div>
      <div v-for="(user, index) in users" class="row" :key="user.id">
        <div class="pos">{{ index + 1 }}</div>
        <div class="name">{{ user.username }}</div>
        <div class="points">{{ user.points }}</div>
        <div class="bloods">{{ user.bloods }}</div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Rank",
  props: ["users"]
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h2 {
  margin-top: 80px;
  margin-bottom: 80px;
  font-size: 40px;
}
.standing-wrapper {
  width: 100%;
  float: left;
  display: table;
  border-collapse: collapse;
  border-spacing: 30px 10px;
  margin-bottom: 160px;
  .row {
    display: table-row;
    font-size: 25px;
    margin-bottom: 30px;
    & > div {
      display: table-cell;
      padding-top: 20px;
    }
    .name {
      text-transform: uppercase;
    }
    .bloods {
      color: red;
    }

    &.heading {
      border-bottom: 5px solid #fff;
      & > div {
        padding-bottom: 20px;
        padding-top: 0;
      }
    }
  }
}
</style>
