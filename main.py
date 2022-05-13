"""
Author: Cesar Augusto Gil Ortiz
"""

import numpy as np
flag=True
while flag==True:
  opt=int(input('''Bienvenido a nuestra miscelánea de ejercicios, por favor elija el tema relacionado: 
  1. Operadores
  2. Condicionales
  3. Ciclos
  99. Salir (detener ejecución) \n''' ))
  if opt == 99:
    break
  if opt == 1:
    while flag==True:
        opt=int(input('''Bienvenido al menú Operadores, ingrese el ejercicio deseado:
      0. Volver al menú principal                    
      1. Área de un triangulo
      2. Suma de dos números
      3. Cuadrado de un número
      4. Conversión euros a dolares
      5. Área y perímetro cuadrado
      6. Área y volumen cilindro
      7. Área de un círculo
      8. Suma y promedio números
      99. Salir (detener ejecución) \n''' ))
  
        if opt == 0:
          break
        #Ejercicio 1
        if opt == 1:
          while True:
            base = float(input('ingrese la base del triángulo \n'))
            altura = float(input('ingrese la altura del triángulo \n'))
            area = base * altura/2
            print('el área del triángulo es: ', area)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
            
              
        #Ejercicio 2
        if opt == 2:
          while True:
            print('Suma de dos números')
            n1= float(input('ingrese el primer numero a sumar: \n'))
            n2= float(input('ingrese el segundo numero a sumar: \n'))
            res=n1 + n2
            print('la suma es: ', res)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 3
        if opt == 3:
          while True:
            print('Cuadrado de un número')
            n1= float(input('ingrese el número: \n'))
            res=n1**2
            print('el número ', n1, 'elevado al cuadrado es: ', res)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break  
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 4
        if opt == 4:
          while True:
            print('Conversión euros a dolares')
            x=float(input('ingrese la cantidad de euros: \n'))
            rate=float(input('Ingrese la tasa de cambio (1 EUR equivale a x USD) \n'))
            res=x*rate
            print(x, 'EUR', 'equivalen a: ', res, 'USD')
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 5
        if opt == 5:
          while True:
            print('Área y perímetro cuadrado')
            lado=float(input('ingrese el lado del cuadrado: \n'))
            area=lado**2
            perimetro=lado*4
            print('el área del cuadrado es:', area, '\n' ,'el perímetro del cuadrado es:', perimetro)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 6
        if opt == 6:
          while True:
            r=float(input('ingrese el radio del circulo de la base del cilindro: \n'))
            h=float(input('ingrese la altura del cilindro: \n'))
            vol=round(h*np.pi*(r**2),2)
            A_L=2*np.pi*r*h
            A_B=np.pi*(r**2)
            A_T=round(A_L+2*A_B,2)
            print('el volumen del cilindro es:', vol)
            print('el área del cilindro es:', A_T)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 7
        if opt == 7:
          while True:
            print('Área de un círculo')
            r=float(input('escriba el radio del círculo: '))
            perimetro=round(2*r*np.pi,2)
            area=round(np.pi*(r**2),2)
            print('el área del círculo es:' , area)
            print('el perímetro del círculo es:', perimetro)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 8
        if opt == 8:
          while True:
            print('suma y promedio números')
            n1=float(input('ingrese número 1: '))
            n2=float(input('ingrese número 2: '))
            n3=float(input('ingrese número 3: '))
            suma=n1+n2+n3
            prom=suma/3
            print('la suma es:', suma)
            print('el promedio es:' , prom)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
  
  if opt == 2:
    while flag == True:
        opt=int(input('''Ingrese el ejercicio deseado: 
      0. Volver al menú principal                    
      1. Determinar si el número es positivo o negativo
      2. Determinar número mayor y menor de dos números
      3. Determinar número mayor y menor de tres números
      4. Dados dos números A y B, sumarlos si A es menor que B o sino restarlos
      5. Cociente entre dos números
      6. Sumar dos números si al menos uno de ellos es negativo, en caso contrario multiplicarlos
      7. Determinar si un año es bisiesto
      99. Salir (detener ejecución) \n''' ))
        if opt == 0:
          break
          
        #Ejercicio 1  
        if opt == 1: 
          while True:
            n=float(input('ingrese un numero: \n'))
            if n<0:
              print('el número es negativo')
            else:
              print('el número es positivo')
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 2
        if opt == 2:
          while True:
            n1=float(input('ingrese un numero: \n'))
            n2=float(input('ingrese un numero: \n'))
            if n1 > n2:
              print('el mayor número es:', n1, 'y el menor es:', n2)
            else:
              print('el mayor número es:', n2, 'y el menor es:', n1)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 3
        if opt == 3:
          while True:
            mayor = None
            menor = None
            numeros=[]
            for n in range(3):
              numero = int(input('ingrese un número: '))
              numeros.append(numero)
            for n in numeros:
              if mayor == None and menor == None:
                mayor = menor = n
              if n > mayor:
                mayor = n
              if n < menor:
                menor = n
            print('el número menor es:', menor)
            print('el número mayor es:', mayor)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
          
        #Ejercicio 4
        if opt == 4:
          while True:
            n1=float(input('ingrese el primer numero: \n'))
            n2=float(input('ingrese el segundo numero: \n'))
            if n1 < n2:
              res=n1+n2
              print('el primer número es menor, por tanto se procede a realizar la suma de ambos números:', res)
            else:
              res=n1-n2
              print('el segundo número es menor o igual, por tanto se procede a realizar la resta de ambos números:', res)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 5
        if opt == 5:
          while True:
            n1=float(input('ingrese el primer número (dividendo): \n'))
            n2=float(input('ingrese el segundo número (divisor): \n'))
            try:
              res = n1 / n2
              print('el cociente entre', n1, 'y', n2, 'es:', res)
            except:
              print('no es posible realizar una división por 0')
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
          
        #Ejercicio 6
        if opt == 6:
          while True:
            n1=float(input('ingrese el primer numero: \n'))
            n2=float(input('ingrese el segundo numero: \n'))
            if n1<0 or n2<0:
              res = n1 + n2
              print('Número negativo detectado, se realiza la suma:', res)
            else: 
              res = n1 * n2
              print('Ambos números son positivos, se realiza el producto:', res)
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
      
        #Ejercicio 7
        if opt == 7:
          while True:
            año=int(input('Ingrese el año que desea conocer:'))
            if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0 and año % 100 == 0):
              print('el año', año, 'es bisiesto')
            else:
              print('el año', año, 'no es bisiesto')  
            choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
            if choice=='1':
              continue
            elif choice == '2':
              break
            elif choice == '99':
              flag=False
              break
  
  if opt == 3:   
    while flag == True:
      opt=int(input('''Ingrese el ejercicio deseado: 
      0. Volver al menú principal                  
      1. Múltiplos de 3 entre 1 y 100
      2. Números impares entre 0 y 100
      3. Números pares entre 1 y 100
      4. Cuadrado de los números del 1 al 30
      5. Suma de los cuadrados de los cien primeros números naturales
      6. Números comprendidos en un rango
      7. Suma de todos los números digitados
      99. Salir (detener ejecución) \n''' ))
      if opt == 0:
          break
        
      #Ejercicio 1
      if opt == 1: 
        while True:
          nums=[]
          for i in range(1,101):
            if i % 3 == 0:
              nums.append(i)
          print(nums)
          choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
          if choice=='1':
            continue
          elif choice == '2':
            break
          elif choice == '99':
              flag=False
              break
      
      #Ejercicio 2
      if opt == 2:
        while True:
          nums=[]
          for i in range(101):
            if i % 2 != 0:
              nums.append(i)
          print(nums)
          choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
          if choice=='1':
            continue
          elif choice == '2':
            break
          elif choice == '99':
              flag=False
              break
      
      #Ejercicio 3
      if opt == 3:
        while True:
          nums=[]
          for i in range(1,101):
            if i % 2 == 0:
              nums.append(i)
          print(nums)
          choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
          if choice=='1':
            continue
          elif choice == '2':
            break
          elif choice == '99':
              flag=False
              break
        
      #Ejercicio 4
      if opt == 4:
        while True:
          nums=[]
          for i in range(1,31):
            nums.append(i**2)
          print(nums)
          choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
          if choice=='1':
            continue
          elif choice == '2':
            break
          elif choice == '99':
              flag=False
              break
      
      #Ejercicio 5
      if opt == 5:
        while True:
          nums=[]
          suma=0
          for i in range(1,101):
            nums.append(i**2)
          print(nums) 
          print('la suma de los cuadrados de los 100 primeros números es:',sum(nums))
          choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
          if choice=='1':
            continue
          elif choice == '2':
            break
          elif choice == '99':
              flag=False
              break
     
      #Ejercicio 6
      if opt == 6:
        while True:
          n1=int(input('Digite el número inicial de la secuencia \n'))
          n2=int(input('Digite el número final de la secuencia \n'))  
          nums=[]
          for i in range(n1, n2 + 1):
            nums.append(i)
          print('\n La secuencia ascendente de los números es:', nums)
          choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
          if choice=='1':
            continue
          elif choice == '2':
            break 
          elif choice == '99':
              flag=False
              break
      
      #Ejercicio 7
      if opt == 7:
        while True:
          nums=[]
          while True:
              n=float(input('Digite el número a sumar, para concluir la suma por favor digite 0:'))
              if n!=0:
                  nums.append(n)
              else:
                  break
          print('Los números digitados fueron:', nums)
          print('La suma de los números fue:', sum(nums))
          choice=input('''Por favor digite la acción a realizar:
      1. Ejecutar nuevamente el ejercicio
      2. Ejecutar otro ejercicio del mismo tema
      99. Finalizar la sesión \n''')
          if choice=='1':
            continue
          elif choice == '2':
            break
          elif choice == '99':
              flag=False
              break
print('''Programa terminado---Gracias''')      