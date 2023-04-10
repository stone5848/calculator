spe_quotient = 0.0822550831792976 # 특화1당 해방 스킬 피해량
spe = int(input())
damage = (45 * ((spe * spe_quotient)/100)) + 145

print(((damage/145)-1)*100)