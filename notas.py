# Lista para armazenar as notas
notas = []

# Loop para continuar pedindo as notas
while True:
    entrada = input("Digite uma nota (ou 'fim' para encerrar): ")

    # Verifica se o usuário quer encerrar
    if entrada.lower() == 'fim':
        break

    # Tenta converter a entrada para número
    try:
        nota = float(entrada)

        # Verifica se a nota está no intervalo válido
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um número entre 0 e 10.")

    except:
        print("Entrada inválida. Digite um número ou 'fim'.")

# Cálculo e exibição da média
if len(notas) > 0:
    media = sum(notas) / len(notas)
    print("Média da turma:", media)
else:
    print("Nenhuma nota válida foi registrada.")
