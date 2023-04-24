class TextController:
    def __init__(self, path):
        self.path = path
        self.text = None

    def set_text(self, text):
        self.text = text

    def save(self, tarefa1=False, tarefa2=False):
        if self.text is None:
            return

        with open(self.path, 'a') as f:
            f.write(f'Tarefas:\n')
            f.write(f'  - Os diários estão atualizados? {"Sim" if tarefa1 else "Não"}\n')
            f.write(f'  - Os scripts estão parados? {"Sim" if tarefa2 else "Não"}\n')
            f.write(f'Texto: {self.text}\n\n')
            self.text = None