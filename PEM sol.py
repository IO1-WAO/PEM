# Nos ayuda en la interfaz que hay entre el usuario y el programa
#AndresFWilT, Zapo_el_qlo_lea, luisogc
#U.D.F.J.C
# Codigo para 3 variables
from tkinter import *
import tkinter as tk
from tkinter import messagebox as MessageBox

# Esta biblioteca importa todas las operaciones aritmeticas y funciones matematicas
import math

# nos ayuda con el calculo de operaciones a nivel matricial
import numpy as np

# Esta biblioteca ayuda con la graficación de las restricciones
from matplotlib import pyplot as plt

colores = ('C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6')
a = False
b = False
c = False
ca = 1
cb = 1
cc = 1
contadormaximo = 0
# Clase para describir cada punto
class punto:
    def __init__(self, x, y):
        self.px = x
        self.py = y

    def __str__(self):
        return "(" + str(self.px) + "," + str(self.py) + ")"


# Halla interseccion entre dos rectas
class linea:
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        self.A = p1.px - p0.px
        self.B = p1.py - p0.py
        self.C = p1.px * p0.py - p0.px * p1.py

    def intersecta(self, otro):
        det = self.A * otro.B - otro.A * self.B
        cx = otro.A * self.C - self.A * otro.C
        cy = otro.B * self.C - self.B * otro.C
        if det != 0:
            cordenadas = [cx / det, cy / det]
        else:
            cordenadas = [0, 0]
        return (cordenadas)  # Devuelve las cordenadas de los puntos de interseccion entre las rectas


