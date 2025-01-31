document.querySelector("form").addEventListener("submit", function(event) {
    let url = document.getElementById("url").value;
    if (!url.startsWith("https://www.youtube.com/")) {
        event.preventDefault();
        alert("Introduceți un URL valid de YouTube!");
    }
});
