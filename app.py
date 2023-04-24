from flask import Flask, render_template
from controller.text_tarefas import TextController

app = Flask(__name__)
text_controller = TextController()

@app.route('/save', methods=['POST'])
def save_text():
    return text_controller.save()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')