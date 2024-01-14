import random

def simulador_de_dados():
    print("Simulador de Dados")
    
    while True:
        input("Tecle Enter para lançar os dados...")
        
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        
        print(f"Dado 1: {dado1}")
        print(f"Dado 2: {dado2}")
        
        total = dado1 + dado2
        print(f"Total: {total}")
        
        jogar_novamente = input("Deseja lançar os dados novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            break

if __name__ == "__main__":
    simulador_de_dados()
