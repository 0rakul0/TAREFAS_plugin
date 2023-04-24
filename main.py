from urllib import request
from fastapi import FastAPI, Form, Request, Response
from fastapi.responses import PlainTextResponse,  HTMLResponse
from fastapi.templating import Jinja2Templates
from controllers.text_tarefas import TextController
from datetime import date

dia = date.today()
app = FastAPI()
templates = Jinja2Templates(directory="views")
text_controller = TextController(path=f'./bd/situacao_{dia}.txt')
@app.post('/')
async def save_text(request: Request):
    form = await request.form()
    text = form['text']
    tarefa1 = form.get('tarefa1', False)
    tarefa2 = form.get('tarefa2', False)
    text_controller.set_text(text)
    text_controller.save(tarefa1, tarefa2)
    # Renderiza a página de sucesso
    return templates.TemplateResponse("success.html", {"request": request})

@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == '__main__':
    text_controller = TextController(f'situacao_{dia}.txt.txt')
    app.run(debug=True)