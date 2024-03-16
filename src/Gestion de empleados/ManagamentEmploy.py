import ManagamentRol

class ManagamentEmploy:

    def __init__(self):
        self.employ=[]

    def employCreate(self, empl, ind):
        try:
            rol = ManagamentRol.roles.roles[ind]
            self.employ.append(empl)
            print("El empleado {} con el rol {} fue creado correctamente!".format(empl, rol))
        except IndexError:
            print("No existe un rol diferente a {} para ser asignado, se cancela la creacion del empleado".format(
                ManagamentRol.roles.roles[0]))

    def updateEmploy(self, employChange, newEmploy):
        try:
            self.employ.remove(employChange)
            self.employ.append(newEmploy)
            print(f'El Empleado {employChange}, fue actualizado por {newEmploy}')
        except ValueError:
            print(f'El Empleado {employChange} no existe')

    def quitEmploy(self, empl):
        try:
            self.employ.remove(empl)
        except ValueError:
            print(f'El empleado {empl} no existe dentro de la lista')

    def getEmploy(self):
        print(f'Tus empleados son: {', '.join(self.employ)}')
        print("===========================")

employ = ManagamentEmploy()
employ.employCreate("Laura", 0)
employ.updateEmploy("Laura", "Daniel")
employ.quitEmploy("Daniel")
employ.getEmploy()
employ.employCreate("Sara", 1)
employ.updateEmploy("Sara", "Natalia")
employ.quitEmploy("Carlos")
employ.getEmploy()
