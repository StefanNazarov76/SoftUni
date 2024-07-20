pen_packages = int(input())
marker_packages = int(input())
litres_detergent = int(input())
percent_discount = int(input())

total_pens_price = pen_packages * 5.8
total_markers_price = marker_packages * 7.2
total_detergent_price = litres_detergent * 1.2
total_price_without_discount = total_pens_price + total_markers_price + total_detergent_price
discount = total_price_without_discount * (percent_discount / 100)
final_price = total_price_without_discount - discount

print(final_price)
