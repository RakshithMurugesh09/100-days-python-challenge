# Improved username generator + simple profile display
name = input("Enter Name: ").strip()
age = input("Enter your Age: ").strip()
location = input("Enter your location: ").strip()

# Validate age
if not age.isdigit():
    print("Invalid age. Please enter numbers only.")
else:
    name_title = name.title()     # Title Case for display
    first_name = name_title.split()[0] if name_title else ""
    # first 3 letters of first name (or whole first name if shorter) + age, lowercase
    username_prefix = first_name[:3].lower() if len(first_name) >= 1 else "user"
    username = username_prefix + age

    print("\n==== USER PROFILE ====")
    print(f"Name: {name_title}")
    print(f"Age: {age}")
    print(f"Location: {location.title()}")
    print(f"Username: {username}")
    print("======================")
