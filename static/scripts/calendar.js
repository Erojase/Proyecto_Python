let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}
const dias = ["Lunes","Martes","Miercoles","Jueves","Viernes"]
let selector;
let grupos = {}

document.addEventListener('DOMContentLoaded', ()=>{
    selector = document.getElementById("group");
    selector.addEventListener('change', cargarGrupo);

});

async function testData() {
    let response = await fetch('/calTest', { 
        method: "GET",
        headers: headersList,
    });

    let data = await response.text();
    // console.log(JSON.parse(data));
    loadTable(JSON.parse(data))
}

function loadTable(data){
    // semana data[0]
    // dia data[0][0]
    // hora data [0][0][0]
    
    data.forEach(grupo => {
        grpName = JSON.parse(grupo[0][0])['grupo'];
        let opt = document.createElement('option');
        opt.value = grpName;
        opt.text = grpName;
        selector.appendChild(opt);

        grupos[grpName] = grupo;
    });
    console.log(grupos);
    let cont = 0;
    for (const grupo in grupos) {
        console.log(grupo);
        cont = 0;
        grupos[grupo].forEach(dia => {
            grupos[grupo][dias[cont]] = dia;
            delete grupos[grupo][cont];
            cont++;
        });
    }
}

function cargarGrupo() {
    let currgrp = grupos[selector.value];
    
}