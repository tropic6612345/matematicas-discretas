import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ConvertidorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Convertidor Numérico")
        self.root.geometry("450x320")
        self.root.resizable(False, False)

        self.crear_widgets()

    def crear_widgets(self):

        titulo = tk.Label(self.root,
                          text="CONVERTIDOR DE SISTEMAS NUMÉRICOS",
                          font=("Arial", 13, "bold"))
        titulo.pack(pady=15)

        # Menú desplegable
        self.combo = ttk.Combobox(
            self.root,
            state="readonly",
            values=[
                "Binario a Decimal",
                "Decimal a Binario",
                "Hexadecimal a Octal",
                "Octal a Hexadecimal"
            ],
            width=30
        )
        self.combo.pack(pady=10)
        self.combo.current(0)

        # Entrada
        self.entrada = tk.Entry(self.root, font=("Arial", 12), width=25)
        self.entrada.pack(pady=10)

        # Botones
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        btn_convertir = tk.Button(frame, text="Convertir",
                                  command=self.convertir, width=12)
        btn_convertir.grid(row=0, column=0, padx=5)

        btn_limpiar = tk.Button(frame, text="Limpiar",
                                command=self.limpiar, width=12)
        btn_limpiar.grid(row=0, column=1, padx=5)

        # Resultado
        self.resultado_label = tk.Label(self.root,
                                        text="Resultado:",
                                        font=("Arial", 12))
        self.resultado_label.pack(pady=20)

    def convertir(self):
        numero = self.entrada.get().strip()
        opcion = self.combo.get()

        try:
            if opcion == "Binario a Decimal":
                resultado = str(int(numero, 2))

            elif opcion == "Decimal a Binario":
                resultado = bin(int(numero))[2:]

            elif opcion == "Hexadecimal a Octal":
                decimal = int(numero, 16)
                resultado = oct(decimal)[2:]

            elif opcion == "Octal a Hexadecimal":
                decimal = int(numero, 8)
                resultado = hex(decimal)[2:].upper()

            self.resultado_label.config(text=f"Resultado: {resultado}")

        except ValueError:
            messagebox.showerror("Error", "Número inválido para la conversión seleccionada.")

    def limpiar(self):
        self.entrada.delete(0, tk.END)
        self.resultado_label.config(text="Resultado:")


# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ConvertidorApp(root)
    root.mainloop()



