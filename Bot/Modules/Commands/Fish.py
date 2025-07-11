import random
import time
import os
from typing import List

from dotenv import load_dotenv
from typing import cast

from Modules.Configurations import FISH_SPECIES, FISH_VARIANT_TIERS
from Modules.SafeDB import getDB
from Modules.Webhook import Webhook

load_dotenv()
WEBHOOK_KEY = cast(str, os.getenv("WEBHOOK"))
Web = Webhook(WEBHOOK_KEY)

def AnnounceRarity(user, caught):
    if caught.variant_multiplier > 6.5:
        Web.send_message(f"{user} caught a Legendary ({caught.variant}) variant!", False)
    elif caught.variant_multiplier > 4.4:
        Web.send_message(f"{user} caught a Rare ({caught.variant}) variant!", False)

class Fish:
    VARIANTS = FISH_VARIANT_TIERS

    def __init__(self, name: str, min_weight: float, max_weight: float, base_value: int, boat_level: int):
        self.base_name = name
        self.min_weight = min_weight
        self.max_weight = max_weight
        self.base_value = base_value

        self.weight = round(random.uniform(min_weight, max_weight), 2)
        self.variant = None
        self.variant_multiplier = 1.0

        self.roll_variant(boat_level)

        self.name = f"{self.variant} {self.base_name}" if self.variant else self.base_name
        self.weight = round(self.weight * self.variant_multiplier, 2)
        self.value = int(self.base_value * self.weight)

    def roll_variant(self, boat_level: int):
        """
        Roll for a fish variant based on boat level.
        """
        # Filter variants allowed for the current boat level
        available_variants = [
            v for v in self.VARIANTS
            if v.get("boat_level", 0) <= boat_level
        ]

        if not available_variants:
            self.variant = "Normal"
            self.variant_multiplier = 1.0
            return

        roll = random.uniform(0, 100)
        cumulative = 0

        for variant in available_variants:
            cumulative += variant["chance"]
            if roll <= cumulative:
                self.variant = variant["name"]
                self.variant_multiplier = variant["multiplier"]
                return

        self.variant = "Normal"
        self.variant_multiplier = 1.0

    def __str__(self):
        return f"{self.name} ({self.weight}kg) — {self.value} coins"

def Reel(user: str) -> List[Fish]:
    # Inner-Functions
    def get_random_fish(boat_level: int):
        """
        Get a fish based on boat level.
        """
        # Filter fish species allowed by the boat level
        available_fish = [
            fish for fish in FISH_SPECIES
            if fish.get("boat_level", 0) <= boat_level
        ]

        if not available_fish:
            raise ValueError("No fish available for this boat level.")

        # Adjust weights (optional: add logic here to favor rarer fish more as boat_level increases)
        weights = [fish["chance"] for fish in available_fish]

        fish_data = random.choices(available_fish, weights=weights, k=1)[0]

        return Fish(
            name=fish_data["name"],
            min_weight=fish_data["min_weight"],
            max_weight=fish_data["max_weight"],
            base_value=fish_data["base_value"],
            boat_level=boat_level
        )


    # Vars
    ## A place to store caught fish, used in multi-fishing with higher fishing rod levels
    catches = []
    ## How many times it will fish
    count = 0

    # Get Database
    db = getDB()
    
    # Get Fishing Rod Level
    fishing_rod_level_RESULT = db.fetchone(
        "SELECT rod_level FROM profiles WHERE user = ?", 
        (
            user,
        )
    )
    boat_level_RESULT = db.fetchone(
        "SELECT boat_level FROM profiles WHERE user = ?",
        (
            user,
        )
    )

    rod_level = fishing_rod_level_RESULT[0] if fishing_rod_level_RESULT else 1
    boat_level = boat_level_RESULT[0] if boat_level_RESULT else 0
    
    count = rod_level
    
    for i in range(count):
        if i == 0:
            caught = get_random_fish(boat_level)
            catches.append(caught)

            AnnounceRarity(user, caught)
        else:
            # 50% Chance to get an extra fish!
            if (random.randint(1,2)) == 1:
                caught = get_random_fish(boat_level)
                catches.append(caught)

                AnnounceRarity(user, caught)
    
    for i, fish in enumerate(catches):
        # Add fish into catches table
        db.execute(
            """
            INSERT INTO catches (user, fish_name, weight, value, variant, timestamp, isFav)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                user,
                fish.base_name,
                int(fish.weight * 1000),  # kg -> g
                fish.value,
                fish.variant,
                int(time.time()),
                False
            )
        )
    
    # Add total coin value from all caught fish
    total_value = sum(fish.value for fish in catches)
    
    # Add money into users table
    db.execute(
        """
        INSERT INTO profiles (user, coins)
        VALUES (?, ?)
        ON CONFLICT(user) DO UPDATE SET coins = coins + excluded.coins
        """,
        (
            user,
            total_value
        )
    )
    
    return catches