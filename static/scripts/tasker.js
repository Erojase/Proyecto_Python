let headersList = {
    Accept: "*/*",
    "Content-Type": "application/json",
  };

document.addEventListener("DOMContentLoaded", () => {});


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


