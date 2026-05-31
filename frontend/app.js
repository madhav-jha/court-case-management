function checkStatus() {

    let caseNumber =
        document.getElementById("caseNumber").value;

    if(caseNumber===""){
        alert("Please Enter Case Number");
        return;
    }

    document.getElementById("result")
        .innerHTML =
        "Case No : " + caseNumber +
        "<br>Status : Pending Hearing";
}