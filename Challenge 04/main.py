import os

# Leer archivo con los datos
def read_data() -> str:
  """
  Abre y lee un archivo específico para analizar su contenido.
  """
  input_dir = os.path.dirname(__file__)
  file_path = os.path.join(input_dir, "data.txt")

  with open(file_path) as f:
    return f.read().splitlines(False)
  
def prepare_data(data):
  i = 0
  lines = []
  while i < len(data):
    lines.append(data[i].split('-'))

    i += 1



  
print(prepare_data(read_data()))