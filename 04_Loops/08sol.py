num = int(input("Enter a No. : "))
is_Prime = True

if num>1:
    for i in range(2, num):
        if num%i == 0:
            is_Prime = False

print(num,"is Prime:", is_Prime)