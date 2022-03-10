

preco_menu = 15    # €
IVA        = 0.23  # 23%
gorjeta    = 0.10  # 10%

num_pessoas = int(input("Jantar para quantas pessoas? "))

despesa_s_iva = num_pessoas * preco_menu
montante_iva  = despesa_s_iva * IVA
despesa_c_iva = despesa_s_iva + montante_iva
montante_gorj = despesa_c_iva * gorjeta

print("Despesa S/ IVA:  {:.2f}€".format(despesa_s_iva))
print("Montante IVA:    {:.2f}€".format(montante_iva))
print("Despesa C/ IVA:  {:.2f}€".format(despesa_c_iva))
print("Gorjeta ({}%):   {:.2f}€".format(gorjeta, montante_gorj))
print()  
print("Despesa TOTAL:   {:.2f}€".format(despesa_c_iva + montante_gorj))
print()
