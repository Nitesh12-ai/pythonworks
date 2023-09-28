email = input("En")
k,j,d = 0,0,0
if len(email)>= 6:
    if email[0].isalpha():
        if("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j =1
                    elif i.isdigit():
                        continue
                    elif i =="_" or i == "." or i == "@":
                        continue
                    else:
                        d =1
                if k == 1 or j == 1 or d == 1 :
                    print("It's not a valid E-mail -- result5")
                else:
                    print("Yeah, You have entered the right E -mail ! ")
            else:
                print("It's not a valid E- mail -- result4")
        else:
            print("It's not a valid E- mail --result3")
    else:
        print("It's not a valid E-mail -- result 2 ")
else:
    print("It's not a valid Email -- result 1 ")

    