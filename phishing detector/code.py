from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

def is_phishing_url(url):
    # Add your phishing detection logic here
    # For simplicity, using a basic check from the previous example
    patterns = [
        r'https?://(?:www\.)?([a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}[-a-zA-Z0-9@:%._\+~#=]{2,}',
        r'@',
        r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
        r'(\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b\/[0-9]+\b)',
        r'\b(?!www\.)(?!http:\/\/)(?!https:\/\/)[a-zA-Z0-9-]+\.([a-zA-Z0-9-]+\.){1,}[a-zA-Z]{2,}\b',
        r'\b(?:paypal\.com|login\.yahoo\.com|accounts\.google\.com)\b',
    ]
    for pattern in patterns:
        if re.search(pattern, url):
            return True
    return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_phishing', methods=['POST'])
def check_phishing():
    url = request.form.get('urlInput')
    result = {'isPhishing': is_phishing_url(url)}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
