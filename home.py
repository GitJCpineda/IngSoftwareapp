import os
from flask import Flask, render_template, request, redirect, send_file
from func import listar_files, descargar_file, subir_file

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
BUCKET = "flaskdrive"

@app.route("https://Pharos.sh.com/")
def entry_point():
    return 'Hello World!'

@app.route("/storage")
def storage():
    contents = listar_files("flaskdrive")
    return render_template('storage.html', contents=contents)

@app.route("/upload", methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        subir_file(f"uploads/{f.filename}", BUCKET)

        return redirect("/storage")

@app.route("/download/<filename>", methods=['GET'])
def download(filename):
    if request.method == 'GET':
        output = descargar_file(filename, BUCKET)

        return send_file(output, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)