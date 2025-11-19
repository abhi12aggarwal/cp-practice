#263A
def main():
    from sys import stdin,stdout
    for i in range(5):
        a=list(map(int,stdin.readline().split()))
        try:
            x=a.index(1)+1
            y=i+1
        except:
            g=''
    stdout.write(str(abs(x-3)+abs(y-3)))
if __name__=='__main__':
    main()