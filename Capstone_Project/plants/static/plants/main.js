// let foodDataBase = new Vue({
//     el: "#foodDataBase",
//     data: {
//         message: 'Food Database',
//     },
//     methods: {
//         // some data
//     },
//     created: async function () {
//         let response = await axios({
//             method: 'get',
//             url: 'https://api.edamam.com/api/food-database/v2/parser?ingr=red%20apple&app_id=' + app_id + '&app_key=' + app_key,
//             params: {
//                 app_id: APP_ID,
//                 app_key: APP_KEY
//             }
//         }).then((response) => {
//             console.log(response)
//         })
//         // some data
//         // some data
//     }
// })

// // Make the actual CORS request.
// function makeCorsRequest() {
//     let app_id = document.getElementById('app_id').value;
//     let app_key = document.getElementById('app_key').value;
//     let recipe = document.getElementById('recipe').value;
//     let pre = document.getElementById('response');
  
//     var url = 'https://api.edamam.com/api/nutrition-details?app_id=' + app_id + '&app_key=' + app_key;
  
//     var xhr = createCORSRequest('POST', url);
//     if (!xhr) {
//       alert('CORS not supported');
//       return;
//     }