from Utils import *

all_media = load_dataset()

while True:
    user_input = int(input(
        "Enter 1: show all media\nEnter 2: add media\nEnter 3: edit media\nEnter 4: delete media\nEnter 5: search media\nEnter 6: search by time\nEnter 7: exit\n"))

    if user_input == 1:
        show_all_media(all_media)
    elif user_input == 2:
        all_media = add_media(all_media)
    elif user_input == 3:
        all_media = edit_media(all_media)
    elif user_input == 4:
        all_media = delete_media(all_media)
    elif user_input == 5:
        search_media(all_media)
    elif user_input == 6:
        search_media_by_time(all_media)
    elif user_input == 7:
        exit_user(all_media)
        exit()
