dias = int(input("Quantos dias Alugados ? : "))
kmP = float(input("Quantos km percorridos ? : "))

pdiario =dias *60+kmP*0.15
print("O total a pagar é de {:.2f}" .format(pdiario))
