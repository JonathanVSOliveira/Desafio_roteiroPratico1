gastos_pedro = [300, 500, 200, 800]
gastos_joao = [200, 400, 500, 700]

valorP = sum(gastos_pedro)
valorJ = sum(gastos_joao)

if valorP>valorJ:
    print(f"Pedro gastou mais dinheiro esse mês")
else: 
    print(f"João gastou mais dinheiro esse mês")