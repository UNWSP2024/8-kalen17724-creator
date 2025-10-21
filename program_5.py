# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.# Finally, the program will display the ID and name of all the courses having that subject.

# Dictionary to store course ID and course name pairs
courses = {}

print("Enter course information (leave Course ID blank to finish):")
while True:
    course_id = input("Course ID: ").strip()
    if course_id == "":
        break
    course_name = input("Course Name: ").strip()
    courses[course_id] = course_name

# Ask the user for a subject prefix to filter courses
subject = input("\nEnter a subject code to filter (e.g., 'COS'): ").strip().upper()

# Display matching courses
print(f"\nCourses with subject '{subject}':")
found = False
for cid, name in courses.items():
    if cid.upper().startswith(subject):
        print(f"{cid}: {name}")
        found = True

if not found:
    print("No courses found with that subject.")