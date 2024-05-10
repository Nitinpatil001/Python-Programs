#input day in number and print day in word
d=int(input("enter day in number"))
if d==1:
    print("sunday")
else:
    if d==2:
        print("monday")
    else:
        if d==3:
            print("tuesday")
        else:
            if d==4:
                print("wednesday")
            else:
                if d==5:
                    print("thursday")
                else:
                    if d==6:
                        print("friday")
                    else:
                        if d==7:
                            print("saturday")
                        else:
                            print("wrong day")
