import os

# funções para cadastro e login
def cadastrar_usuario():
    print("\n=== Cadastro de Novo Usuário ===")
    nome = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite uma senha: ").strip()

    with open("usuarios.txt", "a") as f:
        f.write(f"{nome};{senha}\n")

    print("✅ Usuário cadastrado com sucesso!")

def autenticar_usuario():
    nome = input("Digite seu nome de usuário: ").strip()
    senha = input("Digite sua senha: ").strip()
    with open("usuarios.txt", "r") as f:
        for linha in f:
            partes = linha.strip().split(";")
            if len(partes) != 2:
                continue  # pula linha inválida
            usuario, senha_cadastrada = partes
            if nome == usuario and senha == senha_cadastrada:
                print("✅ Login realizado com sucesso!")
                return nome
    print("❌ Usuário ou senha incorretos.")
    return None


# funções de manipulação de tarefas
def carregar_tarefas(usuario):
    arquivo = f"tarefas_{usuario}.txt"
    if not os.path.exists(arquivo):
        return []
    
    with open(arquivo, "r") as f:
        tarefas = [linha.strip().split(";") for linha in f]
    return tarefas

def salvar_tarefas(usuario, tarefas):
    arquivo = f"tarefas_{usuario}.txt"
    with open(arquivo, "w") as f:
        for tarefa in tarefas:
            f.write(f"{tarefa[0]};{tarefa[1]}\n")

def contar_executando(tarefas):
    return sum(1 for t in tarefas if t[1] == "Executando")

# função principal do sistema de tarefas
def menu_tarefas(usuario):
    tarefas = carregar_tarefas(usuario)

    while True:
        print(f"\n=== Lista de Tarefas de {usuario} ===")
        for i, (nome, status) in enumerate(tarefas):
            print(f"{i + 1}. [{status}] {nome}")
        
        print("\nOpções:")
        print("1 - Adicionar tarefa")
        print("2 - Mudar status da tarefa")
        print("3 - Excluir tarefa")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            if len(tarefas) >= 100:
                print("❌ Limite de tarefas atingido.")
                continue

            nome_tarefa = input("Digite o nome da tarefa (até 80 caracteres): ").strip()
            if len(nome_tarefa) > 80:
                print("❌ Tarefa excede 80 caracteres.")
                continue
            tarefas.append([nome_tarefa, "A FAZER"])
            salvar_tarefas(usuario, tarefas)
            print("✅ Tarefa adicionada.")

        elif opcao == "2":
            if not tarefas:
                print("⚠️ Nenhuma tarefa para atualizar.")
                continue

            try:
                indice = int(input("Digite o número da tarefa a atualizar: ")) - 1
                if indice < 0 or indice >= len(tarefas):
                    print("❌ Índice inválido.")
                    continue

                print("Escolha o novo status:")
                print("1 - A FAZER")
                print("2 - EXECUTANDO")
                print("3 - PRONTA")
                escolha = input("Digite o número do status: ")

                novo_status = {
                    "1": "A FAZER",
                    "2": "Executando",
                    "3": "PRONTA"
                }.get(escolha)

                if not novo_status:
                    print("❌ Opção inválida.")
                    continue

                if novo_status == "Executando" and contar_executando(tarefas) >= 10:
                    print("❌ Limite de 10 tarefas em 'Executando' atingido.")
                    continue

                tarefas[indice][1] = novo_status
                salvar_tarefas(usuario, tarefas)
                print("✅ Status atualizado.")

            except ValueError:
                print("❌ Entrada inválida.")

        elif opcao == "3":
            if not tarefas:
                print("⚠️ Nenhuma tarefa para excluir.")
                continue

            try:
                indice = int(input("Digite o número da tarefa a excluir: ")) - 1
                if indice < 0 or indice >= len(tarefas):
                    print("❌ Índice inválido.")
                    continue

                confirmacao = input("Tem certeza que deseja excluir? (s/n): ")
                if confirmacao.lower() == "s":
                    tarefas.pop(indice)
                    salvar_tarefas(usuario, tarefas)
                    print("✅ Tarefa excluída.")
            except ValueError:
                print("❌ Entrada inválida.")

        elif opcao == "4":
            print("👋 Encerrando...")
            break
        else:
            print("❌ Opção inválida.")

# início do programa
def main():
    while True:
        print("\n=== Bem-vindo ao Sistema de Lista de Tarefas ===")
        print("1 - Cadastrar novo usuário")
        print("2 - Fazer login")
        print("3 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            usuario = autenticar_usuario()
            if usuario:
                menu_tarefas(usuario)
        elif escolha == "3":
            print("Até a próxima!")
            break
        else:
            print("❌ Opção inválida.")

# executar o programa
main()
