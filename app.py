class Enemy :
    def __init__(self, health: int, attack: int, name: str):
        self.health = health
        self.attack = attack
        self.name = name

    def attack(self):
        pass
        
    def print_status(self):
        print(f"Fiende med namnet {self.name} har {self.health} hp")

batteri = Enemy(10, 5, "Batteri")
batteri.print_status()