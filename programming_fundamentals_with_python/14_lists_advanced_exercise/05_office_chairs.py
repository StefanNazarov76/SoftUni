def check_room(number_of_rooms):
    free_chairs = 0

    for number_of_current_room in range(1, number_of_rooms + 1):
        chairs_in_current_room, visitors = input().split()
        chairs_in_current_room = len(chairs_in_current_room)
        visitors = int(visitors)

        diff = chairs_in_current_room - visitors

        if chairs_in_current_room < visitors:
            print(f'{abs(diff)} more chairs needed in room {number_of_current_room}')

        free_chairs += diff

    return free_chairs


rooms = int(input())

total_free_chairs = check_room(rooms)

if total_free_chairs >= 0:
    print(f'Game On, {total_free_chairs} free chairs left')
