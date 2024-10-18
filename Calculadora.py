import tkinter as tk

main = tk.Tk()
main.title("Calculadora")

def exibir_numero():
    numero_tela = entrada_numero.get()
    numero_mostrado.config(text=f"Numero Digitado: {numero_tela} ")

entrada_numero = tk.Entry(main, font=("Arial", 25))
entrada_numero.pack()

numero_mostrado = tk.Label(main, text="", font=("Arial", 20))
numero_mostrado.pack()

botao_exibir_numero = tk.Button(main, text="Mostrar Texto", command=exibir_numero)
botao_exibir_numero.pack()

#Texto_1 = tk.Label(main, text="NUMERO: ", font={"Arial", 30})
#Texto_1.pack()
#numero = int(input("DIGITAR UM NUMERO:"))

#Numero_tela = tk.Label(main,text=f"{numero}")
#Numero_tela.pack()

main.mainloop()