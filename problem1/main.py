# input
student_score = 80

# Process: Your Solution Code Here
if 80 <= student_score <= 100:
  print('Nilai A')
elif 65 <= student_score <=79:
  print('Nilai B+')
elif 50 <= student_score <= 64:
  print('Nilai B')
elif 35 <= student_score <= 49:
  print('Nilai C')
elif 0 <= student_score <= 34:
  print('Nilai D')
else:
  print('error')


# Output "Nilai A"