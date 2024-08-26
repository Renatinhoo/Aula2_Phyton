#calculador de bonus na rolagem de D100

import random

input("Pressione enter para Rolar um dado D100!")

dado = random.randint(0, 100)

match dado:
    case dado if 0 <= dado <= 10:
        bonus = 0
    case dado if 11 <= dado <= 20:
        bonus = 1
    case dado if 21 <= dado <= 30:
        bonus = 2
    case dado if 31 <= dado <= 40:
        bonus = 3
    case dado if 41 <= dado <= 50:
        bonus = 4
    case dado if 51 <= dado <= 60:
        bonus = 5
    case dado if 61 <= dado <= 70:
        bonus = 6
    case dado if 71 <= dado <= 80:
        bonus = 7
    case dado if 81 <= dado <= 90:
        bonus = 8
    case dado if 91 <= dado <= 100:
        bonus = 9

resultado = dado + bonus


print(f"Você tirou: {dado} e ganhou: {bonus} de bonus!")
print(f"Seu número total de pontos foi: {resultado}")


