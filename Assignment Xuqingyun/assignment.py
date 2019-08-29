def menu():
    print("Menu:")
    print("L - List places")
    print("A - Add new place")
    print("M - Mark a place as visited")
    print("Q - Quit")
    choice=str(input("Enter to continue:"))
    if choice=="l":
        place=open("list.csv","r+")
        place_list = place.readlines()
        n=0
        for i in place_list:
            n=n+1
            if 'v' in i:
                print(str(n)+".*{0:>10}  in  {1:>10} priority {2:>3}".format(i.split(',')[0],i.split(',')[1],i.split(',')[2]))
            else:
                print(str(n)+".{0:>9}  in  {1:>9} priority {2:>3}".format(i.split(',')[0], i.split(',')[1], i.split(',')[2]))
        place.close()
        menu()
    elif choice=="a":
        list_out=[]
        output_file=open("list.csv","a")
        name=str(input("enter your name:"))
        list_out.append(name)
        while name=="":
            name = str(input("can not be blank,enter your name:"))
            list_out.append(name)
        country=str(input("enter the country:"))
        list_out.append(country)
        while country=="":
            country = str(input("can not be blank,enter the country:"))
            list_out.append(country)
        priority=str(input("enter a number:"))
        if priority.isdigit():
            list_out.append(priority)
        else:
            print("should be digit")
            priority = str(input("enter a number:"))
        while "-"in priority:
            priority = str(input("invalid,enter a new number:"))
            list_out.append(priority)
        list_out.append("n")
        a=","
        print(a.join(list_out),file=output_file)
        output_file.write('/n')
        output_file.close
        print("{0:>10}  in  {1:>10} (priority {2:>3}) added to travel tracker ".format(list_out[0],list_out[1],list_out[2]))
        memu()
    elif choice=="m":
        place_choice=input("enter a number of place to mark as visited:")
        while place_choice:
            if place_choice.isdigit():
                break
            else:
                place_choice = input("invalid:")
        print("valid number")
        place = open("list.csv", "r+")
        place_list = place.readlines()
        n = 0

        for i in place_list:
            n = n + 1
            while n == int(place_choice):
                print("place found")
                if 'v' in i:
                    print("this place has already been visited")
                    place.close()
                    menu()
                elif 'n' in i:

                    output_file=open("list.csv","r+")

                    output_file.write(i.replace("n","v"))
                    output_file.close
                    print("marked successfully")
                    menu()
    elif choice=="q":
        import sys
        sys.exit()
    else:
        print("invalid")
        menu()






print("Travel Tracker 1.0 - by Xu Qingyun")
print("3 places loaded from places.csv")

menu()