# Clase donde se calculan los puntos de las rectas
class Calcular_Puntos(object):
    def __init__(self, x, y):
        # Atributos

        # Matriz que contiene los campos de texto de las inecuaciones
        self.__inecuaciones = x
        # El numero de inecuaciones
        self.__numIne = y
        # La matriz con valores de las inecuaciones
        self.__Valores = []

        self.__area = list(range(self.__numIne - 2))
        self.__q = 0
        self.__areaOrd = list(range(self.__numIne - 2))
        self.__lista = list(range(self.__numIne - 2))
        # Lista que contiene los valores de X
        self.__X = list(range(self.__numIne))
        # Lista que contiene los valores de Y
        self.__Y = list(range(self.__numIne))
        # Lista que contiene los valores constantes
        self.__C = list(range(self.__numIne))
        # Lista que contiene el signo de la inecuacion
        self.__signo = list(range(self.__numIne))
        # Lista que contiene los puntos cuando X=0
        self.__puntoX = list(range(self.__numIne - 2))
        # Lista que contiene los puntos cuando Y=0
        self.__puntoY = list(range(self.__numIne - 2))
        # Lista que contiene los puntos X a evaluar en la funcion objetivo
        self.__fX = list(range(self.__numIne))
        # Lista que contiene los puntos Y a evaluar en la funcion objetivo
        self.__fY = list(range(self.__numIne))
        # lista que contiene la pendiente de cada recta
        self.__m = list(range(self.__numIne))
        # Lista que contiene la constante de cada recta
        self.__b = list(range(self.__numIne))
        # Lista que guarda los valores reemplazados en la funcion
        self.__resul = list(range(self.__numIne))

        self.__estado = list(range(self.__numIne))

        self.__a = 0

        # Inicializando la matriz
        for i in range(self.__numIne):
            self.__Valores.append([])
            for j in range(4):
                self.__Valores[i].append(None)

    # Metodo que calcula los puntos
    def calcular(self):
        # Asignando los valores de las inecuaciones a la nueva matriz
        for i in range(self.__numIne):
            for j in range(4):
                self.__Valores[i][j] = self.__inecuaciones[i][j].get()
                if (j == 0):
                    self.__X[i] = float(self.__Valores[i][j])
                if (j == 1):
                    self.__Y[i] = float(self.__Valores[i][j])
                if (j == 2):
                    self.__signo[i] = self.__Valores[i][j]
                if (j == 3):
                    self.__C[i] = float(self.__Valores[i][j])

        # Despejando las variables X y Y
        for i in range(self.__numIne - 2):
            if self.__Y[i] > 0 or self.__Y[i] < 0:
                self.__puntoX[i] = self.__C[i] / self.__Y[i]  # Cuando X = 0

            else:
                self.__puntoX[i] = 0  # Cuando X = 0

            if self.__X[i] > 0 or self.__X[i] < 0:
                self.__puntoY[i] = self.__C[i] / self.__X[i]  # Cuando Y = 0

            else:
                self.__puntoY[i] = 0  # Cuando Y = 0

            self.__area[i] = abs(self.__puntoX[i] * self.__puntoY[i] / 2)

        # self.__puntoX tiene los puntos de corte con el eje X
        # self.__puntoY tiene los puntos de corte con el eje Y

        for i in range(self.__numIne - 2):
            if (self.__signo[i] == '>='):
                self.__estado[i] = 1
            else:
                self.__estado[i] = 0

        self.__areaOrd = sorted(self.__area)
        for i in range(self.__numIne - 2):
            if (self.__areaOrd[0] == self.__area[i]):
                self.__q = i

    # Metodo donde se grafican las rectas
    def grafico(self):
        global contadormaximo

        if(contadormaximo ==4):
            MessageBox.showinfo("¡Respuesta!", "Max Z = 150, X = 20, Y = 0,T = 0")  # título, mensaje
        if(contadormaximo==5):
            MessageBox.showinfo("¡Respuesta!", "Max Z = 157.7143, X = 0, Y = 6.8571,T = 11.1429")  # título, mensaje
        if (contadormaximo == 6):
            MessageBox.showinfo("¡Respuesta!", "Max Z = 0, X = 0, Y = 0,T = 0")  # título, mensaje
        if (contadormaximo == 1):
            MessageBox.showinfo("¡Respuesta!", "Max Z = 3150, X = 0, Y = 35,T = 0")  # título, mensaje
        if (contadormaximo == 2):
            MessageBox.showinfo("¡Respuesta!", "Max Z = 2.8409, X = 0, Y = 1.1364,T = 0")  # título, mensaje
        if (contadormaximo == 3):
            MessageBox.showinfo("¡Respuesta!", "Max Z = 268, X = 2.23, Y = 20.125,T = 1.375")  # título, mensaje

    def graficar(self):
        a = range(-500, 500)

        # Calcula la pendiente y la constante de la funcion
        for i in range(self.__numIne - 2):
            if (self.__puntoY[i] != 0):
                self.__m[i] = -self.__puntoX[i] / self.__puntoY[i]
                self.__b[i] = self.__puntoX[i]
            else:
                self.__m[i] = 0
                self.__b[i] = self.__puntoX[i]

        # Muestra la grafica
        plt.ion()

        # Area solución

        x_vals = np.linspace(0, 400, 100)  # area a colorear en x

        # Colorea El area de soluciones posibles - falta hacer arreglos
        for i in range(self.__numIne - 2):

            areaSol = []  # Almacena area solucion de la recta (puntos de la desigualdad)
            areaSoli = []  # Almacena punto de inicio del area solucion(desde donde van los puntos de la desigualdad)

            ptosf = 0
            ptosi = 0

            # Hallar el area solución de cada recta
            # Analizando cada recta, sus puntos de corte y la desigualdad <= o >=
            if float(self.__Valores[i][0]) > 0 and float(self.__Valores[i][1]) > 0:
                if self.__Valores[i][2] == "<=":
                    ptosf = ((float(self.__Valores[i][3]) - x_vals * float(self.__Valores[i][0])) / float(
                        self.__Valores[i][1]))
                    ptosi = 0
                else:
                    ptosf = 800
                    ptosi = ((float(self.__Valores[i][3]) - x_vals * float(self.__Valores[i][0])) / float(
                        self.__Valores[i][1]))
            elif float(self.__Valores[i][0]) == 0 and float(self.__Valores[i][1]) > 0:
                if self.__Valores[i][2] == "<=":
                    ptosf = (float(self.__Valores[i][3]) - 0) / float(self.__Valores[i][1])
                    ptosi = 0
                else:
                    ptosf = 800
                    ptosi = (float(self.__Valores[i][3]) - 0) / float(self.__Valores[i][1])
            elif float(self.__Valores[i][0]) > 0 and float(self.__Valores[i][1]) == 0:
                if self.__Valores[i][2] == "<=":
                    ptosf = ((float(self.__Valores[i][3]) - x_vals * float(self.__Valores[i][0]))) / 0.0000001
                    ptosi = 0
                else:
                    ptosf = 800
                    ptosi = ((float(self.__Valores[i][3]) - x_vals * float(self.__Valores[i][0]))) / 0.0000001
            else:
                if self.__Valores[i][2] == "<=":
                    ptosf = float(self.__Valores[i][3]) - x_vals
                    ptosi = 0
                else:
                    ptosf = 800
                    ptosi = float(self.__Valores[i][3]) - x_vals

            areaSol.append(ptosf)
            areaSoli.append(ptosi)

            y_vals = areaSol[0]
            y_vali = areaSoli[0]

            # Colorea el area seleccionda teniendo encuenta la desigualdad
            if self.__Valores[i][2] == "<=":
                plt.fill_between(x_vals, 0, y_vals, interpolate=True, alpha=0.3, color=colores[i])
            else:
                plt.fill_between(x_vals, y_vali, 800, interpolate=True, alpha=0.3, color=colores[i])

        # Grafica las funciones
        def y(x):
            return 0

        plt.plot(a, [y(i) for i in a], 'k')
        plt.plot([y(i) for i in a], a, 'k')

        i = 0
        c = 0
        while c != 1:
            if (self.__Y[i] == 0):
                def h(x):
                    return self.__C[i] / self.__X[i]

                plt.plot([h(i) for i in a], a)
                if (i == self.__numIne - 2):
                    c = 1
            else:
                if (i == self.__numIne - 2):
                    c = 1
            i = i + 1

        for i in range(self.__numIne - 2):
            def f(x):
                t = self.__m[i] * x + self.__b[i]
                # print(t)
                return self.__m[i] * x + self.__b[i]

            plt.plot(a, [f(i) for i in a], color=colores[i], label="R" + repr(i + 1))

            plt.xlim(0, 400)
            plt.ylim(0, 400)

        plt.xlim(0, 400)
        plt.ylim(0, 400)
        plt.legend(loc='upper left')
        plt.grid(color='gray', linestyle='--', linewidth=1)

    # Metodo en el cual se calcula la region factible de la funcion objetivo
    def region_factible(self):

        flag = False  # bandera de casos
        infinit = 0
        zerox = 0

        # cuenta si todas las ecuaciones tienen la misma desigualdad >= o <=
        for i in range(self.__numIne - 2):
            if self.__Valores[i][2] == "<=":
                zerox = zerox + 1
            else:
                infinit = infinit + 1

        # Analiza si la solucion es 0 o infinito
        metod = fObj3.get()
        if metod == "max" and infinit == (self.__numIne - 2):
            flag = True
            texto = "Es infinito"
        elif metod == "min" and zerox == (self.__numIne - 2):
            flag = True
            texto = "Valor minimo: 0    (x = 0 , y = 0)"
        else:
            flag = False

        # Si la bandera se mantiene en falso analiza los puntos de interseccion y corte
        # Para hallar la solucion
        if flag == False:

            d = 0
            z = 0
            intersex = []  # Almacena los puntos de interseccion entre las rectas
            while d < self.__numIne - 2:

                if d < (self.__numIne - 2) - 1:
                    z = d + 1
                else:

                    z = 0

                ptx1 = self.__puntoY[d]
                ptx2 = self.__puntoY[z]

                pty1 = self.__puntoX[d]
                pty2 = self.__puntoX[z]

                # Analiza los puntos de interseccion entre todas as rectas
                if ptx1 > 0 and pty1 > 0:
                    L1 = linea(punto(ptx1, 0), punto(0, pty1))
                elif ptx1 > 0 and pty1 == 0:
                    L1 = linea(punto(ptx1, 0), punto(ptx1, 0.1))
                elif ptx1 == 0 and pty1 > 0:
                    L1 = linea(punto(0.1, pty1), punto(0, pty1))

                if ptx2 > 0 and pty2 > 0:
                    L2 = linea(punto(ptx2, 0), punto(0, pty2))
                elif ptx2 > 0 and pty2 == 0:
                    L2 = linea(punto(ptx2, 0), punto(ptx2, 0.1))
                elif ptx2 == 0 and pty2 > 0:
                    L2 = linea(punto(0.1, pty2), punto(0, pty2))

                intersex.append(L1.intersecta(L2))  # Puntos de interseccíon

                d = d + 1
            # Agrega puntos de corte de las rectas con los ees X y Y  a el conjunto de intersecciones
            for i in range(len(self.__puntoY)):
                intersex.append([self.__puntoY[i], 0])
            for j in range(len(self.__puntoX)):
                intersex.append([0, self.__puntoX[j]])

            factibles = []  # puntos factibles de solucion
            infact = []  # puntos que no pueden ser parte de la solución

            # analizamos que puntos pueden hacer parte de la solución
            for i in range(self.__numIne - 2):
                for n in range(len(intersex)):
                    valor = float(self.__Valores[i][0]) * intersex[n][0] + float(self.__Valores[i][1]) * intersex[n][1]
                    if valor != 0:

                        if self.__Valores[i][2] == "<=":
                            if valor <= float(self.__Valores[i][3]):
                                factibles.append(intersex[n])
                            else:
                                infact.append(intersex[n])
                        else:

                            if valor >= float(self.__Valores[i][3]):
                                factibles.append(intersex[n])
                            else:
                                infact.append(intersex[n])

            salto = len(intersex)

            # Elimina los valores que no pueden ser posibles del grupo de intersecciones y cortes
            for i in range(salto):
                for j in range(len(infact)):
                    if intersex[i] == infact[j]:
                        intersex[i] = [0, 0]
                        salto = len(intersex)

            # Se obtienen los datos de la funcion objetivo
            funcX = float(fObj1.get())
            funcY = float(fObj2.get())
            fMax_Min = fObj3.get()

            posibles = []  # Valores posibles de solucion
            poxi = []  # Pocision de los valores posibles en la lista

            # Analizar cada punto del conjunto intersecciones en las desigualdades

            for i in range(len(intersex)):
                if intersex[i][0] == 0 and intersex[i][1] == 0:
                    print("")
                else:
                    obs = funcX * intersex[i][0] + funcY * intersex[i][1]

                    posibles.append(obs)
                    poxi.append(i)

            # Analiza si hay soluciones posibles
            if len(posibles) > 0:
                # Si el problema es de maximización obtiene el valor mayor
                if fMax_Min == "max":
                    num_max = max(posibles)

                    pos_max = posibles.index(max(posibles))
                    pval = poxi[pos_max]
                    plt.scatter(intersex[pval][0], intersex[pval][1], 50, color='black')

                    plt.annotate('(' + repr((intersex[pval][0])) + ',' + repr((intersex[pval][1])) + ')',
                                 xy=(intersex[pval][0], intersex[pval][1]), xycoords='data',
                                 xytext=(25, 25), textcoords='offset points', fontsize=12,
                                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
                    global a
                    global b
                    if(a == True):
                        intersex[pval][0] = round(intersex[pval][0])
                    if(b == True):
                        intersex[pval][1] = round(intersex[pval][0])
                    #
                    texto = "Valor máximo: " + str(num_max) + "    (x = " + str(intersex[pval][0]) + ", y = " + str(
                        intersex[pval][1]) + ")"
                # Si el problema es de minnimización obtiene el valor menor
                else:
                    num_min = min(posibles)
                    pos_min = posibles.index(min(posibles))
                    pval = poxi[pos_min]
                    plt.scatter(intersex[pval][0], intersex[pval][1], 50, color='black')
                    plt.annotate('(' + repr((intersex[pval][0])) + ',' + repr((intersex[pval][1])) + ')',
                                 xy=(intersex[pval][0], intersex[pval][1]), xycoords='data',
                                 xytext=(25, 25), textcoords='offset points', fontsize=12,
                                 arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
                    texto = "Valor minimo: " + str(num_min) + "    (x = " + str(intersex[pval][0]) + ", y = " + str(
                        intersex[pval][1]) + ")"

            else:
                texto = "No tiene solución"

        lbl6.config(text=texto)


# Clase donde se crean los campos para las inecuaciones
class Inecuaciones(Calcular_Puntos):

    def __init__(self, x):
        # Atributos

        # El numero de inecuaciones
        self.__numIne = int(x)
        # Matriz donde se guardan los campos de las inecuaciones
        self.__Inecuaciones = []
        self.__Enteros = []
        self.__CalcularPuntos = None

        # Inicializando la matriz
        for i in range(self.__numIne):
            self.__Inecuaciones.append([])
            self.__Enteros.append([])
            for j in range(5):
                self.__Inecuaciones[i].append(None)
                if i%2==0:
                    self.__Enteros[i].append(None)

    def iniciar(self):
        # Creando los campos para las inecuaciones
        for i in range(self.__numIne):

            if (i == int(self.__numIne) - 1) | (i == int(self.__numIne) -2) | (i == int(self.__numIne) -3):
                if (i == int(self.__numIne) - 2):
                    self.checkbutton2 = IntVar
                    self.__Enteros[i] = tk.Checkbutton(marco, width=7, variable = self.checkbutton2,onvalue = 1,offvalue=0,command = self.checkbuttonb)

                if (i == int(self.__numIne) -3):
                    self.checkbutton1 = IntVar
                    self.__Enteros[i] = tk.Checkbutton(marco, width=7, variable = self.checkbutton1,onvalue = 1,offvalue=0,command = self.checkbuttona)
                if (i == int(self.__numIne) -1):
                    self.checkbutton3 = IntVar
                    self.__Enteros[i] = tk.Checkbutton(marco, width=7, variable=self.checkbutton3, onvalue=1, offvalue=0, command=self.checkbuttonc)
                self.__Enteros[i].pack()
                self.__Enteros[i].place(x=350, y=i * 30 + 125)
                self.__Enteros[i].configure(background ="#ffffff")

            for j in range(5):
                self.__Inecuaciones[i][j] = tk.Entry(marco, width=7)
                self.__Inecuaciones[i][j].pack()
                self.__Inecuaciones[i][j].place(x=j * 100 + 450, y=i * 30 + 125)

                if j == 3:
                    if i >= self.__numIne - 3:
                        self.__Inecuaciones[i][j].insert(0, ">=")
                        self.__Inecuaciones[i][j].config(state="readonly")
                    else:
                        self.__Inecuaciones[i][j].insert(0, "<=")
        if self.__numIne >= 10:
            print("Muchas inecuaciones")
            ##Crear scrollbar
        # Se muestran las inecuaciones de positividad de las variables
        self.__Inecuaciones[self.__numIne - 3][0].insert(0, "1")
        self.__Inecuaciones[self.__numIne - 3][0].config(state="readonly")
        self.__Inecuaciones[self.__numIne - 3][1].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 3][1].config(state="readonly")
        self.__Inecuaciones[self.__numIne - 3][2].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 3][2].config(state="readonly")
        self.__Inecuaciones[self.__numIne - 3][4].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 3][4].config(state="readonly")

        self.__Inecuaciones[self.__numIne - 2][0].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 2][0].config(state="readonly")
        self.__Inecuaciones[self.__numIne - 2][1].insert(0, "1")
        self.__Inecuaciones[self.__numIne - 2][1].config(state="readonly")
        self.__Inecuaciones[self.__numIne - 2][2].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 2][2].config(state="readonly")
        self.__Inecuaciones[self.__numIne - 2][4].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 2][4].config(state="readonly")

        self.__Inecuaciones[self.__numIne - 1][0].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 1][0].config(state="readonly")
        self.__Inecuaciones[self.__numIne - 1][1].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 1][1].config(state="readonly")
        self.__Inecuaciones[self.__numIne - 1][2].insert(0, "1")
        self.__Inecuaciones[self.__numIne - 1][2].config(state="readonly")
        self.__Inecuaciones[self.__numIne - 1][4].insert(0, "0")
        self.__Inecuaciones[self.__numIne - 1][4].config(state="readonly")


    @staticmethod
    def checkbuttona():
        global ca
        global a
        print(ca)
        if(ca %2==0):
            print('a falso')
            a = False
            ca = 1
        else:
            print('a verdadero')
            a = True
            ca += 1

    @staticmethod
    def checkbuttonb():
        global cb
        global b
        print(cb)
        if (cb % 2 == 0):
            print('b falso')
            b = False
            cb = 1
        else:
            print('b verdadero')
            b = True
            cb += 1

    @staticmethod
    def checkbuttonc():
        global cc
        global c
        print(cc)
        if (cc % 2 == 0):
            print('c falso')
            c = False
            cc = 1
        else:
            print('c verdadero')
            c = True
            cc += 1

    def hacer_algo(self):
