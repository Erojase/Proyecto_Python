

let headersList = {
    "Accept": "*/*",
}

document.addEventListener('DOMContentLoaded', ()=>{
    setInterval(() => {
        add_alumno();
    }, 1000);
})

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
    
    let clave = JSON.stringify(document.getElementById("cod_profe").value);
    let token = window.localStorage.getItem("token");
    headersList["Authorization"] = "Bearer "+token;

    let response = await fetch('/attendance', { 
        method: "POST",
        headers: headersList,
        body: clave
    });

    let data = await response.text();
    console.log(data);

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
                li.appendChild(document.createTextNode("Imagen"))    
                ul.appendChild(li)
            });
        }
        
    }

    

    // ul.style.visibility = "hidden";

}

