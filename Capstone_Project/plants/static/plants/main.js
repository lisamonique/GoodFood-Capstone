let foodDataBase = new Vue({
    el: "#foodDataBase",
    delimiters: ['[[', ']]'],
    data: {
        message: 'Food Library',
        userQuery: '',
        categories: '',
        selectedCategory: '',
        ingrResult: [
        
        ]
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
        // console.log(response.data.hints)
        this.categories = response.data.hints
    }
})

let recipeDataBase = new Vue({
    el: "#recipeDataBase",
    delimiters: ['[[', ']]'],
    data: {
        message: 'Food Recipe Search',
        userQuery: '',
        categories: '',
        selectedCategory: '',
        mealsResult: [{
            label: '',
            image: '',
            url: '',
            mealType: '',

        }]
    },
    methods: {
        searchMeals: async function() {
            let response = await axios({
                method: 'get',
                url: "../viewRecipe/",
                params: {
                    q : this.userQuery,
                    categoryLabel: this.selectedCategory
                }
            })
            console.log(response.data.hits)
            this.mealsResult = response.data.hits
        }
    },
    created: async function () {
        let response = await axios({
            method: 'get',
            url: '../viewRecipe/'
        })
        // console.log(response.data.hits)
        this.categories = response.data.hits
    }
})


window.onscroll = function() {myFunction()};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function myFunction() {
    if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
    } else {
    header.classList.remove("sticky");
    }
}