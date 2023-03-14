let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}


document.addEventListener('DOMContentLoaded', ()=>{
    getAsignaturas();
    loadUserData(window.localStorage.getItem("token"));

});

async function loadUserData(token){
    let parsedToken = parseJwt(window.localStorage.getItem("token"));
    headersList["Authorization"] = "Bearer "+token;

    let response = await fetch('/info/'+parsedToken["nick"], { 
        method: "GET",
        headers: headersList
    });

    let data = JSON.parse(await response.text());

    let campos = document.getElementById("infoForm").children;

    campos["nick"].value = data["nick"];
    campos["nombre"].value = data["nombre"];
    campos["mail"].value = data["mail"];
    campos["tipo"].value = data["tipo"];

    if (data["tipo"] != "Profesor") {
        HideTeacherFields(campos);
    } else {
        ShowTeacherFields(campos);
        campos["tutor"].checked = data["tutor"];
    }

    
}

function HideTeacherFields(campos) {
    campos[8].style.visibility = "hidden";
    campos["tutor"].style.visibility = "hidden";
    campos[10].style.visibility = "hidden";
    campos["asignaturas"].style.visibility = "hidden";
    campos[12].style.visibility = "hidden";
    campos["horario"].style.visibility = "hidden";
    
}

function ShowTeacherFields(campos) {
    campos[8].style.visibility = "visible";
    campos["tutor"].style.visibility = "visible";
    campos[10].style.visibility = "visible";
    campos["asignaturas"].style.visibility = "visible";
    campos[12].style.visibility = "visible";
    campos["horario"].style.visibility = "visible";
}

async function updateUser() {
    let campos = document.getElementById("infoForm").children;
    

    let parsedToken = parseJwt(window.localStorage.getItem("token"));
    headersList["Authorization"] = "Bearer "+token;

    let response = await fetch('/info/update/'+parsedToken["nick"], { 
        method: "PUT",
        headers: headersList,
        body: {}
    });

    let data = JSON.parse(await response.text());
}

function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}

async function getAsignaturas() {
    
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;

    let response = await fetch('horario/mongo/asignaturas', {
        method: "GET",
        headers: headersList
    })

    let data = await response.text()

    let div = document.getElementById("asignaturas")
    let select = document.createElement("select")
    select.id = "Asignaturas"
    JSON.parse(data).forEach(asign => {
        let op = document.createElement("option")
        op.value = asign
        op.innerText = asign
        select.appendChild(op)
    });
    div.appendChild(select)
}

let asignaturas = [];
function añadirAsignaturas(){
    let asign = document.getElementById("Asignaturas").value;
    let ul = document.getElementById("lista_asignaturas");
    let li = document.createElement('li');
    li.className = "asignatura"

    let quitar = document.createElement('input');
    quitar.type = 'button';
    quitar.style.margin = "10px";
    quitar.value = "x";
    quitar.addEventListener("click", (e)=>{quitarAsignaturas(e)});

    li.innerText = asign;
    ul.appendChild(li);
    li.appendChild(quitar);
}

function quitarAsignaturas(e){
    e.target.parentNode.remove();
}