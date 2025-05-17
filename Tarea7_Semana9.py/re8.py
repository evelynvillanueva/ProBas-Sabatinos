# Validar nombre del usuario
import re 

patron_usuario = r"^[a-zA-Z0-9_]{3,16}$"

re.match(patron_usuario, "usuario_454")
re.macth(patron_usuario, "nm")