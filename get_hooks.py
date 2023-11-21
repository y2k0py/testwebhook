from flask import Flask, request
import ssl

app = Flask(__name__)
# Обработчик входящих вебхуков


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print(data)
        return "OK"
    return "Invalid request method"

if __name__ == '__main__':
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
    app.run(host='0.0.0.0', port=8443, ssl_context=ssl_context)
