# Remove the i'th value in the String
txt="Hello World"
res=txt[:3]+txt[4:]
print(res)

#Palindrome
txt1=input("Enter the string : ")
if(txt1 == txt1[::-1]):
    print("This is a Palindrome")
else:
    print("This is not a Palindrome")
    
