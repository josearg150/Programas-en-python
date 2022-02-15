#Para renombrar agregar as, from permite seleccionar desde donde y que se quiere importar
import modulos as xs
from camelcase import CamelCase
 
print(xs.mascotas)
xs.saludo('jose')
 
c = CamelCase()
s = 'esta oracion necesita CamelCase!'
 
camelcased = c.hump(s)
print(camelcased)