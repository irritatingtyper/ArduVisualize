let dataValues1 = [5, 3, 7, 2, 7, 3, 8, 2, 5, 1, 8];
let dataValues2 = [8, 5, 9, 1, 9, 8, 2, 1, 7, 9, 3];
let dataValues3 = [6, 9, 9, 9, 1, 8, 7, 3, 7, 8, 6];

const sessionName = 'ArduVisualize Demo';
const graphType = 'line';
const labels_temp = ['A', 'B', 'C'];
const graphColor1 = 'rgb(8, 11, 194)';
const graphColor2 = 'rgb(222, 4, 41)';
const graphColor3 = 'rgb(28, 235, 9)';

const labels = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
];

const data = {
    labels: labels,
    datasets: [{
        label: labels_temp[0],
        backgroundColor: graphColor1,
        borderColor: graphColor1,
        data: dataValues1,
    },
{
    label: labels_temp[1],
    backgroundColor: graphColor2,
    borderColor: graphColor2,
    data: dataValues2,
},
{
    label: labels_temp[2],
    backgroundColor: graphColor3,
    borderColor: graphColor3,
    data: dataValues3,
}]
};

const config = {
    type: graphType,
    data: data,
    options: {}
};

const myChart = new Chart(
    document.getElementById('myChart'),
    config
);