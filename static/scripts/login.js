let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}

document.addEventListener('DOMContentLoaded', ()=>{

});

function toggle(obj) {
    if (obj == "reg") {
        document.getElementById("login").style.display = 'none';
        document.getElementById("register").style.display = 'flex';
    } else{
        document.getElementById("register").style.display = 'none';
        document.getElementById("login").style.display = 'flex';
    }
}


async function login() {
    let username = document.getElementById("log_username").value;
    let password = MD5.generate(document.getElementById("log_passwd").value)
    let content = JSON.stringify({
        "nick": username,
        "password": password
    });
    if (username.length < 3 || document.getElementById("log_passwd").value.length < 8) {
        console.error("Esto no va asi campeón");
        warning("Esto no va asi campeón");
        return "ja"
    }
    let response = await fetch('/login', { 
        method: "POST",
        headers: headersList,
        body: content 
    });

    let data = await response.text();
    console.log(data);
    if (response.ok) {
        window.localStorage.setItem("token", data);
        window.location.href = '/web';
    } else{
        warning(data);
    }
    
}


async function register() {
    let username = document.getElementById("reg_name").value;
    let mail = document.getElementById("reg_mail").value;
    let tipo = document.getElementById("tipo").value;
    let password = MD5.generate(document.getElementById("reg_passwd").value);
    let password2 = MD5.generate(document.getElementById("re_reg_passwd").value);
    if (password == password2 && /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(mail)) {
        let content = JSON.stringify({
            "user": username,
            "password": password,
            "mail": mail,
            "tipo":tipo
        });
        let response = await fetch('/register', { 
            method: "POST",
            headers: headersList,
            body: content 
        });
        
        let data = await response.text();
        console.log(data);
        if (response.ok) {
            window.location.href = '/web';
        } else{
            warning(data);
        }
        
        
        
    } else{
        warning("Algun input no es válido");
    }
    
}   

function warning(text) {
    let warning = document.createElement("div");
        warning.innerHTML = text.replaceAll("\"", "");
        warning.style.backgroundColor = "red";
        warning.style.padding = "20px";
        warning.style.borderRadius = "10px";
        warning.style.position = "absolute";
        warning.style.margin = "10px";
        warning.style.fontWeight = "bold";
        warning.style.textAlign = "center";
        warning.classList.add("texto-warning");
        document.body.appendChild(warning);
        setTimeout(() => {
            document.getElementsByClassName("texto-warning")[0].remove();
        }, 2000);
}