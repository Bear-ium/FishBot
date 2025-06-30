import random
import time
from Modules.Configurations import FISH_SPECIES, FISH_VARIANT_TIERS
from Modules.SafeDB import getDB

class Fish:
    VARIANTS = FISH_VARIANT_TIERS

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
        self.weight = round(self.weight * self.variant_multiplier, 2)
        self.value = int(self.base_value * self.weight)

    def roll_variant(self):
        roll = random.uniform(0, 100)
        cumulative = 0

        for variant in self.VARIANTS:
            cumulative += variant["chance"]
            if roll <= cumulative:
                self.variant = variant["name"]
                self.variant_multiplier = variant["multiplier"]
                return

        self.variant = "Normal"

    def __str__(self):
        return f"{self.name} ({self.weight}kg) — {self.value} coins"

def Reel(user: str) -> Fish:
    #fish_data = random.choice(FISH_SPECIES)
    fish_data = random.choices(
        FISH_SPECIES,
        weights = [fish["chance"] for fish in FISH_SPECIES],
        k = 1
    )[0]
    
    fish = Fish(
        name=fish_data["name"],
        min_weight=fish_data["min_weight"],
        max_weight=fish_data["max_weight"],
        base_value=fish_data["base_value"]
    )

    db = getDB()
    db.execute(
        """
        INSERT INTO catches (user, fish_name, weight, value, variant, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            user,
            fish.base_name,
            int(fish.weight * 1000),  # kg -> g
            fish.value,
            fish.variant,
            int(time.time())
        )
    )

    return fish