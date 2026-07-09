
// ==============================
// PIE CHART
// ==============================

const pieCtx = document.getElementById("pieChart");

if (pieCtx) {

new Chart(pieCtx, {

type: "pie",

data: {

labels: wasteLabels,

datasets: [{

data: wasteCounts,

backgroundColor: [

"#198754",
"#20c997",
"#fd7e14",
"#0dcaf0",
"#0d6efd",
"#6c757d",
"#ffc107",
"#6610f2",
"#d63384",
"#dc3545"

]

}]

},

options: {

responsive: true

}

});

}
// ==============================
// LINE CHART (Real-Time)
// ==============================

const lineCtx = document.getElementById("lineChart");

if (lineCtx) {

new Chart(lineCtx,{

type:"line",

data:{

labels:dailyLabels,

datasets:[{

label:"Predictions",

data:dailyCounts,

borderColor:"#198754",

backgroundColor:"rgba(25,135,84,0.2)",

fill:true,

borderWidth:3,

pointRadius:6,

pointBackgroundColor:"#198754",

tension:0.4

}]

},

options:{

responsive:true,

maintainAspectRatio:false,

plugins:{

legend:{display:false}

},

scales:{

x:{

grid:{display:false}

},

y:{

beginAtZero:true,

ticks:{stepSize:1}

}

}

}

});

}