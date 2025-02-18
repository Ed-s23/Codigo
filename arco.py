import numpy as np
from scipy.integrate import quad

def calcular_longitud_arco():
    print("Programa para calcular la longitud de arco de una curva paramétrica.")

    # Solicitar las ecuaciones paramétricas
    print("Introduce las funciones paramétricas en términos de t.")
    x_func = input("x(t) = ")
    y_func = input("y(t) = ")

    # Solicitar el rango de t
    t_min = float(input("Valor mínimo de t: "))
    t_max = float(input("Valor máximo de t: "))

    # Definir las funciones paramétricas
    try:
        x_t = lambda t: eval(x_func, {"np": np, "t": t})
        y_t = lambda t: eval(y_func, {"np": np, "t": t})
    except Exception as e:
        print(f"Error al evaluar las funciones: {e}")
        return

    # Función integrando para calcular la longitud de arco
    def integrando(t):
        dx_dt = (eval(x_func, {"np": np, "t": t + 1e-5}) - eval(x_func, {"np": np, "t": t - 1e-5})) / (2e-5)
        dy_dt = (eval(y_func, {"np": np, "t": t + 1e-5}) - eval(y_func, {"np": np, "t": t - 1e-5})) / (2e-5)
        return np.sqrt(dx_dt**2 + dy_dt**2)

    # Calcular la longitud de arco mediante integración numérica
    try:
        L, _ = quad(integrando, t_min, t_max)
        print(f"La longitud de arco de la curva entre t = {t_min} y t = {t_max} es: {L:.4f}")
    except Exception as e:
        print(f"Error al calcular la longitud de arco: {e}")

# Llamar a la función principal
calcular_longitud_arco()
