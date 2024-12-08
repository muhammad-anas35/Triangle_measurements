def Area_of_Triangle():
  try:
    Base : int = int(input("Enter Base of Triangle : "))
    Height : int = int(input("Enter Height of Triangle : "))
  except ValueError:
    print("Invalid Input of Base or Height ")

  Area = 0.5 * Base * Height
  return print(f"Area of Triangle is {Area}")

def Perimeter_of_Triangle():
  try:
    side1 = int(input("Enter first side of triangle : "))
    side2 = int(input("Enter second side of triangle : "))
    side3 = int(input("Enter third side of triangle : "))
  except ValueError:
    print("Invalid Sides Input")

  try:
    result :int = side1+ side2 + side3
  except ValueError:
    print("Invalid Sides Input")
  return print(f"Perimeter of Triangle is {result}")


print("\U0001F496 Triangle Mathematics \U0001F496 ")
print("----------------------------\n")
print("Select one from Below ")
print("1: For Area of Triangle ")
print("2: For Perimeter of Triangle")
print("3: For Exit\n" )

def main():
    try:
      choice :int = int(input("Enter you Choice to Execute the Programme on Triangle : "))
    except ValueError:
      print("Invalid Selection Input")
    if choice == 1:
      Area_of_Triangle()
    elif choice == 2:
      Perimeter_of_Triangle()
    elif choice == 3:
      print("Ok the programe exited successfully.\n")
    else:
      print("Invalid Choice\n")

    print("I hope You enjoy \U0001F497")



if __name__ == '__main__':
  main()