from funcsi import register, login
from todo_funk import see_task, add_task, up_date_task, delete

while True:
    k = int(input('Exit/Sing up/Sing in(0/1/2): '))
    user_reg = -1

    if k == 0:
        break

    elif k == 1:
        users_reg = register()
    elif k == 2:
        users_reg = login()

    while user_reg != -1:
        print("Exit/Task/Create new/Up date task/Delete(0/1/2/3/4): ")
        option = int(input("option: "))
        if option == 0:
            break
        elif option == 1:
            see_task(user_reg)
        elif option == 2:
            add_task(user_reg)
        elif option == 3:
            up_date_task(user_reg)
        elif option == 4:
            delete(user_reg)