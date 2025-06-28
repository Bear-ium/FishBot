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
)

# Fish Species
# Format: (name, min_weight_kg, max_weight_kg, base_value)
FISH_SPECIES = [
    {"name": "Trout",    "min_weight": 1.0, "max_weight": 3.0,  "base_value": 5},
    {"name": "Pike",     "min_weight": 2.0, "max_weight": 7.0,  "base_value": 8},
    {"name": "Bass",     "min_weight": 1.5, "max_weight": 5.0,  "base_value": 6},
    {"name": "Sturgeon", "min_weight": 4.0, "max_weight": 12.0, "base_value": 15},
]

# Defines variant types, their appearance chance (%), and reward multiplier
FISH_VARIANT_TIERS = [
    {"name": "Cursed",   "chance": 0.1,  "multiplier": 7.0},
    {"name": "Holy",     "chance": 0.2,  "multiplier": 5.0},
    {"name": "Void",     "chance": 0.5,  "multiplier": 4.0},
    {"name": "Diamond",  "chance": 1.0,  "multiplier": 3.0},
    {"name": "Ruby",     "chance": 1.0,  "multiplier": 2.5},
    {"name": "Emerald",  "chance": 1.0,  "multiplier": 2.5},
    {"name": "Golden",   "chance": 2.0,  "multiplier": 2.0},
    {"name": "Toxic",    "chance": 5.0,  "multiplier": 1.3},
    {"name": "Test",     "chance": 39.2, "multiplier": 50.0},
]