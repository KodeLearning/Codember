import os

def read_data():
  input_dir = os.path.dirname(__file__)
  file_path = os.path.join(input_dir, "data.txt")

  with open(file_path) as f:
    return f.read().split(' ')
  
def unique_animals(data: list) -> list:
  animals: list = []

  for animal in data:
    if animal not in animals:
      animals.append(animal)
      
  return animals

def count_unique_animals(animals):
  

data = read_data()
print(unique_animals(data))
