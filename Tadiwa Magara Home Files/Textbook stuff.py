PI = 3.14
A = 34
B = 0
B = B + 1

#print(PI, A, B,)

YourName = 'Tadiwa'
Number1 = 567

#print("Hello", YourName, ".Your number is", Number1)
#print("Hello")


print("Hello {0}. Your number is {1}".format(YourName,Number1))
#C = int(input("Prompt: "))
#C = False
#if C < 0:
    #print("Negative")
#elif C == 0:
   # print("Zero")
#else:
   # print("Positive")
#print(C)


#repeat = ''
#while repeat != 1:

#if grade != 'A' or "B" or "C" or "D" or "E" or "F":
    #grade = str(input("Input Your Grade from A-E, Again: "))

#grade = ''
#while grade != "A" or "B" or"C" or"D" or "E" or"F":
   # grade = input("Input Your Grade from A-E: ")

grade = str(input("Input Your Grade from A-E: "))
if grade != ("A", "B", "C", "D", "E", "F"):
    
if grade == "A":
    print("Top Grade!")
elif grade == "F" or grade == "U":
    print("Fail")
elif grade in ("B","C","D","E"):
    print("Pass")
else:
    grade = str(input("Input Your Grade from A-E, Again: "))


