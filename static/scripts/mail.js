let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}


document.addEventListener('DOMContentLoaded', ()=>{getUsers()});

async function getUsers() {
    let mailSelector = document.getElementById('reciever');
    let response = await fetch('/listUsers', { 
        method: "GET",
        headers: headersList,
    });

    let data = await response.text();

    for (const mail of JSON.parse(data)) {
        let obj = document.createElement('option');
        obj.value = mail;
        obj.text = mail;
        mailSelector.appendChild(obj);
    }

    console.log(JSON.parse(data));
}

async function sendMail() {
    let mailSelector = document.getElementById('reciever');
    let to = document.getElementById('reciever').value;
    let subject = document.getElementById('subject').value;
    let body = document.getElementById('body').value
    let content = JSON.stringify({
        "to": to,
        "subject": subject,
        "body":body
    });
    let response = await fetch('/sendMail', { 
        method: "POST",
        headers: headersList,
        body: content
    });
    let data = await response.text();
    console.log(JSON.parse(data));
}