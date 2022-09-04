import serial
import pandas as pd

# Functions of the application
def dataCollection(port, baudR, frequency):
    openCSV = open('data.csv', 'w')
    ser = serial.Serial(port, baudrate=baudR, timeout=5)
    i = 0
    openCSV.write("A,B,C" + "\n")

    while i <= frequency:
        arduinoData = ser.readline().decode("ISO-8859-1")
        openCSV.write(arduinoData)
        i += 1
    
    openCSV.close()

def prepareData(daGraph, sessionName):
    trueSessionName = sessionName

    trueDF = pd.read_csv("data.csv")
    print(trueDF)
    getColumn1 = trueDF["A"].to_numpy()
    print(getColumn1)
    getColumn1 = list(getColumn1)

    getColumn2 = trueDF["B"].to_numpy()
    print(getColumn2)
    getColumn2 = list(getColumn2)

    getColumn3 = trueDF["C"].to_numpy()
    print(getColumn3)
    getColumn3 = list(getColumn3)

    jsonContent = """let dataValues1 = {column1};
let dataValues2 = {column2};
let dataValues3 = {column3};

const sessionName = '{sessName}';
const graphType = '{graph}';
const labels_temp = ['A', 'B', 'C'];
const graphColor1 = 'rgb(8, 11, 194)';
const graphColor2 = 'rgb(222, 4, 41)';
const graphColor3 = 'rgb(28, 235, 9)';\n\n""".format(column1=getColumn1, column2=getColumn2, column3=getColumn3, graph=daGraph, sessName = trueSessionName)

    jsonContentNonEditable = """const labels = [
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
);"""
    writeFile = open("graph_details.js", "w")
    writeFile.write(jsonContent)
    writeFile.write(jsonContentNonEditable)
    writeFile.close()