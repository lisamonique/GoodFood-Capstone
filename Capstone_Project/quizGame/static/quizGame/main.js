
const term = document.querySelector('#term');
const definition = document.querySelector('#definition');
const checkButton = document.querySelector('#check');
const nextButton = document.querySelector('#next');
let input = document.querySelector('#userInput');

let score = 0
let flip = true

words = {
    "Name a fruit that starts with 'A'. It is white on the inside and can be red, yellow, or green on the outside.": "Apple",
    "Name a spiny, green vegetable that starts with 'A'." : "Artichoke",
    "Name a long, thin fruit that starts with 'B'. It is yellow on the outside and white on the inside.": "Banana",
    "Name a long, thin, orange vegetable that grows underground. It starts with a 'C'.": "Carrot",
    "Name a crisp, green vegetable that has long stalks. It starts with 'C'.": "Celery",
    "Name a yellow vegetable that grows on a cob and starts with 'C'.": "Corn",
    "Name a vegetable that is green on the outside and white on the inside. It starts with 'C'.": "Cucumber",
    "Name a purple vegetable that starts with 'E'.": "Eggplant",
    "Name a big fruit that starts with 'G'. It can be yellow or pink and sometimes squirts you when you eat it.": "Grapefruit",
    "Name a sweet fruit that grows in bunches on vines. It starts with 'G'.": "Grapes",
    "You can cook fruit with sugar to make a sweet spread that tastes good on bread. What is this spread called? It starts with 'J'.": "Jam",
    "Name a sour, yellow fruit that starts with 'L'.": "Lemon",
    "Name a green, leafy vegetable that tastes good in salads. It starts with an 'L'.": "Lettuce",
    "Name a sour, green fruit that starts with 'L'.": "Lime",
    "Name a type of big fruit that has a rind. It starts with 'M'.": "Melon",
    "Name an oily, green fruit that starts with 'O'.": "Olive",
    "Name a sharp-tasting vegetable that starts with 'O'. It grows underground.": "Onion",
    "Name a sweet fruit that start with the letter 'P' and grows on trees. ": "Peach",
    "Name a tiny, round green vegetable that grows in pods. It starts with 'P'.": "Peas",
    "Name a vegetable that is brown on the outside and white on the inside. It grows underground and starts with the letter 'P'.": "Potato",
    "Name an orange vegetable that can be made into pie. It starts with 'P'.": "Pumpkin",
    "What do you get when you dry a plum? It starts with 'P'.": "Prune",
    "What do you get when you dry a grape? It starts with 'R'.": "Raisin",
    "Name a sweet, red fruit that starts with 'S'.": "Strawberry",
    "Name a soft, red fruit that starts with 'T'. It is not sweet.": "Tomato",
    "Name a sweet fruit that starts with 'W'. It is green on the outside and pink on the inside.": "Watermelon",
    "Name a sweet, orange vegetable that starts with 'Y'. It grows underground and can be made into pie.": "Yam",
    }

data = Object.entries(words)

function getRandomWord() {
    randomTerm = data[Math.floor(Math.random() * data.length)]
    term.innerHTML = `<h3>${randomTerm[0]}</h3>`;
    definition.innerHTML = `<h3>${randomTerm[1]}</h3>`;
}

checkButton.addEventListener('click', function() {
    definition.style.display = 'block'; 
});

nextButton.addEventListener('click', function() {
    getRandomWord();
});

button.addEventListener('click', function(){
    // alert(input.value) 
    // if user input equals answer flip card and show answer; else alert wrong answer,
    header.innerText = input.value
})





// let app = new Vue({
//     el: '#app',
//     delimiters: ["[[", "]]"],
//     data: {
//         term: '',
//         definition: '',
//         baseURL: '../getQuiz/'
//     },
//     methods: {
//         getRandomWord: async function() {
//             let randomIndex = Math.floor(Math.random() * data.length)
//             let randomTerm = data[randomIndex]
//             let response = await axios({
//                 url: '../getQuiz/'
//             })
//             console.log(response)
//             // this.term = randomTerm[0]
//             // this.definition = randomTerm[1]
//         }
//     }
// })

// let app = new Vue({
//     el: '#app',
//     delimiters: ['[[', ']]'],
//     data: {
//         baseURL: '../edamam/',
//         veggie_question: '',
//         veggie_answer: '',
//         questions: []
//     },
//     methods: {
//         getQuiz: async function () {
//             const response = await axios({
//                 method: 'get',
//                 url: this.baseURL,
//                 params: {

//                 }
//             })
//             console.log(response)
            // let questions = response.data.results
            // for (question of questions) {
            //     this.questions.push({
            //         question: question.question,
            //         answers: [question.correct_answer].concat(question.incorrect_answers)
            //     })
            // }
    //     },
    //     decodeHTML: function (html) {
    //         const txt = document.createElement('textarea');
    //         txt.innerHTML = html;
    //         return txt.value;
    //     }

    // },
    // created: async function () {
    //     const response = await axios({
    //         method: 'get',
    //         url: 'https://opentdb.com/api_category.php'
    //     })
    //     this.categories = response.data.trivia_categories
    // }
// })