
let app = new Vue({
    el: '#game',
    delimiters: ['[[', ']]'],
    data:{
        message: 'Hello from Vue',
        questions: []
        // some data
    },
    methods: {

    },
    created: async function () {
        let response = await axios({
            method: 'get',
            url:'../getQuiz/'
        })
    }
})
