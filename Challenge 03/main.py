import os
import re

# Leer archivo con los datos
def read_data() -> str:
  """
  Abre y lee un archivo específico para analizar su contenido.
  """
  input_dir = os.path.dirname(__file__)
  file_path = os.path.join(input_dir, "data.txt")

  with open(file_path) as f:
    return f.read().splitlines(False)
  
# Extraer linea para analizarla
def select_line(data: list, position: int) -> str:
  """
  Recibe contenido a traves de $data en forma de lista.
  Indica la $posicion dentro de $data
  Devuelve solo la $posicion que se ha pedido.
  """
  return data[position]

# Extrae la parte de los rangos y añadirlos a una lista
def find_range(line: str) -> list:
  """
  Recibe una cadena de texto.
  Extrae números separados por simbolos y los añade a una lista.
  Devuelve un diccionario con el rango mínimo y máximo.
  """
  range_part = []
  range_part.append(re.findall(r'\b\d+\b', line))
  ranges = range_part[0]

  return { 
    'min_range': int(ranges[0]),
    'max_range': int(ranges[1]) 
  }

# Extrae la letra que debe repetirse
def find_letter(line: str) -> str:
  """
  Recibe una cadena de texto.
  Busca una sola letra de A a Z en minuscula delimitada por simbolos.
  Convierte el resultado en una cadena.
  Devuelve la letra encontrada
  """
  letter_part = []
  letter_part.append(re.findall(r'\b[a-z]\b', line))
  letter = ' '.join(letter_part[0])
  return letter

# Extrae el código a revisar
def find_code(line: str) -> str:
  """
  Recibe una cadena de texto.
  Busca una cadena dentro de la recibida que se encuentra despues de ':'
  Convierte el resultado en una cadena.
  Devuelve lo encontrado.
  """
  code_part = []
  code_part.append(re.findall(r':\s(.+)', line))
  code = ' '.join(code_part[0])
  return code

# Analiza si el codigo cumple los requisitos
def analize_code(range: str, letter: str, code: str) -> bool:
  """
  Recibe los dos rangos de find_range()
  Recibe la letra encontrada de find_letter()
  Recibe la cadena encontrada de find_code()
  Averigua si $letter se encuentra en $code
    más veces que $min_range y menos que $max_range
  Devuelve Bool segun la averiguacion.
  """
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
  """
  Recibe contenido a traves de $data en forma de lista.
  Analiza cada linea dentro de $data y guarda la averiguacion.
  Devuelve una lista de todos los códigos no válidos.
  """
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

# Imprime el elemento nº 42
print('submit ' + select_line(invalid_codes(read_data()), 41))