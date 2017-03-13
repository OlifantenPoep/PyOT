quara_mantassin = genMonster("Quara Mantassin", 72, 6064)
quara_mantassin.health(800)
quara_mantassin.type("blood")
quara_mantassin.defense(armor=17, fire=0, earth=1.1, energy=1.25, ice=0, holy=1, death=1, physical=1, drown=0)
quara_mantassin.experience(400)
quara_mantassin.speed(520)
quara_mantassin.behavior(summonable=0, hostile=True, illusionable=False, convinceable=480, pushable=False, pushItems=True, pushCreatures=False, targetDistance=1, runOnHealth=40)
quara_mantassin.walkAround(energy=1, fire=0, poison=1)
quara_mantassin.immunity(paralyze=1, invisible=0, lifedrain=0, drunk=1)
quara_mantassin.voices("Shrrrr", "Zuerk Pachak!")
quara_mantassin.loot( ("halberd", 4.0), (2148, 100, 129), ("blue robe", 0.25), ("stealth ring", 1.0), ("fish fin", 0.5, 3), ("two handed sword", 1.0), ("cape", 1.0), ("small sapphire", 1.25), ("shrimp", 4.75), ("mantassin tail", 9.5), ("strange helmet", 0.0025) )

quara_mantassin.melee(140)
quara_mantassin.selfSpell("Haste", 360, 360, length=8, check=chance(9)) #strength time?
#quara_mantassin.selfSpell("Invisible", 360, 360, length=8, check=chance(9))