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

        let btnLogout = document.createElement("div");
        btnLogout.style.backgroundColor = "#242424";
        btnLogout.style.color = "white";
        btnLogout.style.position = "relative";
        btnLogout.style.marginTop = "10px";
        btnLogout.style.padding = "10px";
        btnLogout.style.borderRadius = "5px";
        btnLogout.innerHTML = "Cerrar Sesion";
        btnLogout.id = "cerrarSesion";

        btnLogout.addEventListener("click", ()=>{
            logout();
        });

        let btnInfo = document.createElement("div");
        btnInfo.style.backgroundColor = "#242424";
        btnInfo.style.color = "white";
        btnInfo.style.position = "relative";
        btnInfo.style.marginTop = "10px";
        btnInfo.style.padding = "10px";
        btnInfo.style.borderRadius = "5px";
        btnInfo.innerHTML = "Info";
        btnInfo.id = "editInfo";

        btnInfo.addEventListener("click", ()=>{
            info();
        });

        let div = document.createElement("div");
        div.style.backgroundColor = "#242424";
        div.style.color = "white";
        div.style.position = "absolute";
        div.style.marginTop = "10px";
        div.style.padding = "10px";
        div.style.borderRadius = "5px";
        div.style.zIndex = "100";
        div.id = "containeroo";

        div.appendChild(btnInfo);
        div.appendChild(btnLogout);
        document.getElementById("loginAnchor").appendChild(div);
       
    } else{
        document.getElementById("cerrarSesion").remove();
    }
    toggleSession = !toggleSession;
    
}

function logout() {
    window.localStorage.removeItem("token");
    window.location.href = window.location.href;
}