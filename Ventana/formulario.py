import tkinter as Ventana #colocar sobre-nombre

class Formulario:
    def __init__(self):
        self.color = "rojo"
        self.entry_nombre = " "
        self.label_resultado = " "
        self.formulario = " "

    def iniciar_ventana(self):
        self.formulario = Ventana.Tk() #widgets
        self.formulario.title("Registro de usuario")
        self.formulario.geometry("800x800")
        self.formulario.resizable(False, True)
        self.formulario.config(bg="red", cursor="hand2") #solo usar cuando el objeto o widgets este creado
        return self.formulario #hago retorno porque my loop finaliza al final del codigo
    
    def iniciar_preguntas(self):
        #label --> titulos textos
        label_nombre = Ventana.Label(text = "digite el nombre del cliente: ")
        label_nombre.config(padx=10, pady = 10, borderwidth=2, fg = "blue")
        label_nombre.pack()
        #entry ----> input text ---->cajitas de texto
        self.entry_nombre = Ventana.Entry(self.formulario)
        self.entry_nombre.config(bg = "yellow")
        self.entry_nombre.pack()

        #button ----> boton
        boton_enviar = Ventana.Button(self.formulario, text="Enviar", command=self.hacer_clic) #para enviar informacion, usar Lambda
        boton_enviar.configure(bg="orange")
        boton_enviar.pack()  

    def hacer_clic(self):
        print("clik....")