import subprocess as Subprocess
import sympy as Sympy
import numpy as Numpy
from scipy import integrate as Integrate


def CalcularIntegralDefinidaExacta(integralDefinida, limiteSuperiror, limiteInferior):
    elementoDiferencial = 'dx'
    integral = Sympy.sympify(integralDefinida)
    integralCalculada = Sympy.integrate(integral, ('x', limiteSuperiror, limiteInferior))
    print(f'El resultado de la integral {integral} {elementoDiferencial} con límite superior de {limiteSuperiror} y límite inferior de {limiteInferior} es: {integralCalculada}')


def CalcularIntegralIndefinida(funcion):
    variableSimbolica = Sympy.Symbol('x')
    integralIndefinidaCalculada = Sympy.integrate(funcion, variableSimbolica)
    print(f'La Integral Indefinida de la función {funcion} es: {integralIndefinidaCalculada}')


def CalcularIntegralDefinida_ReglaTrapecio(funcion, limiteSuperior, limiteInferior, numeroSubintervalos):
    f = lambda x: eval(funcion)
    a, b, n = limiteSuperior, limiteInferior, numeroSubintervalos
    x = Numpy.linspace(a, b, n)
    y = f(x)
    reglaTrapecio = Integrate.trapz(y, x)
    print(f'La integral de la función {funcion} dx con límite superior de {a}, con límite inferior de {b} y con un número de subintervalos de {n}, utilizando la regla de Trapecio es: {reglaTrapecio}')
    
    
def CalcularIntegralDefinida_ReglaSimpson(funcion, limiteSuperior, limiteInferior, numeroSubintervalos):
    f = lambda x: eval(funcion)
    a, b, n = limiteSuperior, limiteInferior, numeroSubintervalos
    x = Numpy.linspace(a, b, n)
    y = f(x)
    reglaSimpson = Integrate.simps(y, x)
    print(f'La integral de la función {funcion} dx con límite superior de {a}, con límite inferior de {b} y con un número de subintervalos de {n}, utilizando la regla de Trapecio es: {reglaSimpson}')    


def IntroducirIntegralDefinida():
    Subprocess.run('cls', shell=True)

    integralDefinidaInput = input('Introduzce la Integral Definida: ')
    limiteSuperior = float(input('Introduce el Límite Superior: '))
    limiteInferior = float(input('Introduce el Límite Inferior: '))
    print('\n')
    esExacta = input('¿Es la Integral introducida exacta? [Si/No]: ').lower()

    if esExacta == 'si':
        Subprocess.run('cls', shell=True)
        CalcularIntegralDefinidaExacta(integralDefinidaInput, limiteInferior, limiteSuperior)

    elif esExacta == 'no':
        Subprocess.run('cls', shell=True)
        print('LA FUNCION ES APROXIMADA')
        print('\n')
        trapecio_simpson = input('¿Qué regla vas a usar? ¿Trapecio o Simpson? ').lower()

        if trapecio_simpson == 'trapecio':
            while True:
                try: 
                    n = int(input('Inserta el número de Subintervalos: '))
                    f = integralDefinidaInput
                    a = limiteSuperior
                    b = limiteInferior
                    CalcularIntegralDefinida_ReglaTrapecio(f, a, b, n)
                    break;
                except ValueError:
                    print("ERROR: Debes ingresar un número entero. Vuelve a intentarlo.\n")
                    
        elif trapecio_simpson == 'simpson':
            while True:
                try: 
                    n = int(input('Inserta el número de Subintervalos: '))
                    f = integralDefinidaInput
                    a = limiteSuperior
                    b = limiteInferior
                    CalcularIntegralDefinida_ReglaSimpson(f, a, b, n)
                    break;
                except ValueError:
                    print("ERROR: Debes ingresar un número entero. Vuelve a intentarlo.\n")
    else:
        Main()


def IntroducirIntegralIndefinida():
    funcion = input('Introduce la función: ')
    CalcularIntegralIndefinida(funcion)


def Main():
    while True:
        print('ELIGA EL TIPO DE INTEGRAL A INTRODUCIR')
        print('1. Integral Definida')
        print('2. Integral Indefinida')
        print('3. Salir del Programa')

        try:
            opcion = int(input('Introduzca el número de la opción: '))

            if opcion == 1:
                Subprocess.run('cls', shell=True)
                print('SELECCIONASTE LA OPCIÓN 1: INTEGRAL DEFINIDA')
                print('\n')
                IntroducirIntegralDefinida()
                break

            elif opcion == 2:
                Subprocess.run('cls', shell=True)
                print('SELECCIONASTE LA OPCIÓN 2: INTEGRAL INDEFINIDA')
                print('\n')
                IntroducirIntegralIndefinida()
                break

            elif opcion == 3:
                Subprocess.run('cls', shell=True)
                print('Has salido del Programa')
                break

            else:
                Subprocess.run('cls', shell=True)
                print("ERROR: La opción insertada está fuera del rango establecido(1-3). Vuelve a intentarlo.")
                print('\n')

        except ValueError:
            Subprocess.run('cls', shell=True)
            print("ERROR: Debes ingresar un número entero. Vuelve a intentarlo.")
            print('\n')


Main()
