import os
from flask import Flask,render_template, request

_author_="Marie"

app = Flask(_name_)

APP_ROOT = os.path.dirname(os.path.abspath(_file_))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload")
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)

    return render_template("complete.html")

if _name_ == "_main_":
    app.run(port=4555, debug=True)