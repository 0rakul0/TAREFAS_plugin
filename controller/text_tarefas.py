from flask import request

class TextController:
    def save(self):
        text = request.form['text']
        with open('text.txt', 'w') as f:
            f.write(text)
        return 'Text saved to file.'