def serach(list,n):
    for i in list:
        if i == n:
            return True
    else:
        return False

list = [1,2,3,4,5,6,7,8,9]
n = int(input('enter the number you want to serach in list '))
if serach(list,n):
    print('found')
else:
    print('not found')