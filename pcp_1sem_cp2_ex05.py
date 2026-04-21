nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("Empréstimo negado: Menor de 18 anos.")
else:
    renda = float(input("Digite a sua renda mensal: "))
    valor = float(input("Digite o valor do empréstimo: "))

    if valor > (renda * 20):
        print("Empréstimo negado: Valor acima de 20x a renda.")
    else:
        n = 0
        while n < 3 or n > 24:
            n = int(input("Digite o número de parcelas (3-24): "))
            if n < 3 or n > 24:
                print("Erro: Parcelas devem ser entre 3 e 24.")

        if n <= 6:
            taxa = 0.05
        elif n <= 12:
            taxa = 0.08
        else:
            taxa = 0.10

        parcela = valor * (taxa * (1 + taxa)**n) / ((1 + taxa)**n - 1)
        total = parcela * n
        juros = total - valor

        print("Status: Aprovado")
        print(f"Nome: {nome}")
        print(f"Valor financiado: {valor:.2f}")
        print(f"Taxa: {taxa*100:.0f}%")
        print(f"Parcela: {parcela:.2f}")
        print(f"Total pago: {total:.2f}")
        print(f"Total juros: {juros:.2f}")

        