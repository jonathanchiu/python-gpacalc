class Course:
  """Contains information regarding a course

  Parameters:

  grade   -- String representing letter grade received
  credits -- Integer representing number of credits course has
  name    -- String representing the name of the course (optional)
  """
  def __init__(self, grade, credits, name = "N/A"):
    self.grade   = letter_to_num[grade]
    self.letter  = grade
    self.credits = credits
    self.name    = name

  def __str__(self):
    """Return a string representing this course

    self -- A Course object
    """
    return (self.letter + "," + str(self.credits) + "," + self.name)

letter_to_num = {
  'A' : 4.000,
  'A-': 3.667,
  'B+': 3.333,
  'B' : 3.000,
  'B-': 2.667,
  'C+': 2.333,
  'C' : 2.000,
  'C-': 1.667,
  'D+': 1.333,
  'D' : 1.000,
  'D-': 0.667,
  'F' : 0.000
}

fall2014 = [
  Course('A', 4, "Potato Theory"),
  Course('B', 4, "History of Swag"),
  Course('A-', 4, "Particle Physics"),
  Course('A-', 4, "History of Chinese Culture")
]

def gpa(semester):
  """Given a list of Course objects, calculate the gpa for that semester

  semester -- A list of Course objects representing courses taken in a semester
  """
  total_qpt = 0
  total_credits = 0

  for course in semester:
    qpt           = course.grade * course.credits
    total_qpt     += qpt
    total_credits += course.credits

  gpa = total_qpt / total_credits
  return gpa
