import PySimpleGUI as projeto
import os


def selecao_cadastro():
    #  Layout
    projeto.theme("Reddit")

    layout = [
        [
            projeto.Radio('Professor', 'cadastro', key='cadProf'),
            projeto.Radio('Aluno', 'cadastro', key='cadAluno'),
            projeto.Radio('Disciplina', 'cadastro', key='cadDiscp'),
        ],
        [projeto.Button('Ver Cadastros'),projeto.Text("      "), projeto.Button('Prosseguir Cadastro')]
    ]
    return projeto.Window('Tela de Seleção de Cadastro', layout=layout, finalize=True)


def cadastro_prof():
    #  Layout
    projeto.theme("Reddit")
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
    return projeto.Window('Tela de Cadastro de Professor', layout=layout, finalize=True)


def cadastro_aluno():
    #  Layout
    projeto.theme("Reddit")

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
    return projeto.Window('Tela de Cadastro de Aluno', layout=layout, finalize=True)


def cadastro_disciplina():
    #  Layout
    projeto.theme("Reddit")

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
    return projeto.Window('Tela de Cadastro de Professor', layout=layout, finalize=True)

def saida_de_dados():
    projeto.theme("Reddit")

    layout = [
        [projeto.Output(size=(50, 10))]
        ]
    return projeto.Window('Dados do Cadastro', layout=layout, finalize=True)

# Criação de Janelas
janela1, janela2 = selecao_cadastro(), None

# Loop de leitura dos eventos
while True:
    janela, evento, valores = projeto.read_all_windows()
    # Lendo cadastros registrados
    if janela == janela1 and evento == 'Ver Cadastros':
        file = open(projeto.popup_get_file("Escolha o arquivo", file_types=(('.txt', '*.*'),), no_window=True), 'r',
                    encoding="utf8")
        janela1.hide()
        janela2 = saida_de_dados()
        file.seek(0, 0)
        print(file.read())

    # Se a janela1 for fechada
    if janela == janela1 and evento == projeto.WIN_CLOSED:
        projeto.popup('Operação cancelada pelo usuário')
        break

    # Executando janelas seguintes

    # Janela de cadastro do Professor
    if janela == janela1 and evento == 'Prosseguir Cadastro' and valores['cadProf'] == True:
        janela2 = cadastro_prof()
        janela1.hide()
        buttons, vallues = janela2.read()
        # Criação de Arquivo
        file = open(f"Prof - {vallues['nome']}.txt", 'w+', encoding="utf8")
        file.write('Informações do Professor\n')
        file.write(f"\nProfessor: {vallues['nome']}\n")
        file.write(f"Nascimento: {vallues['nascimento']}\n")
        file.write(f"Gênero: {vallues['genero']}\n")
        file.write(f"Endereço: {vallues['endereco']}\n")
        file.write(f"Instituição: {vallues['instituicao']}\n")
        if vallues['mestrado']:
            file.write(f"Formação: Mestre\n")
        if vallues['doutorado']:
            file.write(f"Formação: Doutor\n")
        file.write(f"Curso: {vallues['curso']}\n")
        file.write(f"Cadeira: {vallues['cadeira']}\n")
        file.close()

    # Janela de cadastro do Aluno
    if janela == janela1 and evento == 'Prosseguir Cadastro' and valores['cadAluno']:
        janela2 = cadastro_aluno()
        janela1.hide()
        buttons, vallues = janela2.read()
        # Criação de Arquivo
        file = open(f"Aluno(a) - {vallues['nome']}.txt", 'w+', encoding="utf8")
        file.write('Informações do Aluno\n')
        file.write(f"\nAluno: {vallues['nome']}\n")
        file.write(f"Nascimento: {vallues['nascimento']}\n")
        file.write(f"Gênero: {vallues['genero']}\n")
        file.write(f"Endereço: {vallues['endereco']}\n")
        file.write(f"Instituição: {vallues['instituicao']}\n")
        file.write(f"Curso: {vallues['curso']}\n")
        file.write(f"Periodo: {vallues['periodo']}\n")
        file.close()

    # Janela de cadastro de Disciplina
    if janela == janela1 and evento == 'Prosseguir Cadastro' and valores['cadDiscp']:
        janela2 = cadastro_disciplina()
        janela1.hide()
        buttons, vallues = janela2.read()
        # Criação de Arquivo
        file = open(f"Disciplina - {vallues['curso']}.txt", 'w+', encoding="utf8")
        file.write('Informações da Disciplina\n')
        file.write(f"\nDepartamento: {vallues['departamento']}\n")
        file.write(f"Curso: {vallues['curso']}\n")
        file.write(f"Disciplina: {vallues['disciplina']}\n")
        if vallues['prsim']:
            file.write(f"Pré-Requisito: {vallues['prequisito']}\n")
        if vallues['prnao']:
            file.write(f"Pré-Requisito: {vallues['prequisito']}\n")
        file.write(f"Carga Horária: {vallues['choraria']}\n")
        file.write(f"Dias da Semana: {vallues['dsemana']}\n")
        file.write(f"Horários: {vallues['hdodia']}\n")
        file.write(f"Quantidade Máxima de Alunos: {vallues['totalAlunos']}\n")
        file.close()

    if janela == janela2 and evento == 'Confirmar Cadastro':
        projeto.popup('Cadastro realizado com sucesso!')
        break

    if janela == janela2 and evento == projeto.WIN_CLOSED:
        projeto.popup('Operação cancelada pelo usuário')
        break
