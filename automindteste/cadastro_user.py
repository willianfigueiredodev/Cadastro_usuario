usuarios = []

def cadastrar_usuario():
    print("\n=== Cadastro de Usuário ===")
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    idade = input("Digite a idade: ")
    usuario = {
        "nome": nome,
        "email": email,
        "idade": idade
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def listar_usuarios():
    print("\n=== Lista de Usuários Cadastrados ===")
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for i, usuario in enumerate(usuarios, 1):
            print(f"\nUsuário {i}")
            print(f"Nome: {usuario['nome']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Idade: {usuario['idade']}")

def buscar_usuario():
    print("\n=== Buscar Usuário por Nome ===")
    nome_busca = input("Digite o nome do usuário: ")
    encontrado = False
    for usuario in usuarios:
        if usuario["nome"].lower() == nome_busca.lower():
            print("\nUsuário encontrado:")
            print(f"Nome: {usuario['nome']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Idade: {usuario['idade']}")
            encontrado = True
            break
    if not encontrado:
        print("Usuário não encontrado.")

def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Cadastrar usuário")
        print("2. Listar usuários")
        print("3. Buscar usuário por nome")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            print("Encerrando o programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()