# Validar una fecha en formato DD//MM//AAAA
import re 

patron_fecha = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$"

re.match(patron_fecha, "16/05/2025")
re.match(patron_fecha, "43/03/2022")