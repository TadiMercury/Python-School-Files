
def varFunc(name,*args):
        print("This is the first argument "+str(name))
        #This print will make you understand that the args is a list
        print(args)
        for item in args:
                print(item)

print("First time:")
varFunc("of 1st function call",2, 3, 4, 5)

print("Second time:")
varFunc("of 2nd function call","asd","Bcd")

print("Third time:")
varFunc("and only argument of 3rd function call")
