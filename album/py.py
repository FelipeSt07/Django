class Estudiante:
    def __init__(self,cod_est,nom_est):
        self.cod_est = cod_est
        self.nom_est = nom_est    
class Materia:
    def __init__(self,cod_mat,nom_mat):
        self.cod_mat = cod_mat
        self.nom_mat = nom_mat


class Registro:
    def __init__(self):
            self.notas = {}
    def agregar_notas(self, cod_est, cod_mat, nota):
        if cod_est not in self.notas:
            self.notas[cod_est] = {}
        self.notas[cod_est][cod_mat] = nota

def  mostrar_notas(self, cod_est):
        if cod_est in self.notas:
         return self.notas[cod_est]
        else:
            print("Estudiante no encontrado")
            return
    def modificar_nota (self, cod_est, cod_mat, nueva_nota):
        if cod_est in self.notas and cod_mat in self.notas(cod_est):
             self.notas(cod_est)(cod_mat) in self

    


estudiante1 = Estudiante(1,"Ana")
estudiante2 = Estudiante(2,"Juan carlos")

materia1 = Materia(101, "Matematicas Generales")
materia2 = Materia(102, "Logica Matematica")
materia3 = Materia(201, "Calculo I")


#print(estudiante1)
print(estudiante1.nom_est)
print(estudiante1.cod_est)


#print(estudiante2)
print(estudiante2.nom_est)
print(estudiante2.cod_est)


#Print(Materia1)
print (materia1.cod_mat)
print (materia1.nom_mat)

#Print(materia2)
print (materia2.cod_mat)
print (materia2.nom_mat)

#Print(materia3)
print (materia3.cod_mat)
print (materia3.nom_mat)


Registro = Registro()
Registro.agregar_notas(estudiante1.cod_est, materia1.cod_mat, 3.5)
print("Ana maria: ", Registro.mostrar_notas(estudiante1.cod_est))

























































































