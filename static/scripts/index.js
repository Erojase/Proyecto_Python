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
    window.location.href = '/attendance';

    
}

function report(){
    let token = window.localStorage.getItem("token");
    if (token != null) {
        window.location.href = '/tasker?token='+token;
    }
}

function discord(){
    window.location.href = '/report';
}

function mail(){
    window.location.href = '/mail';
}
