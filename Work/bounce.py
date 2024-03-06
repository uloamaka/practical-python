# bounce.py
#
# Exercise 1.5
height = 100
bum_bounce = 3/5
times_of_bounce = 0

while times_of_bounce  < 10:
  times_of_bounce = times_of_bounce  + 1
  height =  height * bum_bounce
  print(round(height, 4))


