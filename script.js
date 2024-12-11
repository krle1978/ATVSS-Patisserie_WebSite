fetch('http://127.0.0.1:5000/api/test')
    .then(response => response.json())
    .then(data => console.log(data.message))
    .catch(error => console.error('Greška:', error));

let sastojci = [];
let porudzbina = [];

document.getElementById("dodaj-sastojak").addEventListener("click", () => {
    const naziv = document.getElementById("sastojak-name").value;
    const kalorije = parseInt(document.getElementById("kalorije").value, 10);
    const cena = parseFloat(document.getElementById("cena").value);

    if (naziv && kalorije && cena) {
        sastojci.push({ naziv, kalorije, cena });

        const li = document.createElement("li");
        li.textContent = `${naziv} (Kalorije: ${kalorije}, Cena: ${cena} RSD)`;
        document.getElementById("sastojci-lista").appendChild(li);

        document.getElementById("sastojak-name").value = "";
        document.getElementById("kalorije").value = "";
        document.getElementById("cena").value = "";
    }
});

document.getElementById("kreiraj-kolac").addEventListener("click", () => {
    const ime = document.getElementById("kolac-name").value;
    const osnovneKalorije = parseInt(document.getElementById("osnovne-kalorije").value, 10);
    const osnovnaCena = parseFloat(document.getElementById("osnovna-cena").value);

    if (ime && osnovneKalorije && osnovnaCena) {
        const kolac = {
            ime,
            osnovneKalorije,
            osnovnaCena,
            sastojci: [...sastojci],
        };

        porudzbina.push(kolac);
        sastojci = [];
        document.getElementById("sastojci-lista").innerHTML = "";

        const li = document.createElement("li");
        li.textContent = `${ime} (Cena: ${kolac.osnovnaCena + kolac.sastojci.reduce((sum, s) => sum + s.cena, 0)} RSD)`;
        document.getElementById("porudzbina-lista").appendChild(li);

        document.getElementById("kolac-name").value = "";
        document.getElementById("osnovne-kalorije").value = "";
        document.getElementById("osnovna-cena").value = "";
    }
});

document.getElementById("obracun-cena").addEventListener("click", () => {
    const ukupnaCena = porudzbina.reduce(
        (sum, k) => sum + k.osnovnaCena + k.sastojci.reduce((suma, s) => suma + s.cena, 0),
        0
    );
    document.getElementById("rezultat").textContent = `Ukupna cena porudžbine: ${ukupnaCena} RSD`;
});

document.getElementById("obracun-kalorije").addEventListener("click", () => {
    const ukupneKalorije = porudzbina.reduce(
        (sum, k) => sum + k.osnovneKalorije + k.sastojci.reduce((suma, s) => suma + s.kalorije, 0),
        0
    );
    document.getElementById("rezultat").textContent = `Ukupne kalorije porudžbine: ${ukupneKalorije}`;
});
