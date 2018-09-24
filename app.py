import json
import difflib

data = json.load(open("data .json"))
print("Please note the commands can be entered in small or capital letters as you like")

def trans(w):
  w= w.lower()
  if w in data:
    return data[w]
  else:
    bestMatch= difflib.get_close_matches(w,data.keys())
    for match in bestMatch:
      match=match.capitalize()
      command=input("Did you mean "+match+" Y for yes and N for no and -1 to go back\n")
      command=command.lower()
      if command=='y':
        return trans(match)
      elif command=='-1':
        return ""
    return "The word does not exist"

word=input("Enter a word or -1 to exit\n")

while word != "-1":
  translations=trans(word)
  if type(translations)==str:
    print("Definition: ")
  if len(translations)==1:
    print(translations[0])
  else:
    for tranz in translations:
      print(tranz)
  word=input("Enter a word or -1 to exit\n")
