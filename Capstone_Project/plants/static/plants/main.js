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
            // console.log(response.data.hints)
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
        message: 'Recipe/Meals Database',
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

// function buildCard(data) {
//     const energy = data.nutrients.ENERC_KCAL ? `<li><b>Energy: </b><span>${data.nutrients.ENERC_KCAL.toFixed(1)}kcal</span></li>` : ''
//     const carbs = data.nutrients.CHOCDF ? `<li><b>Carbs: </b><span>${data.nutrients.CHOCDF.toFixed(1)}g</span></li>` : ''
//     const protein = data.nutrients.PROCNT ? `<li><b>Protein: </b><span>${data.nutrients.PROCNT.toFixed(1)}g</span></li>` : ''
//     const fat = data.nutrients.FAT ? `<li><b>Fat: </b><span>${data.nutrients.FAT.toFixed(1)}g</span></li>` : ''

//     const html = `
//     <div class="card">
//       <div class="card-header">
//         <h3>${data.label}</h3>
//         <h4>${data.category}</h4>
//       </div>
//       <div class="card-body">
//         <ul>
//           ${energy}
//           ${carbs}
//           ${protein}
//           ${fat}
//         </ul>
//       </div>
//       <div class="card-footer">
//         <p><b>Brand: </b><span>${data.brand || 'None :('}</span></p>
//       </div>
//     </div>
//     `

//     return html