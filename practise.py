def check_pal(n,rev_n):
    if int(n)==int(rev_n):
        return True
    else:
        return False

n=input()

rev_n=n[::-1]


check_pal(n,rev_n)





