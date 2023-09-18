
let texta = window.document.getElementById("content-text")
let button = window.document.getElementById("sendbutton")
let statuslabel = window.document.getElementById("status")
let voicesLabel = window.document.getElementById("voices")
let voicesAvalaibleLabel = window.document.getElementById("availablevoices")
let section_all_voices = window.document.getElementById("allvoices__section")

//HARDCODE
async function getvoices() {
    let response = await fetch("http://localhost:5000/api/getVoices");

    let voicesJson = await response.json();
    console.log(voicesJson);
    voicesLabel.innerText = ""

    Object.keys(voicesJson).forEach(function (k) {
        Object.keys(k).forEach(function (a) {
            voicesLabel.innerHTML += "<article class=\"articulo__voz\"> <p>" + k + ' - ' + voicesJson[k][a] + "</p> </article>";
        });
    });
}
async function getvoicesAvalaible() {
    let response = await fetch("http://localhost:5000/api/getVoicesAvalaible");

    let voicesAJson = await response.json();
    console.log(voicesAJson);

    voicesAvalaibleLabel.innerText = ""

    Object.keys(voicesAJson).forEach(function (k) {
        voicesAvalaibleLabel.innerHTML += "<article class=\"articulo__voz\"> <p>" + k + ' prefix = '+ ' <span class=\"voice--prefix\"> ' + voicesAJson[k]["prefix"] + "</span></p> </article>";
    });
}

//

button.onclick = async () => {
    statuslabel.innerText = "generating"
    let headersList = {
        "Accept": "*/*",
        "User-Agent": "Thunder Client (https://www.thunderclient.com)",
        "Content-Type": "application/json"
    }

    let bodyContent = JSON.stringify({
        "contenttext": texta.value
    });

    let response = await fetch("http://localhost:5000/api/generate", {
        method: "POST",
        body: bodyContent,
        headers: headersList
    });

    let data = await response.text();
    statuslabel.innerText = "ready"
    console.log(data);


}

getvoicesAvalaible()
getvoices()