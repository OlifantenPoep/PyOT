slick_water_elemental = genMonster("Slick Water Elemental", 286, 8965)
slick_water_elemental.health(550, healthmax=550)
slick_water_elemental.type("undead")
slick_water_elemental.defense(armor=39, fire=0, earth=0, energy=1, ice=0, holy=0.4, death=0.5, physical=0.3, drown=1)
slick_water_elemental.experience(450)
slick_water_elemental.speed(280)
slick_water_elemental.behavior(summonable=0, hostile=True, illusionable=True, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=0)
slick_water_elemental.walkAround(energy=1, fire=0, poison=0)
slick_water_elemental.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
slick_water_elemental.voices("BLUUUUB", "SPLISH SPLASH")
slick_water_elemental.melee(175)
slick_water_elemental.loot( (2148, 100, 126), ("shiver arrow", 5.25, 3), ("iced soil", 6.0) )