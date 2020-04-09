import tkinter as tk
from tkinter import ttk
from sense_emu import SenseHat # pip3 install sense_emu
import matplotlib as plt
import time

sense = SenseHat()
temp = sense.temp
pre = sense.pressure
hum = sense.humidity

#tiempo =time.time(10)

class Aplicacion:
    def __init__(self):
        self.sense=SenseHat()
        self.ventana1=tk.Tk()
        self.ventana1.title("Practica Interfaz con SenseHat")

        self.inicio=0
        self.para=0

        self.cuaderno1 = ttk.Notebook(self.ventana1)
        
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Button")

        self.label1=tk.Label(self.pagina1, text="Control")
        self.label1.grid(column=0, row=2)
        self.boton1=tk.Button(self.pagina1, text="PARAR", command=self.parar)
        self.boton1.grid(column=1, row=2)
        self.label2=tk.Label(self.pagina1, text="Periodo:")
        self.label2.grid(column=1, row=3)

        self.label1=tk.Label(self.pagina1, text="Medidas")
        self.label1.grid(column=0, row=6)
        
        self.dato=tk.StringVar(value="0.0")        
        self.entrydatos=tk.Entry(self.pagina1, width=10, textvariable=self.dato)
        self.entrydatos.grid(column=1, row=6)

        
        self.labelframe2=ttk.LabelFrame(self.pagina1, text="Medidas")        
        self.labelframe2.grid(column=0, row=1, padx=5, pady=10)        

       
        self.seleccion=tk.IntVar()
        self.seleccion.set(0) 

        self.radio1=tk.Radiobutton(self.pagina1,text="Temperatura", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=9)
        self.radio2=tk.Radiobutton(self.pagina1,text="Presión", variable=self.seleccion, value =2)
        self.radio2.grid(column=1, row=9)
        self.radio3=tk.Radiobutton(self.pagina1,text="Humedad", variable=self.seleccion, value =3)
        self.radio3.grid(column=2, row=9)




        self.scroll1 = tk.Scrollbar(self.ventana1, orient=tk.VERTICAL)
        self.listbox1=tk.Listbox(self.ventana1, selectmode=tk.MULTIPLE, yscrollcommand=self.scroll1.set)
        self.listbox1.grid(column=0,row=18)


        '''self.labelframe3=ttk.LabelFrame(self.pagina1, text="Historico")        
        self.labelframe3.grid(column=0, row=15, padx=20, pady=30, sticky="NS")        

        self.labelnum1=tk.Label(self.labelframe3, text="Num")
        self.labelnum1.grid(column=0, row=16)


        self.labelvalor1=tk.Label(self.labelframe3, text="Valor")
        self.labelvalor1.grid(column=10, row=16)

        self.labelfecha1=tk.Label(self.labelframe3, text="Fecha/hora")
        self.labelfecha1.grid(column=20, row=16)

        self.labeltipo1=tk.Label(self.labelframe3, text="Tipo")
        self.labeltipo1.grid(column=30, row=8)'''


        self.pagina2 = ttk.Frame(self.cuaderno1)
         
        self.cuaderno1.add(self.pagina2, text="Grafica")

        self.boton1=ttk.Button(self.ventana1, text="datos:", command=self.datos)
        self.boton1.grid(column=0, row=1)
      
        self.cuaderno1.grid(column=0, row=0)        
        self.ventana1.mainloop()

        self.ventana1(time.sleep(10), self.datos)
        

    def datos(self):
            if self.seleccion.get()==1 or self.inicio==0:
                temp = self.sense.temp
                self.listbox1.insert(0,str(temp))
                self.inicio=1
            elif  self.seleccion.get()==2 or self.inicio==0:
                pre = self.sense.pressure
                self.listbox1.insert(0,str(pre))
                self.inicio=1
            
            elif  self.seleccion.get()==3 or self.inicio==0:
                hum = self.sense.humidity
                self.listbox1.insert(0,str(hum))
                self.inicio=1

    def parar (self):
        if self.inicio==1 or self.para==1:
            self.inicio=0

        
        
aplicacion1=Aplicacion()