from flask import Flask, render_template, request, redirect, url_for, Response, flash, session
from flask_mysqldb import MySQL
import socket
import pickle
import struct
import time
import cv2

app = Flask(__name__)
app.secret_key = "Secret Key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'frbdus'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if "id" in session:
        return redirect(url_for("index"))
    else:
        if request.method == 'POST':
            name = request.form['name']
            phone = request.form['phone']
            email = request.form['email']
            passwd1 = request.form['pass1']
            passwd2 = request.form['pass2']
            if passwd1 == passwd2:
                mycurser = mysql.connection.cursor()
                mycurser.execute("INSERT INTO admin (name, phone, email, password) VALUES (%s, %s, %s, %s)",
                                 (name, phone, email, passwd2))
                mysql.connection.commit()
                # flash("Data Inserted Successfully")
                print("Data Inserted Successfully")
            else:
                # flash("Password Doesnot Mached")
                print("Password Doesnot Mached")

    return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if "id" in session:
        return redirect(url_for("index"))
    else:
        if request.method == 'POST':
            email = request.form['email']
            passwd = request.form['password']
            mycurser = mysql.connection.cursor()
            mycurser.execute("SELECT * FROM admin WHERE email=%s", (email,))
            log = mycurser.fetchall()
            mycurser.close()

            for row in log:
                id = row[0]
                password = row[4]
                print(id)
                print(password)

            if passwd == password:
                session["id"] = id
                print("session id:", session["id"])
                return redirect(url_for('index'))
            else:
                print("else")
                return render_template("login.html")

    return render_template("login.html")


@app.route('/logout')
def logout():
    if "id" in session:
        session.pop("id", None)
        return redirect(url_for('index'))
    else:
        return redirect(url_for("index"))


@app.route('/data')
def data():
    if "id" in session:
        aid = session["id"]
        mycurser = mysql.connection.cursor()
        mycurser.execute("SELECT * FROM users WHERE aid=%s", (aid,))
        fetch = mycurser.fetchall()
        mycurser.close()
        return render_template('data.html', users=fetch)
    else:
        return redirect(url_for('login'))


@app.route('/test')
def test():
    if "id" in session:
        id = session["id"]
        return render_template("test.html", id=id)
    else:
        return redirect(url_for('login'))


@app.route('/live')
def live():
    if "id" in session:
        id = session["id"]
        return render_template("live.html", id=id)
    else:
        return redirect(url_for('login'))


def gen():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = '192.168.1.152'  # Here Require CACHE Server IP
    port = 9066
    client_socket.connect((host_ip, port))  # a tuple
    data = b""
    payload_size = struct.calcsize("Q")
    while True:
        while len(data) < payload_size:
            packet = client_socket.recv(4 * 1024)  # 4K
            if not packet: break
            data += packet
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4 * 1024)
            frame_data = data[:msg_size]
        data = data[msg_size:]
        frame = pickle.loads(frame_data)
        #cv2.imshow("RECEIVING VIDEO FROM CACHE SERVER", frame)

        frame = cv2.imencode('.jpg', frame)[1].tobytes()

        time.sleep(0.016)
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/senddata')
def senddata():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host_ip = '192.168.225.224'  # Here according to your server ip write the address
        port = 9090
        cs.connect((host_ip, port))

        if cs:
            try:
                code = "1"
                cs.send(str.encode(code))
                print('Data Sent')
            except:
                print('Data Not Sent')
        return redirect(url_for('live'))
    except:
        return redirect(url_for('index'))


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        if "id" in session:
            aid = session["id"]
            name = request.form['name']
            phone = request.form['phone']
            email = request.form['email']
            address = request.form['address']

            mycurser = mysql.connection.cursor()
            mycurser.execute("INSERT INTO users (aid, name, phone, email, address) VALUES (%s, %s, %s, %s, %s)",
                             (aid, name, phone, email, address))
            mysql.connection.commit()
            flash("Data Inserted Successfully")

            return redirect(url_for('data'))
        else:
            return redirect(url_for('login'))


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        if "id" in session:
            id = request.form['id']
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']
            address = request.form['address']

            mycurser = mysql.connection.cursor()
            mycurser.execute("UPDATE users SET name=%s, phone=%s, email=%s, address=%s WHERE id=%s",
                             (name, phone, email, address, id))
            mysql.connection.commit()
            flash("Data Updated Successfully")

            return redirect(url_for('data'))
        else:
            return redirect(url_for('login'))


@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    if "id" in session:
        id = request.form['id']
        mycurser = mysql.connection.cursor()
        mycurser.execute("DELETE FROM users WHERE id=%s", (id,))
        mysql.connection.commit()
        flash("Data Deleted Successfully")
        return redirect(url_for('data'))
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(host='192.168.225.224', debug=True, port=5000, threaded=True)
    logout()
