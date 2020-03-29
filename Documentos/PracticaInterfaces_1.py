import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba del control Notebook")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Button")

        self.label1=tk.Label(self.pagina1, text="Control")
        self.label1.grid(column=0, row=2)
        self.boton1=tk.Button(self.pagina1, text="PARAR")
        self.boton1.grid(column=1, row=2)
        self.label2=tk.Label(self.pagina1, text="Periodo:")
        self.label2.grid(column=1, row=3)

        self.label1=tk.Label(self.pagina1, text="Medidas")
        self.label1.grid(column=0, row=6)
        
        self.dato=tk.StringVar(value="0.0")        
        self.entryCantidad=tk.Entry(self.pagina1, width=10, textvariable=self.dato)
        self.entryCantidad.grid(column=1, row=7)

        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
       
        self.labelframe2=ttk.LabelFrame(self.pagina1, text="Medidas")        
        self.labelframe2.grid(column=0, row=1, padx=5, pady=10)        


        self.radio1=tk.Radiobutton(self.pagina1,text="Temperatura", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=9)
        self.radio2=tk.Radiobutton(self.pagina1,text="Preción", variable=self.seleccion, value=2)
        self.radio2.grid(column=1, row=9)
        self.radio3=tk.Radiobutton(self.pagina1,text="Humedad", variable=self.seleccion, value=3)
        self.radio3.grid(column=2, row=9)

        self.labelframe3=ttk.LabelFrame(self.pagina1, text="Historico")        
        self.labelframe3.grid(column=0, row=15, padx=20, pady=30, sticky="WE")        

        self.labelnum1=tk.Label(self.labelframe3, text="Num")
        self.labelnum1.grid(column=0, row=16)

        self.labelvalor1=tk.Label(self.labelframe3, text="Valor")
        self.labelvalor1.grid(column=10, row=16)

        self.labelfecha1=tk.Label(self.labelframe3, text="Fecha/hora")
        self.labelfecha1.grid(column=20, row=16)

        self.labeltipo1=tk.Label(self.labelframe3, text="Tipo")
        self.labeltipo1.grid(column=30, row=8)


        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Grafica")
        self.label2=ttk.Label(self.pagina2, text="La clase Label ")
        self.label2.grid(column=0, row=0)
        self.label3=ttk.Label(self.pagina2, text="con los caracteres \\n podemos hacer un salto de línea dentro de la Label")
        self.label3.grid(column=0, row=1)

        self.cuaderno1.grid(column=0, row=0)        

        self.ventana1.mainloop()


aplicacion1=Aplicacion()