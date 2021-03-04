import PySimpleGUI as projeto
import os


class CadastroDeMonitoria:
    def __init__(self):
        #  Layout
        projeto.ChangeLookAndFeel("Reddit")

        layout = [
            [
                projeto.Radio('Professor', 'cadastro', key='cadProf'),
                projeto.Radio('Aluno', 'cadastro', key='cadAluno'),
                projeto.Radio('Disciplina', 'cadastro', key='cadDiscp'),
                projeto.Button('Confirma')
            ],
        ]
        # Janela
        self.janela = projeto.Window('Página de Seleção de Cadastro').layout(layout)
        # Extrair Dados da Tela
        self.buttons, self.vallues = self.janela.Read()

        if self.vallues['cadProf']:
            layout = [
                [projeto.Text('Nome', size=(12, 0)), projeto.Input(size=(50, 0), key='nome')],
                [projeto.Text('Nascimento', size=(12, 0)), projeto.Input(size=(50, 0), key='nascimento')],
                [projeto.Text('Gênero', size=(12, 0)), projeto.Input(size=(50, 0), key='genero')],
                [projeto.Text('Endereço', size=(12, 0)), projeto.Input(size=(50, 0), key='endereco')],
                [projeto.Text('Instituição', size=(12, 0)), projeto.Input(size=(50, 0), key='instituicao')],
                [projeto.Text('Qual a sua formação?')],
                [
                    projeto.Radio('Mestre', 'formacao', key='mestrado'),
                    projeto.Radio('Doutor', 'formacao', key='doutorado'),
                ],
                [projeto.Text('Curso', size=(12, 0)), projeto.Input(size=(50, 0), key='curso')],
                [projeto.Text('Cadeira(s)', size=(12, 0)), projeto.Input(size=(50, 0), key='cadeira')],
                [projeto.Button('Confirmar Cadastro')]
            ]
            # Janela
            self.janela = projeto.Window('Página de Cadastro de Professores').layout(layout)

            # Extrair Dados da Tela
            self.buttons, self.vallues = self.janela.Read()

            # Criação de Arquivo
            file = open(f"Prof - {self.vallues['nome']}.txt", 'w+', encoding="utf8")
            file.write('Informações do Professor\n')
            file.write(f"\nProfessor: {self.vallues['nome']}\n")
            file.write(f"Nascimento: {self.vallues['nascimento']}\n")
            file.write(f"Gênero: {self.vallues['genero']}\n")
            file.write(f"Endereço: {self.vallues['endereco']}\n")
            file.write(f"Instituição: {self.vallues['instituicao']}\n")
            if self.vallues['mestrado']:
                file.write(f"Formação: Mestre\n")
            if self.vallues['doutorado']:
                file.write(f"Formação: Doutor\n")
            file.write(f"Curso: {self.vallues['curso']}\n")
            file.write(f"Cadeira: {self.vallues['cadeira']}\n")
            file.close()

        elif self.vallues['cadAluno']:
            layout = [
                [projeto.Text('Nome', size=(12, 0)), projeto.Input(size=(50, 0), key='nome')],
                [projeto.Text('Nascimento', size=(12, 0)), projeto.Input(size=(50, 0), key='nascimento')],
                [projeto.Text('Gênero', size=(12, 0)), projeto.Input(size=(50, 0), key='genero')],
                [projeto.Text('Endereço', size=(12, 0)), projeto.Input(size=(50, 0), key='endereco')],
                [projeto.Text('Instituição', size=(12, 0)), projeto.Input(size=(50, 0), key='instituicao')],
                [projeto.Text('Curso', size=(12, 0)), projeto.Input(size=(50, 0), key='curso')],
                [projeto.Text('Periodo', size=(12, 0)), projeto.Input(size=(50, 0), key='periodo')],
                [projeto.Button('Confirmar Cadastro')]
            ]

            # Janela
            self.janela = projeto.Window('Página de Cadastro de Alunos').layout(layout)

            # Extrair Dados da Tela
            self.buttons, self.vallues = self.janela.Read()

            # Criação de Arquivo
            file = open(f"Aluno(a) - {self.vallues['nome']}.txt", 'w+', encoding="utf8")
            file.write('Informações do Aluno\n')
            file.write(f"\nAluno: {self.vallues['nome']}\n")
            file.write(f"Nascimento: {self.vallues['nascimento']}\n")
            file.write(f"Gênero: {self.vallues['genero']}\n")
            file.write(f"Endereço: {self.vallues['endereco']}\n")
            file.write(f"Instituição: {self.vallues['instituicao']}\n")
            file.write(f"Curso: {self.vallues['curso']}\n")
            file.write(f"Periodo: {self.vallues['periodo']}\n")
            file.close()

        elif self.vallues['cadDiscp']:
            layout = [
                [projeto.Text('Departamento', size=(13, 0)), projeto.Input(size=(50, 0), key='departamento')],
                [projeto.Text('Curso', size=(13, 0)), projeto.Input(size=(50, 0), key='curso')],
                [projeto.Text('Disciplina', size=(13, 0)), projeto.Input(size=(50, 0), key='disciplina')],
                [projeto.Text('A disciplina tem algum pré-requisito?')],
                [
                    projeto.Radio('Sim', 'requisito', key='prsim'),
                    projeto.Radio('Não', 'requisito', key='prnao'),
                ],
                [projeto.Text('Pré-Requisito', size=(13, 0)), projeto.Input(size=(50, 0), key='prequisito')],
                [projeto.Text('Carga Horária', size=(13, 0)), projeto.Input(size=(50, 0), key='choraria')],
                [
                    projeto.Text('Dia da Semana', size=(13, 0)), projeto.Input(size=(15, 0), key='dsemana'),
                    projeto.Text('Hora', size=(4, 0)), projeto.Input(size=(15, 0), key='hdodia')
                ],
                [projeto.Text('Quantidade máxima de Alunos')],
                [
                    projeto.Slider(range=(1, 80),  # Valor mínimo e máximo da barra
                              default_value=1,  # Valor inicial da barra
                              orientation='h',  # Orientação da barrinha ('h' = Horizontal, 'v' = Vertical)
                              size=(55, 20),  # Tamanho da barrinha na tela (Horizontal, Vertical)
                              key='totalAlunos')  # Nome da chave da barrinha
                ],
                [projeto.Button('Confirmar Cadastro')]
            ]

            # Janela
            self.janela = projeto.Window('Página de Cadastro de Disciplinas').layout(layout)

            # Extrair Dados da Tela
            self.buttons, self.vallues = self.janela.Read()

            # Criação de Arquivo
            file = open(f"Disciplina - {self.vallues['curso']}.txt", 'w+', encoding="utf8")
            file.write('Informações da Disciplina\n')
            file.write(f"\nDepartamento: {self.vallues['departamento']}\n")
            file.write(f"Curso: {self.vallues['curso']}\n")
            file.write(f"Disciplina: {self.vallues['disciplina']}\n")
            if self.vallues['prsim']:
                file.write(f"Pré-Requisito: {self.vallues['prequisito']}\n")
            if self.vallues['prnao']:
                file.write(f"Pré-Requisito: {self.vallues['prequisito']}\n")
            file.write(f"Carga Horária: {self.vallues['choraria']}\n")
            file.write(f"Dias da Semana: {self.vallues['dsemana']}\n")
            file.write(f"Horários: {self.vallues['hdodia']}\n")
            file.write(f"Quantidade Máxima de Alunos: {self.vallues['totalAlunos']}\n")
            file.close()

    def iniciar(self):
        print(self.vallues)


cadastrar = CadastroDeMonitoria()
cadastrar.iniciar()
