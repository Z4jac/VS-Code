try {
    document.getElementById("content-wrapper").className = "wrapper content-wrapper";

}
catch(error) {
    console.error(error);
}
try {
    var element = document.getElementById("vue-default-module")
    element.parentNode.removeChild(element);
    console.log("Wyjebany")

}
catch(error) {
    console.error(error);
}



