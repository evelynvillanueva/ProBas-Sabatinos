#Validar número de tarjeta de crédito. 

import re 

patron_tarjeta = r"^\d{4}-\d{4}-\d{4}-\d{4}$"

re.match(patron_tarjeta, "1234-5678-9012-3456")