from Utils import *

all_media = load_dataset()

while True:
    user_input = int(input(
        "Enter 1: show all media\n"
        "Enter 2: add media\n"
        "Enter 3: edit media\n"
        "Enter 4: delete media\n"
        "Enter 5: search media\n"
        "Enter 6: search by time\n"
        "Enter 7: download media\n"
        "Enter 8: exit\n"
    ))

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
        download_media()
    elif user_input == 8:
        exit_user(all_media)
        exit()
