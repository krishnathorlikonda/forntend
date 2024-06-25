async function runCode() {
    const code = document.getElementById('code').value;
    const language = document.getElementById('language').value;
    const outputElement = document.getElementById('output');

    const response = await fetch('http://localhost:8000/run', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ language, code })
    });

    const result = await response.json();
    outputElement.textContent = result.output;
}
