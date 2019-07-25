Students = []
ans = True
while ans:
	print("""
************************************************
		1. Add a Student
		2. Delete a Student
		3. Update a Student
		4. Look Up Student Record
		5. Exit
		""")

	ans = input ("What would you like to do? ")
	if ans =="1":
		add = str (input ("Enter Student Name. "))
		Students.append(add)
		print ("Added " + add + " to Students")
		print (Students)
	elif ans=="2":
		print (Students)
		dele = int (input ("Enter index number on Student to remove: "))
		print ("Would you like to delete? " + Students[dele])
		gg = True
		while gg:
			wp = str (input("Yes or No?"))
			if wp == "Yes":
				print ("Successfully deleted " + Students[dele])
				Students.gg[dele]
				print ("These are the Students: ")
				print (Students)
				gg = None
			elif wp == "No":
				print ("Cancelled")
				gg = None
			else:
				print ("Not a valid Answer")
	elif ans == "3":
		print (Students)
		up = int (input ("Enter index number on Student to Update: "))
		print (Students[up] + " is selected")
		upd = str (input ("What would you like to change it to? "))
		Students[up] = upd
		print ("Successfully Updated")
		print (Students)
	elif ans == "4":
		print ("These are your Students: ")
		print (Students)
	elif ans == "5":
		print ("Goodbye")
		ans = None
	else:
		print ("Not a valid choice")

			
