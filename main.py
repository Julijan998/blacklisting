import fileinput
import re

print('Unesite redni broj nacina kako zelite da cenzurisete: \n 1. porn -> **** \n 2. porn -> p*rn \n 3. porn -> p**n')

test = input ("Unesite broj: ")
number = int(test)

if number == 1:
  dictonary = {}
  with open('dictonary.txt', 'r') as reader:
   line = reader.readline()
   while line != '':
            words = line.split()
            dictonary[words[0]] = words[1]
            line = reader.readline()

   filename = 'test.txt'

   for k, v in dictonary.items():
       with fileinput.FileInput(filename, inplace=True) as file:
         for line in file:
             print(re.sub(r"\b%s\b" % k , v, line), end='')


if number==2:
       dictonary = {}
       with open('dictonary.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            words = line.split()
            dictonary[words[0]] = words[2]
            line = reader.readline()

        filename = 'test.txt' # fajl koji treba da cenzurišeš

        for k, v in dictonary.items():
           with fileinput.FileInput(filename, inplace=True) as file:
              for line in file:
               print(re.sub(r"\b%s\b" % k , v, line), end='')

if number==3:
          dictonary = {}
          with open('dictonary.txt', 'r') as reader:
            line = reader.readline()
            while line != '':
              words = line.split()
              dictonary[words[0]] = words[3]
              line = reader.readline()

            filename = 'test.txt' # fajl koji treba da cenzurišeš

            for k, v in dictonary.items():
             with fileinput.FileInput(filename, inplace=True) as file:
               for line in file:
                 print(re.sub(r"\b%s\b" % k , v, line), end='')

