davlatlar = ["Turkiya", "Germaniya", "AQSH", "Italiya"]

print( davlatlar)
print( len(davlatlar))
print( sorted(davlatlar, reverse=True))
print( sorted(davlatlar))
print( davlatlar)

davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print( davlatlar)
davlatlar.sort(reverse=True)
print( davlatlar)

juft_sonlar = list(range(120, 1201, 2))
print( sum(juft_sonlar))
print( max(juft_sonlar) - min(juft_sonlar))
print( len(juft_sonlar))

orta_boshlanish = (len(juft_sonlar) - 20) // 2
print( juft_sonlar[:20])
print( juft_sonlar[orta_boshlanish:orta_boshlanish + 20])
print( juft_sonlar[-20:])

taomlar = ["osh", "manti", "shashlik", "tuxum", "non"]
nonushta = taomlar.copy()
nonushta = [taom for taom in nonushta if taom in ["tuxum", "non"]]
nonushta.extend(["bo'tqa", "qaymoq va non"])

print( taomlar)
print( nonushta)

nonushta = tuple(nonushta)
print("O'zgarmas nonushta ro'yxati:", nonushta)
