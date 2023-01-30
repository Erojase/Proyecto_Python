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
    let username = document.getElementById("log_usename").value;
    let password = MD5.generate(document.getElementById("log_passwd").value)
    let content = JSON.stringify({
        "user": username,
        "password": password
    });
    if (username.length < 3 || document.getElementById("log_passwd").value.length < 8) {
        console.error("Esto no va asi campeón");
        return "ja"
    }
    let response = await fetch('/login', { 
        method: "POST",
        headers: headersList,
        body: content 
    });

    let data = await response.text();
    console.log(data);
}

async function register() {
    let username = document.getElementById("reg_username").value;
    let password = MD5.generate(document.getElementById("reg_passwd").value)
    let mail = document.getElementById("reg_mail").value;
    let content = JSON.stringify({
        "user": username,
        "password": password,
        "mail":mail
    });
    let response = await fetch('/register', { 
        method: "POST",
        headers: headersList,
        body: content 
    });

    let data = await response.text();
    console.log(data);
}