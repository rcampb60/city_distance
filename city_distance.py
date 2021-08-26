'''
A script which asks the user for their unit preference then determines the distance between Tallinn and Helsinki
'''

from geopy import distance

def cities():

    print("This program will determine the distance between Tallinn and Helsinki")
    unit = input("Please select your unit of measurement: Miles or Kilometres: ")

    tallinn = (59.4370, 24.7536) # the long and lat for each city
    helsinki = (60.1699, 24.9384)

    if unit.lower() == 'miles' or unit.lower() == 'm': # checks whether user has selected miles or kilometeres
        # uses geopy's distance method to find the distance in miles between two tuples of co-ordinates, and round to set it to
        # two decimal place precision
        print("You have selected Miles")
        print(f"The distance between Tallinn and Helsinki is {round(distance.distance(tallinn, helsinki).miles,2)} miles") 
    else:
        # same as above but for kilometres
        print("You have selected Kilometres")
        print(f"The distance between Tallinn and Helsinki is {round(distance.distance(tallinn,helsinki).km,2)} km")


cities()