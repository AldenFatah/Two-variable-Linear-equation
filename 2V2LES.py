def solve(a,b,c,d,e,f,):
    Y = ((a*f)-(d*c))/((a*e)-(d*b))
    X = (c-(b*Y))/a
    return [X,Y]

print("===2V2LES===")
print("""1.aX + bY = c
2.dX + eY = f""")
