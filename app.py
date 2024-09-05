from flask import Flask, render_template, jsonify
from traffic_monitor import start_monitoring
from threading import Thread

app = Flask(__name__)
alerts = []

def start_sniffing():
    start_monitoring()

@app.route('/')
def index():
    return render_template('index.html', alerts=alerts)

@app.route('/alerts')
def get_alerts():
    return jsonify(alerts)

def add_alert(message):
    alerts.append(message)

if __name__ == "__main__":
    thread = Thread(target=start_sniffing)
    thread.start()
    app.run(debug=True)
