'''
Optiver problems

An ant leaves its anthill in order to forage for food. It moves
with the speed of 10cm per second, but it doesn't know where to go,
therefore every second it moves randomly 10cm directly north, south,
east or west with equal probability.
'''

'''
3.Can you write a program that comes up with an estimate of average
time to find food for any closed boundary around the anthill? What
would be the answer if food is located outside an defined by
( (x – 2.5cm) / 30cm )2 + ( (y – 2.5cm) / 40cm )2 < 1 in coordinate
system where the anthill is located at (x = 0cm, y = 0cm)?
Provide us with a solution rounded to the nearest integer.

NB: This food distribution is an oval centered on [2.5, 2.5] (in cm)
'''

import random as rand
import matplotlib.pyplot as plt

def direction_coordinate_changer(a, b): # b = [x, y] format
    # 1 = North
    # 2 = East
    # 3 = South
    # 4 = West
    if a == 1:
        b[1] += 10

    elif a == 2:
        b[0] += 10

    elif a == 3:
        b[1] -= 10

    else:
        b[0] -= 10


def food_distribution(x, y):
    ans = ((x - 2.5)/30)**2 + ((y - 2.5)/40)**2
    return ans

coordinates_within_food = []
#We must work out points that are inside the oval
for i in range(-50, 50, 1): #Loop over x coordinate
    for j in range(-50, 50, 1): #Loop over y coordinate
        if food_distribution(i,j) < 1:
            coordinates_within_food.append([i,j])


#We find 3760 points within the food oval

#Repeat ant journey many times
time_for_each_journey = []

number_of_ant_journeys = 1000000

for i in range(number_of_ant_journeys):
    #Loop over which ant moves
    ant_coordinates = [0,0] #Start at 0
    time = 0

    while ant_coordinates in coordinates_within_food:
        #While loop checks that ant has not reached the food
        #This while loop is what varies between questions
        random_direction = rand.randint(1,4)

        direction_coordinate_changer(random_direction, ant_coordinates)
        time += 1

    time_for_each_journey.append(time)

average_time = sum(time_for_each_journey) / number_of_ant_journeys
print(average_time) #FINAL ANSWER

#Plotting a histogram of the ant journeys
# plt.hist(time_for_each_journey, density=False, bins=100)
# plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
# plt.xlabel('Journey time [seconds]', fontsize = 16)
# plt.xlim(1, 30)
# plt.ylabel('Number of journeys', fontsize = 16)
# plt.savefig('Optiver_Q3_Ant_journey_timings_histogram.png', format = 'png', dpi = 600)
# plt.show()
