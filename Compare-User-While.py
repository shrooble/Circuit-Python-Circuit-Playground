# Assignments:
# 8.1.2.4.n


def main():
  y = True
  while y:
    try:
      user = int(input("Enter a number between 0-9: "))
      if user > 9: 
        continue
    except ValueError:
      continue
    else:
      x = 0
      print("Starting While Loop - Comparing User and Count Variable")
      while x != 10:
        print(x)
        x += 1
        if x == user:
          print("The User variable is equal to the count variable: ", x)
          print("user = ", user)
          print("x = ", x)
      print("Ending While Loop")
      y = False
main()
