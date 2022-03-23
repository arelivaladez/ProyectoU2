#Menú
print("Menú")
print("1: Área del circulo")
print("2: Números Fibonacci")
r = int(input("¿Qué deseas hacer?: "))

<<<<<<< HEAD

=======
if r == 1:
	print ("Area Circulo")
	pi = 3.14

	radio = int(input("Ingresa el valor del radio: "))
	area = (radio ** 2) * pi
	print ("El área es ", area)
	
elif r == 2:
	n = int(input("Ingresa el numero: "))
	a = 1
	b = 1
	if n == 1:
		print('0')
	elif n == 2:
		print('0','1')
	else:
		print('0')
		print(a)
		print(b)
	for i in range(n-3):
		total = a + b
		b=a
		a= total
		print(total)
			
>>>>>>> NumerosFibonacci


