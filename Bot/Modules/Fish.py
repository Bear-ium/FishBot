import random
from Modules.Tables import fishVariants

class Fish:
    VARIANTS = [
        # Higher chances must be at the bottom
        {"name": "Cursed", "chance": 0.1, "multiplier": 7.0},
        {"name": "Holy", "chance": 0.2, "multiplier": 5.0},
        {"name": "Void", "chance": 0.5, "multiplier": 4.0},
        {"name": "Diamond", "chance": 1.0, "multiplier": 3.0},
        {"name": "Ruby", "chance": 1.0, "multiplier": 2.5},
        {"name": "Emerald", "chance": 1.0, "multiplier": 2.5},
        {"name": "Golden", "chance": 2.0, "multiplier": 2.0},
        {"name": "Toxic", "chance": 5.0, "multiplier": 1.3},
        {"name": "Test", "chance": 39.2, "multiplier": 50},
    ]

    def __init__(self, name: str, min_weight: float, max_weight: float, base_value: int):
        self.base_name = name
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.base_value = base_value
        self.weight = round(random.uniform(min_weight, max_weight), 2)

        self.variant = None
        self.variant_multiplier = 1.0

        self.roll_variant()

        self.name = f"{self.variant} {self.base_name}" if self.variant else self.base_name
        self.value = int(self.base_value * self.weight * self.variant_multiplier)
        self.weight = round((self.weight * self.variant_multiplier), 2)

    def roll_variant(self):
        roll = random.uniform(0, 100)
        cumulative = 0
        for variant in self.VARIANTS:
            cumulative += variant["chance"]
            if roll <= cumulative:
                self.variant = variant["name"]
                self.variant_multiplier = variant["multiplier"]
                return

    def __str__(self):
        return f"{self.name} ({self.weight}kg) — {self.value} coins"

def Reel():
    fishData = random.choice(fishVariants)
    fish = Fish(**fishData)
    return fish