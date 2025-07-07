from typing import List

def Inventory(user: str, args: list) -> str:
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
    pass