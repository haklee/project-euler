def f(n):
    if int(n**.5)**2==n:
        return 0
    s=str(int(n**.5))
    i = 1
    while len(s)<100:
        for j in range(1, 10):
            x = int(s+str(j))
            if x**2 > n*10**(2*i):
                j-=1
                break
        s+=str(j)
        i+=1
    return sum(int(c) for c in s)
            
print(sum(f(i)for i in range(1,101)))