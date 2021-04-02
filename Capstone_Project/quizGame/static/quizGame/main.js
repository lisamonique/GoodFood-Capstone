let app = new Vue({
    el: '#app',
    data: {
        question: '<b>Quiz Game Question</b>',
        answer: '<b>Quiz Game Answer</b>',
    },
})

// const axios = require("axios");
// export default {
//   name: "app2",
//   data() {
//     return {
//       data: {}
//     };
//   },
//   beforeMount(){
//     this.getName();
//   },
//   methods: {
//     async getName(){
//       const { data } = await axios.get("https://api.agify.io/?name=michael");
//       this.data = data;
//     }
//   }
// };