let app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data:{
        message: 'Hello from Vue',
        baseURL: '/capstone/fruitveggie.json',
        amount: "",
        questions: []
        // some data
    },

    methods: {
        getQuiz: async function () {
            const response = await axios({
                method: 'get',
                url: this.baseURL
            })
        },
        decodeHTML: function (html) {
            const txt = document.createElement('textarea');
            txt.innerHTML = html;
            return txt.value;
        }
        // some data
    },
    created: async function () {
        const response = await axios({
            method: 'get',
            url: this.baseURL
        })
        // this.blank()
        // this.blank()
    }
})