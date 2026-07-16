import json


def add_profile():
    try:
        while True:
            name = input("What is your name: ").strip().title()
            if name:
                break
            print("Name cannot be empty!")

        while True:
            age = int(input("What is your age: "))
            if age > 0:
                break
            print("Age must be greater than 0!")

        while True:
            city = input("What is your city: ").strip().title()
            if city:
                break
            print("City cannot be empty!")

        skills = []

        while True:
            no_of_skills = int(input("How many skills? "))
            if no_of_skills > 0:
                break
            print("Enter at least 1 skill!")

        for i in range(no_of_skills):
            while True:
                skill = input(f"Skill {i + 1}: ").strip().title()

                if not skill:
                    print("Skill cannot be empty!")
                    continue

                if skill in skills:
                    print("Duplicate skill! Please enter a different skill.")
                    continue

                skills.append(skill)
                break

        with open("data.json", "w") as file:
            json.dump(
                {
                    "name": name,
                    "age": age,
                    "city": city,
                    "skills": skills
                },
                file,
                indent=4
            )

        print("\n✅ Profile successfully added!")

    except ValueError:
        print("Age and number of skills must be numbers.")


def view_profile():
    try:
        with open("data.json", "r") as file:
            profile = json.load(file)

            if not profile:
                print("No profile found!")
                return

            print("========== USER PROFILE ==========\n")
            print("Name:", profile["name"])
            print("Age:", profile["age"])
            print("City:", profile["city"])
            print("")
            print("Skills:\n-----------")

            for skill in profile["skills"]:
                print("•", skill)
    except FileNotFoundError:
        print("No profile found!")

def update_city():
    try:
        with open("data.json", "r") as file:
            profile = json.load(file)
            if not profile:
                print("No profile found!")
                return
            while True:
                city = input("What is your new city: ").strip().title()
                if city:
                    break
                print("City cannot be empty!")

            profile["city"] = city

        with open("data.json", "w") as file:
            json.dump(profile, file, indent=4)

        print("✅ City updated successfully!")

    except FileNotFoundError:
        print("No profile found!")

def add_new_skill():
    try:
        with open("data.json", "r") as file:
            profile = json.load(file)
            if not profile:
                print("No profile found!")
                return

            new_skill = input("What is your new skill: ").strip().title()
            if new_skill and new_skill not in profile["skills"]:
                profile["skills"].append(new_skill)

        with open("data.json", "w") as file:
            json.dump(profile, file, indent=4)
        print("New skills added successfully")
    except FileNotFoundError:
        print("No profile found!")

def delete_profile():
    confirmation = input("Are you sure you want to delete this profile? (y/n): ").strip().lower()
    if confirmation == "y":
        with open("data.json", "w") as file:
            json.dump({}, file, indent=4)
        print("Profile successfully deleted!")