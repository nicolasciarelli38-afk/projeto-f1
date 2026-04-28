
clima = input("Qual é o clima?(chuva leve, seco, chuva pesada): ").lower()

pneu = int(input("Qual é o nivel de desgaste do pneu?: "))

voltas = int(input("Quantas voltas faltam?(1/58): "))

posicao = int(input("Qual nossa posição?(1/20): "))

mult_clima = 1.0

if clima == "chuva pesada":
    mult_clima = 4.0
elif clima == "chuva leve":
    mult_clima = 2.1


risco1 = int((pneu * 1.5) + (voltas * 1.8))

risco2 = (risco1 + posicao) / 2

risco_final = risco2 * mult_clima

if risco_final >= 110:
    print("BOX BOX, ir para os boxes agora.")
elif 70 <= risco_final < 110:
    print("Box box, boxes nessa volta")
elif 40 <= risco_final < 70:
    print("No seu painel PMF tem uma estrategia de parada antes, porem recomendamos q fique na pista.")
elif risco_final < 40:
    print("Não pare agora.")
