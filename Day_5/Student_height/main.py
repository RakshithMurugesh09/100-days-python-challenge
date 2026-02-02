# List of student heights
heights = [151, 145, 179]

# Initialize total height to 0
total_height = 0

# Initialize student count to 0
no_student = 0

# Loop through the list to calculate the total height
for height in heights:
    total_height += height  # Add each height to total_height

# Loop through the list again to count the number of students
for student in heights:
    no_student += 1  # Increase the student count by 1 for each student

# Calculate average height (converted to integer to remove decimals)
avg_height = int(total_height / no_student)

# Print the results
print(f"Total height = {total_height}")
print(f"No of Students = {no_student}")
print(f"Average height is {avg_height}")
