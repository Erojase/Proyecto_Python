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

    console.log(data);

    campos["nick"].value = data["nick"];
    campos["nombre"].value = data["nombre"];
    campos["mail"].value = data["mail"];
    campos["tipo"].value = data["tipo"];
    
    if (data["tipo"] != "Profesor") {
        HideTeacherFields(campos);
    } else {
        ShowTeacherFields(campos);
        campos["tutor"].checked = data["tutor"];
        addAsignaturas(data["asignaturas"]);
        addHoras(data["horario"]);
    }

    
}

function addAsignaturas(sourceData) {
    if (sourceData != null) {
        let asignaturas = document.getElementById("lista_asignaturas");
        for (const asignatura of sourceData) {
            let li = document.createElement('li');
            li.className = "asignatura"

            let quitar = document.createElement('input');
            quitar.type = 'button';
            quitar.style.margin = "10px";
            quitar.value = "x";
            quitar.addEventListener("click", (e)=>{quitarAsignaturas(e)});

            li.innerText = asignatura;
            asignaturas.appendChild(li);
            li.appendChild(quitar);
        }
    }
}

function addHoras(sourceData) {
    if (sourceData != null) {
        let horario = document.getElementById("horario");
        let horas = horario.getElementsByTagName("div");
        let index = 0;
        sourceData.forEach(dia => {
            horas[index].children[1].value = dia[0];
            horas[index+1].children[1].value = dia[1];
            index+=2;
        });
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
    campos["marco"].style.visibility = "visible";
}

async function updateUser() {
    let campos = document.getElementById("infoForm").children;
    
    let body = {
        "nick": campos["nick"].value,
        "nombre": campos["nombre"].value,
        "mail": campos["mail"].value,
        "tipo": campos["tipo"].value
    };

    if (campos["tipo"].value == "Profesor") {
        let HTMLasignaturas = document.getElementById("lista_asignaturas").children;
        let asignaturas = [];
        for (const asignatura of HTMLasignaturas) {
            if (asignatura.innerText != "") {
                asignaturas.push(asignatura.innerText);
            }
        }

        let HTMLHorario = document.getElementById("horario").getElementsByTagName("div");
        let i = 0;
        let horario =[]
        let dia = []
        for (const hora of HTMLHorario) {
            dia.push(hora.children[1].value);
            if (i == 1) {
                horario.push(dia);
                dia = [];
                i = -1;
            }
            i++
        }


        body["tutor"] = campos["tutor"].checked;
        body["horario"] = horario;
        body["asignaturas"] = asignaturas;
    }
    console.log(body);
    let parsedToken = parseJwt(window.localStorage.getItem("token"));
    headersList["Authorization"] = "Bearer "+window.localStorage.getItem("token");

    let response = await fetch('/info/update/'+parsedToken["nick"], { 
        method: "PUT",
        headers: headersList,
        body: JSON.stringify(body)
    });

    let data = await response.text();
    console.log(data);
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