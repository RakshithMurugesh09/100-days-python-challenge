# Tuple containing the scores of students in the class
student_scores = (78, 35, 89, 67, 92, 85)

# Initialize the highest_score variable with a very low value
# Assuming scores can't be below zero, so set to zero
highest_score = 0

# Iterate over each score in the student_scores tuple
for score in student_scores:
    # If the current score is greater than the recorded highest_score,
    # update highest_score to this score
    if score > highest_score:
        highest_score = score

# Display the highest score found in the class
print(f"The highest score in the class is {highest_score}")
