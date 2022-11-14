import random
import numpy as np



def backtracking(tabla:np.ndarray, asignacion_actual:np.ndarray, N:int, paso=0, mejor_asignacion = None):
    if mejor_asignacion is None:
        nuevo_mejor = np.empty(N, dtype=int)
        for i in range(N):
            nuevo_mejor[i] = i
        return backtracking(tabla=tabla, asignacion_actual=asignacion_actual, N=N, paso=0, mejor_asignacion=nuevo_mejor)
    
    else:
        if paso == N:
            tiempo_actual = 0
            mejor_tiempo = 0
            for i in range(N):
                tiempo_actual += tabla[i][asignacion_actual[i]]
                mejor_tiempo += tabla[i][mejor_asignacion[i]]
            if tiempo_actual < mejor_tiempo:
                for i in range(N):
                    mejor_asignacion[i] = asignacion_actual[i]
                

        else:
            for i in range(N):
                if i not in asignacion_actual:
                    asignacion_actual[paso] = i
                    backtracking(tabla=tabla, asignacion_actual=asignacion_actual, N=N, paso=paso+1, mejor_asignacion=mejor_asignacion)
                    asignacion_actual[paso] = -1
            return mejor_asignacion
                



if __name__ == "__main__":
    N = 4
    random.seed(23)
    tabla_trabajadores_tareas = np.empty((N, N), dtype=int)
    for i in range(N):
        for j in range(N):
            tabla_trabajadores_tareas[i][j] = random.randrange(1, 21)

    print("Tabla de trabajadores y tareas")
    
    cadena = "{0:<13}".format("Trabajador")

    for i in range(N):
        cadena += "{0:<10}".format("Tarea {0}".format(i+1))

    
    for i in range(N):
        cadena += "\n{0:<13}".format(i+1)
        for j in range(N):
            cadena += "{0:<10}".format(tabla_trabajadores_tareas[i][j])
    
    print(cadena)

    asignacion_actual = np.empty(N, dtype=int)
    asignacion_actual.fill(-1)
    print("\n")
    mejor_asignacion = backtracking(tabla=tabla_trabajadores_tareas, asignacion_actual=asignacion_actual, N=N)



    print("La mejor asignacion posible es: ")
    for i in range(N):
        print("Trabajador {0} con tarea {1}".format(i+1, mejor_asignacion[i]+1))
    
    tiempo = 0
    for i in range(N):
        tiempo += tabla_trabajadores_tareas[i][mejor_asignacion[i]]
    print("El tiempo para esta asignacion es {0}".format(tiempo))