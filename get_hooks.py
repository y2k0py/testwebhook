from flask import Flask, request

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
    app.run(host='0.0.0.0', port=8443)
