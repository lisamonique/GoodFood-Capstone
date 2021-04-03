

let app = new Vue({
    el: '#app',
    data: {
        question: '<b>Quiz Game Question</b>',
        answer: '<b>Quiz Game Answer</b>',
        quiz: '',
        qa: ''
    },
    methods: {

    },
    created: async function () {
        let response = await axios({
            method: 'get',
            url: 'getQuestion/'
        })
    }
})
