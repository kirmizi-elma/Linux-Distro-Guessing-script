import time

print("Do you like tinkering ?")


print("A: No, i just want it to work.")

print("B: Meh, maybe a bit of tinkering")

print("C: Sure, i would like to Compile my whole kernel")

print("D: Absolutely, i'd like to compile my whole ENTIRE operating system from scratch")


var = input("Enter a choice between A and D: ")

print("Thank you for your answer, you will get an answer shortly.")
time.sleep(5)

if var == "A":
    print("You are Ubuntu or Debian")
    
elif var == "B":
    print("You are most likely Fedora!")

elif var == "C":
    print("You are an Arch user")

elif var == "D":
    print("You are a gentoo user (basically mentally insane)")
    
else: 
    print("No answer received")