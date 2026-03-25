from formulario import Formulario

#zona codigo principal 
obj_formulario = Formulario()


#linea 9 es traer la ventana....
aux_formulario = obj_formulario.iniciar_ventana()
obj_formulario.iniciar_preguntas()
aux_formulario.mainloop() #siempre ir al final!!! oyo eliana
#hacer 5 preguntas y agregar dos botones mas, agregar el comando command