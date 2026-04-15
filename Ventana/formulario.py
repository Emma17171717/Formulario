import tkinter as Ventana #colocar sobre-nombre

class Formulario:
    def __init__(self):
        self.color = "rojo"
        self.entry_nombre = " "
        self.label_resultado = " "
        self.formulario = " "
        self.datos_cliente = []
        self.entry_apellido = " "
        self.entry_cedula = " "
        self.entry_telefono = " "
        self.entry_correo = " "

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

        label_apellido = Ventana.Label(text = "digite el apellido del cliente: ")
        label_apellido.pack()

        self.entry_apellido = Ventana.Entry(self.formulario)
        self.entry_apellido.pack()

        label_cedula = Ventana.Label(text = "digite la cedula del cliente: ")
        label_cedula.pack()

        self.entry_cedula = Ventana.Entry(self.formulario)
        self.entry_cedula.pack()

        label_telefono = Ventana.Label(text = "digite el telefono del cliente: ")
        label_telefono.pack()

        self.entry_telefono = Ventana.Entry(self.formulario)
        self.entry_telefono.pack()

        label_correo = Ventana.Label(text = "digite el correo del cliente: ")
        label_correo.pack()

        self.entry_correo = Ventana.Entry(self.formulario)
        self.entry_correo.pack()

        #button ----> boton
        boton_enviar = Ventana.Button(self.formulario, text="Enviar", command=self.procesar_formulario) #para enviar informacion, usar Lambda
        boton_enviar.configure(bg="orange")
        boton_enviar.pack()  

    def hacer_clic(self):
        print("clik....")

    def validar_campos(self):
        if self.entry_nombre.get() == "":
            return False
        if self.entry_apellido.get() == "":
            return False
        if self.entry_cedula.get() == "":
            return False
        if self.entry_telefono.get() == "":
            return False
        if self.entry_correo.get() == "":
            return False
        return True

    def guardar_datos(self):
        self.datos_cliente = [
            self.entry_nombre.get(),
            self.entry_apellido.get(),
            self.entry_cedula.get(),
            self.entry_telefono.get(),
            self.entry_correo.get()
        ]

    def procesar_formulario(self):
        if self.validar_campos():
            self.guardar_datos()
            print("Formulario guardado correctamente")
            print(self.datos_cliente)
        else:
            print("Hay campos vacios")
