people=int(input("how many people you wants to invite to the party: "))
def invitepeople():
    if people < 10:
        for i in range(people):
            name = input(f"Enter the name of peoples : ")
            print(f"{name} has been invited.")
    else:
        print("Too many people")
invitepeople()