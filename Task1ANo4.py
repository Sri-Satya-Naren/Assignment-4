try:
  with open("sample.txt","rt") as rd:
    content=rd.read()
    print(content)   
except FileNotFoundError:
  print(" The file 'sample.txt' was not found")
