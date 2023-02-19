import random

# Define a dictionary of Pokemon types and their weaknesses
type_data = {
    "Normal": ["Fighting"],
    "Fire": ["Water", "Rock", "Ground"],
    "Water": ["Grass", "Electric"],
    "Electric": ["Ground"],
    "Grass": ["Fire", "Ice", "Poison", "Flying", "Bug"],
    "Ice": ["Fire", "Fighting", "Rock", "Steel"],
    "Fighting": ["Flying", "Psychic", "Fairy"],
    "Poison": ["Ground", "Psychic"],
    "Ground": ["Water", "Grass", "Ice"],
    "Flying": ["Electric", "Ice", "Rock"],
    "Psychic": ["Bug", "Ghost", "Dark"],
    "Bug": ["Fire", "Flying", "Rock"],
    "Rock": ["Water", "Grass", "Fighting", "Ground", "Steel"],
    "Ghost": ["Ghost", "Dark"],
    "Dragon": ["Ice", "Dragon", "Fairy"],
    "Dark": ["Fighting", "Bug", "Fairy"],
    "Steel": ["Fire", "Fighting", "Ground"]
}

# Define a list of Pokemon types for the user to be tested on
type_list = list(type_data.keys())

# Define a function to ask the user a question and return the correct answer
def ask_question():
    # Choose a random Pokemon type and its corresponding weaknesses
    type = random.choice(type_list)
    weaknesses = type_data[type]
    # Prompt the user to enter the weaknesses of the chosen type
    print("What are the weaknesses of", type, "type Pokemon?")
    print("Enter the weaknesses separated by commas.")
    answer = input().split(",")
    answer = [w.strip() for w in answer]
    # Check if the user's answer is correct
    if set(answer) == set(weaknesses):
        print("Correct!")
        return True
    else:
        print("Incorrect. The weaknesses are:", ", ".join(weaknesses))
        return False

# Define variables to keep track of the user's score and the number of questions asked
score = 0
num_questions = 0

# Ask the user 10 questions and keep track of their score
for i in range(10):
    print("Question", i+1)
    if ask_question():
        score += 1
    num_questions += 1

# Display the user's score and the number of questions asked
print("You got", score, "out of", num_questions, "questions correct.")
