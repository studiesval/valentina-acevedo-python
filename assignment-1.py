#Section 1

favorite_movie = "Donnie Darko"
release_year = 2001
imdb_rating = 8.0
is_top_pick = True

print(favorite_movie, type(favorite_movie))
print(release_year, type(release_year))
print(imdb_rating, type(imdb_rating))
print(is_top_pick, type(is_top_pick))

#Section 2

name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

age = 2026 - birth_year

print(f"Hi, {name}! You are approximately {age} years old.")

#Section 3

n_1 = float(input("Give me a number "))
n_2 = float(input("Give me another one! "))

print(f"{n_1} x {n_2} = {n_1 * n_2}")

#Section 4

print("================")
print("    RECEIPT")
print("================")
item_name = "VHS tape"
price = 20
quantity = 4

total = price * quantity
print(f"Item:     {item_name}")
print(f"Price:    ${price:.2f}")
print(f"Quantity: {quantity}")
print("----------------")

print(f"Total: ${total:.2f}")
print("================")

#Section 5

username = input("Whats your name? ")
hometown = input("What is your hometown? ")
favorite_hobby = input("What is your favorite_hobby? ")
fun_fact = input("Tell us one fun fact about you! ")
user_birth_year = int(input("What year were you born? "))

age = 2026 - user_birth_year

print("==============================")
print(f"PROFILE: {username}")
print("==============================")
print(f"Hometown: {hometown}")
print(f"Hobby: {favorite_hobby}")
print(f"Fun fact: {fun_fact}")
print(f"Age: {age}")
