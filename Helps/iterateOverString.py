"""
Program:
 Python Program to iterate strings char by char
"""
def Main():
   # string_to_iterate = "Data Science"
   # for char in string_to_iterate:
   #    print(char)

   # string_to_iterate = "Data Science"
   # for char_index in range(len(string_to_iterate)):
   #    print(string_to_iterate[char_index])
      
   string_to_iterate = "Python Data Science"
   for char in string_to_iterate[0 : 6 : 1]:
      print(char)
      
   # string_to_iterate = "Python_Data_Science"
   # for char in string_to_iterate[ :  : 2]:
   #    print(char)

   # string_to_iterate = "Machine Learning"
   # for char in string_to_iterate[ :  : -1]:
   #    print(char)

   # string_to_iterate = "Machine Learning"
   # char_index = len(string_to_iterate) - 1
   # while char_index >= 0:
   #    print(string_to_iterate[char_index])
   #    char_index -= 1

   # string_to_iterate = "Learn Python"
   # char_index = 1
   # while char_index <= len(string_to_iterate):
   #    print(string_to_iterate[-char_index])
   #    char_index += 1

if __name__ == "__main__":
    Main()