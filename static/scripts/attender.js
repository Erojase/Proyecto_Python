

let headersList = {
    "Accept": "*/*",
}

document.addEventListener('DOMContentLoaded', ()=>{
    setInterval(() => {
        add_alumno();
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
    // let img = document.getElementById("img_alumn").files[0];


    let dat = new FormData();
    // dat.append("img", img);

    // console.log(img);

    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;
    headersList["clave"] = clave;

    let response = await fetch('/attendance', { 
        method: "POST",
        headers: headersList,
        // body: dat
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

    JSON.parse(data)['Alumnos'].forEach(alumno => {
        let nombre = alumno.split("@")[0].replaceAll("."," ");
        let li = document.createElement('li');
        li.innerText = nombre;
        let check = document.createElement("input");
        check.type = "checkbox";
        check.className = "checks";
        check.disabled = true;
 
        li.appendChild(check)
        ul.appendChild(li)
    });

}

async function add_alumno() {
    
    let token = parseJwt(window.localStorage.getItem("token"));
    

    if (token["tipo"] == 'Profesor') {
            headersList["Authorization"] = "Bearer "+window.localStorage.getItem("token");
            let response = await fetch('/attendance/getclass', { 
            method: "POST",
            headers: headersList
        });

        let dato = await response.text();

        console.log(dato);

        let checks = document.getElementsByClassName("checks");

        if (dato != '' && JSON.parse(dato)['Checks'] != null) {
            let cont = 0;
            JSON.parse(dato)['Checks'].forEach(check => {
                if (check == "1"){
                    checks[cont].checked = true;
                }
                cont++;
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


async function crear_informe() {
    
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;

    let dat = JSON.stringify(document.getElementById("poa").value)

    let responce = await fetch('/attendance/fichero', { 
        method: "POST",
        headers: headersList,
        body: dat
    });

    let dato = await responce.text();

    console.log(dato)

    let a = document.createElement('a');

    a.download = "/static/attender/Asistencia.txt"
    // a.innerHTML = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    a.href = "/static/attender/Asistencia.txt"
    document.body.appendChild(a)
    a.click();
    document.body.removeChild(a)
    

}


function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}