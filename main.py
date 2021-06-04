def do_stuff(num):
	try:
		if num:
			return int(num) + 5
		else:
			return 'Please Enter Number'

	except ValueError as err:
		return err