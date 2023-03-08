

let headersList = {
    Accept: "*/*",
    "Content-Type": "application/json",
  };

document.addEventListener("DOMContentLoaded", () => {
  tareas_load();
});



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

async function tareas_load() {
  
  let token = window.localStorage.getItem("token");
  headersList["Authorization"] = "Bearer "+token;

  let response = await fetch('/tasker/getTask', { 
    method: "POST",
    headers: headersList,
  });

  let data = await response.text();
  console.log(data)

  let ul = document.getElementById('lista_tareas')

  dato.forEach(tarea => {
    let li = createElement('li')
    let asig = createElement('ul')
    asig.innerHTML = data['Asignatura']
    let tit = createElement('ul')
    tit.innerHTML = data['Titulo']
    let desc = createElement('ul')
    desc.innerHTML = data['Descripcion']
    let inp = createElement('input')
    inp.type = 'file'
    inp.id = data['Titulo']
    let btn = createElement('button')
    btn.innerHTML = 'Entregar'
    btn.addEventListener("click", entregarTarea(), false);
    li.appendChild(asig)
    li.appendChild(tit)
    li.appendChild(desc)
    li.appendChild(inp)
    li.appendChild(btn)
    ul.appendChild(li)
  });





}
