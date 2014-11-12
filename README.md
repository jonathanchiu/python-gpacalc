GPA Calculator
===============
A small GPA calculator coded in Python. Uses Northeastern University's grading system found [here](http://www.northeastern.edu/registrar/gradingsystem.html)

How to use
----------
Define an array of Course objects. A Course object represents a course taken in some arbitrary semester and can be initialized like so, where the first argument is the letter grade received (mapping of letter to number equivalent can be found in the code), the second argument is the number of credits for that course, and the third argument is the name of the course (which is an optional parameter):

```python
x = Course('A', 4, "Potato Theory")
y = Course('B', 4, "History of Swag")
z = Course('A-', 4, "Particle Physics")
fall2014 = [x,y,z]
```

The GPA is calculated by calling the defined 'gpa' function which takes in an array of courses:

```python
print gpa(fall2014)    # 3.5835
```

Hope to eventually make this more interactive and terminal driven instead of having to download the file and edit it manually..
