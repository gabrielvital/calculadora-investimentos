print ("Bem vindo à Calculadora de Investimentos")
capital = float (input ("Capital investido: "))
juros = float (input ("Juros (%): "))
periodo = int (input ("Quantidade de meses: "))

for mes in range (1,periodo+1):
    capital = capital + (capital * (juros/100))
    print ("Mês", mes, "= R$", capital)
