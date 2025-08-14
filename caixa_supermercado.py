def pessoa():
    try:
        cpf = input("Digite o CPF (11 dígitos): ")
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError("CPF deve ter exatamente 11 dígitos numéricos.")

        nome = input("Digite o nome: ")
        if nome.strip() == "":
            raise ValueError("Nome não pode estar vazio.")

        print(f"Seja bem-vindo, {nome}!")

    except ValueError as e:
        print("Erro:", e)
        return

    categorias = {
        1: "bebidas",
        2: "alimentos",
        3: "limpeza",
        4: "higiene pessoal",
        5: "açougue",
        6: "hortifruti",
        7: "outros"
    }

    bebidas = {
        1: {"produto": "Água", "marca": "Crystal", "preco": 2.50},
        2: {"produto": "Coca-Cola", "marca": "Lata", "preco": 4.00},
        3: {"produto": "Cerveja", "marca": "Skol", "preco": 4.75},
        4: {"produto": "Suco", "marca": "Tang", "preco": 2.30}
    }

    alimentos = {
        1: {"produto": "Arroz", "marca": "Camil", "preco": 35.00},
        2: {"produto": "Feijão", "marca": "Camil", "preco": 11.50},
        3: {"produto": "Pipoca", "marca": "Yoki", "preco": 5.00},
        4: {"produto": "Farinha", "marca": "Yoki", "preco": 4.50},
        5: {"produto": "Farofa de milho", "marca": "Yoki", "preco": 3.50}
    }

    limpeza = {
        1: {"produto": "Água Sanitária", "marca": "Ypê", "preco": 3.50},
        2: {"produto": "Desinfetante", "marca": "Pinho", "preco": 4.00},
        3: {"produto": "Detergente", "marca": "Ypê", "preco": 1.75}
    }

    higiene_pessoal = {
        1: {"produto": "Pasta de dente", "marca": "Colgate", "preco": 4.00},
        2: {"produto": "Protetor solar", "marca": "Neutrogena", "preco": 25.00},
        3: {"produto": "Fio dental", "marca": "Sensodyne", "preco": 3.50},
        4: {"produto": "Protetor labial", "marca": "Nivea", "preco": 5.00}
    }

    açougue = {
        1: {"produto": "Carne moída", "marca": "Friboi", "preco": 30.00},
        2: {"produto": "Frango", "marca": "Sadia", "preco": 20.00},
        3: {"produto": "Bife", "marca": "Friboi", "preco": 35.00},
        4: {"produto": "Linguiça", "marca": "Sadia", "preco": 15.00}
    }

    hortifruti = {
        1: {"produto": "Melancia", "marca": "Nacional", "preco": 20.00},
        2: {"produto": "Banana", "marca": "Nanica", "preco": 5.00},
        3: {"produto": "Maçã", "marca": "Red", "preco": 4.00},
        4: {"produto": "Laranja", "marca": "Bahia", "preco": 3.00},
        5: {"produto": "Tomate", "marca": "Italiano", "preco": 6.00}
    }

    outros = {
        1: {"produto": "Lâmpada", "marca": "LED", "preco": 15.00},
        2: {"produto": "Panela", "marca": "Inox", "preco": 45.00},
        3: {"produto": "Talheres", "marca": "Colheres Inox", "preco": 20.00},
        4: {"produto": "Copos", "marca": "Vidro", "preco": 30.00}
    }

    print("\nCategorias disponíveis:")
    for cod, nome in categorias.items():
        print(f"{cod} - {nome}")

    cliente = int(input("Digite o código da categoria desejada: "))

    if cliente == 1:
        print("Você escolheu bebidas. Produtos disponíveis:")
        for cod, info in bebidas.items():
            print(f"{cod} - {info['produto']} ({info['marca']}) - R${info['preco']:.2f}")

    elif cliente == 2:
        print("Você escolheu alimentos. Produtos disponíveis:")
        for cod, info in alimentos.items():
            print(f"{cod} - {info['produto']} ({info['marca']}) - R${info['preco']:.2f}")

    elif cliente == 3:
        print("Você escolheu limpeza. Produtos disponíveis:")
        for cod, info in limpeza.items():
            print(f"{cod} - {info['produto']} ({info['marca']}) - R${info['preco']:.2f}")

    elif cliente == 4:
        print("Você escolheu higiene pessoal. Produtos disponíveis:")
        for cod, info in higiene_pessoal.items():
            print(f"{cod} - {info['produto']} ({info['marca']}) - R${info['preco']:.2f}")

    elif cliente == 5:
        print("Você escolheu açougue. Produtos disponíveis:")
        for cod, info in açougue.items():
            print(f"{cod} - {info['produto']} ({info['marca']}) - R${info['preco']:.2f}")

    elif cliente == 6:
        print("Você escolheu hortifruti. Produtos disponíveis:")
        for cod, info in hortifruti.items():
            print(f"{cod} - {info['produto']} ({info['marca']}) - R${info['preco']:.2f}")

    elif cliente == 7:
        print("Você escolheu outros. Produtos disponíveis:")
        for cod, info in outros.items():
            print(f"{cod} - {info['produto']} ({info['marca']}) - R${info['preco']:.2f}")

    else:
        print("Categoria inválida")
    
    while True:
        Opcao 1 = "bebidas"
        Opcao 2 = "alimentos"
        Opcao 3 = "Limpeza" 
        Opcao 4 = "Higiene_pessoal"
        Opcao 5 = "acougue"
        Opcao 6 = "Hortifruti"
        Opcao 7 = "Outros"
        opcao = input("Digite o número da opção desejada: ")
        if opcao == 1: 
            print("Voce escolheu bebidas")
        if opcao == 2: 
            print("Voce escolheu alimentos")
        if opcao == 3: 
            print("Voce escolheu limpeza")
        if opcao == 4: 
            print("Voce escolheu higiene pessoal")
        if opcao == 5: 
            print("Voce escolheu açougue")
        if opcao == 6: 
            print("Voce escolheu hortifruti")
        if opcao == 7: 
            print("Voce escolheu outros")
          
