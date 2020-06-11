import random


f=open("text.txt")
for line in f:
   for line1 in line.rstrip().split(" "):
      print(line1)
      file = open('ok.txt', "a")
      file.write(line1+"\n")
      file.close()





f=open("text.txt")
for line in f:
   for line1 in line.rstrip().split(" "):
      text = line1
      words = text.split()
      for i, word in enumerate(map(list, words)):
         random.shuffle(word)
         words[i] = ''.join(word)
         print(*words)
         file = open('wrong.txt', "a")
         file.write(str(*words)+"\n")
         file.close()
