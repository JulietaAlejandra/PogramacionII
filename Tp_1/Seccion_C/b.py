#Muñoz Julieta Alejandra

def fibonacci(numero):
    fn = [0,1]
    if numero == 1:
        print('0')
    elif numero == 2:
        print('[0,','1]')
    else:
        while len(fn) < numero:
            fn.append(0)
        if numero == 0 or numero == 1:
            return 1
        else:
            fn[0] = 0
            fn[1] = 1
            for i in range(2, numero):
                fn[i] = fn[i-1] + fn[i-2]
            print(fn)
    
while True: #Validacion numero
    try:
        numero = int(input('Ingrese un numero: '))
        break
    except ValueError:
        print('El valor ingresado es incorrecto. Ingrese un valor numerico.')
fibonacci(numero)