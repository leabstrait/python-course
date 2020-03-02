num = 0
print('\t\t\t*ENTER A NUMBER TO CHECK WHETHER IT IS PRIME OR NOT*\t\t\t_____(ENTER 1 TO EXIT)_____ \n')
while num != 1:
    num = int(input())
    if num == 1:
        break
    else:
        count = 0
        for i in range(1,num):
            if num % i == 0:
                count = count + 1
                
        if count == 1 :
            print('*PRIME*_*PRIME*_*PRIME*_*PRIME*_*PRIME*_*PRIME*_*PRIME*_*PRIME*_*PRIME*_*PRIME*_*PRIME*_*PRIME* _____(ENTER 1 TO EXIT)_____\n')
        else:
            print('*NOT PRIME*_*NOT PRIME*_*NOT PRIME*_*NOT PRIME*_*NOT PRIME*_*NOT PRIME*_*NOT PRIME*_*NOT PRIME* _____(ENTER 1 TO EXIT)_____\n')
    
