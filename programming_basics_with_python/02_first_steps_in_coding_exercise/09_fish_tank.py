length = int(input())
width = int(input())
height = int(input())
percent_accessories = float(input())

volume_centimeters = length * width * height
volume_litres = volume_centimeters / 1000
accessories = volume_litres * (percent_accessories / 100)
total_litres = volume_litres - accessories

print(total_litres)
