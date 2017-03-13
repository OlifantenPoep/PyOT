muddy_earth_elemental = genMonster("Muddy Earth Elemental", 301, 8933)
muddy_earth_elemental.health(650)
muddy_earth_elemental.type("undead")
muddy_earth_elemental.defense(armor=62, fire=1.15, earth=0, energy=0.85, ice=0.8, holy=0.5, death=0.6, physical=0.65, drown=1)
muddy_earth_elemental.experience(450)
muddy_earth_elemental.speed(260)
muddy_earth_elemental.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
muddy_earth_elemental.walkAround(energy=0, fire=1, poison=0)
muddy_earth_elemental.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
muddy_earth_elemental.melee(160)
muddy_earth_elemental.loot( (2148, 100, 128), ("lump of earth", 20.5), ("small stone", 100, 5), (2244, 19.5), ("coal", 0.5), ("natural soil", 4.25), ("clay lump", 0.75) )