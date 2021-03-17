def func1(num):
    if num==1: # 1이 될 때까지 이므로 ==1을 사용
        return 1

    elif num>1:
        if num %2==0:
            current = num/2
            return func1(current)
        elif num%2==1:
            current = num*3+1
            return func1(current)

def func1_2(num):
    if num==1:
        return 1
    
    if num%2 ==1:
        return (func1_2(int(num*3+1)))
    else:
        return (func1_2(int(num/2)))

def func2(num):
    if num==1:
        return 1
    
    elif num==2:
        return 2
    
    elif num==3:
        return 4
    
    else:
        return func2(num-1)+func2(num-2)+func2(num-3)
        


def main():
    print(func1(20))
    print(func1_2(10))
    print(func2(13))
if __name__ == "__main__":
    main()

