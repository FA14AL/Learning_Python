import random
from art import logo, vs
from game_data import data

def format_data(account):
    account_name = account["name"]
    account_des = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_des}, from {account_country}"

def check_answer(guess,a_follower_count,b_follower_count):
    if a_follower_count > b_follower_count:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

while should_continue:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #compare the answer of the random choices
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n"*20)
    print(logo)

    a_follower = account_a["follower_count"]
    b_follower = account_b["follower_count"]

    is_correct = check_answer(user_guess, a_follower, b_follower)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else :
        print(f"Sorry, that's wrong. Final score: {score}.")
        should_continue = False
