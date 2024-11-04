f =  open("/Users/christopherhart/workspace/github.com/chart5766/bookbot/books/frankenstein.txt")


dict_letters = {}


# def count_words(f):
#    text_read = f.read()
#    text_split = (text_read.split())
#    wc =  (len(text_split))
#    print(wc)


def countLetters(f):
   
   text = f.read().lower()
   
   for letter in text:
      if letter in dict_letters:
         dict_letters[letter] += 1
      else:
         dict_letters[letter] = 1
         
   print(dict_letters)
      


         
   

countLetters(f)
      

         

      


   
   
   
   
 

   
         

      


      
   
      
    