from math import floor

world_record = float(input())
distance = float(input())
seconds_per_meter = float(input())

time_without_delay = distance * seconds_per_meter
delay = floor(distance / 15) * 12.5
final_time = time_without_delay + delay

if final_time < world_record:
    print(f'Yes, he succeeded! The new world record is {final_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {final_time - world_record:.2f} seconds slower.')
