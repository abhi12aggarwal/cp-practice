#266B
def main():
    from sys import stdin,stdout
    n,x=map(int,stdin.readline().split())
    s=stdin.readline().strip()
    for _ in range(x):
        s=s.replace('BG','GB')
    stdout.write(s)
if __name__=='__main__':
    main()