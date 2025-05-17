#Buscar números de teléfono.
import re 

patron_telefono = r"\+\d{2}[- ]\d{4}[- ]\d{4}"

re.findall(patron_telefono, "Marque al +78-3453-3456 o al +78 3452 4563")