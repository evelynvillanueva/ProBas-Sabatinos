#Validar una dirección IPv4

import re 

patron_ipv4 = r"((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.{3}(25[0-5]|2[0-4]\d|1\d\d|" \
"[1-9]?\d)$"

re.match(patron_ipv4, "192.168.0.1")
re.match(patron_ipv4, "999.0.0.1")