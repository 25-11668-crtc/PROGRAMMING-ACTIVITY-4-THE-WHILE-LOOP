correct_pin ="1234"
attempts = 0
max_attempts = 3
access_granted = False

while attempts<max_attempts:
	pin = input("PIN: ")
	if pin == correct_pin:
		print("access granted")
		access_granted = True
		break
	else:
		attempts +=1

if not access_granted:
	print("card blocked")