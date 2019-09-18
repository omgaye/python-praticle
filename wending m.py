t = 0
while t < 125:
    print"------------------------------------------"
    i = input("plz enter money for soda \n")

    
    if i == 25:
        t = t+i
        if t >= 125:
            a = t-125
            print"------------------------------------------"
            print "plz collect your soda with rs",a
            print"------------------------------------------\n"
        else:
            ad = 125-t
            print"------------------------------------------"
            print"Sorry!!!!!!!!! you need to pay",ad
            print"------------------------------------------\n"
            
    elif i == 100:
        t = t+i
        if t >= 125:
            a = t-125
            print"------------------------------------------"
            print "plz collect your soda with rs",a
            print"------------------------------------------\n"
        else:
            ad = 125-t
            print"------------------------------------------"
            print"Sorry!!!!!!!!! you need to pay",ad
            print"------------------------------------------\n"

    else:
        print ("plz give money in multiples of 25 or 100 \n")
