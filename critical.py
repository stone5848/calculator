cri_percentage = float(input())
increase = float(input())
cri_damage = float(input())
cri = 3.578740157480315 #치명100
result_cri = cri_percentage + increase
if result_cri > 100:
    result_cri = 100

before_damage = (100 * 100) + (cri_damage-100) * cri_percentage # 기본 식은 (100*100)+((100+크리템)*확률)
after_damage = (100 * 100) +  (cri_damage-100) * (result_cri)
print(before_damage)
print(after_damage)
print((after_damage - before_damage) / before_damage * 100)