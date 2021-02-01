def main():
	msg='''
	En este programa se observa la tabla de multplicar de 
	un numero determinado
	:)
	'''
	print(msg)
	x = input("Ingrese la tabla del numero que desea ")
	x = int (x)
	print("Ahora la tabla del {}".format(x))

	for e in range(12):
		M=x*e
		print("Operacion {} x {} = {}".format(x,e,M))
if __name__ =="__main__":
	main()
