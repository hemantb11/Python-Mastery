# Import random module (used for generating random numbers and selections)
import random as r

# Generate random integer between 1000 and 9999
print(r.randint(1000,9999))

# Generate random float between 0 and 1
print(r.random())

# Generate random number with step (1 to 10, skip 2 numbers)
print(r.randrange(1,10,2))

# List of colors
x=["red","black","blue","pink"]

# Pick one random element from list
print(r.choice(x))

# Pick multiple random elements from list (k=2 means 2 items)
print(r.choices(x,k=2))

# Shuffle list elements randomly
r.shuffle(x)
print(x)


# Import datetime module (used for date and time operations)
import datetime

# Get current date and time
d=datetime.datetime.now()
print(d)

# Extract time from current datetime
print(d.time())

# Extract day from date
print(d.day)

# Extract month from date
print(d.month)

# Extract year from date
print(d.year)

# Get today's date only
today_date=datetime.date.today()
print(today_date)

# Add 5 days to current date
after=today_date+datetime.timedelta(days=5)
print(after)

# Create date object for birth date (DOB)
dob=datetime.date(2006,2,11)

# Current date
cd=datetime.date.today()

# Difference between dates (age in days)
print(cd-dob)

# Difference between years (approx age)
print(cd.year-dob.year)


# Take input for first user
user1=input("enter ur name: ")
year1=int(input("enter birth year: "))
mon1=int(input("enter birth mon: "))
date1=int(input("enter birth date: "))

# Create DOB object for user1
dob1=datetime.date(year1,mon1,date1)

# Take input for second user
user2=input("enter ur name: ")
year2=int(input("enter birth year: "))
mon2=int(input("enter birth mon: "))
date2=int(input("enter birth date: "))

# Create DOB object for user2
dob2=datetime.date(year2,mon2,date2)

# Compare both birth dates
# Whoever is earlier (older) is greater in age
if dob1>dob2:
    print("greater is: ",user2)

elif dob2>dob1:
    print("greater is: ",user1)

else:
    print("both are equal")