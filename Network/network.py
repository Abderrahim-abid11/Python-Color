
light_with = "\033[1;37m"
light_red = "\033[1;31m"
light_green = "\033[1;32m"

status = int(input("Enter Status Network (ON = 1, OFF=0) : ")) 
if status == 0:
  print(light_red, end="")
  print("                 ●  ")
else:
  print(light_green, end="")
  print("            )))  ●  (((  ")
print(light_with, end="")

print("                ---      ")
print("               /   \     ")
print("              |  *  |    ")
print("              |  *  |    ")
print("              |  *  |    ")
print("              |  *  |    ")
print("            _/_______\_  ")
print("           |___________| ")





