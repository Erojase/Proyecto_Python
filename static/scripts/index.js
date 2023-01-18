let headersList = {
    "Accept": "*/*",
    "User-Agent": "Thunder Client (https://www.thunderclient.com)"
}
   

document.addEventListener('DOMContentLoaded', ()=>{






});

function testActions() {
    let response = fetch('/testAction', { 
        method: "POST",
        headers: headersList
    });
}

function calendario() {
    window.location.href = '/calendario';
}