Italy_points = 0
Hawaii_points = 0
Japan_points = 0
Spain_points = 0

answer = input("How long would you want to be on a flight, A 9 hours, B 6 hours, C 11 hours, or D 7 hours? ")
if answer == "A"or answer == "a":
	Italy_points += 1
elif answer == "B" or answer == "b":
	Hawaii_points += 1
elif answer == "C" or answer == "c":
	Japan_points += 1
elif answer == "D" or answer == "d":
	Spain_points += 1
else: 
	print("Answer only with A, B, C, or D")
	
answer = input("What food would you most want on your trip, A Pizza, B Empanada, C Poke, or D Sushi? ")
if answer == "A"or answer == "a":
	Italy_points += 1
elif answer == "B" or answer == "b":
	Spain_points += 1
elif answer == "C" or answer == "c":
	Hawaii_points += 1
elif answer == "D" or answer == "d":
	Japan_points += 1
else:
	print("Answer only with A,B,C,or D")

answer = input("What kind of scenery would you want to be surrounded by, A koi ponds and cherry blossoms, B Palm trees and beaches, C rustic villas and rolling hills, or D plazas and colorful buildings? ")
if answer == "A"or answer == "a":
	Japan_points += 1
elif answer == "B" or answer == "b":
	Hawaii_points += 1
elif answer == "C" or answer == "c":
	Italy_points += 1
elif answer == "D" or answer == "d":
	Spain_points += 1
else:
	print("Answer only with A,B,C,or D")

answer = input("How would you want to relax on your trip, A Laying in a hammock by the ocean, B A picnic in the countryside, C Snoozing on a terrace enjoying the view of beautiful buildings, or D Sipping tea in a garden? ")
if answer == "A"or answer == "a":
	Hawaii_points += 1
elif answer == "B" or answer == "b":
	Italy_points += 1
elif answer == "C" or answer == "c":
	Spain_points += 1
elif answer == "D" or answer == "d":
	Japan_points += 1
else:
	print("Answer only with A,B,C,or D")

answer = input("What kind of activities excite you most on trips, A exploring ancient castles, B wandering the city and going on a food tour, C Surfing and snorkeling, or D Countryside bike ride and cooking class? ")
if answer == "A"or answer == "a":
	Spain_points += 1
elif answer == "B" or answer == "b":
	Japan_points += 1
elif answer == "C" or answer == "c":
	Hawaii_points += 1
elif answer == "D" or answer == "d":
	Italy_points += 1
else:
	print("Answer only with A,B,C,or D")
	
if Spain_points > Japan_points and Spain_points > Hawaii_points and Spain_points > Italy_points:
	print("You should visit Spain!")
elif Japan_points > Spain_points and Japan_points > Hawaii_points and Japan_points > Italy_points:
	print("You should visit Japan!")
elif Hawaii_points > Spain_points and Hawaii_points > Japan_points and Hawaii_points > Italy_points:
	print("You should visit Hawaii!")
elif Italy_points > Spain_points and Italy_points > Hawaii_points and Italy_points > Hawaii_points:
	print("You should visit Italy!")
else:
	print("Looks like you would have fun visiting Hawaii, Japan, Spain, or Italy!")