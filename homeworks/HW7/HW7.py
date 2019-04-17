# CSCI 1133, Lab Section 013, HW7 Jeffery Liu

#==========================================
# Problem 1
#==========================================
# Class Name: StopWatch
# Purpose: Using the functions from the time module, this class simulates a
#   stopwatch that is able to set start and set end and then display the time
#   elapsed in seconds as well as display current local time in HH:MM:SS format
#   and get the start and stop times.
# Preconditions: Can use time() and localtime() functions of time module
#==========================================
#==========================================
# Name: __init__()
# Purpose: This is the constructor function for StopWatch instances. It creates
#   a StopWatch object with instance variables _start and _end set to the
#   current time in seconds since the epoch.
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): None
#============================================
# Name: get_start()
# Purpose: This function returns the start time stored in the _start instance
#   variable.
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): self._start - start time
#============================================
# Name: get_end()
# Purpose: This function returns the end time stored in the _end instance
#   variable.
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): self._end - end time
#============================================
# Name: current_time()
# Purpose: This function returns the current local time in the HH:MM:SS format.
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): a string that contains the current local time, 'HH:MM:SS'
#============================================
# Name: set_start()
# Purpose: This function sets the start time stored in the _start instance to
#   the current time.
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): None
#============================================
# Name: set_end()
# Purpose: This function sets the end time stored in the _end instance to
#   the current time.
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): None
#============================================
# Name: elapsed_time()
# Purpose: This function returns the elapsed time between the start and stop
#   time, which can be set with set_start() and set_end()
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): a float representing the amount of seconds elapsed between
#   the start and stop time.
#============================================


import time

class StopWatch:

    def __init__(self):
        self._start = time.time()
        self._end = time.time()

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def current_time(self):

        tm = time.localtime()
        return '{0:02}:{1:02}:{2:02}'.format(tm.tm_hour, tm.tm_min, tm.tm_sec)

    def set_start(self):
        self._start = time.time()
 
    def set_end(self):
        self._end = time.time()

    def elapsed_time(self):
        return self._end - self._start



# ===================TESTS========================
import random

if __name__ == '__main__':
    # StopWatch object instance
    stopwatch = StopWatch()

    # print current time
    print(stopwatch.current_time())


    # sort time for 30000 random integers from 0 to 10000
    randomlist = [random.randint(0, 10000) for n in range(30000)]
        
    
    stopwatch.set_start() # start time
    randomlist.sort() # sort
    stopwatch.set_end() # stop time

    # print elapsed time
    print(stopwatch.elapsed_time())

    # print current time again
    print(stopwatch.current_time())
    
    # sort time for 50000 random integers from 0 to 10000
    randomlist = [random.randint(0, 10000) for n in range(50000)]
    
    stopwatch.set_start()
    randomlist.sort()
    stopwatch.set_end()

    print(stopwatch.elapsed_time())

    # print current time again
    print(stopwatch.current_time())


#==========================================
# Problem 2
#==========================================
# Class Name: VideoGame
# Purpose: This class creates objects to represent video games, with information
#   about the game's title, esrb, and ratings.
#==========================================
#==========================================
# Name: __init__()
# Purpose: This is the constructor function for VideoGame instances. Given input
#   parameters for title, esrb, and the amount of each rating (1-5), it creates
#   a VideoGame object with instance variables title, esrb, and ratings.
# Precondition: The ratings must be stored as a list, with position 0 as the
#   number of 1 ratings, position 1 as number of 2 ratings, etc.
# Input Parameter(s): self - object self reference
#   title - a string containing the title of the game
#   esrb - a string containing the esrb rating of the game
#   ratings - a list containing the number of each rating (1-5).
#       Defaults to [0, 0, 0, 0, 0].
# Return Value(s): None
#============================================
# Name: set_title()
# Purpose: Given a new game title as input, this function resets the title stored in
#   the title instance variable to the new game title.
# Precondition: None
# Input Parameter(s): self - object self reference
#   title - a string containing the new title of the game
# Return Value(s): None
#============================================
# Name: set_esrb()
# Purpose: Given a new esrb as input, this function resets the esrb stored in
#   the esrb instance variable to the new game esrb.
# Precondition: None
# Input Parameter(s): self - object self reference
#   esrb - a string containing the esrb rating of the game
# Return Value(s): None
#============================================
# Name: get_title()
# Purpose: This function returns the title stored in the title instance variable.
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): self.title - a string containing the game title
#============================================
# Name: get_esrb()
# Purpose: This function returns the esrb stored in the esrb instance variable.
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): self.esrb - a string containing the esrb
#============================================
# Name: get_average()
# Purpose: This function returns the average rating rounded to the nearest integer
#   as calculated from the list of ratings stored in the ratings instance variable.
# Precondition: ratings must be in a list.
# Input Parameter(s): self - object self reference
# Return Value(s): an integer reprenting the average rating
#============================================
# Name: __str__()
# Purpose: This function overloads the special __str__() function so that when
#   when it is called, for example by print(), it returns a string containing
#   the game's title, esrb and average rating in
#   'Title: {}, ESRB Rating: {}, Average Rating: {}' format
# Precondition: None
# Input Parameter(s): self - object self reference
# Return Value(s): a string containing
#   the game's title, esrb and average rating in
#   'Title: {}, ESRB Rating: {}, Average Rating: {}' format
#============================================


class VideoGame:

    def __init__(self, title, esrb, ratings = [0] * 5):
        self.title = title
        self.esrb = esrb
        self.ratings = ratings


    def set_title(self, title):
        self.title = title

    def set_esrb(self, esrb):
        self.esrb = esrb

    def get_title(self):
        return self.title

    def get_esrb(self):
        return self.esrb

    def get_average(self):
        return int(sum((i + 1) * self.ratings[i] for i in range(len(self.ratings))) / sum(self.ratings))

    def __str__(self):
        return 'Title: {}, ESRB Rating: {}, Average Rating: {}'.format(self.title, self.esrb, self.get_average())


# ===================TESTS========================
if __name__ == '__main__':
    # 3 VideoGame instance objects
    game1 = VideoGame('Octopath Traveler', 'T', [367, 33, 15, 15, 14])
    game2 = VideoGame('Pokémon Ultra Moon', 'E', [384, 57, 21, 14, 32])
    game3 = VideoGame('Super Mario Odyssey', 'E10+', [2208, 149, 58, 17, 57])

    # put in one list.
    gamelist = [game1, game2, game3]

    # loop through and print.
    for x in gamelist:
        print(x)

    # testing out setters for title, esrb; and getters for title, esrb, and average rating.
    gamelist[0].set_title('The Legend of Zelda: Breath of the Wild')
    
    gamelist[0].set_esrb('E10+')
    
    print(gamelist[0].get_title())
    
    print(gamelist[0].get_esrb())

    print(gamelist[2].get_average())
    


    
