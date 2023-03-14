let toggleSession = false;
document.addEventListener("DOMContentLoaded", async () => {
    let token = window.localStorage.getItem("token");
    try {
        if (token != null) {
            token = parseJwt(token);
            replaceLoginWithName(token);
        }
    } catch (error) {
        document.getElementById("loginAnchor").innerHTML = "Login";
        document.getElementById("loginAnchor").removeEventListener("click");
     }
});


function replaceLoginWithName(data) {
    document.getElementById("loginAnchor").innerHTML = data["nick"];
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
        document.getElementById("containeroo").remove();
    }
    toggleSession = !toggleSession;
    
}

function logout() {
    window.localStorage.removeItem("token");
    window.location.href = "/web";
}

function info() {
    window.location.href = "/info";
}

function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}