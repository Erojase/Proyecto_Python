let headersList = {
    Accept: "*/*",
    // "Content-Type": "application/json",
  };

document.addEventListener("DOMContentLoaded", () => {
  // console.log('tumadre')
  // tareas_load();
  getGrupos()
  
});

async function getGrupos() {
    
  let token = window.localStorage.getItem("token");
  headersList["Authorization"] = "Bearer "+token;

  let response = await fetch('attendance/mongo', {
      method: "GET",
      headers: headersList
  })

  let data = await response.text()

  let div = document.getElementById("caja")
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

async function subirtarea() {
    let titulo = document.getElementById("titulo").value;
    let tarea = document.getElementById("tarea").value;
    let grupo = document.getElementById("Grupos").value;

    let token = window.localStorage.getItem('token');
    headersList["Authorization"] = "Bearer "+token;
    let content = JSON.stringify({
      titulo: titulo, //esto hatml
      tarea: tarea, //esto lo coje el html
      grupo : grupo
    });
    let response = await fetch("/tasker", {
      method: "POST",
      headers: headersList,
      body: content,
    });

    let data = await response.text();
    console.log(data);
  }

// async function tareas_load() {
//   console.log('tumadre')
//   let token = window.localStorage.getItem("token");
//   headersList["Authorization"] = "Bearer "+token;

//   let response = await fetch('/tasker/getTask', { 
//     method: "POST",
//     headers: headersList,
//   });

//   let data = await response.text();
  




// }

