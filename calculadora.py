import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def sumar_vectores(v1, v2):
    return np.add(v1, v2)

def restar_vectores(v1, v2):
    return np.subtract(v1, v2)

def producto_punto(v1, v2):
    return np.dot(v1, v2)

def producto_cruz(v1, v2):
    return np.cross(v1, v2)

def graficar_vectores(v1, v2, resultado=None, operacion=""):
    plt.figure(figsize=(8, 8))
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    # Dibujar los vectores
    plt.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
    plt.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 2')

    if resultado is not None:
        if len(resultado) == 3:  # Si es un producto cruz, graficar en 3D
            ax = plt.figure().add_subplot(projection='3d')
            ax.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r', label='Vector 1')
            ax.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b', label='Vector 2')
            ax.quiver(0, 0, 0, resultado[0], resultado[1], resultado[2], color='g', label=f'Resultado ({operacion})')
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.legend()
            plt.show()
            return
        else:
            plt.quiver(0, 0, resultado[0], resultado[1], angles='xy', scale_units='xy', scale=1, color='g', label=f'Resultado ({operacion})')

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.title(f'Operación: {operacion}')
    plt.show()

def graficar_curva_parametrica(x_func, y_func, t_range):
    t = np.linspace(*t_range, 500)
    x = x_func(t)
    y = y_func(t)

    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='Curva paramétrica')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.title('Curva paramétrica')
    plt.show()

def graficar_curva_polar(r_func, theta_range):
    theta = np.linspace(*theta_range, 500)
    r = r_func(theta)

    plt.figure(figsize=(8, 8))
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r, label='Curva polar')
    ax.legend()
    plt.title('Curva en forma polar')
    plt.show()

def longitud_arco_parametrica(x_func, y_func, t_range):
    integrand = lambda t: np.sqrt((np.gradient(x_func(t))**2) + (np.gradient(y_func(t))**2))
    longitud, _ = quad(integrand, t_range[0], t_range[1])
    return longitud

def main():
    print("Calculadora avanzada de vectores y curvas")
    print("1. Suma y resta de vectores")
    print("2. Producto punto y cruz de vectores")
    print("3. Graficación de curvas paramétricas")
    print("4. Graficación de curvas en forma polar")
    print("fin")

    opcion = int(input("Seleccione una opción (1-5): "))

    if opcion == 1:
        v1 = np.array([float(x) for x in input("Ingrese las componentes del vector 1 (separadas por espacio): ").split()])
        v2 = np.array([float(x) for x in input("Ingrese las componentes del vector 2 (separadas por espacio): ").split()])

        print("\n1. Sumar vectores")
        print("2. Restar vectores")
        sub_opcion = int(input("Seleccione una operación: "))

        if sub_opcion == 1:
            resultado = sumar_vectores(v1, v2)
            print(f"\nResultado de la suma: {resultado}")
            graficar_vectores(v1, v2, resultado, "Suma")
        elif sub_opcion == 2:
            resultado = restar_vectores(v1, v2)
            print(f"\nResultado de la resta: {resultado}")
            graficar_vectores(v1, v2, resultado, "Resta")

    elif opcion == 2:
        v1 = np.array([float(x) for x in input("Ingrese las componentes del vector 1 (separadas por espacio): ").split()])
        v2 = np.array([float(x) for x in input("Ingrese las componentes del vector 2 (separadas por espacio): ").split()])

        print("\n1. Producto punto")
        print("2. Producto cruz")
        sub_opcion = int(input("Seleccione una operación: "))

        if sub_opcion == 1:
            resultado = producto_punto(v1, v2)
            print(f"\nResultado del producto punto: {resultado}")
        elif sub_opcion == 2:
            resultado = producto_cruz(v1, v2)
            print(f"\nResultado del producto cruz: {resultado}")
            graficar_vectores(v1, v2, resultado, "Producto cruz")

    elif opcion == 3:
        print("\nIngrese las funciones paramétricas de x(t) y y(t) en Python.")
        x_func = eval(f"lambda t: {input('x(t) = ')}")
        y_func = eval(f"lambda t: {input('y(t) = ')}")
        t_range = tuple(map(float, input("Ingrese el rango de t (inicio y fin separados por espacio): ").split()))

        graficar_curva_parametrica(x_func, y_func, t_range)

    elif opcion == 4:
        print("\nIngrese la función polar r(θ) en Python.")
        r_func = eval(f"lambda theta: {input('r(θ) = ')}")
        theta_range = tuple(map(float, input("Ingrese el rango de θ (inicio y fin separados por espacio, en radianes): ").split()))

        graficar_curva_polar(r_func, theta_range)

    elif opcion == 5:
        print("\nIngrese las funciones paramétricas de x(t) y y(t) en Python.")
        x_func = eval(f"lambda t: {input('x(t) = ')}")
        y_func = eval(f"lambda t: {input('y(t) = ')}")
        t_range = tuple(map(float, input("Ingrese el rango de t (inicio y fin separados por espacio): ").split()))

        longitud = longitud_arco_parametrica(x_func, y_func, t_range)
        print(f"\nLa longitud del arco es: {longitud}")

    else:
        print("\nOpción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
