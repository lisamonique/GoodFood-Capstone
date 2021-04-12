let foodDataBase = new Vue({
    el: "#foodDataBase",
    delimiters: ['[[', ']]'],
    data: {
        message: 'Food Database',
        userQuery: '',
        categories: '',
        selectedCategory: '',
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
                    ingr : this.userQuery,
                    categoryLabel: this.selectedCategory
                }
            })
            console.log(response.data.hints)
            this.ingrResult = response.data.hints
        }
    },
    created: async function () {
        let response = await axios({
            method: 'get',
            url: '../edamam/'
        })
        console.log(response.data.hints)
        this.categories = response.data.hints
    }
})

