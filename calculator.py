a=input('what type of calculation you want N for normal and S for scientific>')
if a=='N':
    b=int(input('enter number'))
    c=int(input('enter number'))
    d=input('what operation you want to do, enter +,-,*,%>')
    if d=='+':
        sum=b+c
        print(sum)
    elif d=='-':
        minus= b-c
        print(minus)
    elif d=='*':
        multi=b*c
        print(multi)
    elif d=='%':
        div=b/c
        print(div)
elif a=='S':
    g=input('operations f for factorial, r for root,p for exponential>')
    e=int(input('enter number>'))
    if g=='f':
        fec=1
        for i in range (1,e+1):
            fec=fec*i
        print('your ans',fec)
    elif g=='r':
        h=input('enter type of root, r for square root,q for cubic root>')
        if h=='r':
            j=e**0.5
            print(j)
        elif h=='q':
            k=e**0.33
            print(k)
    elif g=='p':
        l=input('enter the exponential power,s for square,qa for quarder,t for cubic')
        if l=='s':
            m=e**2
            print(m)
        elif l=='t':
            n=e**3
            print(n)
        elif l=='qa':
            o=e**4
            print(o)
        else:
            print('enter small power')