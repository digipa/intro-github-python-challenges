# ===== DON'T TOUCH THIS CODE =====
import random
import time
from faker import Faker
fake = Faker()
# ==================================
#import dice roll function below:
import dice_rolling_simulator as ds


def start():

	# initialize empty dictionary "details"
	details = {}

	# prompt user for name
	name = input("Enter name: ")
	print("Hi " + name + "!")


	# generate new name
	newname = fake.name()
	details['name'] = newname


	# roll dice for number of children
	input("Roll dice for number of kids. (press enter to roll): ")
	dice = ds.roll_dice()
	print("You rolled a {}!".format(dice))

	details['children'] = []
	for x in range(dice):
		child = fake.first_name()
		details['children'].append(child)


	# ask user if they want a job, generate job title and company
	jobChoice = input("Do you want a job? (y/n): ")
	If jobChoice.lower()[0] == 'y':
		job = fake.job()
		company = fake.company

		details['job'] = job
		details['company'] = company

		print("Your new job is {} at {}".format(job, company))
	else:
		details['job'] = "stay at home"

	# Ask user for preferred location.
	# If they roll the right number, they get to live there.
	# If they don't, a location will be generated for them
	location = input("Where do you want to live?: ")
	target = ds.roll_dice()
	input("You must roll a {} to live in {}".format(target,location))

	roll = ds.roll_dice()
	if roll == target:
		details['location'] = location
	else:
		details['location'] = fake.state()

		print("You will live in" + details['location'])




	# pick a car for the user from a list of options




	def list_details(dict):
		for key,value in dict.items():
			print("{}: {}".format(key,value))

	time.sleep(2)
	print()
	print()
	print()
	print("DETAILS:")
	print("=========")
	list_details(details)





if __name__ == "__main__":
	start()
