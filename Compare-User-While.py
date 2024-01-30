# Assignments:
# 8.1.2.4.n


def main():
  y = True
  while y:
    try:
      user = int(input("Enter a number between 0-9: "))
    except ValueError:
      print("Error")
      continue
    else:
      if user > 9 or user < 0: 
        continue
      x = 0
      print("Starting While Loop - Comparing User and Count Variable")
      while x != 10:
        print(x)
        if x == user:
          print("The User variable is equal to the count variable: ", x)
          print("user = ", user)
          print("x = ", x)
        x += 1
      print("Ending While Loop")
      y = False
main()
