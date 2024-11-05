# f =  open("/Users/christopherhart/workspace/github.com/chart5766/bookbot/books/frankenstein.txt")
f = open("/Users/christopherhart/workspace/bootdev/bookbot/books/frankenstein.txt")

dict_letters = {}


def count_words(f):
   text_read = f.read()
   text_split = (text_read.split())
   wc =  (len(text_split))
   return wc


def countLetters(f):
   
   text = f.read().lower()
   
   for letter in text:
      if letter in dict_letters:
         dict_letters[letter] += 1
      else:
         dict_letters[letter] = 1
         
   return dict_letters
      






def sortKey():

   view = countLetters(f).items()

   view_sorted = sorted(view, key = lambda x: x[1])

   for letter, num in view_sorted:
      if str.isalpha(letter):

         print(f"The {letter} character was found {num} times")

      else:
         pass


   


         
   
sortKey()

         

      


   
   
   
   
 

   
         

      


      
   
      
    