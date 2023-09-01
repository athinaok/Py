temperature = int(input("Please insert the current temperature: "))
rain = True
wind = False


if temperature > 20:
    print("It's warm")
    if rain:
        print("Warm & raining: summer in Athens")
        if wind:
            print ("It's warm, it rains and it's windy")
        else:
            print("Warn, raining , no wind at all")
    else:
        print("Warm and dry, beatiful!")
        if wind:
            print ("Warm, Dry and Windy: Good Weather for sailing")
        else:
            print("Warn, dry, windless: Just lie in the sun")
else:
    print("If it's cold, i dont't care about rain and wind")