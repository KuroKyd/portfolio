#total de energia a pagar
Consumo = int(input(Consumo de energia: ))
if Consumo < 100 : Vconsumo = float(Consumo * 0.50)
if Consumo >= 100 < 250 : Vconsumo = float(Consumo * 0.75)
if Consumo >= 250 < 500 : Vconsumo = float(Consumo * 1.00)
if Consumo >= 500 : Vconsumo = float(Consumo * 1.25)
Total = Vconsumo + 50
print(round(Total, 2))