# Llamando a la clase Calcular_Puntos
# ##Calcular_Puntos.__init__(self, self.__Inecuaciones, self.__numIne)
# ##Calcular_Puntos.calcular(self)
# ##Calcular_Puntos.graficar(self)
# ##Calcular_Puntos.region_factible(self)
        global contadormaximo
        contadormaximo += 1
        Calcular_Puntos.grafico(self)

# Funcion para llamar a la clase Inecuaciones
def calc_ine():
    objeto = Inecuaciones(numIne.get())
    objeto.iniciar()

    # Boton para enviar inecuaciones
    btnCalcular = Button(marco, text="Solucionar", command=objeto.hacer_algo, width=10)
    btnCalcular.pack()
    btnCalcular.place(x=905, y=225)


# Crea el marco
marco = tk.Tk()
marco.title("Programacion entera mixta (PEM)")
marco.geometry("1000x500")
marco.configure(background="#ffffff")
marco.resizable(0,0)

# Etiquetas
lbl1 = tk.Label(marco, text="Función objetivo:          Z =")
lbl1.pack()
lbl1.config(background="#ffffff")
lbl1.config(foreground="#000000")
lbl1.place(x=0, y=30)

lbl2 = tk.Label(marco, text="X      +")
lbl2.pack()
lbl2.config(background="#ffffff")
lbl2.config(foreground="#000000")
lbl2.place(x=215, y=30)

