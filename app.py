from flask import Flask, render_template, request

app = Flask(__name__)

todo_list = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_task = request.form.get("newtask")
        todo_list.append(new_task)
        
    return render_template("index.html", todo_list=todo_list)