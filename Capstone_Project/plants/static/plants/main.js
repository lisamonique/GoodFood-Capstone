let foodDataBase = new Vue({
    el: "#foodDataBase",
    delimiters: ['[[', ']]'],
    data: {
        message: 'Food Database',
        userQuery: '',
        ingrResult: [{
            label: '',
            image: ''
        }]
    },
    methods: {
        searchIngr: async function() {
            let response = await axios({
                method: 'get',
                url: "../edamam/",
                params: {
                    ingr : this.userQuery
                }
            })
            // console.log(response.data.hints)
            this.ingrResult = response.data.hints
        }
    }
})

