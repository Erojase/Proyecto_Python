let headersList = {
    Accept: "*/*",
    "Content-Type": "application/json",
  };

document.addEventListener("DOMContentLoaded", () => {

  var video = document.createElement('video');
video.setAttribute('playsinline', '');
video.setAttribute('autoplay', '');
video.setAttribute('muted', '');
video.style.width = '200px';
video.style.height = '200px';

/* Setting up the constraint */
var facingMode = "user"; // Can be 'user' or 'environment' to access back or front camera (NEAT!)
var constraints = {
  audio: false,
  video: {
   facingMode: facingMode
  }
};

/* Stream it to video element */
console.log(navigator.);
navigator.mediaDevices.getUserMedia(constraints).then(function success(stream) {
  video.srcObject = stream;
});

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


