class ManagamentRol:

    #es un constructor, self es this
    def __init__(self):
        self.roles=[]

    #def son metodos, append agrega el dato siempe en la ultima posicion
    def addRol(self, rol):
        self.roles.append(rol)
        print(f'El rol {rol} fue agregado correctamente!')

    def quitRol(self, rol):
        try:
            self.roles.remove(rol)
        except ValueError:
            print(f'El rol {rol} no existe dentro de la lista')

    def updateRol(self, rolChange, newRol):
        try:
            self.roles.remove(rolChange)
            self.roles.append(newRol)
        except ValueError:
            print(f'El rol {rolChange}, fue actualizado por {newRol}')

    def getRol(self):
        print(f'Tus roles son: {', '.join(self.roles)}')
        print("==============================")

roles = ManagamentRol()
roles.addRol("Administrador")
roles.quitRol("Contador")
roles.getRol()
roles.addRol("Medico")
roles.quitRol("Arquitecto")
roles.getRol()