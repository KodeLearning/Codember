import os

def read_data():
  input_dir = os.path.dirname(__file__)
  file_path = os.path.join(input_dir, "data.txt")

  with open(file_path) as f:
    return f.read()
  
  # "#" Incrementa el valor numérico en 1.
  # "@" Decrementa el valor numérico en 1.
  # "*" Multiplica el valor numérico por sí mismo.
  # "&" Imprime el valor numérico actual.

def decode_message(data: str) -> int:
  message_decoded = str(0)
  current = 0
  for symbol in data:
    if symbol == "#":
      current = current + 1
    elif symbol == "@":
      current = current - 1
    elif symbol == "*":
      current = current**2
    elif symbol == "&":
      message_decoded = message_decoded + str(current)

    current = current

  return int(message_decoded)

print(decode_message(read_data()))