# WarhammerCombatSimulator
Warhammer 40k combat simulator used for simulating melee combat between two units.

The simulator follows the core 40k combat sequence:
- Hit rolls
- Wound rolls
- Saving throws (including invulnerable saves)
- Damage and model removal

Object oriented design for:
  - Units
  - Models
  - Weapons
  - Combat resolution
- Accurate strength vs toughness wound rules
- Armor saves and invulnerable saves
- Mixed weapon profiles within units (e.g. sergeants / leaders)
- Two combat modes:
  - **Slow mode** – detailed dice rolls per model, more suspense
  - **Fast mode** – aggregated rolls for faster simulations
- Turn-based combat rounds until one unit is destroyed

=== HOW TO RUN PROGRAM: ===

1. Make sure you have **Python 3.10+** installed
2. Clone the repository
3. Run the program from the project root:
```bash
python main.py