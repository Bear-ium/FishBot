from Modules.SafeDB import getDB

def UpgradeFishingRodLevel(user: str, confirm: int):
    db = getDB()
    r = 1        # Default to 1 for Module Error
    i = "NomNom" # Twitch Emoji
    
    fishingRodLevel = db.fetchone(
            "SELECT rod_level FROM profiles WHERE user = ?",
            (user,)
        )
    fishingRodLevel = fishingRodLevel[0] if fishingRodLevel else 1
    
    coins = db.fetchone(
            "SELECT coins FROM profiles WHERE user = ?",
            (user,)
        )
    coins = coins[0] if coins else 0
    
    base_cost = 500
    cost = int(base_cost * (1.1 ** fishingRodLevel))
    
    if confirm == "c":
        if coins >= cost:
            newCoins = coins - cost
            newFishingRodLevel = fishingRodLevel + 1
            
            db.execute(
                """
                UPDATE profiles
                SET coins = ?, rod_level = ?
                WHERE user = ?
                """,
                (
                    newCoins,
                    newFishingRodLevel,
                    user,
                )
            )
            
            r = 200
            i = newFishingRodLevel
        else:
            r = 400
            i = f"{cost:,}"
    else:
        r = 100
        i = f"{cost:,}"
    
    return r, i #Request, Info

def UpgradeFishingBoatLevel(user: str, confirm: int):
    db = getDB()
    r = 1        # Default to 1 for Module Error
    i = "NomNom" # Twitch Emoji
    
    boatLevel = db.fetchone(
            "SELECT boat_level FROM profiles WHERE user = ?",
            (user,)
        )
    boatLevel = boatLevel[0] if boatLevel else 1
    
    coins = db.fetchone(
            "SELECT coins FROM profiles WHERE user = ?",
            (user,)
        )
    coins = coins[0] if coins else 0
    
    base_cost = 2500
    cost = int(base_cost * (1.4 ** boatLevel))
    
    if confirm == "c":
        if coins >= cost:
            newCoins = coins - cost
            newboatLevel = boatLevel + 1
            
            db.execute(
                """
                UPDATE profiles
                SET coins = ?, boat_level = ?
                WHERE user = ?
                """,
                (
                    newCoins,
                    newboatLevel,
                    user,
                )
            )
            
            r = 200
            i = newboatLevel
        else:
            r = 400
            i = f"{cost:,}"
    else:
        r = 100
        i = f"{cost:,}"
    
    return r, i #Request, Info

def GetFishingRodLevel(user):
    db = getDB()
    pass

def GetFishingBoatLevel(user):
    db = getDB()
    pass

def Balance(user: str) -> str:
    db = getDB()
    
    result = db.fetchone(
        "SELECT coins FROM profiles WHERE user = ?",
        (user,)
    )
    
    balance = result[0] if result else 0
    return f"{balance:,}"