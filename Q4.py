#Q4.1
i=0
while(i<11):
    print(i)
    i=i+1

password=12345
e_pass=int(input("Enter your password:"))

while(e_pass!=password):
    e_pass=int(input("Enter right password:"))
print("Successfull!")

num=123

print(str(num)[::-1])