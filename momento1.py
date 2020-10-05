lista_trabajadores = []
Nomina_Emp= 0
SalarioT=0
PSalario=0
MSalario=0


print("Digite  los datos de cada uno de los 5 Empleados")

for i in range(1,6):

   Empleado = {}
   print("Empleado " + str(i))
   Empleado["nombre"] = input("nombre: ")
   Empleado["Salario_Basic"] = float(input("Salario Basico mes: "))
   Empleado["nro_Hext"] = float(input("Nro horas Extras mes: "))
   Empleado["Valor_Hext"] =Empleado["Salario_Basic"]*0.005729166
   Empleado["Salario_Total"]= Empleado["Salario_Basic"]+(Empleado["Valor_Hext"]*Empleado["nro_Hext"])
   print("Salario Total :")
   print(Empleado["Salario_Total"])
   Nomina_Emp = Nomina_Emp + Empleado["Salario_Total"]
   PSalario=Empleado["Salario_Total"]
   MSalario=Empleado["Salario_Total"]
   if Empleado["Salario_Total"]>=200000 and Empleado["Salario_Total"] <= 600000:
      print("Categoria A")
   elif Empleado["Salario_Total"]>600000:
      print("Categoria B")
 
   
   Nomina_Emp=Nomina_Emp+Empleado["Salario_Total"]


lista_trabajadores.append(Empleado)

print("Nomina de La Empresa:")
print(Nomina_Emp)







