film_name = input()

student_tickets_count = 0
standard_tickets_count = 0
kids_tickets_count = 0
total_tickets_count = 0

while film_name != 'Finish':
    capacity = int(input())
    ticket_type = input()

    current_tickets_count = 0

    while ticket_type != 'End':
        current_tickets_count += 1
        total_tickets_count += 1

        if ticket_type == 'student':
            student_tickets_count += 1
        elif ticket_type == 'standard':
            standard_tickets_count += 1
        elif ticket_type == 'kid':
            kids_tickets_count += 1
        if current_tickets_count == capacity:
            break

        ticket_type = input()

    current_capacity_percentage = (current_tickets_count / capacity) * 100
    print(f'{film_name} - {current_capacity_percentage:.2f}% full.')

    film_name = input()

student_tickets_percentage = (student_tickets_count / total_tickets_count) * 100
standard_tickets_percentage = (standard_tickets_count / total_tickets_count) * 100
kids_percentage = (kids_tickets_count / total_tickets_count) * 100

print(f'Total tickets: {total_tickets_count}')
print(f'{student_tickets_percentage:.2f}% student tickets.')
print(f'{standard_tickets_percentage:.2f}% standard tickets.')
print(f'{kids_percentage:.2f}% kids tickets.')
