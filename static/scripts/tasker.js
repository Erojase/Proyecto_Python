let headersList = {
    Accept: "*/*",
    // "Content-Type": "application/json",
  };

document.addEventListener("DOMContentLoaded", () => {
  // console.log('tumadre')
  // tareas_load();
  
});


async function subirtarea() {
    let titulo = document.getElementById("titulo").value;
    let tarea = document.getElementById("tarea").value;

    let token = window.localStorage.getItem('token');
    headersList["Authorization"] = "Bearer "+token;
    let content = JSON.stringify({
      titulo: titulo, //esto hatml
      tarea: tarea, //esto lo coje el html
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

