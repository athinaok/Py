year = input("Check if year is a leap year:")


if year.isdigit():

    year = int(year)

    if (year%4 == 0) and ((year%100 != 0) or (year % 400 == 0)):
        print ("The Year ", year," is a leap year.")
    else:
        print ("The Year ", year," is not a leap year.")
else:
    print("Sorry, you did not enter a year!")