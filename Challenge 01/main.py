import os

def read_data():
  input_dir = os.path.dirname(__file__)
  file_path = os.path.join(input_dir, "data.txt")

  with open(file_path) as f:
    return f.read().split()
  
def count_animals(wordlist: str) -> int:
  ordered_list = {}
  for word in wordlist:
    if word not in ordered_list:
      ordered_list[word] = 1
    else:
      value = ordered_list.get(word)
      ordered_list[word] = value + 1
  print(ordered_list)
  return ordered_list

def report_words_ordered(words: dict) -> str:
  report = ''.join("{!s}{}".format(key, val) for (key, val) in words.items())

  return report

data = read_data()
animals = count_animals(data)
print(report_words_ordered(animals))
