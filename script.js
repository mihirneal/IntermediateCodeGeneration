function generateIntermediateCode() {
    var cppCode = document.getElementById("cpp-code").value;

    // Send the C++ code to the server for intermediate code generation
    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: cppCode })
    })
    .then(response => response.text())
    .then(intermediateCode => {
        // Display the intermediate code in the browser
        document.getElementById("intermediate-code").textContent = intermediateCode;
    })
    .catch(error => console.error(error));
}
