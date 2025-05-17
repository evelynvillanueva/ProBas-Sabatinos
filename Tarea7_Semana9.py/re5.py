# Buscar palabras que empiecen con mayúscula.
import re 

patron_mayusculas = r"\b[A-Z][a-z]*\b"

texto = "Pepe pica papas."
re.findall(patron_mayusculas, texto)