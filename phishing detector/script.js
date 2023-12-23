function checkPhishing() {
    var urlInput = document.getElementById('urlInput').value;
    var resultMessage = document.getElementById('resultMessage');

    if (urlInput.trim() === '') {
        resultMessage.textContent = 'Please enter a URL.';
        return;
    }

    // Use AJAX or fetch to send the URL to the server for phishing detection
    // For simplicity, we'll just do a client-side check using the provided function
    var isPhishing = isPhishingUrl(urlInput);

    if (isPhishing) {
        resultMessage.textContent = 'This URL is identified as a phishing URL.';
    } else {
        resultMessage.textContent = 'This URL is not identified as a phishing URL.';
    }
}
