import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_names = ['chicago', 'new york city', 'washington']
months_names = ['all','january', 'february', 'march', 'april', 'may', 'june']
days_names =['all','saturday', 'sunday','monday','tuesday','wednesday','thursday','friday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Type the city you want from these cities",city_names,": ", end = "")
    city = input().lower()
    while city not in city_names:
        print("Incorect!, please type a city name from choices", city_names,": ", end = "")
        city = input().lower()
    print("Great! you choose to get your information from '{}'".format(city))
    
    # TO DO: get user input for month (all, january, february, ... , june)
    print("Type the month name you want or type all to choice all months",months_names[1:],": ",end = "")
    month = input().lower()
    while month not in months_names:
            print("Incorect!, please type a month name from choices",months_names[1:]," or type all for all months:",end = "")
            month = input().lower()
    print("Great! you choose to get your information in {} month(s)".format(month))
            
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    print("Type the day name you want ",days_names[1:]," or type all to choice all days:", end = "")
    day = input().lower()
    while day not in days_names:
            print("Incorect!, please type a day name from choices",days_names," or type all to choice all days:", end="")
            day = input().lower()
    print("Great! you choose to get your information on {} day(s)".format(day))
            
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load the choosen file
    file_name = CITY_DATA[city]
    df = pd.read_csv(file_name)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
     # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months_names.index(month)

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # convert Start Time column to datetime 
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    #display the most commn month
    
    print("the most commn month:", months_names[(df['month'].mode()[0])])

    # TO DO: display the most common day of week
    print("the most common day of week:", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("the most common start hour:", df['Start Time'].dt.hour.mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most commonly used start station:", df['Start Station'].mode()[0],end = '\n')

    # TO DO: display most commonly used end station
    print("the most commonly used end station:", df['End Station'].mode()[0],end = '\n')

    # TO DO: display most frequent combination of start station and end station trip
    # add new column From To 
    df['From To'] = "From "+df['Start Station']+" To "+df['End Station']
    print("most frequent combination of start station and end station trip:", df['From To'].mode()[0], end = '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*4)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time", str(datetime.timedelta(seconds= int(df['Trip Duration'].sum()))), end = '\n')

    # TO DO: display mean travel time
    print("mean travel time",str(datetime.timedelta(seconds = int(df['Trip Duration'].mean()))), end = '\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts of user types:\n")
    print(df['User Type'].value_counts())
    print()
    # TO DO: Display counts of gender
    # Gender column not exists in all cities data 
    #check if the gender column is in the df
    print('Genders:')
    if 'Gender' in df:
        print("counts of gender:\n")
        print(df['Gender'].value_counts(), end = '\n')
    else:
        print("These data don't have a gender column\n")
    print()
    
    # TO DO: Display earliest, most recent, and most common year of birth
    # the birth_year column not exists in all cities data
    #chech if the year column exists in the df
    
    print('Birth Year:')
    if 'Birth Year' in df:
        print("Earliest birth year:", int(df['Birth Year'].min()), end = '\n')
        print("Most recent birth year:", int(df['Birth Year'].max()), end = '\n')
        print("Most common year of birth:", int(df['Birth Year'].mode()[0]), end = '\n')
        
    else:
        print("These data don't have birth year column ")
    print()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_raw_data(df):
    """ Your docstring here """
    i = 0
    n = 5 # set the number of raws to show 
    # TO DO: convert the user input to lower case using lower() function
    raw = input("Do you want to see the first 5 rows of data? 'yes' or 'no': ").lower()
    
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i : i+n]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("Do you want to see the next 5 rows? 'yes' or 'no': ").lower() # TO DO: convert the user input to lower case using lower() function
            i += n
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no': ").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        display_raw_data(df)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
