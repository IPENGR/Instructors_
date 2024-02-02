"""
Python String Formatting:::-

String format()
The format() method allows you to format selected parts of a string.

Sometimes there are parts of a text that you do not control, maybe they come from a database, or user input?

To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method:

"""

x="my name is {name},and age is {age}".format(name="saleem",age=23)
print(x)
new_string="python is a {language} language".format(language="interpreted")
print(new_string)

count="there are toatal {} alphabets in english"
print(count.format("26"))
names=["sal","bot","goat","lvelup"]
read_books=["novels","adventures","tutorss","actions cpics"]
for i in range(len(names)):
   # print("the person names mentioned : ",names[i],"read the books",read_books[i])
    print("books read by {1},are {1}".format(names[i],read_books[i]))
    