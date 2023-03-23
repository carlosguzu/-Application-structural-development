from person import Person
from address import Address
from package import Package
from deliver import Deliver


print("_________________________")
print("| ID | NOMBRE | APELLIDO |")
cliente1 = Person(id_person= 65185, name="Carlos", last_name="Zuniga")
print(cliente1)
cliente1.last_name = "Guzman" #Accede al atributo name para update it.
print(cliente1)

cliente2 = Person() #Objeto vacío
print(cliente2)
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

print("\n__________________________________________")
print("| ID | PESO | DESCRIPCIÓN | COSTO | ITEMS |")
package = Package(123, 5.0, "Paquete pequeño", 10.5, items = "Airpods")
print(package)
package2 = Package() #Objeto vacío
print(package2)
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

print("\n________________________________________________________________________________________________________")
print("| FECHA | HORA |   ENVÍA   |    RECIBE    |  DIR. REMITENTE  |  DIR. DESTINATARIO  |  CONTACTO  | ITEMS |")
deliver1 = Deliver(date = "1/5/23", time = "20:58", sender = "Mario Zuniga", recive = "Carlos Guzman", sender_add = "Bogotá, Calle 38", recive_add = "Cartagena Crra 104", contac = +573046356749, items = "Airpods")
print(deliver1)
deliver = Deliver() #Objeto vacío
print(deliver)
print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")