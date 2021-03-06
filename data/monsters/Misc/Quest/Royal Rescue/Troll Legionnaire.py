troll_legionnaire = genMonster("Troll Legionnaire", 53, 5998)
troll_legionnaire.health(210)
troll_legionnaire.type("blood")
troll_legionnaire.defense(armor=13, fire=1, earth=1, energy=1, ice=1, holy=1, death=1, physical=1, drown=1)
troll_legionnaire.experience(140)
troll_legionnaire.speed(190)
troll_legionnaire.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=4, runOnHealth=10)
troll_legionnaire.walkAround(energy=0, fire=0, poison=0)
troll_legionnaire.immunity(paralyze=0, invisible=1, lifedrain=0, drunk=0)
troll_legionnaire.voices("Attack!", "Graaaaar!")
troll_legionnaire.melee(40)
troll_legionnaire.loot( (2148, 100, 156), ("throwing star", 100, 10), ("frosty ear of a troll", 2.75), ("stealth ring", 0.5) )