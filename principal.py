from formulario import Formulario

#zona codigo principal 
obj_formulario = Formulario()

#linea 9 es traer la ventana....
aux_formulario = obj_formulario.iniciar_ventana()
obj_formulario.iniciar_preguntas()
aux_formulario.mainloop()
