let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}

document.addEventListener('DOMContentLoaded', ()=>{})

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
    let username = document.getElementById("name").value;
    let password = MD5.generate(document.getElementById("passwd").value)
    let content = JSON.stringify({
        "user": username,
        "password": password
    });
    let response = await fetch('/login', { 
        method: "POST",
        headers: headersList,
        body: content 
    });

    let data = await response.text();
    console.log(data);
    window.localStorage.setItem("token", data);
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
        // window.location.href = '/login';
    } else{
        let warning = document.createElement("div");
        warning.innerHTML = "Algo salió mal";
        warning.style.backgroundColor = "red";
        warning.style.textAlign = "center";
        document.body.appendChild(warning);
    }
    
}   

