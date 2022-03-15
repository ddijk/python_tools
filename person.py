class Student:
  marks = 88
  name = 'Sheeran'

  def __init__(self, city):
    self.city=city

person = Student('vleuten')
person2 = Student('utrecht')

name = getattr(person, 'name')
print(name)

city = getattr(person,'city')
print(f'city {city}')
city2 = getattr(person2,'city')
print(f'city {city2}')

marks = getattr(person, 'marks')
print(marks)

# Output: Sheeran
#         88
