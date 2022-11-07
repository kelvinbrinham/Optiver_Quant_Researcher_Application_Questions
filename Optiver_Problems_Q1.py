'''
Optiver problems

An ant leaves its anthill in order to forage for food. It moves
with the speed of 10cm per second, but it doesn't know where to go,
therefore every second it moves randomly 10cm directly north, south,
east or west with equal probability.
'''

'''
1. If the food is located on east-west lines 20cm to the north
and 20cm to the south, as well as on north-south lines 20cm to
the east and 20cm to the west from the anthill, how long will it
take the ant to reach it on average?
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


#Repeat ant journey many times
time_for_each_journey = []

number_of_ant_journeys = 10000000

for i in range(number_of_ant_journeys):
    #Loop over which ant moves
    ant_coordinates = [0,0] #Start at 0
    time = 0

    while abs(ant_coordinates[0]) < 20 and abs(ant_coordinates[1]) < 20:
        #While loop checks that ant has not reached the food
        #This while loop is what varies between questions
        random_direction = rand.randint(1,4)

        direction_coordinate_changer(random_direction, ant_coordinates)

        time += 1

    time_for_each_journey.append(time)

average_time = sum(time_for_each_journey) / number_of_ant_journeys
print(average_time) #FINAL ANSWER

#Plotting a histogram of the ant journeys
plt.hist(time_for_each_journey, density=False, bins=100)
plt.ticklabel_format(axis="y", style="sci", scilimits=(0,0))
plt.xlabel('Journey time [seconds]', fontsize = 16)
plt.xlim(1, 30)
plt.ylabel('Number of journeys', fontsize = 16)
plt.savefig('Optiver_Q1_Ant_journey_timings_histogram.png', format = 'png', dpi = 600)
plt.show()
