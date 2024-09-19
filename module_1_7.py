grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)
result = {}
for student in students_list:
  scores = grades[students_list.index(student)]
  total_score = sum(scores)
  count = len(scores)
  average_score = total_score / count
  result[student] = average_score
print(result)