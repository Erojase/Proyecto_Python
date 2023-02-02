let headersList = {
    "Accept": "*/*",
    "Content-Type": "application/json"
}


async function testData() {
    let response = await fetch('/calTest', { 
        method: "GET",
        headers: headersList,
    });

    let data = await response.text();
    console.log(JSON.parse(data));
    loadTable(JSON.parse(data))
}

function loadTable(data){
    // semana data[0]
    // dia data[0][0]
    // hora data [0][0][0]
    let selector = document.getElementById("group");
    let grupos = []
    data.forEach(grupo => {
        let opt = document.createElement('option');
        opt.value = JSON.parse(grupo[0][0])['grupo'];
        opt.text = JSON.parse(grupo[0][0])['grupo'];
        selector.appendChild(opt);
    });





}