import shutil

size = shutil.get_terminal_size()
seps = "-" * size.columns

def writing_skills():
    is_using = True
    while is_using == True:
        print(seps)
        action = input("What do you want to use? [N]otice writing. Press [ENTER] to exit. ").strip().lower()
        if action == "n":
            print(seps)
            import notice_writing
            notice_writing.notice()
            print(seps)
        elif not action:
            print(seps)
            is_using = False
        else:
            print("An error occured !! ")
writing_skills()