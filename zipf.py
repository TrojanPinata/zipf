import csv
import string

def list_of_words(filename):
   print("reading file data...")
   input = open(filename,"r", encoding='utf-8')
   output = open("LOW.txt","w", encoding='utf-8')
   text = input.readlines()
   m = False
   c = 0
   r = 0
   stringer = ""
   while m == False:
      if (text[c][r] == "<" and text[c][r + 1] == "!" and text[c][r + 2] == "-"and text[c][r + 3] == "-" and text[c][r + 4] == ">"):
         m = True
      else:
         l1 = len(text)
         if text[c][r] == "\n":
            output.write(stringer + "\n")
            c += 1
            r = 0
            stringer = ""
         elif text[c][r] == " " and text[c][r + 1] == "\n":
            c += 1
            r = 0
            stringer = ""
         elif text[c][r] == " ":
            output.write(stringer + "\n")
            r += 1
            stringer = ""
         else:
            stringer += text[c][r]
            r += 1

def generate_csv(sorted):
   print("generating csv...")
   fields = ['Word', 'Count', 'Rank']
   rows = len(sorted)

   with open("zipf.csv", "w", encoding='utf-8') as csvfile:
      csvw = csv.writer(csvfile)
      csvw.writerow(fields)
      for i in range(rows):
         csvw.writerow(sorted[i])

def removeblanks(sorted):
   for k in range(len(sorted)):
      if sorted[k][0] == '':
         sorted.pop(k)
         break

def sortSecond(value):
   return value[1]

def sorter(counted):
   # O( n log(n) ) sucks, but is fine for now
   return counted.sort(key=sortSecond, reverse=True)

def rank(sorted):
   print("ranking...")
   o = len(sorted)
   for i in range(o):
      sorted[i][2] = i + 1
   return sorted

def count():
   input = open("LOW.txt","r", encoding='utf-8')
   words = input.readlines()
   num_words = len(words)
   print("trimming...")
   for g in range(num_words):
      words[g] = words[g].rstrip('\n')
      words[g] = words[g].lower()
      words[g] = words[g].translate(str.maketrans('', '', string.punctuation))
   counter = []
   print("counting...")
   for i in range(num_words):
      ctr = len(counter)
      location = -1
      for j in range(ctr):
         if counter == []:
            continue
         elif words[i] == counter[j][0]:
            location = j
            break
         else:
            location = -1 # repetitive for insurance

      if location == -1:
         counter.append([words[i], 1, 0])
      else: 
         counter[j][1] += 1
   return counter

print("starting...")
filename = 'post.txt'
list_of_words(filename)
counted = count()
sorter(counted)
sorted = rank(counted)
removeblanks(sorted)
generate_csv(sorted)