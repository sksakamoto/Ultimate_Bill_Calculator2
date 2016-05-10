"""This program will determine how much to pay when dining out."""

def prompt_user():
	"""This function will prompt the user for information."""
	global bill_without_tip
	bill_without_tip = float(raw_input("How much is the bill not including tip? "))
	global dine_alone
	dine_alone = raw_input("Did you dine alone? Y or N ")
	done = None

	if (dine_alone == 'Y'):
		done = True
	else: done = False
	if not done:
		global number_of_people
		number_of_people = int(raw_input("How many people were at dinner? "))
	else: None

	global eighteen_percent_tip
	eighteen_percent_tip = raw_input("Is 18% tip okay? Y or N ")
	if (eighteen_percent_tip == 'Y'):
		done = True
	else: done = False
	if not done:
		global tip_amount
		tip_amount = float(raw_input("How much do you want to leave for tip? "))
	else: tip_amount = 0.18

def calculate_bill():
	global total_bill
	global bill_per_person
# Why can I define the global variables before defining them here?
	if (dine_alone == 'N' and eighteen_percent_tip == 'Y'):
		total_bill = bill_without_tip * 1.18
		bill_per_person = total_bill / number_of_people
	elif (dine_alone == 'N' and eighteen_percent_tip == 'N'):
		total_bill = bill_without_tip + (bill_without_tip * tip_amount)
		bill_per_person = total_bill / number_of_people
	elif (dine_alone == 'Y' and eighteen_percent_tip == 'N'):
		total_bill = bill_without_tip + (bill_without_tip * tip_amount)
	else: total_bill = bill_without_tip * 1.18

def display_bill_amounts(bill_without_tip = 1, tip_amount = 0.1, total_bill = 1.1, bill_per_person = 1.1):
#Parameters passed in always picked over optional parameters?
	print "Original bill amount is", bill_without_tip
	print "Tip amount (percent) is", (tip_amount * 100)
	print "Total bill is", total_bill
	if (dine_alone == 'N'):
		print "Each person pays", bill_per_person
	else: None

def main():
	prompt_user()
	calculate_bill()
	display_bill_amounts()

if __name__ == '__main__':
	main()
