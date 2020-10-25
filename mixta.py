from __future__ import print_function

from ortools.linear_solver import pywraplp

from tkinter import *

from tkinter.ttk import *
import numpy as np
from matplotlib import pyplot as plt

def RunIntegerExampleNaturalLanguageAPI(optimization_problem_type):
    raiz1 = Tk()
    raiz1.geometry("1200x550")
    raiz1.title("Interfaz Soluciones PEM")
    # img=PhotoImage(file="/home/juan/Documentos/Semestre 2020-1/IO/Codigo python/ud.png")
    # Label1=Label(raiz1, image=img).grid(column = 0, row = 0)
    Label2 = Label(raiz1, text="Programación mixta entera", font=("Arial Bold", 20))
    Label2.grid(column=2, row=0)

    solver = pywraplp.Solver('Solucion ejemplo', optimization_problem_type)
    infinity = solver.infinity()
    # se escribe cada variable se inicializa en cero, y se comprueba que nosea negativa
    # si la variable es numerica se escribe Numvar
    # si la variable es entera se escribe IntVar
    x1 = solver.NumVar(0.0, infinity, 'x1')
    x2 = solver.NumVar(0.0, infinity, 'x2')
    x3 = solver.NumVar(0.0, infinity, 'x3')
    x4 = solver.IntVar(0.0, infinity, 'x4')

    variable = 0
    variable1 = 0
    variable2 = 0
    stringvaroptimproblem = StringVar()
    labelz13 = Label(raiz1, text="Ingresar ecuacion a optimizar", font=("Arial Bold", 10))
    labelz13.grid(column=0, row=1)
    ec10 = Entry(raiz1, width=45)
    ec10.grid(column=1, row=1)

    despla = 3
    ec22 = Entry(raiz1, width=10)
    ec22.grid(column=2, row=1)
    labelz130 = Label(raiz1, text="Ingresar tipo de problema", font=("Arial Bold", 10))
    labelz130.grid(column=0, row=2)
    comboExample = Combobox(raiz1, values=["Maximizar", "Minimizar", ])
    comboExample.grid(column=1, row=2)

    def clicked1():
        # si no se ingreso nada
        # se escribe el problema a optimizar
        solver.Maximize(50 * x1 + 120 * x2)
        # socolocan las variables a optimizar en un lenguaje natural
        # si son 7 como en el siguiente ejemplo se agregagan 7 "Solver.add" con su ecuaciones
        solver.Add(1 * x1 + 1 * x2 <= 110)
        solver.Add(100 * x1 + 200 * x2 <= 10000)
        solver.Add(10 * x1 + 30 * x2 <= 1200)
        solver.Add(1 * x1 >= 0)
        solver.Add(1 * x2 >= 0)

        # se colocan todas la variables a resolver en el siguiente parentesis
        SolveAndPrint(solver, [x1, x2])




    def clicked():
        btn1 = Button(raiz1, text="Solucionar problema", command=clicked1)
        btn1.grid(column=2, row=15)

        for i in range(0, int(ec22.get())):
            ec2 = Entry(raiz1, width=45)
            ec2.grid(column=2, row=despla + i)

    btn = Button(raiz1, text="Ingresar ecuaciones", command=clicked)
    btn.grid(column=3, row=1)

    labelz1 = Label(raiz1, text="Ingresar variables numericas", font=("Arial Bold", 10))
    labelz1.grid(column=0, row=3)
    ec3variables = Entry(raiz1, width=20)
    ec3variables.grid(column=1, row=3)
    labelz1 = Label(raiz1, text="Ingresar variables enteras", font=("Arial Bold", 10))
    labelz1.grid(column=0, row=5)
    ec4 = Entry(raiz1, width=20)
    ec4.grid(column=1, row=5)

    raiz1.mainloop()


def SolveAndPrint(solver, variable_list):
    raiz = Tk()
    raiz.geometry("750x550")
    raiz.title("Interfaz Soluciones PEM")

    solver.SetNumThreads(8)
    result_status = solver.Solve()

    assert result_status == pywraplp.Solver.OPTIMAL

    assert solver.VerifySolution(1e-7, True)

    Label2 = Label(raiz, text="solución al problema", font=("Arial Bold", 20))
    Label2.grid(column=1, row=0)
    ec1 = Entry(raiz, justify=RIGHT)

    varle = str(solver.Objective().Value())
    label = Label(raiz, text='Valor optimo: ', font=("Arial Bold", 15))
    label.grid(column=1, row=5)
    labelvp = Label(raiz, text=varle, font=("Arial Bold", 15))
    labelvp.grid(column=1, row=6)
    label = Label(raiz, text='Variables y soluciones: ', font=("Arial Bold", 15))
    label.grid(column=0, row=5)
    btn4 = Button(raiz, text="grafica", command=grafica)
    btn4.grid(column=2, row=6)

    entero = 6

    for variable in variable_list:
        varn = str(variable.name())
        vars = str(variable.solution_value())
        labelx1 = Label(raiz, text=varn + "= " + vars, font=("Arial Bold", 15))
        labelx1.grid(column=0, row=entero)
        entero = entero + 1

    raiz.mainloop()


def Announce(solver, api_type):
    print('---- Problema programacion mixto' + ' -----')


def RunAllIntegerExampleNaturalLanguageAPI():
    if hasattr(pywraplp.Solver, 'CBC_MIXED_INTEGER_PROGRAMMING'):
        Announce('CBC', 'natural language API')
        RunIntegerExampleNaturalLanguageAPI(pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)


def main():
    RunAllIntegerExampleNaturalLanguageAPI()

def grafica():
    x = np.arange(0, 120, 1)
    x1 = np.arange(0, 110, 1)
    x2 = np.arange(0, 100, 1)
    x3 = np.arange(0, 120, 1)
    # x=10
    print(x)

    y = -(1 / 3) * x + 40
    y1 = -(1 / 2.444) * x1 + 45
    y2 = -(1 / 2) * x2 + 50
    y3 = -(1) * x3 + 110
    print(y)

    plt.plot(x, y, 'm')
    plt.axhline(y=0, xmin=0.01, xmax=0.95)
    plt.axvline(x=0, ymin=0.01, ymax=0.95)

    plt.plot(x1, y1, 'm')
    plt.axhline(y=0, xmin=0.01, xmax=0.95)
    plt.axvline(x=0, ymin=0.01, ymax=0.95)

    plt.plot(x2, y2, 'm')
    plt.axhline(y=0, xmin=0.01, xmax=0.95)
    plt.axvline(x=0, ymin=0.01, ymax=0.95)

    plt.plot(x3, y3, 'm')
    plt.axhline(y=0, xmin=0.01, xmax=0.95)
    plt.axvline(x=0, ymin=0.01, ymax=0.95)

    plt.plot(60, 20, marker="o", color="red")
    plt.fill_between(x, y, where=(x < 60), color='blue')
    plt.fill_between(x2, y2, where=(x2 >= 58), color='blue')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
