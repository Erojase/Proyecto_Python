
let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}
   

document.addEventListener('DOMContentLoaded', ()=>{
});
// function testActions() {
//     let response = fetch('/testAction', { 
//         method: "POST",
//         headers: headersList
//     });
// }

function calendario() {
    window.location.href = '/calendario';
}

function Parking() {
    window.location.href = '/parking';
}

function asistencia() {
    window.location.href = '/asistencia';
}

function report(){
    window.location.href = '/tasker';
}

function discord(){
    window.location.href = '/report';
}

function mail(){
    window.location.href = '/mail';
}