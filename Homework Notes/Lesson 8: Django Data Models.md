- Dr. Chuck makes a statement about the learning curve for SQL. What exactly does he say?  
  - "You can learn the first 60% of SQL in about three hours, the last 40% is a lifetime."

- In your own words, how would you define Object-relational mapping (ORM)? How will we use it in Django and what specifically will it do?  
  -   A programming technique that allows for databases to be interacted with, using classes and objects in a general programming language. In Django, the ORM will be used to define Python classes as models that represent database tables and perform CRUD operations using Python, rather than writing the SQL itself. A class represents a table in a database, while an object is an entry/row in that database.

- What does Dr. Chuck say are the advantages of the ORM? What disadvantages (if any) does it have?    
  - An ORM can be used to complete around "80%" of operations one would do to a database. Additional benefits are portability (different SQL services), simplicity, and automatic handling of migrations and table schema generation. However, Chuck mentions that more complex concepts tend not to be done with an ORM. 

- Dr. Chucks says that most (he mentions a percentage) of the things you want to do with SQL can be done effectively with an ORM. What exactly does he say?    
  - "80% of the most common things you would do with a database are easily done with an ORM."

- What is the name of the file in which the ORM data objects are defined?  
  - models.py

- In the example of an ORM object:
  - class User(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128).  
    Dr. Chuck draws a line to models.Model and mentions what that is. What does he say? Of which OOP feature is this an example?   
  - We are extending models.Model using class inheritance. We are inheriting many lines of code which are already written for us.

- What two commands do you need to run to go from an ORM to deployment in a database? 
  - python3 manage.py makemigrations, python3 manage.py migrate

- What does running python3 manage.py shell do? Be specific!    
  - Creates a python shell with Django functionality, while also utilizing databases in the django application.

- In the example session Dr. Chuck talks about, he creates a new user named Kristen with email address kf@umich.edu. Where is this user created when:  
u = User(name='Kristen', email='kf@umich.edu')  
is run? What command needs to be used to add this new user to the database?  
  - It is stored in the u variable. u.save() must be run to add this user to the database.