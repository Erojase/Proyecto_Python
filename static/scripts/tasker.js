let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}

document.addEventListener('DOMContentLoaded', ()=>{})



async function subir() {
let tarea = document.getElementById("tarea").value;
let titulo = document.getElementById("titulo").value;
let content = JSON.stringify({
    "tarea": tarea, //esto lo coje el html
    "titulo": titulo //esto hatml
})


}


    // let username = document.getElementById("name").value;
    // let password = MD5.generate(document.getElementById("passwd").value)
    // let content = JSON.stringify({
    //     "user": username,
    //     "password": password
    // });
    // let response = await fetch('/login', { 
    //     method: "POST",
    //     headers: headersList,
    //     body: content 
    // });

    // let data = await response.text();
    // console.log(data);
