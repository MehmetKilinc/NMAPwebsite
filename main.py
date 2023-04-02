from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ip = request.form['ip']
        port_range = range(1, 1025)
        open_ports = []
        for port in port_range:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        return render_template('result.html', ip=ip, open_ports=open_ports)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
