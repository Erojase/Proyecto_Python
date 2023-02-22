

let headersList = {
    Accept: "*/*",
    "Content-Type": "application/json",
  };

document.addEventListener("DOMContentLoaded", () => {});



// terminar
async function presentarTarea() {

  let archiv = document.getElementById("subir_archivo").files;

  let dat = new FormData();
  dat.append("archiv", archiv);

  console.log(archiv);

  let token = window.localStorage.getItem("token");
  headersList["Authorization"] = "Bearer "+token;
  headersList["clave"] = clave;

  let response = await fetch("/tasker", {
    method: "POST",
    headers: headersList,
    body: archiv
  });
} 



// terminar
async function tienes_tarea(){

let dato = await responce.text();

console.log(dato);

let ul = document.getElementById('lista_tareas');
ul.innerHTML = '';

if (dato != '' && JSON.parse(dato)['traeas'] != null){
  let li = document.createElement('li');
  li.appendChild("tarea")
}
}