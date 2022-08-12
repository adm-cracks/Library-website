function input() {
    var nam = document.getElementById('names').value;
    var em = document.getElementById('ema').value;
    var com = document.getElementById('com').value;

    if (nam != '' && em != '' && com != '') {
        document.getElementById("but").disabled = false;

    } else {
        document.getElementById("but").disabled = true;
    }
}