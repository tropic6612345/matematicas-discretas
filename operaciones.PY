import tkinter as tk
from tkinter import messagebox


# ==============================
# COLORES FUTURISTAS
# ==============================
BG_COLOR = "#0f0f1a"        # Fondo oscuro espacial
BTN_COLOR = "#1f1f3a"
NEON_BLUE = "#00f5ff"
NEON_PURPLE = "#9d00ff"
TEXT_COLOR = "#ffffff"


class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Numérico 2077")
        self.root.geometry("550x450")
        self.root.config(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.menu_principal()

    # ==============================
    # MENU PRINCIPAL
    # ==============================
    def menu_principal(self):
        self.limpiar_ventana()

        titulo = tk.Label(self.root,
                          text="SISTEMA NUMÉRICO 2077",
                          font=("Consolas", 20, "bold"),
                          fg=NEON_BLUE,
                          bg=BG_COLOR)
        titulo.pack(pady=30)

        self.crear_boton("BINARIO (Base 2)", lambda: self.menu_operaciones(2))
        self.crear_boton("OCTAL (Base 8)", lambda: self.menu_operaciones(8))
        self.crear_boton("HEXADECIMAL (Base 16)", lambda: self.menu_operaciones(16))
        self.crear_boton("SALIR", self.root.quit)

    # ==============================
    # MENU OPERACIONES
    # ==============================
    def menu_operaciones(self, base):
        self.base = base
        self.limpiar_ventana()

        titulo = tk.Label(self.root,
                          text=f"OPERACIONES BASE {base}",
                          font=("Consolas", 18, "bold"),
                          fg=NEON_PURPLE,
                          bg=BG_COLOR)
        titulo.pack(pady=20)

        self.entrada1 = self.crear_entry()
        self.entrada2 = self.crear_entry()

        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(pady=20)

        self.crear_boton_frame(frame, "SUMAR", "+", 0)
        self.crear_boton_frame(frame, "RESTAR", "-", 1)
        self.crear_boton_frame(frame, "MULTIPLICAR", "*", 2)

        self.resultado = tk.Label(self.root,
                                  text="RESULTADO:",
                                  font=("Consolas", 16),
                                  fg=NEON_BLUE,
                                  bg=BG_COLOR)
        self.resultado.pack(pady=25)

        self.crear_boton("VOLVER AL MENÚ", self.menu_principal)

    # ==============================
    # CREAR BOTÓN PRINCIPAL
    # ==============================
    def crear_boton(self, texto, comando):
        boton = tk.Button(self.root,
                          text=texto,
                          font=("Consolas", 12, "bold"),
                          fg=NEON_BLUE,
                          bg=BTN_COLOR,
                          activebackground=NEON_PURPLE,
                          activeforeground=TEXT_COLOR,
                          width=25,
                          height=2,
                          bd=0,
                          command=comando)
        boton.pack(pady=10)

    # ==============================
    # CREAR BOTÓN EN FRAME
    # ==============================
    def crear_boton_frame(self, frame, texto, operacion, columna):
        boton = tk.Button(frame,
                          text=texto,
                          font=("Consolas", 11, "bold"),
                          fg=NEON_BLUE,
                          bg=BTN_COLOR,
                          activebackground=NEON_PURPLE,
                          activeforeground=TEXT_COLOR,
                          width=14,
                          height=2,
                          bd=0,
                          command=lambda: self.calcular(operacion))
        boton.grid(row=0, column=columna, padx=10)

    # ==============================
    # ENTRY FUTURISTA
    # ==============================
    def crear_entry(self):
        entry = tk.Entry(self.root,
                         font=("Consolas", 14),
                         fg=NEON_BLUE,
                         bg="#1a1a2e",
                         insertbackground=NEON_BLUE,
                         width=20,
                         justify="center",
                         bd=0)
        entry.pack(pady=8)
        return entry

    # ==============================
    # CALCULAR
    # ==============================
    def calcular(self, operacion):
        try:
            num1 = int(self.entrada1.get(), self.base)
            num2 = int(self.entrada2.get(), self.base)

            if operacion == "+":
                res = num1 + num2
            elif operacion == "-":
                res = num1 - num2
            elif operacion == "*":
                res = num1 * num2

            if self.base == 2:
                resultado = bin(res)[2:]
            elif self.base == 8:
                resultado = oct(res)[2:]
            elif self.base == 16:
                resultado = hex(res)[2:].upper()

            self.resultado.config(text=f"RESULTADO: {resultado}")

        except ValueError:
            messagebox.showerror("ERROR", "Número inválido para esta base.")

    # ==============================
    # LIMPIAR
    # ==============================
    def limpiar_ventana(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ==============================
# EJECUTAR
# ==============================
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
