# ================================
# PIM II - NotaFlow (Python)
# Universidade Paulista - UNIP
# Autor(es): Gabriel Mazzaron
# ================================

from collections import deque    # deque será usado para implementar a fila de alunos
import unicodedata               # usado para remover acentos dos nomes dos arquivos
import os                        # usado para manipular caminhos de arquivos

# ===========================
# Menu principal
# ===========================
def menu1():
    while True:
        print("\nOlá! Seja bem vindo ao\n   === NotaFlow ===   \n")

        # pergunta se o usuário quer cadastrar um aluno
        opc = input("Você deseja cadastrar um aluno? (s/n): ").lower()

        if opc == 'n':  # se não quiser cadastrar, encerra o programa
            print("\nEncerrando o sistema...")
            break

        # se dentro do menu2 o usuário escolher sair, encerramos
        elif menu2() == "sair":
            break


        else:   # se não for 'n', ele volta para menu2 novamente
            menu2()

def menu2():
    # lista com as diciplinas diponíveis
    discipinas = ["Português", "Matemática", "História", "Filosofia", "Sociologia", "Geografia", "Biologia", "Química", "Física", "Inglês", "Educação_Física"]

    while True:
        print("\n=== NotaFlow ===")
        print("\nEscolha a disciplina para cadastro:")

        # exibe cada disciplina com um número
        for i, disc in enumerate(discipinas, start=1):
            print(f"{i}. {disc}")
        
        print("0. Sair")    # opção de sair

        opcao = input("Opção: ")

        # se digitar 0, encerra o sistema e volta pro menu anterior
        if opcao == "0":
            print("\nEncerrando o sistema...")
            return "sair"
        
        # verifica se é número e se está dentro da lista
        elif opcao.isdigit() and 1 <= int(opcao) <= len(discipinas):
            disciplina = discipinas[int(opcao) - 1]
            cadastro(disciplina)    # chama a função de cadastro
        else:
            print("Opção inválida. Tente Novamente.")

# ===========================
# Cadastro de Alunos
# ===========================

# função para calcular média
def cal_media(notas):
    return sum(notas) / len(notas)

# função para cadastro
def cadastro(disciplina):
    fila = Fila()   # cria uma fila para armazenar os alunos
    print(f"\n=== Cadastro de Aluno - {disciplina.upper()} ===")

    while True:
        # entrada de dados do aluno
        nome = input("Nome do Aluno: ").strip()
        ra = input("RA: ").strip()
        turma = input("Turma: ").strip()

        # coleta 4 notas do aluno
        notas = []
        for i in range(1,5):
            nota = float(input(f"Digite a nota {i}: "))
            notas.append(nota)
        
        # calcula média usando a função anterior
        media = cal_media(notas)

        # dicionário com os dados do aluno
        aluno = {
            "Nome": nome,
            "RA": ra,
            "Turma": turma,
            "Notas": notas,
            "Média": media
        }

        # adciona o aluno à fila
        fila.add(aluno)
        print(f"\nAluno {nome} cadastrado\nCom média de {media}")

        # pergunta se deseja cadastar outro aluno
        continuar = input("\nDeseja cadastrar outro aluno (s/n): ").lower()
        if continuar != 's':
            break

    # após finalizar o cadastro, salva os dados no arquivo da disciplina
    fila.salvar(disciplina)
    return fila

# ===========================
# Estrutura de fila
# ===========================

class Fila:
    def __init__(self):
        self.fila = deque() # fila baseada em deque

    # adciona o aluno ao final da fila
    def add(self, aluno):
        self.fila.append(aluno)

    # lista todos os alunos cadastrados
    def lista(self):
        for a in self.fila:
            print(a)

    # salva os alunos em arquivo txt
    def salvar(self, disciplina):
        # caminho fixo onde os arquivos serão salvos
        pasta = r"C:\Users\bielm\OneDrive\Documentos\2 semestre faculdade\PIM\output"

        # nome do arquivo recebe o nome da disciplian em minúsculas
        nome_arquivo = (f"{disciplina}.txt").lower()

        # remove acentos e caracteres especias
        nome_arquivo = unicodedata.normalize('NFD', nome_arquivo)
        nome_arquivo = ''.join(c for c in nome_arquivo if unicodedata.category(c) != 'Mn')

        # monta o caminho completo
        caminho = os.path.join(pasta, nome_arquivo)

        # abre o arquivo em modo append
        with open(caminho, 'a', encoding="utf-8") as arquivo:
            for a in self.fila:
                # junta as notas com ponto-e-vírgula
                notas_str = ";".join(str(n) for n in a["Notas"])

                # escreve os dados formatados no arquivo
                arquivo.write(f"{a['Nome']};{a['RA']};{a['Turma']};{notas_str};{a['Média']:.2f}\n")
                print(f"Salvo em {nome_arquivo} com sucesso!\n")

# ===========================
# Execução do código
# ===========================


if __name__ == "__main__":
    menu1() # inicia o sistema
