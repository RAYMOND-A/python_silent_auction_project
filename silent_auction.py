
from art import display_art

# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "loop": "The action of doing something over and over again"
# }

# # retrieving items in a directionary
# print(programming_dictionary['Bug'])

# # Adding new items to directionary
# programming_dictionary[123] = "one hundred and twenty three."

# print(programming_dictionary)

# # Create an empty directionary
# empty_dictionary = {}

# # edit an item in a directionary
# programming_dictionary['Bug'] = 'a different definition of a bug'
# print(programming_dictionary)

# # loop through a directionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])

# # wipe an existing directionary
# programming_dictionary = {}
# print(programming_dictionary)

# Grading program exercise

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {

}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80: 
        student_grades[student] = "Exceeds Expectations"
    elif score > 70 :
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting dictionary in a dictionary

travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visit": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visit": 23
    },
}

# Nestting a dictionary in a list

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visit": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visit": 23
    },
]

def add_new_country(country_name, total_visit, cities_visited):
    travel_log.append({"country" : country_name, "cities_visited": cities_visited, "total_visit": total_visit})

## alternatively

# def add_new_country1(country_visited, times_visited, cities_visited):
#     new_country = {}
#     new_country["country"] = country_visited
#     new_country["visits"] = times_visited
#     new_country["cities"] = cities_visited
#     travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Auction program

print(display_art)

print("Welcome to Silent Auction Program")

bids = {

}

bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Ray": 123, "jame": 432}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?")
    bid_prize = int(input("What is your bid prize? $"))
    bids[name] = bid_prize
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        print("clear screen")