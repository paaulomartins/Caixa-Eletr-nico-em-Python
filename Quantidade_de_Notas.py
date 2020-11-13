def QTDNOTAS():
    NOTAS = [100, 50, 20, 10, 5, 2]
    CAIXA = [0,0,0,0,0,0]
    VEZES = [0,0,0,0,0,0]
    TOTAL = 0
    i = 0
    while i <= 5:
        CAIXA[i] = int(input("Quantas notas de R$ {},00? ".format(NOTAS[i])))
        VEZES[i] = NOTAS[i] * CAIXA[i]
        print("VALOR TOTAL DE CADA NOTA, INDIVIDUALMENTE {} ".format(VEZES[i]))
        TOTAL += VEZES[i]
        print("Valor total de todas as notas {} ".format(TOTAL))
        i += 1
    if ((VEZES[0]+VEZES[1]+VEZES[2]+VEZES[3]+VEZES[3]+VEZES[4]+VEZES[5]) == 0):
	    print(" SEM NOTAS DISPONIVEIS PARA INICIALIZAR")