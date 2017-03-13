
minotaur = genMonster("Minotaur", 25, 5969)
minotaur.health(100)
minotaur.type("blood")
minotaur.defense(armor=11, fire=0.8, earth=1, energy=1, ice=1.1, holy=0.9, death=1.1, physical=1, drown=1)
minotaur.experience(50)
minotaur.speed(170)
minotaur.behavior(summonable=330, hostile=True, illusionable=True, convinceable=330, pushable=True, pushItems=False, pushCreatures=False, targetDistance=1, runOnHealth=0)
minotaur.walkAround(energy=1, fire=1, poison=1)
minotaur.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
minotaur.voices("Kaplar!")
minotaur.melee(45)
minotaur.loot( ("mace", 13.0), ("chain armor", 9.75), (2148, 100, 25), ("axe", 3.25), ("minotaur horn", 2.75, 2), ("brass helmet", 8.5), ("meat", 5.25), ("sword", 5.25), ("plate shield", 20.0), ("minotaur leather", 1.0, 3), ("shovel", 0.25), ("bronze amulet", 0.0025) )