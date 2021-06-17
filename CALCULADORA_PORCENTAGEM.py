print()
print(" ---- CÁLCULO DE PORCENTAGEM ---- ")

while True:
    try:
        print()
        valor = float(input("   Valor: R$"))
        porcentagem = float(input("   Porcentagem % : "))
        print("   ----------------------------------")
        resultado = (valor * porcentagem) / 100
        desconto = valor - resultado
        acrescimo = valor + resultado
        print()
        print(f"   -> {porcentagem:.2f}% de R${valor:.2f} é R${resultado:.2f}")
        print(f"   -> Se for {porcentagem:.2f}% de desconto, o valor final é R${desconto:.2f}")
        print(f"   -> Se for {porcentagem:.2f}% de acréscimo, o valor final é R${acrescimo:.2f}")
        print()
        print("   ----------------------------------")
        selecione = str(input("   Deseja encerrar o programa? [S/N]: ")).upper().strip()

        while selecione not in "SN":
            selecione = str(input("   Deseja encerrar o programa? [S/N]: ")).upper().strip()

        if selecione == "S":
            break

    except (ValueError,TypeError):
        print("\t-----------------------")
        print("\tERRO! Digite um número!")
        print("\t-----------------------")
        continue

    except KeyboardInterrupt:
        print("\t-----------------------")
        print("\tO usuário resolveu não digitar nada.")
        print("\t-----------------------")
        continue
