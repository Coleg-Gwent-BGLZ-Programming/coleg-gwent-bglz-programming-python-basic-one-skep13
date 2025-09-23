# Personal Data Manager
# -------------------------------------------------
# Reflection Questions & Answers:
# 1. Why might we use a set instead of a list for hobbies?
#    - A set automatically removes duplicates, so if the user
#      enters the same hobby more than once, it will only be stored once.
#
# 2. What are the benefits of using a dictionary to store user data?
#    - A dictionary allows us to organize related information (name, age, hobbies, years)
#      under clear keys, making the data easy to access and modify later.
#
# 3. How does tuple unpacking help us work with fixed data?
#    - A tuple is great for fixed values that shouldn’t change (e.g., birth year and current year).
#      Tuple unpacking lets us assign these values to variables in one step, improving readability.

def collect_user_data():
    # Collect user name and age
    name = input("Enter your name: ").strip()
    age = int(input("Enter your age: "))

    # Collect hobbies (use a set to ensure uniqueness)
    hobbies = set()
    print("Enter your hobbies one by one. Type 'done' to finish:")
    while True:
        hobby = input("Hobby: ").strip()
        if hobby.lower() == "done":
            break
        hobbies.add(hobby)

    # Tuple for fixed data: (birth year, current year)
    from datetime import datetime
    current_year = datetime.now().year
    birth_year = current_year - age
    fixed_data = (birth_year, current_year)

    # Store all user data in a dictionary
    user_data = {
        "name": name,
        "age": age,
        "hobbies": list(hobbies),  # convert set to list for storage
        "years": fixed_data
    }

    return user_data


def display_user_data(user_data):
    name = user_data["name"]
    age = user_data["age"]
    hobbies = ", ".join(user_data["hobbies"])
    birth_year, current_year = user_data["years"]

    print("\n--- Personal Data Summary ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Hobbies: {hobbies if hobbies else 'None'}")
    print(f"Birth Year: {birth_year}")
    print(f"Current Year: {current_year}")
    print("------------------------------")


# 🧩 Extension Challenge
def format_user_summary(user_data):
    """Return a formatted summary string for the user."""
    name = user_data["name"]
    age = user_data["age"]
    hobbies = ", ".join(user_data["hobbies"])
    birth_year, current_year = user_data["years"]

    return (
        f"{name} is {age} years old.\n"
        f"They enjoy: {hobbies if hobbies else 'No hobbies listed'}.\n"
        f"Born in {birth_year}, and the current year is {current_year}."
    )


# Main Program
if __name__ == "__main__":
    user_data = collect_user_data()
    display_user_data(user_data)

    # Optional: show formatted summary
    print("\n--- Formatted Summary ---")
    print(format_user_summary(user_data))
