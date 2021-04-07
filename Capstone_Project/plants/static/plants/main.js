let foodDataBase = new Vue({
    el: "#foodDataBase",
    data: {
        message: 'Food Database',
        userQuery: '',
        ingrResult: [{
            label: '',
            image: ''
        }],
        // food: '',
        // label: ''
    },
    methods: {
        searchIngr: function() {
            let response = await axios({
                method: 'get',
                url: "https://api.edamam.com/api/food-database/v2/parser?app_id={app_id}&app_key={app_key}&ingr={ingr}",
                params: {
                    app_id: APP_ID,
                    app_key: APP_KEY,
                    ingr : this.userQuery
                }
            })
            console.log(response.data)
            // this.userQuery = ""
            // this.ingrResult = response.data
        }
        // some data
    }
})
