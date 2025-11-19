#69A
def main():
    from sys import stdin,stdout
    a,b,c=0,0,0
    for _ in range(int(stdin.readline())):
        x,y,z=map(int,stdin.readline().split())
        a+=x
        b+=y
        c+=z
    if a or b or c:
        stdout.write('NO')
    else:
        stdout.write('YES')
if __name__=='__main__':
    main()