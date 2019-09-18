sp = 0
op = 0
while sp < 40 or op < 40:
    i = raw_input("who wins the match")
    if i == 's':
        if sp == 30:
            sp = sp + 10
            print(sp,":",op)
        elif sp < 30:
            sp = sp + 15
            print(sp,":",op)
        else:
            break
    else:
        if op == 30:
            op = op + 10
            print(sp,":",op)
        elif op < 30:
            op = op + 15
            print(sp,":",op)
        else:
            break
if sp == op:
    ts = 0
    to = 0
    print ("match tie")
    while ts <= 20 or to <= 20:
        i = raw_input("who wins the match")
        if i == 's':
            ts = ts + 10
            if to > 0:
                to = 0
            if ts == 20:
                break
        else:
            to = to + 10
            if ts > 0:
                ts = 0
            if to == 20:
                break

    if ts == 20:
        print "server wins the match"
    else:
        print "operent wins the match"
elif sp > op:
    print("server wins")

else:
    print("op wins")