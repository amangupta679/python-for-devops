num_1 = 10 
num_2 = 5

sum = num_1 + num_2
print(sum)

# input type 
num_1 = int(input("enter a number :")) 
num_2 = int(input("enter another number :"))

choice  = input("enter the operation + - / *")
if choice == "+":
    sum = num_1 + num_2
    print("the sum is " , sum)

elif choice == "-":
    diff = num_1 - num_2
    print("the difference is " , diff)

elif choice == "*":
    mul  = num_1 * num_2 
    print("the multiplication of two is " , mul)
else:
    print("invalid cloice")
