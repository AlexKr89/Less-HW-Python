import interface
import func


def user_response():
    flag = True
    while flag:
        action = interface.menu()
        if action == 1:
            func.add_contact(interface.get_contact())
        elif action == 2:
            func.search_contact()
        elif action == 3:
            func.print_contacts()
        elif action == 4:
            func.delete_contact(interface.get_delete_contact())
        elif action == 5:
            func.change_contact
        else:
            flag = False


user_response()