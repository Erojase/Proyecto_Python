let toggleSession = false;
document.addEventListener("DOMContentLoaded", async () => {

    let headersList = {
        Accept: "*/*",
        "Content-Type": "application/json",
    };
    try {
        let token = window.localStorage.getItem("token");
        if (token != null) {
            headersList["Authorization"] = "Bearer " + token;
            let response = await fetch("/token", {
                method: "POST",
                headers: headersList,
            });

            let data = await response.text();
            console.log(data);
            replaceLoginWithName(data)
        }
    } catch (error) {
        document.getElementById("loginAnchor").innerHTML = "Login";
        document.getElementById("loginAnchor").removeEventListener("click");
     }
});


function replaceLoginWithName(data) {
    document.getElementById("loginAnchor").innerHTML = JSON.parse(data)["nick"];
    document.getElementById("loginAnchor").addEventListener("click", click);
}

function click(event) {
    event.preventDefault();
    if (!toggleSession) {
        let context = document.createElement("div");
    context.style.backgroundColor = "#242424";
    context.style.color = "white";
    context.style.position = "absolute";
    context.style.marginTop = "10px";
    context.style.padding = "10px";
    context.style.borderRadius = "5px";
    context.innerHTML = "Cerrar Sesion";
    context.id = "cerrarSesion";

    context.addEventListener("click", ()=>{
        logout();
    });

    document.getElementById("loginAnchor").appendChild(context)
    } else{
        document.getElementById("cerrarSesion").remove();
    }
    toggleSession = !toggleSession;
    
}

function logout() {
    window.localStorage.removeItem("token");
    window.location.href = window.location.href;
}