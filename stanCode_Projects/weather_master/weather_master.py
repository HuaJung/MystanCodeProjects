"""
File: weather_master.py
Name: HJ
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
QUIT = -100


def main():
	"""
	This program print the highest, lowest, and average temperature
	by computing the users inputs.
	"""
	print("standCode \"Weather Master 4.0")
	data = int(input('Next Temperature: (or '+str(QUIT)+' to quit)? '))
	if data == QUIT:
		# filter the first input is QUIT
		print('No temperatures were entered.')
	else:
		high_temp = data
		low_temp = data
		total_temp = data
		days = 1
		cold_days = 0
		if data < 16:
			# whether the first input is below 16 degree
			cold_days += 1
		while True:
			data = int(input('Next Temperature: (or ' + str(QUIT) + ' to quit)? '))
			if data == QUIT:
				# leave the loop if QUIT number is entered
				break
			if data > high_temp:
				high_temp = data
			if data < low_temp:
				low_temp = data
			if data < 16:
				cold_days += 1
			total_temp += data
			days += 1
		print('Highest temperature = '+str(high_temp))
		print('Lowest temperature = '+str(low_temp))
		print('Average = '+str(total_temp/days))
		print(str(cold_days)+' cold day(s)')








###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
