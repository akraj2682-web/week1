# This program collects basic information from the user
# and displays a friendly welcome message.

# Ask the user for their name using input()
name = str(input("What is your name? "))

# Ask the user for their age
age = int(input("How old are you? "))

# Ask the user about their hobby
hobby = str(input("What is your favorite hobby? "))

# Print a blank line to make the output look cleaner
print()

# Display a friendly welcome message using f-strings
print(f"Hello {name}! 👋 Welcome!")

# Display the user's age
print(f"It's great to know that you are {age} years old.")

# Display the user's hobby
print(f"{hobby} sounds like a really fun hobby!")

# Final friendly message
print(f"We are happy to have you here, {name}. Enjoy your day! 😊")