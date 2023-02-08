let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}

async function connect_clase_Click() {
    
    let clave = document.getElementById("cod_profe").value;
    console.log(clave)

    let response = await fetch('/attendance', { 
        method: "POST",
        headers: headersList,
        body: clave
    });



    let data = await response.text();
    console.log(data);
}

async function create_clase_Click() {
    
    let clave = document.getElementById("cod_profe").value;
    

    let response = await fetch('/attendance', { 
        method: "POST",
        headers: headersList,
        body: clave
    });

    let data = await response.text();
    console.log(data);

}

