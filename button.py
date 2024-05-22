from flask import Flask, request, render_template
import requests
esp32_ip='172.16.0.246' # 請根據ESP32端的IP來填寫
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/toggle', methods=['POST'])
def toggle():
    state = request.form['state']
    print(state)
    requests.get(f'http://{esp32_ip}/{state}')
    return ('', 204)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
