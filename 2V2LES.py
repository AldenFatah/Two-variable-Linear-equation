def solve(a,b,c,d,e,f,):
    Y = ((a*f)-(d*c))/((a*e)-(d*b))
    X = (c-(b*Y))/a
    return [X,Y]

print("===2V2LES===")
print("""1.aX + bY = c
2.dX + eY = f
""")

a = input('a:')
b = input('b:')
c = input('c:')
d = input('d:')
e = input('e:')
f = input('f:')
print()

if a/d == c/e:
    if a/d == c/f:
        print("infinite solutions exist") 
    else:
        print("no solution exist") 
else:
    print(solve(a,b,c,d,e,f)) 
