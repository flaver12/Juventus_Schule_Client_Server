def same_name(name, name_to_compare):
	if name == name_to_compare:
		return True
	return False

if same_name("Flavio", "Flavio"):
	print("Works")
else:
	print("Nope")

if not same_name("Flavio", "flavio"):
	print("Works")
else:
	print("Nope")