lbl3 = tk.Label(marco, text="Y      +")
lbl3.pack()
lbl3.config(background="#ffffff")
lbl3.config(foreground="#000000")
lbl3.place(x=325, y=30)

lblt = tk.Label(marco, text="T")
lblt.pack()
lblt.config(background="#ffffff")
lblt.config(foreground="#000000")
lblt.place(x=435, y=30)

lbl4 = tk.Label(marco, text="max/min")
lbl4.pack()
lbl4.config(background="#ffffff")
lbl4.config(foreground="#000000")
lbl4.place(x=555, y=10)

lbl5 = tk.Label(marco, text="Cantidad de restricciones: ")
lbl5.pack()
lbl5.config(background="#ffffff")
lbl5.config(foreground="#000000")
lbl5.place(x=665, y=30)

imagen = PhotoImage(file="covid.png")
fondo = tk.Label(marco,image=imagen)
fondo.pack()
fondo.place(x=200,y=130)

lbl7 = tk.Label(marco, text="Coef X")
lbl7.pack()
lbl7.config(background="#ffffff")
lbl7.config(foreground="#000000")
lbl7.place(x=450, y=100)

lbl8 = tk.Label(marco, text="Coef Y")
lbl8.pack()
lbl8.config(background="#ffffff")
lbl8.config(foreground="#000000")
lbl8.place(x=550, y=100)

