from flask import Flask, render_template, request, redirect
from utils import authenticate_icloud, upload_file, list_files, encrypt_data, decrypt_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    icloud_session = authenticate_icloud(username, password)
    return render_template('dashboard.html', files=list_files(icloud_session))

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    encrypted_file = encrypt_data(file.read())
    upload_file(encrypted_file, icloud_session)
    return redirect('/dashboard')

if __name__ == '__main__':
    app.run(debug=True)
