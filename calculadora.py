import numpy as np
import matplotlib.pyplot as plt

def suma_vectores(v1, v2):
    return v1 + v2

def resta_vectores(v1, v2):
    return v1 - v2

def producto_punto(v1, v2):
    return np.dot(v1, v2)

def producto_cruz(v1, v2):
    return np.cross(v1, v2)

def norma_vector(v):
    return np.linalg.norm(v)

def multiplicar_escalar(v, escalar):
    return v * escalar

def graficar_vectores(vectores, colores, titulo):
    origen = [0, 0, 0]  # Origen para todos los vectores

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for i, v in enumerate(vectores):
        ax.quiver(*origen, *v, color=colores[i], arrow_length_ratio=0.1)

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(titulo)
    plt.show()

def producto_vectorial(v1, v2):
    resultado = producto_cruz(v1, v2)
    print(f"Resultado del producto vectorial: {resultado}")
    graficar_vectores([v1, v2, resultado], ['r', 'g', 'b'], "Producto Vectorial")

def ecuacion_plano(p1, p2, p3):
    v1 = p2 - p1
    v2 = p3 - p1
    normal = np.cross(v1, v2)
    d = -np.dot(normal, p1)
    ecuacion = f"{normal[0]}x + {normal[1]}y + {normal[2]}z + {d} = 0"
    print(f"Ecuación del plano: {ecuacion}")
    
    # Graficar el plano
    graficar_plano(p1, p2, p3, normal)

    return normal, d, ecuacion

def graficar_plano(p1, p2, p3, normal):
    # Graficar los puntos
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter([p1[0], p2[0], p3[0]], [p1[1], p2[1], p3[1]], [p1[2], p2[2], p3[2]], color="r", s=100)

    # Graficar el plano
    xx, yy = np.meshgrid(np.linspace(-10, 10, 10), np.linspace(-10, 10, 10))

    # Verificar si normal[2] es diferente de cero para evitar división por cero
    if normal[2] != 0:
        zz = (-normal[0] * xx - normal[1] * yy - np.dot(normal, p1)) / normal[2]
    else:
        # Si normal[2] es cero, calculamos el plano de otra manera
        zz = np.zeros_like(xx)  # Plano paralelo al eje XY

    ax.plot_surface(xx, yy, zz, color='b', alpha=0.5)

    # Ajustes
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

def ecuacion_linea(p1, p2):
    # Vector director de la línea
    d = p2 - p1
    print(f"Vector director de la línea: {d}")

    # Ecuación paramétrica de la línea: r(t) = p0 + t * d
    print(f"Ecuación de la línea recta en forma paramétrica: r(t) = ({p1[0]}, {p1[1]}, {p1[2]}) + t * ({d[0]}, {d[1]}, {d[2]})")

    # Graficar la línea
    t = np.linspace(-10, 10, 100)
    linea = p1[:, np.newaxis] + t * d[:, np.newaxis]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(linea[0, :], linea[1, :], linea[2, :], label="Línea recta", color='g')
    ax.scatter(*p1, color="r", s=100, label="Punto 1")
    ax.scatter(*p2, color="b", s=100, label="Punto 2")

    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title("Ecuación de la Línea Recta")
    ax.legend()
    plt.show()

def menu():
    print("\nOperaciones con Vectores")
    print("1. Suma de vectores")
    print("2. Resta de vectores")
    print("3. Producto punto")
    
    print("4. Producto cruz")
    print("5. Norma de un vector")
    print("6. Producto vectorial")
    print("7. Ecuación de un plano")
    print("8. Multiplicación por un escalar")
    print("9. Ecuación de una línea recta")
    print("10. Salir")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "10":
            print("Saliendo del programa...")
            break

        elif opcion in ["1", "2", "3", "4", "6"]:
            v1 = np.array([float(x) for x in input("Introduce el primer vector (separado por espacios): ").split()])
            v2 = np.array([float(x) for x in input("Introduce el segundo vector (separado por espacios): ").split()])

            if opcion == "1":
                resultado = suma_vectores(v1, v2)
                print(f"Resultado de la suma: {resultado}")
                graficar_vectores([v1, v2, resultado], ['r', 'g', 'b'], "Suma de Vectores")

            elif opcion == "2":
                resultado = resta_vectores(v1, v2)
                print(f"Resultado de la resta: {resultado}")
                graficar_vectores([v1, v2, resultado], ['r', 'g', 'b'], "Resta de Vectores")

            elif opcion == "3":
                resultado = producto_punto(v1, v2)
                print(f"Resultado del producto punto: {resultado}")

            elif opcion == "4":
                resultado = producto_cruz(v1, v2)
                print(f"Resultado del producto cruz: {resultado}")
                graficar_vectores([v1, v2, resultado], ['r', 'g', 'b'], "Producto Cruz")

            elif opcion == "6":
                producto_vectorial(v1, v2)

        elif opcion == "5":
            v = np.array([float(x) for x in input("Introduce el vector (separado por espacios): ").split()])
            resultado = norma_vector(v)
            print(f"Norma del vector: {resultado}")
            graficar_vectores([v], ['r'], "Norma del Vector")

        elif opcion == "7":
            p1 = np.array([float(x) for x in input("Introduce el primer punto del plano (separado por espacios): ").split()])
            p2 = np.array([float(x) for x in input("Introduce el segundo punto del plano (separado por espacios): ").split()])
            p3 = np.array([float(x) for x in input("Introduce el tercer punto del plano (separado por espacios): ").split()])
            normal, d, ecuacion = ecuacion_plano(p1, p2, p3)

        elif opcion == "8":
            v = np.array([float(x) for x in input("Introduce el vector (separado por espacios): ").split()])
            escalar = float(input("Introduce el valor escalar: "))
            resultado = multiplicar_escalar(v, escalar)
            print(f"Resultado de la multiplicación por el escalar {escalar}: {resultado}")
            graficar_vectores([v, resultado], ['r', 'g'], f"Multiplicación por escalar {escalar}")

        elif opcion == "9":
            p1 = np.array([float(x) for x in input("Introduce el primer punto de la línea (separado por espacios): ").split()])
            p2 = np.array([float(x) for x in input("Introduce el segundo punto de la línea (separado por espacios): ").split()])
            ecuacion_linea(p1, p2)

        else:
            print("Opción no válida. Intenta de nuevo.")
