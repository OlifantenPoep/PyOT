phantasm = genMonster("Phantasm", 241, 6344)
phantasm.health(3950)
phantasm.type("undead")
phantasm.defense(armor=2, fire=1.1, earth=0.8, energy=1.1, ice=0.8, holy=1.1, death=0, physical=0, drown=1)
phantasm.experience(4400)
phantasm.speed(280)
phantasm.behavior(summonable=0, hostile=True, illusionable=False, convinceable=0, pushable=False, pushItems=True, pushCreatures=True, targetDistance=1, runOnHealth=400)
phantasm.walkAround(energy=1, fire=1, poison=1)
phantasm.immunity(paralyze=1, invisible=1, lifedrain=1, drunk=1)
phantasm.voices("Oh my, you forgot to put your pants on!", "Weeheeheeheehee!", "Its nothing but a dream.", "Dream a little dream with me!", "Give in.")
phantasm.melee(470)
phantasm.summon("phantasm summon", 15)
phantasm.maxSummons(4)
phantasm.loot( (2148, 100, 268), ("blank rune", 36.25, 2), ("shadow herb", 29.25), ("demonic essence", 19.5, 3), ("small emerald", 15.0, 3), ("rusty armor", 7.75), ("soul orb", 11.25), ("great mana potion", 5.0), ("platinum coin", 1.25), ("crown armor", 0.5), ("stealth ring", 0.75), ("abyss hammer", 0.25) )