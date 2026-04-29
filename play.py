import calculos
import random
import equipes
def jogar():
    opcoes_clima = ["seco","seco","seco","seco","seco","seco", "chuva leve","chuva leve","chuva leve","chuva leve", "chuva pesada"]

    clima = random.choice(opcoes_clima)

    print(f"o clima sorteado foi {clima}")

    escolha = input("escolha sua equipe(Williams, Ferrari, Mercedes, Audi, Haas, Red Bull): ").lower()

    dados_equipe = equipes.buscar_equipe(escolha)

    pneu = 0

    voltas = 55

    posicao = int(input("Qual nossa posição?(1/20): "))

    motor = dados_equipe["motor"]

    aero = dados_equipe["aero"]

    tecnico = dados_equipe["tecnico"]





    while voltas > 0:
        print(f"n--- VOLTA ATUAL: {voltas} para o fim ---" )


        posicao, pneu = calculos.calcular_estrategia(clima, pneu, voltas, posicao, motor, aero, tecnico,)
        pneu = pneu + (50 / aero) 
        print(f"Desgaste do pneu: {pneu:.1f}%")

        voltas = voltas - 5
    
        desicao = input("você entrou nos boxes nessa volta?(s/n): ").lower()

        if desicao == "s":
            pneu = 0
            perda = 12 - tecnico
            posicao = posicao + perda
            print(f"🚀 Pneus novos! Você voltou em {posicao}º lugar.")


        input("aperte ENTER para proxima volta.")






    print("Bandeira quadriculada! Fim de prova")
    print(f"você ficou em {posicao}")

while True:
    print("\n" + "="*30)
    print("🏎️  F1 STRATEGY SIMULATOR 🏎️")
    print("="*30)
    print("1. Iniciar Nova Corrida")
    print("2. Sair do Jogo")

    escolha = input("\nO que deseja fazer? ")

    if escolha == "1":
        jogar()
    elif escolha == "2":
        print("Saindo... Vejo você no próximo GP! 🏁")
        break
    else:
        print("Opção inválida, piloto!")