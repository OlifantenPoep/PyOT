conjure = spell.Spell("Holy Missile", "adori san", icon=23, group=SUPPORT_GROUP)
conjure.require(mana=350, level=27, maglevel=0, soul=3, learned=0, vocations=(3, 7))
conjure.use(2260)
conjure.cooldowns(0, 3)
conjure.targetEffect(callback=spell.conjure(2295, 5))

rune = spell.Rune(2295, icon=130, count=5, target=TARGET_TARGET, group=ATTACK_GROUP)
rune.cooldowns(0, 2)
rune.require(mana=0, level=27, maglevel=0)
rune.targetEffect(callback=spell.damage(1.8, 3.8, 11, 13, HOLY))
rune.effects(area=EFFECT_HOLYDAMAGE, shoot=ANIMATION_HOLY)