#Question 1

#Task 1

# Write a program that prints off different moods for each day of the week. 
# Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". 
# Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it. 
# Ensure that your program includes the use of the random module to select the mood.

import random

moods = ['Happy', 'Sad', 'Energetic', 'Calm']

#days of week

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#for loop random choice solution

for day in days_of_week:
    mood = random.choice(moods)
    print(f"On {day}, you were feeling {mood}")