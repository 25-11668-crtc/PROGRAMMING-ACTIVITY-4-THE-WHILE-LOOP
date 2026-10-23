num_items = 0
total = 0.0

price = float(input("Price (0 to stop): "))
while price != 0:
	total += price
	num_items += 1
	price = float(input("Price (0 to stop): "))

if num_items > 0:
	average = total / num_items
else:
	average = 0.0

print(f"items: {num_items} total: {total:.2f}")
print(f"average: {average:.2f}")
	