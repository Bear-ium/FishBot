from typing import List

from Modules.SafeDB import getDB
from typing import List

def Inventory(user: str, args: list) -> str: #type: ignore
    """
    View and sort a user's fish inventory by the following:

    - fish_name: total count of each fish type
    - weight:
        - total combined weight
        - top 10 heaviest
        - bottom 10 lightest
        - heaviest single fish
        - lightest single fish
    - value:
        - top 10 most valuable
        - bottom 10 least valuable
        - most valuable single fish
        - least valuable single fish
    - variant:
        - total count of variant
        - total count per variant
        - sort variants by total weight (asc/desc)
        - sort variants by total value (asc/desc)
    - timestamp:
        - fish caught before a duration
        - fish caught after a duration
        - fish caught between two durations
        - oldest catch
        - most recent catch
    - favourites:
        - up to 5 fish marked as favourites (isFav)
    """
    
    filter_map = {
        1: "fish_name",
        2: "weight",
        3: "value",
        4: "variant",
        5: "timestamp",
        6: "favourites"
    }

    filter_by = filter_map.get(int(args[0] if args else 0) if str(filter_by).isdigit() else 1, "fish_name") # type: ignore
    sort_by = args[1] if len(args) > 1 else 0
    
    db = getDB()
    
    match int(filter_by):
        case 1:
            fish_caught = db.fetchall(
                "SELECT fish_name FROM catches WHERE user = ?",
                (user,)
            )
            
            fish_total = len(fish_caught)
            
            return f"{fish_total}"

        case 2:
            return ""
        case 3:
            return ""
        case 4:
            variants_caught = db.fetchall(
                "SELECT variant FROM catches WHERE user = ?",
                (user,)
            )
            
            variants_total = len(variants_caught)
            
            if sort_by == "all":
                return f"{variants_total}"
            elif sort_by == "":
                return ""
        case 5:
            return ""

        case 6:
            favourites = db.fetchall(
                "SELECT fish_name FROM catches WHERE user = ? AND isFav = ?",
                (user,1,)
            )
            favourite_names = [row[0] for row in favourites][:5]
            favourites_string = " | ".join(favourite_names)
            
            return favourites_string

        case _:
            return f"Please refer to our website and see command usage -inventory <filter> <sort>"