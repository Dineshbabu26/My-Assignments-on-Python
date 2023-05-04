# Match program using Months
print("Match program using Months")
month=int(input("Enter the number "))
match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")


# Print the Series
print("SERIES OF NUMBERS")
n=int(input("Enter Digit:"))
s,c=1,1
while s!=n+1:
    print(c)
    c+=s
    s+=1

#Bitwise operator
print("Bitwise ")
a=int(input())
b=int(input())
print("a&b: ",a&b)
print("a|b: ", a|b)
print("~a: ", ~a)
print("a^b: ", a ^ b)

# MANGO TREE
print("MANGO TREE")

row = int(input())
column = int(input())
number = int(input())

if (number % column == 2 or number % column == column - 2 + 1) and number > (row-1)*column:
    print("It is a mango tree")
else:
    print("It is not a mango tree")


