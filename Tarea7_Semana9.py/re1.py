# Validar una direciión de correo electrónico.

import re 

patron_correo = r"^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]{3}$"

re.match(patron_correo, "johndoe@correo.com")
re.match(patron_correo, "janedoe23@correo.com")