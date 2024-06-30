#Question 2

#Task 2

#Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. 
# Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. 
# For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.

import random

#List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Tired", "Excited"]

#List of days

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#times of day

times_of_day = ["morning", "afternoon", "evening"]

#loop for each day and inside of that loop is a nested loop for the times of the day and random mood

for day in days_of_week:
    for time in  times_of_day:
        mood = random.choice(moods)
        print(f"On {day} {time}, you were feeling {mood}.")
        