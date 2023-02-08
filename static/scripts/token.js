


document.addEventListener('DOMContentLoaded', async ()=>{
    let headersList = {
        "Accept": "*/*",
        "Content-Type": "application/json"
    }
    
    token = window.localStorage.getItem("token");
    if (token != null) {
        headersList["Authorization"] = "Bearer "+token;
        let response = await fetch('/token', { 
            method: "POST",
            headers: headersList,
        });

    let data = await response.text();
    console.log(data);
    }
    
});