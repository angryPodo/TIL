while(True):
  name = input("wht is ur name?")
  if (name == "skip"):
    continue
  elif(name == "finish"):
    break
  print("welcome",name)