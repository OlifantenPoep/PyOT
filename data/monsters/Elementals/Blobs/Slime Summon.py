slime = genMonster("Slime", 19, 1496)
slime.health(150)
slime.type("slime")
slime.defense(armor=2, fire=1.1, earth=0, energy=1.1, ice=1.1, holy=1, death=1, physical=1, drown=1)
slime.experience(160)
slime.speed(120)
slime.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=False, targetDistance=1, runOnHealth=0)
slime.walkAround(energy=1, fire=1, poison=0)
slime.immunity(paralyze=0, invisible=0, lifedrain=0, drunk=0)
slime.voices("Blubb")
slime.melee(107)