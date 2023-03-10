let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}
const dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
let selector;
let grupos = {}

document.addEventListener('DOMContentLoaded', () => {
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer " + token;
    document.getElementById("main").click();
    selector = document.getElementById("group");
    selector.addEventListener('change', cargarGrupo);
    getProfesores();
    getAsignaturas();

});

function hideAllTabs() {
    let tabs = document.getElementsByClassName("tab");
    let butonTabs = document.getElementsByClassName("tabBtn");
    for (const tab of tabs) {
        tab.style.display = "none";
    }
    for (const tabtn of butonTabs) {
        tabtn.style.border = "solid 1px black";
    }
}

function toggleTab(curr, thisTab) {
    let tab = document.getElementsByClassName(thisTab)[0];
    hideAllTabs();
    tab.style.display = "block";
    curr.style.borderBottom = "none";
}

async function testData() {
    let response = await fetch('/calTest', {
        method: "GET",
        headers: headersList,
    });

    let data = await response.text();
    // console.log(JSON.parse(data));
    loadTable(JSON.parse(data))
}

function loadTable(data) {
    selector.innerHTML = "";
    // semana data[0]
    // dia data[0][0]
    // hora data [0][0][0]

    let vacio = document.createElement('option');
    vacio.value = "none";
    vacio.text = "vacio";
    selector.appendChild(vacio);

    data.forEach(grupo => {

        grpName = JSON.parse(grupo[0][0])['grupo'];
        let opt = document.createElement('option');
        opt.value = grpName;
        opt.text = grpName;
        selector.appendChild(opt);

        grupos[grpName] = grupo;
    });
    let cont = 0;
    for (const grupo in grupos) {
        cont = 0;
        grupos[grupo].forEach(dia => {
            grupos[grupo][dias[cont]] = dia; cargarGrupo
            delete grupos[grupo][cont];
            cont++;
        });
    }

}

function cargarGrupo() {
    let ElHoras = document.getElementsByClassName("hora");
    let currgrp = {}
    currgrp = Object.create(grupos[selector.value]);
    for (const key in currgrp) {
        tmpdict = {}
        grupos[selector.value][key].forEach((hora, i) => {
            if (hora != "None") {
                let newkey = parseInt(JSON.parse(hora)['tiempo'].split(':')[0]) - 1 + ":" + JSON.parse(hora)['tiempo'].split(':')[1] + " - " + parseInt(JSON.parse(hora)['tiempo'].split(':')[0]) + ":" + JSON.parse(hora)['tiempo'].split(':')[1];
                tmpdict[newkey] = JSON.parse(hora);
            } else {
                tmpdict["None" + i] = "None"
            }
            currgrp[key] = tmpdict;
        });
    }

    for (const elem of ElHoras) {
        for (const key in currgrp) {
            for (const key2 in currgrp[key]) {
                if (key2 == elem.innerText) {
                    // console.log("");
                    // console.log(key);// dia de la semana
                    // console.log(elem.innerText); //rango de horas
                    // console.log(currgrp[key][key2]);
                    for (const el of elem.parentNode.getElementsByTagName('td')) {
                        if (el.className == key) {
                            el.style.border = "1px solid black";
                            el.style.borderRadius = "5px";
                            el.innerText = "";
                            el.innerText += currgrp[key][key2]["nombre"] + "\n";
                            el.innerText += key2;
                        }
                    }
                };
            }
        }
    }
}

function añadirAsignaturas(){
    let asign = document.getElementById("Asignaturas").value;
    let ul = document.getElementById("lista_asignaturas");
    let li = document.createElement('li');
    li.className = "asignatura"
    li.innerText = asign;
    ul.appendChild(li)
}

let tutores = [];
function añadirProfesores(){
    let asign = document.getElementById("Profesores").value;
    let ul = document.getElementById("lista_profesores");
    let li = document.createElement('li');
    li.className = "profesor"
    let check = document.createElement('input');
    check.type = 'checkbox';
    check.style.margin = "10px";
    check.addEventListener("change", (e)=>{
        if (e.target.checked) {
            tutores.push(e.target.parentNode.innerText)
        } else{
            tutores.splice(tutores.indexOf(e.target.parentNode.innerText), 1);
        }
    });

    li.innerText = asign;
    ul.appendChild(li)
    li.appendChild(check);
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

async function getProfesores() {
    
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;

    let response = await fetch('horario/mongo/profesores', {
        method: "GET",
        headers: headersList
    })

    let data = await response.text()

    let div = document.getElementById("profesores")
    let select = document.createElement("select")
    select.id = "Profesores"
    JSON.parse(data).forEach(user => {
        let op = document.createElement("option")
        op.value = user
        op.innerText = user
        select.appendChild(op)
    });
    div.appendChild(select)
}

async function crearGrupos() {
    let nombre = document.getElementById("nombre_grupo").value;
    let turno = document.getElementById("turno").value;

    let lista_asignaturas = document.getElementsByClassName("asignatura");
    let lista_profesores = document.getElementsByClassName("profesor");
    let asignaturas = [];
    let profesores = [];

    for(const elem of lista_asignaturas){
        asignaturas.push(elem.innerText);
    }

    for(const elem of lista_profesores){
        profesores.push(elem.innerText);
    }

    
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;

    let response = await fetch('/horario/mongo/crear', {
        method: "POST",
        headers: headersList,
        body: JSON.stringify({
            "nombre":nombre,
            "asignaturas": asignaturas,
            "profesores": profesores,
            "tutor": tutores,
            "horario": turno 
        })
    });

    let res = await response.text();
    console.log(res);
}


