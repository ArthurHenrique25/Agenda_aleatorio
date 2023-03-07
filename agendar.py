import random


class estagio():
    def __init__(self):
    
        r_range = random.randrange(15876, 20586,254)
        nomes = ["Luiz","Maria","Helena","João"]
        trabalhos = ["medicos","empresarios","policiais","Programadores"]
        setores = ["A","B","C","D"]



        random.shuffle(nomes)
        nomes_aleatorios = random.sample(nomes,k=1)

        randon_nome = random.choice(nomes)
        random_tabalho = random.choice(trabalhos)
        random_setores = random.choice(setores)
# print(nomes_aleatorios)
        print(f"Hoje {randon_nome}, trabalhara com os {random_tabalho} no setor {random_setores}")
    