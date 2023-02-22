

let headersList = {
    "Accept": "*/*",
}

document.addEventListener('DOMContentLoaded', ()=>{
    setInterval(() => {
        // add_alumno();
    }, 1000);

    getGrupos();

    // let div = document.getElementById("profe")
    // let select = document.createElement("select")
    // select.id = clases
    // let op = document.createElement("option")
     

})



async function getGrupos() {
    
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;

    let response = await fetch('attendance/mongo', {
        method: "GET",
        headers: headersList
    })

    let data = await response.text()

    let div = document.getElementById("profe")
    let select = document.createElement("select")
    select.id = "Grupos"
    JSON.parse(data).forEach(group => {
        let op = document.createElement("option")
        op.value = group
        op.innerText = group
        select.appendChild(op)
    });
    div.appendChild(select)
}


async function connect_clase_Click() {
    
    let clave = document.getElementById("cod_profe").value;
    let img = document.getElementById("img_alumn").files[0];


    let dat = new FormData();
    dat.append("img", img);

    console.log(img);

    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;
    headersList["clave"] = clave;

    let response = await fetch('/attendance', { 
        method: "POST",
        headers: headersList,
        body: dat
    });
    
    let data = await response.text();
    console.log(data);

    // add_alumno()

}

async function create_clase_Click() {
    
    let clave = document.getElementById("cod_profe").value;
    let grupo = document.getElementById("Grupos").value;
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;
    headersList["Content-Type"] = "application/json"

    let clave_clase = document.getElementById('clave_clase')
    clave_clase.innerText = clave

    let datos = [clave,grupo]

    let response = await fetch('/attendance', { 
        method: "POST",
        headers: headersList,
        body: JSON.stringify(datos)
    });

    let data = await response.text();
    console.log(data);

    let ul = document.getElementById('lista_alumnos');
    ul.innerHTML = '';

    JSON.parse(data)['alumnos'].forEach(alumno => {
        let nombre = alumno.split("@")[0].replaceAll("."," ");
        let li = document.createElement('li');
        li.innerText = nombre;
        let boton_elim = document.createElement("button")
        boton_elim.innerText = "X"
        boton_elim.id = nombre;
        boton_elim.addEventListener("click", hechar_de_clase, false);
        // let imglink = document.createElement("a");
        // imglink.href = "/static/attender/"+alumno+".png";
        // imglink.target = "_blank";
        // imglink.innerText = " Abrir Imagen"
        // li.appendChild(imglink)    
        li.appendChild(boton_elim)
        ul.appendChild(li)
    });

}

async function add_alumno() {
    
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;
    let response = await fetch('/token', { 
        method: "POST",
        headers: headersList,
     });

    let data = await response.text();

    if (JSON.parse(data)["tipo"] == 'Profesor') {
            headersList["Authorization"] = "Bearer "+token;
        let responce = await fetch('/attendance/getclas', { 
            method: "POST",
            headers: headersList,
            body: JSON.parse(data)["user"]
        });

        let dato = await responce.text();

        console.log(dato);
    
        let ul = document.getElementById('lista_alumnos');
        ul.innerHTML = '';
    
        if (dato != '' && JSON.parse(dato)['alumnos'] != null) {
            JSON.parse(dato)['alumnos'].forEach(alumno => {
                let li = document.createElement('li');
                li.innerText = alumno;
                let boton_elim = document.createElement("button")
                boton_elim.innerText = "X"
                boton_elim.id = alumno;
                boton_elim.addEventListener("click", hechar_de_clase, false);
                let imglink = document.createElement("a");
                imglink.href = "/static/attender/"+alumno+".png";
                imglink.target = "_blank";
                imglink.innerText = " Abrir Imagen"
                li.appendChild(imglink)    
                li.appendChild(boton_elim)
                ul.appendChild(li)
            });
        }
        
    }

    

    // ul.style.visibility = "hidden";

}

async function hechar_de_clase() {

    let clave = JSON.stringify(document.getElementById("clave_clase").value);
    let user = JSON.stringify(this.id)
    console.log(user);
    
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;

    let responce = await fetch('/attendance/hechar', { 
        method: "POST",
        headers: headersList,
        body: user
    });

    let dato = await responce.text();

    console.log(dato);

}
