# ================================
# PIM II - NotaFlow (Python)
# Universidade Paulista - UNIP
# Autor(es): Gabriel Mazzaron
# ================================

from collections import deque
import unicodedata
import os

# ===========================
# Menu principal
# ===========================
def menu1():
    while True:
        print("\nOlá! Seja bem vindo ao\n   === NotaFlow ===   \n")

        opc = input("Você deseja cadastrar um aluno? (s/n): ").lower()

        if opc == 'n':
            print("\nEncerrando o sistema...")
            break
        elif menu2() == "sair":
            break
        else:
            menu2()

def menu2():
    discipinas = ["Português", "Matemática", "História", "Filosofia", "Sociologia", "Geografia", "Biologia", "Química", "Física", "Inglês", "Educação_Física"]

    while True:
        print("\n=== NotaFlow ===")
        print("\nEscolha a disciplina para cadastro:")
        for i, disc in enumerate(discipinas, start=1):
            print(f"{i}. {disc}")
        print("0. Sair")

        opcao = input("Opção: ")

        if opcao == "0":
            print("\nEncerrando o sistema...")
            return "sair"
        elif opcao.isdigit() and 1 <= int(opcao) <= len(discipinas):
            disciplina = discipinas[int(opcao) - 1]
            cadastro(disciplina)
        else:
            print("Opção inválida. Tente Novamente.")

# ===========================
# Cadastro de Alunos
# ===========================

def cal_media(notas):
    return sum(notas) / len(notas)

def cadastro(disciplina):
    fila = Fila()
    print(f"\n=== Cadastro de Aluno - {disciplina.upper()} ===")

    while True:
        nome = input("Nome do Aluno: ").strip()
        ra = input("RA: ").strip()
        turma = input("Turma: ").strip()

        notas = []
        for i in range(1,5):
            nota = float(input(f"Digite a nota {i}: "))
            notas.append(nota)
        
        media = cal_media(notas)
        aluno = {
            "Nome": nome,
            "RA": ra,
            "Turma": turma,
            "Notas": notas,
            "Média": media
        }

        fila.add(aluno)
        print(f"\nAluno {nome} cadastrado\nCom média de {media}")

        continuar = input("\nDeseja cadastrar outro aluno (s/n)").lower()
        if continuar != 's':
            break

    fila.salvar(disciplina)
    return fila

# ===========================
# Estrutura de fila
# ===========================

class Fila:
    def __init__(self):
        self.fila = deque()

    def add(self, aluno):
        self.fila.append(aluno)

    def lista(self):
        for a in self.fila:
            print(a)

    def salvar(self, disciplina):
        pasta = r"C:\Users\bielm\OneDrive\Documentos\2 semestre faculdade\PIM\output"
        nome_arquivo = (f"{disciplina}.txt").lower()
        nome_arquivo = unicodedata.normalize('NFD', nome_arquivo)
        nome_arquivo = ''.join(c for c in nome_arquivo if unicodedata.category(c) != 'Mn')
        caminho = os.path.join(pasta, nome_arquivo)
        with open(caminho, 'a', encoding="utf-8") as arquivo:
            for a in self.fila:
                notas_str = ";".join(str(n) for n in a["Notas"])
                arquivo.write(f"{a['Nome']};{a['RA']};{a['Turma']};{notas_str};{a['Média']:.2f}\n")
                print(f"Salvo em {nome_arquivo} com sucesso!\n")

# ===========================
# Execução do código
# ===========================


if __name__ == "__main__":
    menu1()