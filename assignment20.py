#1. Set the variable test1 to the string 'This is a test of the emergency text system,' and save test1 to a file named test.txt.
#ans:-
test1 = 'This is a test of the emergency text system,'
file = open('test.txt','w')
file.write(test1)
file.close()

#2. Read the contents of the file test.txt into the variable test2. Is there a difference between test 1 and test 2?
#ans:-
file2 = open('test.txt','r')
test2 = file2.read()
print(test2)

#3. Create a CSV file called books.csv by using these lines:
#title,author,year
#The Weirdstone of Brisingamen,Alan Garner,1960
#Perdido Street Station,China Miéville,2000
#Thud!,Terry Pratchett,2005
#The Spellman Files,Lisa Lutz,2007
#Small Gods,Terry Pratchett,1992

#ans:-

obj = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992'''

with open('books.csv','w') as file:
    file.write(obj)

#4. Use the sqlite3 module to create a SQLite database called books.db, and a table called books with these fields: title (text), author (text), and year (integer).
#ans:-

import sqlite3
db = sqlite3.connect('books.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE books (title text, author text, year int)")
db.commit()
db.close()

#5. Read books.csv and insert its data into the book table.
#ans:-
import sqlite3
import csv
conn = sqlite3.connect("books.db")
cursor = conn.cursor()
with open("books.csv","r") as file:
    books = csv.DictReader(file)
    for book in books:
        cursor.execute("INSERT INTO books VALUES (?,?,?)",(book['title'],book['author'],book['year']))
conn.commit()
conn.close()

#6. Select and print the title column from the book table in alphabetical order.
#ans:-

import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
ouput = cursor.execute("SELECT * FROM books ORDER BY year")
for record in ouput:
    print(record)


#7. From the book table, select and print all columns in the order of publication.
#ans:-

import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()
ouput = cursor.execute("SELECT * FROM books ORDER BY year")
for record in ouput:
    print(record)

#8. Use the sqlalchemy module to connect to the sqlite3 database books.db that you just made in exercise 6.
#ans:-
import sqlalchemy
conn = sqlalchemy.create_engine('sqlite:///books.db')
conn

#9. Install the Redis server and the Python redis library (pip install redis) on your computer. Create a Redis hash called test with the fields count (1) and name ('Fester Bestertester'). Print all the fields for test.
#ans:-
#pip install redis
import redis
conn = redis.Redis()
conn.delete('test')
conn.hmset('test', {'count': 1, 'name': 'Fester Bestertester'})
conn.hgetall('test')

#10. Increment the count field of test and print it.
#ans:-

conn.hincrby('test','count', 3)