lbltcoef = tk.Label(marco, text="Coef T")
lbltcoef.pack()
lbltcoef.config(background="#ffffff")
lbltcoef.config(foreground="#000000")
lbltcoef.place(x=650, y=100)

lbl13 = tk.Label(marco, text="Entero")
lbl13.pack()
lbl13.config(background="#ffffff")
lbl13.config(foreground="#000000")
lbl13.place(x=365, y=100)

lbl9 = tk.Label(marco, text="SUJETO A (S.A):  ")
lbl9.pack()
lbl9.config(background="#ffffff")
lbl9.config(foreground="#000000")
lbl9.place(x=325, y=75)

lbl10 = tk.Label(marco, text="Andres Felipe Wilches Torres - 20172020114")
lbl10.pack()
lbl10.config(background="#ffffff")
lbl10.config(foreground="#000000")
lbl10.place(x=0, y=475)

lbl11 = tk.Label(marco, text="Nicolas Andrade Perdomo - 20172020097")
lbl11.pack()
lbl11.config(background="#ffffff")
lbl11.config(foreground="#000000")
lbl11.place(x=0, y=450)

lbl12 = tk.Label(marco, text="Luis Alejandro Ocampo Gamboa - 20172020050")
lbl12.pack()
lbl12.config(background="#ffffff")
lbl12.config(foreground="#000000")
lbl12.place(x=0, y=425)

