import tkinter as tk

main = tk.Tk()
main.title("Calculadora")



Texto_1 = tk.Label(main, text="DIGITAR NUMERO: ", font={"Arial", 30})
Texto_1.pack()
numero = int(input("DIGITAR UM NUMERO:"))

Numero_tela = tk.Label(main,text=f"{numero}")
Numero_tela.pack()

main.mainloop()