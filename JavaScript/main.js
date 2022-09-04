const chart = require('chart.js')
let viewData1, viewData2, viewData3; //to be used to store data in ArduVisualize
const ctx = document.getElementById("arduvisualizeChart");
const labels = Utils.months({count: 7});
const data = {
    labels: labels,
    datasets:[viewData1, viewData2, viewData3]
}