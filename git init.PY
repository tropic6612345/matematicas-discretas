import tkinter as tk
from tkinter import messagebox

# ----- Funciones matemáticas -----

def es_reflexiva(A, R):
    for a in A:
        if (a, a) not in R:
            return False
    return True

def es_simetrica(R):
    for (a, b) in R:
        if (b, a) not in R:
            return False
    return True

def es_transitiva(R):
    for (a, b) in R:
        for (c, d) in R:
            if b == c and (a, d) not in R:
                return False
    return True


# ----- Función principal -----

def verificar_relacion():
    try:
        # Conjunto
        A = entrada_conjunto.get().split()

        # Relaciones
        texto_relaciones = caja_relaciones.get("1.0", tk.END).strip()
        lineas = texto_relaciones.split("\n")

        R = set()

        for linea in lineas:
            a, b = linea.split()
            R.add((a, b))

        reflexiva = es_reflexiva(A, R)
        simetrica = es_simetrica(R)
        transitiva = es_transitiva(R)

        resultado = f"""
Resultados:

Reflexiva: {reflexiva}
Simétrica: {simetrica}
Transitiva: {transitiva}
"""

        if reflexiva and simetrica and transitiva:
            resultado += "\n✅ ES una relación de equivalencia"
        else:
            resultado += "\n❌ NO es una relación de equivalencia"

        etiqueta_resultado.config(text=resultado)

    except:
        messagebox.showerror("Error", "Revisa que los datos estén bien escritos.")


# ----- Ventana -----

ventana = tk.Tk()
ventana.title("Verificador de Relaciones de Equivalencia")
ventana.geometry("500x500")

titulo = tk.Label(
    ventana,
    text="Relaciones de Equivalencia",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

explicacion = tk.Label(
    ventana,
    text=(
        "Instrucciones:\n"
        "1. Escribe los elementos del conjunto separados por espacios.\n"
        "   Ejemplo: 1 2 3\n\n"
        "2. Escribe las relaciones (pares ordenados) una por línea.\n"
        "   Ejemplo:\n"
        "   1 1\n"
        "   2 2\n"
        "   3 3\n"
        "   1 2\n"
        "   2 1"
    ),
    justify="left"
)
explicacion.pack(pady=10)

# Conjunto
tk.Label(ventana, text="Conjunto:").pack()
entrada_conjunto = tk.Entry(ventana, width=40)
entrada_conjunto.pack(pady=5)

# Relaciones
tk.Label(ventana, text="Relaciones:").pack()
caja_relaciones = tk.Text(ventana, height=10, width=40)
caja_relaciones.pack(pady=5)

# Botón
boton = tk.Button(
    ventana,
    text="Verificar relación",
    command=verificar_relacion
)
boton.pack(pady=10)

# Resultado
etiqueta_resultado = tk.Label(ventana, text="", fg="blue")
etiqueta_resultado.pack(pady=10)

ventana.mainloop()