# # how to put strings together (string concatenation)

# different ways to concatenate strings

# print("subscribe to " + youtuber + " on youtube")

# print("subscribe to {}".format(youtuber) + " on youtube")

# print(f"subscribe to {youtuber} on youtube") # f-string (formatted string literal)

youtuber = "Jason Cox" # some string variable

adj = input("Adjective: ")

verb1 = input("Verb: ")

verb2 = input("Verb: ")

noun1 = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because I love {verb1}. Stay hydrated and {verb2} like you are {noun1}!" 

print(madlib)