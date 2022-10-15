#consumo de água
Consumo = int(input())
if Consumo < 10: Vconsumo = float(Consumo * 2.0)
if Consumo >= 10 < 20: Vconsumo = float(Consumo * 2.5)
if Consumo >= 20 < 40: Vconsumo = float(Consumo * 2.75)
if Consumo >= 40: Vconsumo = float(Consumo * 3.0)
total = Vconsumo + 20
print(round(total, 2))
