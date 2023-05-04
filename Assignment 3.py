# Program to calculate the number of digits and letters in a string

text=input()
alpha,numeric=0,0
for i in text:
    if(i.isalpha()):
        alpha+=1
    elif(i.isdigit()):
        numeric+=1
print("Characters = ",alpha)
print("Digits = ",numeric)
