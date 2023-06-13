while(True):
    n = input()
    rn = list(n)
    rn.reverse()
    s = "".join(rn)

    if n == '0':
        break;
    elif n == s:
        print("yes")
    else:
        print("no")