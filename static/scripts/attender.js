let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}

async function connect_clase_Click() {
    
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

    add_alumno()

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

    console.log(data);
    console.log(JSON.parse(data)["user"]);
    

    var ul = document.getElementById('lista_alumnos');
    var li = document.createElement('li');
    li.appendChild(document.createTextNode(JSON.parse(data)["user"]));
    li.appendChild(document.createTextNode('imagen de este alumno'));
    ul.appendChild(li);
    ul.style.visibility = "hidden";

}

