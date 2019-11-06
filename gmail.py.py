a = "Ali"
b = "Ali123"
username = input("Please enter username")
if (username==a) :
	print("Hello",username)
	password = input("please enter password")
	if (password==b) :
		print("you are logged in")
	else:
		print("incorrect password")
else:
	print("incorrect username")