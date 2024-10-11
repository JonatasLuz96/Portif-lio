lista_pessoas = ["João", "Maria", "José", "Ana", "Pedro"]

while True:
  pessoa = input("Digite um nome: ")
  pessoa = pessoa.capitalize()
  
  if pessoa == "sair" or pessoa == "Sair":
    break
  
  if pessoa in lista_pessoas:
    print(f"Nome {pessoa}, encontrado!")
  else:
    print("Nome não encontrado.")
    cadastrar_nome = input("Deseja cadastrar esse nome? ")
    cadastrar_nome = cadastrar_nome.lower()

    if cadastrar_nome == "sim":
        lista_pessoas.append(pessoa)
        print("Nome cadastrado com sucesso!")
    elif cadastrar_nome == "nao":
      print("ok!")

  continuar = input("Deseja continuar? ")

  if continuar == "sim":
    continue
  elif continuar == "nao":
    print("Obrigado, volte sempre!")
    break   

print(lista_pessoas)
