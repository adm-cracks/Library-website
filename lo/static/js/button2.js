function input() {
    var nam = document.getElementById('names').value;
    var em = document.getElementById('ema').value;
    var com = document.getElementById('com').value;



    if (nam != '' && em != '' && com != '') {
        document.getElementById("but").disabled = false;
        b.style.backgroundColor = "red";
        b.style.cursor = "pointer"
        alert("done");


    } else {
        document.getElementById("but").disabled = true;
        b.style.backgroundColor = "rgba(245, 245, 245, 0.397)";

    }
}