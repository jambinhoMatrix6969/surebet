while True:
    print("\nCálculo de apostas com odds ajustadas")
    print()

    try:
        # Entrada das odds (apenas com ponto)
        odma = float(input("Odd maior: "))
        odme = float(input("Odd menor: "))

        # Ajusta a odd maior
        odma1 = round(odma * 1.43, 4)

        # Verifica se a odd maior ajustada é menor que 3.5
        if odma1 < 3.5:
            print("Erro: A odd maior ajustada (odma1) não pode ser menor que 3.5!")
            continue

        # Pergunta quanto deseja apostar no total
        aposta_total = float(input("\nQual o valor total da aposta? R$: "))

        # Cálculo das probabilidades inversas
        prob_odma = 1 / odma1
        prob_odme = 1 / odme

        # Apostas proporcionais às probabilidades
        aposta_odma = round((prob_odma / (prob_odma + prob_odme)) * aposta_total, 2)
        aposta_odme = round((prob_odme / (prob_odma + prob_odme)) * aposta_total, 2)

        # Exibe as apostas em porcentagem
        perc_odma = round((aposta_odma / aposta_total) * 100, 2)
        perc_odme = round((aposta_odme / aposta_total) * 100, 2)

        # Cálculo dos ganhos
        ganho_odma = round(aposta_odma * odma1, 2)
        ganho_odme = round(aposta_odme * odme, 2)

        # Exibe as apostas e os ganhos
        print(f"\nPara garantir o lucro, você deve apostar:")
        print(f" - Odd maior (odma): {perc_odma}% (R${aposta_odma})")
        print(f" - Odd menor (odme): {perc_odme}% (R${aposta_odme})")
        print(f"\nGanhos possíveis:")
        print(f" - Se ganhar na Odd maior (odma): R${ganho_odma}")
        print(f" - Se ganhar na Odd menor (odme): R${ganho_odme}")

    except ValueError:
        print("Erro: Digite as odds com ponto, exemplo: 2.10")
        continue
