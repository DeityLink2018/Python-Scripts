from class_test import Target

tList = input("List of Ips seperated by space\n---> ").split(" ")
tObj = [Target(tgt) for tgt in tList]
graph = "Target\n"

for obj in tObj:
        graph += Target.print_format(obj.ip)
bool = True
while bool:
    print(f"""
Test Menu!

{graph}

1) Noice
2) Cool
3) bye

""")
    choose = int(input("Selection: "))
    if choose == 1:
        print("Noice")
    elif choose == 2:
        print("cool")
    elif choose == 3:
        print("bye")
        bool = False
    else:
        print("Invalid choice")
        input("Press ENTER to continue")
        
