"""
Centralized configuration for bot settings, admin roles, and fish definitions.
"""

# Constants
COMMAND_HANDLE =  "-"
COOLDOWN_SECONDS = 5  # Delay between uses of -fish per user

# Admin list
ADMINS = (
    "majojobears",
    "theactualevie",
    "danmanplayz",
)

# Fish Species
# Format: (name, min_weight_kg, max_weight_kg, base_value, chance)
FISH_SPECIES = [
    # Example
    # {"name": "Trout",    "min_weight": 1.0,  "max_weight": 3.0,  "base_value": 5,  "chance": 40},
    # {"name": "", "min_weight": 1.0, "max_weight": 2.0, "base_value": 1, "chance": 100},

    # 🟢 Common
    {"name": "Bluegill",         "min_weight":  0.67, "max_weight":  2.49, "base_value":   1, "chance":   100},
    {"name": "Guppy",            "min_weight":  1.09, "max_weight":  2.23, "base_value":   2, "chance":   100},
    {"name": "Carp",             "min_weight":  1.00, "max_weight":  2.88, "base_value":   1, "chance":   100},
    {"name": "Perch",            "min_weight":  1.36, "max_weight":  2.91, "base_value":   2, "chance":   100},
    {"name": "Minnow",           "min_weight":  1.47, "max_weight":  2.23, "base_value":   2, "chance":   100},
    {"name": "Sunfish",          "min_weight":  1.31, "max_weight":  2.47, "base_value":   1, "chance":   100},
    {"name": "Tilapia",          "min_weight":  1.29, "max_weight":  1.93, "base_value":   1, "chance":   100},
    {"name": "Molly",            "min_weight":  0.66, "max_weight":  1.92, "base_value":   2, "chance":   100},
    {"name": "Crappie",          "min_weight":  1.50, "max_weight":  2.19, "base_value":   1, "chance":   100},
    {"name": "Catfish",          "min_weight":  1.02, "max_weight":  2.57, "base_value":   3, "chance":   100},
    {"name": "Anchovy",          "min_weight":  0.71, "max_weight":  1.94, "base_value":   3, "chance":   100},
    {"name": "Sardine",          "min_weight":  1.28, "max_weight":  2.39, "base_value":   2, "chance":   100},
    {"name": "Trout",            "min_weight":  1.04, "max_weight":  1.93, "base_value":   2, "chance":   100},
    {"name": "Shiner",           "min_weight":  0.56, "max_weight":  1.56, "base_value":   1, "chance":   100},
    {"name": "Whiting",          "min_weight":  0.33, "max_weight":  1.66, "base_value":   3, "chance":   100},
    {"name": "Chub",             "min_weight":  1.30, "max_weight":  2.86, "base_value":   1, "chance":   100},
    {"name": "Smelt",            "min_weight":  0.82, "max_weight":  2.57, "base_value":   1, "chance":   100},
    {"name": "Roach",            "min_weight":  0.70, "max_weight":  1.57, "base_value":   3, "chance":   100},
    {"name": "White Perch",      "min_weight":  0.26, "max_weight":  2.40, "base_value":   3, "chance":   100},
    {"name": "Largemouth Bass",  "min_weight":  0.39, "max_weight":  2.81, "base_value":   2, "chance":   100},

    # 🔵 Uncommon
    {"name": "Walleye",          "min_weight":  1.18, "max_weight":  4.02, "base_value":   7, "chance":    25},
    {"name": "Pike",             "min_weight":  1.08, "max_weight":  4.54, "base_value":   6, "chance":    25},
    {"name": "Red Drum",         "min_weight":  2.82, "max_weight":  5.51, "base_value":   5, "chance":    25},
    {"name": "Shad",             "min_weight":  2.59, "max_weight":  3.73, "base_value":   5, "chance":    25},
    {"name": "Bowfin",           "min_weight":  2.38, "max_weight":  5.23, "base_value":   7, "chance":    25},
    {"name": "White Bass",       "min_weight":  1.18, "max_weight":  3.06, "base_value":   6, "chance":    25},
    {"name": "Lake Trout",       "min_weight":  2.15, "max_weight":  3.62, "base_value":   4, "chance":    25},
    {"name": "Sheepshead",       "min_weight":  1.04, "max_weight":  5.19, "base_value":   4, "chance":    25},
    {"name": "Skipjack Tuna",    "min_weight":  2.55, "max_weight":  5.42, "base_value":   6, "chance":    25},
    {"name": "Peacock Bass",     "min_weight":  2.69, "max_weight":  4.61, "base_value":   5, "chance":    25},
    {"name": "Brook Trout",      "min_weight":  1.76, "max_weight":  3.84, "base_value":   8, "chance":    25},
    {"name": "Barramundi",       "min_weight":  2.86, "max_weight":  5.21, "base_value":   8, "chance":    25},
    {"name": "Cobia",            "min_weight":  2.16, "max_weight":  5.93, "base_value":   8, "chance":    25},
    {"name": "Arctic Char",      "min_weight":  1.72, "max_weight":  5.79, "base_value":   7, "chance":    25},
    {"name": "Snakehead",        "min_weight":  2.02, "max_weight":  3.58, "base_value":   7, "chance":    25},

    # 🟣 Rare
    {"name": "Sturgeon",         "min_weight":  4.06, "max_weight": 11.96, "base_value":  15, "chance":    10},
    {"name": "Goliath Tigerfish","min_weight":  4.91, "max_weight":  9.75, "base_value":  11, "chance":    10},
    {"name": "Mahseer",          "min_weight":  4.87, "max_weight": 10.52, "base_value":  11, "chance":    10},
    {"name": "Blue Marlin",      "min_weight":  3.17, "max_weight":  7.97, "base_value":  11, "chance":    10},
    {"name": "Arapaima",         "min_weight":  4.46, "max_weight":  9.27, "base_value":  17, "chance":    10},
    {"name": "Taimen",           "min_weight":  3.24, "max_weight":  7.32, "base_value":  17, "chance":    10},
    {"name": "Opah",             "min_weight":  2.19, "max_weight":  6.98, "base_value":  13, "chance":    10},
    {"name": "Alligator Gar",    "min_weight":  4.80, "max_weight": 11.19, "base_value":  18, "chance":    10},
    {"name": "Napoleon Wrasse",  "min_weight":  4.44, "max_weight": 10.48, "base_value":  18, "chance":    10},

    # 🟠 Epic
    {"name": "Giant Trevally",         "min_weight":  2.37, "max_weight":  4.03, "base_value":  17, "chance":     3},
    {"name": "Atlantic Bluefin Tuna",  "min_weight":  4.36, "max_weight": 14.67, "base_value":  49, "chance":     3},
    {"name": "Sailfish",               "min_weight":  4.34, "max_weight":  6.83, "base_value":  54, "chance":     3},
    {"name": "Dogtooth Tuna",          "min_weight":  6.23, "max_weight": 17.97, "base_value":  57, "chance":     3},
    {"name": "Arowana",                "min_weight":  5.42, "max_weight": 15.60, "base_value":  43, "chance":     3},
    {"name": "Oarfish",                "min_weight":  7.70, "max_weight": 18.98, "base_value":  50, "chance":     3},
    {"name": "Mahi-Mahi",              "min_weight":  6.93, "max_weight": 23.47, "base_value":  59, "chance":     3},
    {"name": "Swordfish",              "min_weight":  6.54, "max_weight":  8.42, "base_value":  53, "chance":     3},
    {"name": "Yellowfin Tuna",         "min_weight":  7.12, "max_weight": 21.24, "base_value":  31, "chance":     3},

    # 🔴 Legendary
    {"name": "Coelacanth",        "min_weight": 14.81, "max_weight": 42.52, "base_value": 108, "chance":    0.5},
    {"name": "Mekong Catfish",    "min_weight": 14.39, "max_weight": 53.62, "base_value":  79, "chance":    0.5},
    {"name": "Arapaima gigas",    "min_weight":  9.91, "max_weight": 43.78, "base_value": 117, "chance":    0.5},
    {"name": "Great White Shark", "min_weight":  8.20, "max_weight": 51.50, "base_value": 125, "chance":    0.5},
    {"name": "Megalodon",         "min_weight": 50.00, "max_weight":156.00, "base_value": 185, "chance":   0.05},

    # ⚪ Mythic
    {"name": "🐸 Forgi",             "min_weight":  0.01, "max_weight": 1000.00, "base_value":      9999, "chance": 0.0001},
    {"name": "🐿️ Chipmunk Filter",   "min_weight":  0.01, "max_weight":    0.1, "base_value":      55000, "chance": 0.0001},
    {"name": "🦊 Eevee of the Lake", "min_weight":  0.01, "max_weight":   54.00, "base_value":   1000000, "chance": 0.0001},
    {"name": "🐻 Debug Stick",       "min_weight":  0.01, "max_weight":   5.00, "base_value":      69420, "chance": 0.0001},
]

