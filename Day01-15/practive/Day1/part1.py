def water_fall():
    for num in range(100, 1000):
        low =num%10
        mid = num//10%10
        high = num//100
        if num == low ** 3 + mid ** 3 + high ** 3:
            print(num)
def fevoqi():
    n=0
    num1=1
    num2 =1
    while n <= 20:
        n+=1
        if n<= 2:
            print(1)
        else:
            num1,num2 = num2,num1+num2
            print(num2)
def feboqi2():
    n= int(input('请输入一个整数：'))
    num1,num2 = 1,1
    for i in range(1,n+1):
        if i<=2:
            print(1)
        else:
            num1,num2 = num2,num1+num2
            print(num2)
def gcd (x,y):
    if x > y:
        x,y = y,x
    for factor in range(x,0,-1):
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x,y):
    return x*y // gcd(x,y)
if __name__  == '__main__':
    # water_fall()
    feboqi2()


