from flask import Flask, render_template
import os

app = Flask(__name__)

PYTHON_FILE = "whatispassword_walkthrough-hard.py" # Change your Python file name here

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SUPPORT_FILE = "nth.py"
SCRIPT_PATH = os.path.join(BASE_DIR, PYTHON_FILE)
SUPPORT_PATH = os.path.join(BASE_DIR, SUPPORT_FILE)

@app.route("/")
def index():
    print("TEMPLATE FOLDER:", app.template_folder)
    print("APP ROOT:", app.root_path)
    print("INDEX PATH:", os.path.join(app.root_path, "templates", "index.html"))
    
    with open(SUPPORT_PATH, "r", encoding="utf-8") as file:
        support_code = file.read()
    with open(SCRIPT_PATH, "r", encoding="utf-8") as file:
        source_code = file.read()

    return render_template(
        "index.html",
        python_file=PYTHON_FILE,
        source_code=source_code,
        support_file=SUPPORT_FILE,
        support_code=support_code 
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )