
# 전자매장에는부품이N개있다. 
# 각부품은정수형태의고유한번호가있다. 
# 어느날손님이M개종류의부품을대량으로구매하겠다며당일날견적서를요청했다. 
# 손님이문의한M개종류를모두확인해서견적서를작성해야한다. 
# 이때가게안에부품이모두있는지를확인하는프로그램을작성해보자. 

# •첫째줄에정수N 이주어진다
# •둘째줄에는공백으로구분하여N개의정수가주어진다
# •셋째줄에정수M이주어진다
# •넷째줄에는공백으로구분하여M개의정수가주어진다.
# 공백으로구분하여각부품이존재하면yes를없으면no를출력한다.

# ALGORITHM HOMEWORK입력예시
# 5
# 83792
# 3
# 579
# 출력예시
# no yes yes

def select():
   
    arr = []; brr = []
    
    N = int(input()); arr = list(map(int, input().split())) 
    
    M = int(input()); brr = list(map(int,input().split())) 

    for j in range(M): print('yes',end=" ") if (brr[j] in arr) else print('no',end = " ")



select()



















