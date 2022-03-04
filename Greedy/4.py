#4
#1이 될때까지(처음_2022.03.04 Morning)
n, k = map(int, input().split())


count = 0
while True:
    
    while n%k == 0:
        n = n//k
        count += 1
        if n == 1:
         break
    
    if n == 1:
        break
    n -= 1
    count += 1
    

print(count)

#4
#1이 될때까지(2번_2022.03.04 Night)

n, k =map(int, input().split())

count = 0

while True:

    if n%k == 0 : 
        n = n//k
        count += 1
        if n == 1:
            break


    else:
        n -= 1
        count += 1
        if n == 1:
            break

print(count)

