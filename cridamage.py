cri_percentage = float(input())
cridamage = float(input())
increase = float(input())
cri = 3.578740157480315 #치명100

before_damage = (100 * 100) + (cridamage-100) * cri_percentage # 기본 식은 (100*100)+((100+크리템)*확률)
after_damage = (100 * 100) +  (cridamage + increase -100) * cri_percentage
print(before_damage)
print(after_damage)
print((after_damage - before_damage) / before_damage * 100)