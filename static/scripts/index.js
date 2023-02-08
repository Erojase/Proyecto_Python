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
    let token = window.localStorage.getItem("token");
    console.log('/attendance?token='+token);
    if (token != null) {
        window.location.href = '/attendance?token='+token;
    }
    
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