# Defines variant types, their appearance chance (%), and reward multiplier
FISH_VARIANT_TIERS = [
    # 🔴 Legendary (Total: 0.16%)
    {"name": "🐉 Mythic",       "chance": 0.01, "multiplier": 100.0},
    {"name": "💀 Cursed",       "chance": 0.05, "multiplier": 7.0},
    {"name": "🌑 Shadow",       "chance": 0.1,  "multiplier": 6.5},

    # 🟣 Rare (Total: 1.6%)
    {"name": "📜 Ancient",      "chance": 0.3,  "multiplier": 6.0},
    {"name": "😇 Holy",         "chance": 0.4,  "multiplier": 5.5},
    {"name": "☢️ Radioactive",  "chance": 0.5,  "multiplier": 5.0},
    {"name": "🕳️ Void",         "chance": 0.4,  "multiplier": 4.5},

    # 🔵 Uncommon (Total: 4.6%)
    {"name": "💎 Diamond",      "chance": 0.8,  "multiplier": 3.5},
    {"name": "🔴 Ruby",         "chance": 1.0,  "multiplier": 3.0},
    {"name": "💚 Emerald",      "chance": 1.0,  "multiplier": 2.8},
    {"name": "🏅 Golden",       "chance": 1.2,  "multiplier": 2.2},
    {"name": "❄️ Frozen",       "chance": 0.6,  "multiplier": 2.4},

    # 🟢 Common (Total: 23.59%)
    {"name": "✨ Glowing",      "chance": 1.2,  "multiplier": 1.9},
    {"name": "🪄 Enchanted",    "chance": 1.0,  "multiplier": 1.7},
    {"name": "☠️ Toxic",        "chance": 1.6,  "multiplier": 1.5},
    {"name": "🐟 Speckled",     "chance": 2.0,  "multiplier": 1.4},
    {"name": "🛠️ Rusty",        "chance": 7.0,  "multiplier": 1.1},
    {"name": "🧼 Slimy",        "chance": 9.99, "multiplier": 1.2},
]