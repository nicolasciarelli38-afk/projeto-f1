import random

def calcular_estrategia(clima, pneu, voltas, posicao, motor, aero, tecnico):

    mult_clima = 1.0

    if clima == "chuva pesada":
        mult_clima = 2.3
    elif clima == "chuva leve":
        mult_clima = 1.8



    risco1 = int((pneu * 1.7) + ((55 - voltas) * 0.5) - aero)

    risco2 = (risco1 + posicao) / 2

    risco_final = risco2 * mult_clima


    if risco_final > 85:
        if tecnico >= 7:
            print("O risco era alto, mas sua tecnica te impediu de rodar!")
        else:
            print("O risco era alto e vc rodou!")
            posicao = posicao + 2 

    if risco_final >= 90:
        print("BOX BOX, ir para os boxes agora.")
    elif 70 <= risco_final < 90:
        print("Box box, janela de parada aberta.")
    elif 30 <= risco_final < 70:
        print("No seu painel PMF tem uma estrategia de parada antes, porem recomendamos q fique na pista.")
    elif risco_final < 30:
        print("Não pare agora.")


    
    

    ritmo_ia = random.randint(40, 70) - ((55 - voltas) * 0.2)


    meu_desempenho = (motor * 10) - (pneu * 1.5)
    diferenca = meu_desempenho - ritmo_ia
    if diferenca > 20 and posicao > 1:
        print("🏎️ Você está voando! Ultrapassagem realizada.")
        posicao -= 1
        
    # Para ser ultrapassado (perder posição), você precisa estar 20 pontos ABAIXO da IA
    elif diferenca < -20 and posicao < 20:
        print("🐌 O carro está lento... você foi ultrapassado!")
        posicao += 1
    
    if pneu < 10:
        meu_desempenho += 5

    return posicao, pneu


