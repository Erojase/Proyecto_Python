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
    let cont = 0;
    for (const grupo in grupos) {
        cont = 0;
        grupos[grupo].forEach(dia => {
            grupos[grupo][dias[cont]] = dia;
            delete grupos[grupo][cont];
            cont++;
        });
    }

}

function cargarGrupo() {
    let ElHoras = document.getElementsByClassName("hora");
    let currgrp = {}
    currgrp = grupos[selector.value];
    for(const key in currgrp){
        tmpdict = {}
        grupos[selector.value][key].forEach((hora, i) => {
            if(hora != "None"){
                // currgrp[key][i] = JSON.parse(hora);
                newkey = parseInt(JSON.parse(hora)['tiempo'].split(':')[0])-1
                +":"
                +JSON.parse(hora)['tiempo'].split(':')[1]
                +" - "
                +parseInt(JSON.parse(hora)['tiempo'].split(':')[0])
                +":"
                +JSON.parse(hora)['tiempo'].split(':')[1];
                tmpdict[newkey] = JSON.parse(hora);
            } else{
                tmpdict["None"+i] = "None"
            }
            currgrp[key] = tmpdict;
        });
    }
    console.log(currgrp);

    for(const elem of ElHoras){
        for (const key in currgrp) {
            for (const key2 in currgrp[key]) {
                if (key2 == elem.innerText) {
                    console.log("");
                    console.log(key);// dia de la semana
                    console.log(elem.innerText); //rango de horas
                    console.log(currgrp[key][key2]);
                    for (const el of elem.parentNode.getElementsByTagName('td')) {
                        if(el.className == key){
                            el.style.border = "1px solid black";
                            el.style.borderRadius = "5px";
                            el.innerText = "";
                            el.innerText += currgrp[key][key2]["nombre"] + "\n";
                            el.innerText += key2 ;
                        }
                    }
                };
            }
            
        }
        // console.log(elem.innerHTML);
    }

}