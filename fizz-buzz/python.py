# # VERSION 1 (162/162)
# for i in range(1, 101):
#  if i % 3 == 0:
#   print("Fizz", end="")
#  if i % 5 == 0:
#   print("Buzz", end="")
#  if i % 3 != 0 and i % 5 != 0:
#   print(i, end="")
#  print()

# # VERSION 2 (113/113)
# for i in range(1, 101):
#  print("FizzBuzz" if not i % 15 else "Fizz" if not i % 3 else "Buzz" if not i % 5 else i)

# # VERSION 3 (74/74)
# for i in range(1,101):print(((i,a:="Fizz"),(b:="Buzz",a+b))[i%5<1][i%3<1])

# VERSION 4 (73/73)
i=1
while i<101:print(((i,a:="Fizz"),(b:="Buzz",a+b))[i%5<1][i%3<1]);i+=1



