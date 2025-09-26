class Enemy :
    def __init__(self, health: int, attack: int, name: str):
        self.health = health
        self.attack = attack
        self.name = name

    def attack(self):
        print(f"{self.name} attackerar för {self.attack_power} skada")

    def take_damage(self):
        self.health -= damage
        print(f"{self.name} tar {damage} i skada oc hhar {self.health} i liv kvar")

    def print_status(self):
        print(f"Fiende med namnet {self.name} har {self.health} hp")

batteri = Enemy(10, 5, "Batteri")
batteri.print_status()
batteri.attack