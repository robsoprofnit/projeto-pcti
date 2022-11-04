// var recaplic = document.getElementById("recurso_aplicado").getContext("2d");
// var rechuman = document.getElementById("rechuman").getContext("2d");
// var bolforma = document.getElementById("bolforma").getContext("2d");
// var prodcien = document.getElementById("prodcien").getContext("2d");
// var patentes = document.getElementById("patentes").getContext("2d");
// var inovacao = document.getElementById("inovacao").getContext("2d");

// var myChart = new Chart(recurso_aplicado, {
//   type: "bar",
//   data: {
//     datasets: [
//         {% for resposta in respostas %}
//             {
//             data: [{{resposta.resposta}}],
//             label: "Ciência e Tecnologia",
//             borderColor: ["blue"],
//             backgroundColor: ["blue"],
//             },
//         {% endfor %}
//     //   {
//     //     data: [45],
//     //     label: "Pesquisa e Desenvolvimento",
//     //     borderColor: ["orange"],
//     //     backgroundColor: ["orange"],
//     //   },
//     //   {
//     //     data: [10],
//     //     label: "Atividades Científicas e Técnicas Correlata",
//     //     borderColor: ["green"],
//     //     backgroundColor: ["green"],
//     //   },
//     ],
//     labels: ["2021"],
//   },
//   options: {},
// });

// var myChart = new Chart(rechuman, {
//   type: "bar",
//   data: {
//     datasets: [
//       {
//         data: [0, 20, 50],
//         label: "Privado sem fins lucrativos",
//         borderColor: ["blue"],
//         backgroundColor: ["blue"],
//       },
//       {
//         data: [0, 12, 45],
//         label: "Governo",
//         borderColor: ["yellow"],
//         backgroundColor: ["yellow"],
//       },
//       {
//         data: [0, 37, 10],
//         label: "Empresarial",
//         borderColor: ["green"],
//         backgroundColor: ["green"],
//       },
//       {
//         data: [0, 23, 40],
//         label: "Ensino superior",
//         borderColor: ["purple"],
//         backgroundColor: ["purple"],
//       },
//       {
//         data: [0, 92, 145],
//         label: "Total",
//         borderColor: ["brown"],
//         backgroundColor: ["brown"],
//       },
//     ],
//     labels: ["2019", "2020", "2021"],
//   },
//   options: {},
// });

// var myChart = new Chart(bolforma, {
//   type: "line",
//   data: {
//     datasets: [
//       {
//         data: [0, 20, 50],
//         label: "no País",
//         borderColor: ["blue"],
//         backgroundColor: ["blue"],
//       },
//       {
//         data: [0, 12, 45],
//         label: "no Exterior",
//         borderColor: ["orange"],
//         backgroundColor: ["orange"],
//       },
//       {
//         data: [0, 32, 95],
//         label: "Total",
//         borderColor: ["green"],
//         backgroundColor: ["green"],
//       },
//     ],
//     labels: ["2019", "2020", "2021"],
//   },
//   options: {},
// });

// var mixedChart = new Chart(prodcien, {
//   data: {
//     datasets: [
//       {
//         type: "line",
//         data: [0, 2.76, 2.32],
//         label: "% em relação ao Mundo",
//         borderColor: ["blue"],
//         backgroundColor: ["blue"],
//         yAxisID: "right-y-axis",
//       },
//       {
//         type: "bar",
//         data: [0, 89241, 90000],
//         label: "Nº de artigos",
//         borderColor: ["yellow"],
//         backgroundColor: ["yellow"],
//         yAxisID: "left-y-axis",
//       },
//     ],
//     labels: ["2019", "2020", "2021"],
//   },
//   options: {
//     scales: {
//       "left-y-axis": {
//         type: "linear",
//         position: "left",
//       },
//       "right-y-axis": {
//         type: "linear",
//         position: "right",
//       },
//     },
//   },
// });

// var myChart = new Chart(patentes, {
//   type: "line",
//   data: {
//     datasets: [
//       {
//         data: [0, 45, 56],
//         label: "Total",
//         borderColor: ["green"],
//         backgroundColor: ["green"],
//       },
//       {
//         data: [0, 35, 44],
//         label: "Patente de Invenção",
//         borderColor: ["yellow"],
//         backgroundColor: ["yellow"],
//       },
//       {
//         data: [0, 10, 12],
//         label: "Modelo de Utilidade",
//         borderColor: ["cyan"],
//         backgroundColor: ["cyan"],
//       },
//     ],
//     labels: ["2019", "2020", "2021"],
//   },
//   options: {},
// });

// var myChart = new Chart(inovacao, {
//   type: "bar",
//   data: {
//     datasets: [
//       {
//         data: [0, 20, 50],
//         label: "Total",
//         borderColor: ["blue"],
//         backgroundColor: ["blue"],
//       },
//       {
//         data: [0, 12, 45],
//         label: "Industria",
//         borderColor: ["yellow"],
//         backgroundColor: ["yellow"],
//       },
//       {
//         data: [0, 37, 10],
//         label: "Serviços",
//         borderColor: ["green"],
//         backgroundColor: ["green"],
//       },
//       {
//         data: [0, 23, 40],
//         label: "Eletricidade e Gás",
//         borderColor: ["purple"],
//         backgroundColor: ["purple"],
//       },
//     ],
//     labels: ["2019", "2020", "2021"],
//   },
//   options: {},
// });
