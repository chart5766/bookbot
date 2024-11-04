# print (/Users/christopherhart/workspace/github.com/chart5766/bookbot/books/frankenstein.txt)

# f =  open("/Users/christopherhart/workspace/github.com/chart5766/bookbot/books/frankenstein.txt")
# dict_letters = {}
# character_list = []

# def count_words(f):
#    text_read = f.read()
#    text_split = (text_read.split())
#    wc =  (len(text_split))
#    print(wc)


# def countLetters():
   
#    with open("/Users/christopherhart/workspace/github.com/chart5766/bookbot/books/frankenstein.txt") as f:
#       text_read = f.read()
#       text_split = text_read.split()

#       for words in text_split:
#          for word in words.split():

#           print(words)
         
f =  open("/Users/christopherhart/workspace/github.com/chart5766/bookbot/books/frankenstein.txt")
dict_letters = {}

def count_words(f):
   text_read = f.read()
   text_split = (text_read.split())
   wc =  (len(text_split))
   print(wc)


def countLetters(f):
   text_read = f.read()
   text_split = (text_read.split())
   
   for words in text_split:
      lowered_string = words.lower()
      
      for letter in lowered_string:
         print(letter)
         
   

countLetters(f)
      

         

      


   
   
   
   
 

   
         

      


      
   
      
    