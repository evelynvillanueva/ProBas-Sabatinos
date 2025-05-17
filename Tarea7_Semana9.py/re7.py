# Validar código postal

import re 

patron_postal = r"^\d{5}(-\d{4})?$"

re.match(patron_postal, "65467")
re.match(patron_postal, "76545-8765")