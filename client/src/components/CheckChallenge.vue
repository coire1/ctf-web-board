<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div @click="$emit('close')" class="close">X</div>
          <input v-model="username" type="text" name="username" placeholder="USERNAME" />
          <input v-model="flag" type="text" name="flag" placeholder="FLAG" />
          <button v-on:click="checkChallenge">SUBMIT FLAG</button>
        </div>
      </div>
      <div class="response blood" v-if="isBlood">
        <div class="message">YO HACKER!<br />YOU GOT BLOOD!!!</div>
      </div>
      <div class="response flag" v-if="isFlag">
        <div class="message">GOOD JOB!!!<br />YOU GOT THE FLAG!</div>
      </div>
      <div class="response wrong-flag" v-if="wrongFlag">
        <div class="message">OOOOPS!!! WRONG FLAG!</div>
      </div>
      <div class="response wrong-flag" v-if="alreadyFlagged">
        <div class="message">OOOOPS!!! YOU ALREADY GOT THE FLAG!</div>
      </div>
    </div>
  </transition>
</template>

<script>
import api from "@/api";
export default {
  name: "checkChallenge",
  props: ["challenge"],
  data() {
    return {
      username: "",
      flag: "",
      result: false
    };
  },
  computed: {
    isBlood() {
      return this.result.blood && this.result.flag && !this.result.exists;
    },
    isFlag() {
      return !this.result.blood && this.result.flag && !this.result.exists;
    },
    wrongFlag() {
      return !this.result.blood && !this.result.flag && this.result;
    },
    alreadyFlagged() {
      return this.result.exists && this.result;
    }
  },
  methods: {
    async checkChallenge() {
      if (this.username && this.flag) {
        this.loading = true;
        this.result = await api.checkChallenge(this.challenge.id, {
          username: this.username,
          key: this.flag
        });
        setTimeout(this.resetCheck, 3000);
        this.loading = false;
      }
    },
    resetCheck() {
      this.result = false;
      this.$emit("close");
      this.$emit("updateRank");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 800px;
  margin: 0px auto;
  padding: 60px 50px;
  background-color: #000;
  border: 5px solid #fff;
  transition: all 0.3s ease;
  position: relative;
  input {
    font-family: "Press Start 2P", cursive;
    font-size: 30px;
    -webkit-appearance: none;
    background: #424040;
    color: #fff;
    width: 100%;
    float: left;
    margin-bottom: 30px;
    border: none;
    outline: 0;
    padding: 10px;
  }
  button {
    font-family: "Press Start 2P", cursive;
    font-size: 30px;
    color: #fff;
    width: 100%;
    text-align: center;
    background: #424040;
    outline: 0;
    border: none;
    padding: 10px;
    cursor: pointer;
  }
}

.response {
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  position: absolute;
  background: #000;
  z-index: 9999;
  font-size: 50px;
  text-align: center;
  .message {
    position: absolute;
    top: 50%;
    left: 0;
    width: 100%;
    transform: translateY(-50%);
  }
  &:not(.blood) {
    animation: blink 1s linear infinite;
  }
  &.blood {
    background: red;
    animation: blink-blood 1s linear infinite;
  }
}

.close {
  position: absolute;
  top: 5px;
  right: 2px;
  font-size: 25px;
  cursor: pointer;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

@keyframes blink {
  0% {
    background: #000;
    color: #fff;
  }
  49% {
    background: #000;
    color: #fff;
  }
  50% {
    background: #fff;
    color: #000;
  }
  100% {
    background: #fff;
    color: #000;
  }
}

@keyframes blink-blood {
  0% {
    background: red;
    color: #fff;
  }
  49% {
    background: red;
    color: #fff;
  }
  50% {
    background: #fff;
    color: red;
  }
  100% {
    background: #fff;
    color: red;
  }
}
</style>
