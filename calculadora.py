# Calculadora simples com tratamento de erros básicos

# Repetir até o usuário digitar o primeiro número corretamente
numero_valido = False
while numero_valido == False:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero_valido = True
    except:
        print("Erro: Você precisa digitar um número.")

# Repetir até o usuário digitar o segundo número corretamente
numero_valido = False
while numero_valido == False:
    try:
        numero2 = float(input("Digite o segundo número: "))
        numero_valido = True
    except:
        print("Erro: Você precisa digitar um número.")

# Repetir até que uma operação válida seja feita com sucesso
operacao_concluida = False
while operacao_concluida == False:
    operacao = input("Digite a operação (+, -, *, /): ")

    if operacao == "+":
        resultado = numero1 + numero2
        print("Resultado:", resultado)
        operacao_concluida = True

    if operacao == "-":
        resultado = numero1 - numero2
        print("Resultado:", resultado)
        operacao_concluida = True

    if operacao == "*":
        resultado = numero1 * numero2
        print("Resultado:", resultado)
        operacao_concluida = True

    if operacao == "/":
        # Verificar se o segundo número é zero
        if numero2 == 0:
            print("Erro: Não é possível dividir por zero.")
        else:
            resultado = numero1 / numero2
            print("Resultado:", resultado)
            operacao_concluida = True

    # Se o usuário digitou algo que não é nenhuma das operações
    if operacao != "+" and operacao != "-" and operacao != "*" and operacao != "/":
        print("Erro: operação inválida. Use apenas +, -, * ou /.")
