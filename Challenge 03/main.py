import os
import re

# Leer archivo con los datos
def read_data() -> str:
  input_dir = os.path.dirname(__file__)
  file_path = os.path.join(input_dir, "data.txt")

  with open(file_path) as f:
    return f.read().splitlines(False)
  
# Extraer linea para analizarla
def select_line(data: str, position: int) -> str:
  return data[position]

# Extrae la parte de los rangos y añadirlos a una lista
def find_range(line: str) -> list:
  range_part = []
  range_part.append(re.findall(r'\b\d+\b', line))
  ranges = range_part[0]

  return { 
    'min_range': int(ranges[0]),
    'max_range': int(ranges[1]) 
  }

# Extrae la letra que debe repetirse
def find_letter(line: str) -> str:
  letter_part = []
  letter_part.append(re.findall(r'\b[a-z]\b', line))
  letter = ' '.join(letter_part[0])
  return letter

# Extrae el código a revisar
def find_code(line: str) -> str:
  code_part = []
  code_part.append(re.findall(r':\s(.+)', line))
  code = ' '.join(code_part[0])
  return code

# Analiza si el codigo cumple los requisitos
def analize_code(range: str, letter: str, code: str) -> bool:
  count = 0
  is_valid = False

  for char in code:
    if char == letter:
      count += 1
  
  if count >= range['min_range'] and count <= range['max_range']:
    is_valid = True
  
  return is_valid

# Devuelve una lista de códigos no validos
def invalid_codes(data: str) -> str:
  all_invalids = []
  is_valid = 0
  i = 0

# find_code(select_line(read_data(), 3))
  while i < len(data):
    range = find_range(data[i])
    letter = find_letter(data[i])
    code = find_code(data[i])
    is_valid = analize_code(range, letter, code)

    if not is_valid:
      all_invalids.append(code)

    i += 1

  return all_invalids

print('submit ' + select_line(invalid_codes(read_data()), 41))