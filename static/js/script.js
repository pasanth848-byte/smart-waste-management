/* ==========================================
      SMART WASTE MANAGEMENT
========================================== */

// Wait until page loads
document.addEventListener("DOMContentLoaded", function () {

    animateCounters();

    showWelcomeMessage();

    updateClock();

    setInterval(updateClock, 1000);

});

/* ==========================================
      IMAGE PREVIEW
========================================== */

function previewImage(event){

    const file = event.target.files[0];

    const preview = document.getElementById("preview");

    if(file){

        preview.src = URL.createObjectURL(file);

        preview.style.display = "block";

    }

}

/* ==========================================
      LIVE CLOCK
========================================== */

function updateClock(){

    let now = new Date();

    let time = now.toLocaleTimeString();

    let date = now.toDateString();

    if(document.getElementById("time"))

        document.getElementById("time").innerHTML = time;

    if(document.getElementById("date"))

        document.getElementById("date").innerHTML = date;

}

/* ==========================================
      DARK MODE
========================================== */

function toggleDarkMode(){

    document.body.classList.toggle("dark-mode");

    if(document.body.classList.contains("dark-mode")){

        localStorage.setItem("theme","dark");

    }

    else{

        localStorage.setItem("theme","light");

    }

}

window.onload=function(){

    if(localStorage.getItem("theme")=="dark"){

        document.body.classList.add("dark-mode");

    }

}

/* ==========================================
      SEARCH HISTORY
========================================== */

function searchTable(){

let input=document.getElementById("search");

if(!input) return;

let filter=input.value.toUpperCase();

let table=document.getElementById("historyTable");

let tr=table.getElementsByTagName("tr");

for(let i=1;i<tr.length;i++){

let td=tr[i].getElementsByTagName("td")[2];

if(td){

let txt=td.textContent || td.innerText;

if(txt.toUpperCase().indexOf(filter)>-1){

tr[i].style.display="";

}

else{

tr[i].style.display="none";

}

}

}

}

/* ==========================================
      COUNTER ANIMATION
========================================== */

function animateCounters(){

const counters=document.querySelectorAll(".counter");

counters.forEach(counter=>{

counter.innerText="0";

const target=+counter.getAttribute("data-target");

const update=()=>{

const count=+counter.innerText;

const increment=target/100;

if(count<target){

counter.innerText=Math.ceil(count+increment);

setTimeout(update,20);

}

else{

counter.innerText=target;

}

}

update();

});

}

/* ==========================================
      PROGRESS BAR
========================================== */

window.addEventListener("load",()=>{

let bars=document.querySelectorAll(".progress-bar");

bars.forEach(bar=>{

let width=bar.style.width;

bar.style.width="0";

setTimeout(()=>{

bar.style.width=width;

},400);

});

});

/* ==========================================
      NOTIFICATION
========================================== */

function showWelcomeMessage(){

setTimeout(()=>{

showToast("♻ Welcome to Smart Waste Management");

},1000);

}

function showToast(message){

let toast=document.createElement("div");

toast.className="toast-message";

toast.innerHTML=message;

document.body.appendChild(toast);

setTimeout(()=>{

toast.classList.add("show");

},100);

setTimeout(()=>{

toast.remove();

},3500);

}

/* ==========================================
      LOADER
========================================== */

function showLoader(){

let loader=document.getElementById("loader");

if(loader){

loader.style.display="flex";

}

}

function hideLoader(){

let loader=document.getElementById("loader");

if(loader){

loader.style.display="none";

}

}

/* ==========================================
      PRINT REPORT
========================================== */

function printReport(){

window.print();

}

/* ==========================================
      DOWNLOAD CSV
========================================== */

function downloadCSV(){

alert("CSV Export feature can be connected with Flask backend.");

}

/* ==========================================
      CONFIRM DELETE
========================================== */

function confirmDelete(){

return confirm("Are you sure you want to delete this record?");

}

/* ==========================================
      SCROLL TO TOP
========================================== */

function scrollTopBtn(){

window.scrollTo({

top:0,

behavior:"smooth"

});

}

/* ==========================================
      ACTIVE MENU
========================================== */

const links=document.querySelectorAll(".sidebar ul li");

links.forEach(link=>{

link.addEventListener("click",()=>{

links.forEach(l=>l.classList.remove("active"));

link.classList.add("active");

});

});

/* ==========================================
      FADE ANIMATION
========================================== */

const cards=document.querySelectorAll(".card");

cards.forEach((card,index)=>{

card.style.opacity="0";

card.style.transform="translateY(30px)";

setTimeout(()=>{

card.style.transition=".6s";

card.style.opacity="1";

card.style.transform="translateY(0px)";

},index*150);

});