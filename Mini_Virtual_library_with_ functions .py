Library_data_base = {"THE MAGIC POT": ["ry44564t",True],"THE REEL WORRIOR":["tr55tr",True],"THE PRINCE OF THE DAY":["fjfj",True]}
personal_data = {}
p_info = []
def Display_Library():
    print(Library_data_base)

def Lendbook():
    p_info = []
    B_name = input("Please enter the book name :  ").strip().upper()
    if len(personal_data) >= 3:
        print("Sorry! You have exeeded the limit. You can't more books untill you return any")
    elif Library_data_base[B_name][1]:
        choice = input("Hey! We found that books. Please press S if you want to take the book: ").strip().upper()
        if choice == "S":
            B_code = input("Enter the code of the book : ")
            p_info.append(input("Enter today's Date  : "))
            p_info.append("Taken")
            print(p_info)
            personal_data[B_name] = p_info
            print("Please check your qwn book bank\n {}".format(personal_data))
            Library_data_base[B_name][1] = False
    else:
        print("Sorry, We dont have that book now.")
    

def Donation():
    mini_library = {}
    info_list = []
    B_name = []
    B_name = input("Thanks for Your greate contribution.\n Please enter the book name:  ").strip().upper()
    x = generate_code()
    info_list.append(x)
    print(info_list)
    info_list.append(True)
    mini_library[B_name] = info_list
    Library_data_base.update(mini_library)
    print(Library_data_base)

def generate_code():
    h_list = []
    h_list.append(input("Enter First two digits of your phone number:  ").strip())
    h_list.append(input("Enter First two digits of your phone number:  ").strip())
    h_list.append(input("Enter any of your fav two alphabets ; ").strip())
    print(h_list)
    val = "".join(h_list)
    print(val)
    return val
    

def returning():
    B_name = input("Enter the name of book :  ").strip().upper()
    B_code = input("Enter the code of book :  ").strip()
    print(Library_data_base[B_name][0])
    if Library_data_base[B_name][0]== B_code:
        Library_data_base[B_name][1] = True
        personal_data[B_name][1] = "Given"
        print(personal_data) 
    
while True:
    print("1. Display book \n2. Lend book \n3. Donate \n4. Return books")
    ch = input("Enter your choice  :  ").strip()
    if ch == "1":
        Display_Library()
    elif ch == "2":
        Lendbook()
    elif ch == "3":
        Donation()
    elif ch == "4":
        returning()
    else:
        print("Invalid choice")

    

                 
            
     