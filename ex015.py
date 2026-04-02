codigo = "Aluguel altomotivo"
print(codigo.center(38, '='))#imprime o nome do codigo
km = float(input('Quantos Kms foram percorridos?: ')) #coleta km
dias = int(input('O carro foi alugado quantos dias?: ')) #coleta dias
custo_km = km * 0.15 #calcula valor de km rodado
custo_dias = dias * 60 #calcula valor de dias
custo_total = custo_km + custo_dias #calcula custo total
print(f"O custo contabilizando os Km R${custo_km} e os dias R${custo_dias} totalizando R${custo_total}") #Imprime informativo com valor total