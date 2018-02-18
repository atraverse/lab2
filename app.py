from flask import Flask
from flask import render_template
from main  import main_c

app = Flask(__name__, template_folder='template')

@app.route("/<name>")

def name(name):
    c = main_c(name)
    return ('result.html')

if __name__=="__main__":
    app.run()
