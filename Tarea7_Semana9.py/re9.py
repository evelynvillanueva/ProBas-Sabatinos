# Buscar fechas en formato ISO 8601

import re 

patron_iso8601 = r"\b\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\b"

re.findall(patron_iso8601, "Fecha: 2022-07-21, 2025-05-17")