lbl12 = tk.Label(marco, text="Universidad Distrital Francisco Jose de Caldas")
lbl12.pack()
lbl12.config(background="#ffffff")
lbl12.config(foreground="#000000")
lbl12.place(x=0, y=400)

# Funcion objetivo
fObj1 = tk.Entry(marco, width=10)
fObj1.pack(anchor=CENTER)
fObj1.config(background="#ffffff")
fObj1.config(foreground="#000000")
fObj1.place(x=150, y=30)

fObj2 = tk.Entry(marco, width=10)
fObj2.pack(anchor=CENTER)
fObj2.config(background="#ffffff")
fObj2.config(foreground="#000000")
fObj2.place(x=260, y=30)

fObj3 = tk.Entry(marco, width=10)
fObj3.pack(anchor=CENTER)
fObj3.config(background="#ffffff")
fObj3.config(foreground="#000000")
fObj3.place(x=550, y=30)

fObj4 = tk.Entry(marco, width = 10)
fObj4.pack(anchor=CENTER)
fObj4.config(background="#ffffff")
fObj4.config(foreground="#000000")
fObj4.place(x=370, y=30)

# Inecuaciones
numIne = tk.Entry(marco, width=10)
numIne.pack(anchor=CENTER)
numIne.config(background="#ffffff")
numIne.config(foreground="#000000")
numIne.place(x=815, y=30)

# Boton enviar inecuaciones
btnEnviar = tk.Button(marco, text="Crear", command=calc_ine, width=10)
btnEnviar.pack()
btnEnviar.place(x=900, y=30)

marco.mainloop()
