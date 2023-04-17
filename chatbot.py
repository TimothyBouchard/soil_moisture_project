import csv
import re
import random
import time
import tkinter as tk
from spellchecker import SpellChecker
# Read in the CSV file and store the data in a list of tuples
data = []
failed_attempts = 0;
with open("plants_modified.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip the header row
    for row in reader:
        data.append(tuple(row))

# Create an instance of the PyEnchant spell checker

spell_checker = SpellChecker()
current_plant = None
def respond(input_str):
    global current_plant
    # Split the user input into individual words
    words = input_str.lower().split()

    # Spellcheck the words and suggest corrections
    corrected_words = []
    for word in words:
        if not spell_checker.unknown([word]):
            corrected_words.append(word)
        else:
            corrected_words.append(spell_checker.correction(word))

# Try to find the plant name in the user input
        # If the user says thanks, respond with a polite message
    if "thanks" in input_str.lower() or "thank you" in input_str.lower():
        current_plant = None
        return random.choice([ "You're welcome! Do you have any more questions?","Let me know if i can further assist you"])


    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["Moisture", "moisture"]):
                    return f"{row[1]}"    

    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["Nitrogen", "nitrogen", "fertalizer"]):
                    return f"The best Nitrogen levels for {plant_name} is {row[2]}"    

    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["compaction" , "compaction"]):
                    return f"{row[3]}"

    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["Type", "type"]):
                    return f"{row[4]}"

    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["Temp", "temp", "temps", "Temps", "tempature", "Tempature"]):
                    return f"{row[5]}"    

    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["time", "Time", "start"]):
                    return f"{row[6]}"

    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["harvest", "Harvest", "pick"]):
                    return f"{row[7]}"

    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["Climate", "climate", "area"]):
                    return f"{row[8]}"
    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["Diseases", "diseases", "Disease","diseases"]):
                    return f"{row[9]}"

    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["Pests", "pests", "Pest","pest"]):
                    return f"{row[10]}"

    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["rid", "Rid", "kill","Kill","Solution","solution","medication","Solution","Medication"]):
                    return f"{row[11]}"

        # Loop over each row in the data and try to match the user input to the plant names
    for word in corrected_words:
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the growth habit attribute for the plant
                if any(keyword in corrected_words for keyword in ["How", "how", "Plant","plant"]):
                    return f"{row[12]}"



    # Try to find the plant name in the user input
    for word in corrected_words:
        # Loop over each row in the data and try to match the user input to the plant names
        for row in data:
            plant_name = row[0].lower()
            if word == plant_name or current_plant == plant_name:
                # If there is a match, return the attributes for the plant
                attributes = row[1:]
                current_plant = plant_name
                return random.choice ([f"Great! What about {plant_name} do you want to know?",f"Absolutly! What questions do you have about {plant_name}?"])
                #return '\n'.join([attr.split(':')[1].strip() if len(attr.split(':')) > 1 else attr.strip() for attr in attributes])
    
    # If the user says thanks, respond with a polite message
    if "thanks" in input_str.lower() or "thank you" in input_str.lower():
        return "You're welcome! Do you have any more questions?"

    if "garden" in input_str.lower() or "create" in input_str.lower():
        return random.choice([ "That's great! What kind of plants are you planning on growing?(since im only a beta i can only answer to one plant at a time)", "Fantastic idea! Do you have any specific plants in mind that you want to include in your garden?(since im only a beta i can only answer to one plant at a time)"])

    # If the user asks how the chatbot is doing, respond with a random message
    if "how are you" in input_str.lower():
        return random.choice(["I'm doing well, thank you for asking!",
         "I'm just a chatbot, I don't have feelings but I'm here to help!",
          "I'm functioning within normal parameters, thanks for checking in!"])
    
    # If the user greets the chatbot, respond with a greeting
    if any(word in corrected_words for word in ["hello", "hi", "hey"]):
        return random.choice(["Hello! How can I assist you today?", 
                       "Hi there! What can I help you with?",
                       "Welcome! What brings you here?",
                       "Hey! How can I be of service?",
                       "Good day! What can I assist you with?"])

    # Keep track of the number of times the bot has not been able to identify the plant
    if not hasattr(respond, 'num_attempts'):
        respond.num_attempts = 0
    respond.num_attempts += 1

    # After two failed attempts, prompt the user to see a list of known plants
    if respond.num_attempts >= 0:
        if any(word in corrected_words for word in ["yes", "okay", "ok", "yea", "sure", "great"]):
            plant_names = [row[0] for row in data]
            respond.num_attempts = 0
            return "I know about the following plants: " + ", ".join(plant_names)
        else:
            respond.num_attempts = 0
            return random.choice(["I'm not familiar with that plant. Would you like to see a list of known plants?",
        "Hmm, that one's not ringing a bell. Would you like to see a list of known plants?",
        "I don't think I know about that one. Would you like to see a list of known plants?",
        "I'm sorry, I'm not sure what you're asking about. Would you like to see a list of known plants?",
        "That plant doesn't sound familiar to me. Would you like to see a list of known plants?"])

    # If the user says thanks, respond with a polite message
    if "thanks" in input_str.lower() or "thank you" in input_str.lower():
        return "You're welcome! Do you have any more questions?"

    if "garden" in input_str.lower() or "create" in input_str.lower():
        return "That's great! What kind of plants are you planning on growing?"

    # If the user asks how the chatbot is doing, respond with a random message
    if "how are you" in input_str.lower():
        return random.choice(["I'm doing well, thank you for asking!",
         "I'm just a chatbot, I don't have feelings but I'm here to help!",
          "I'm functioning within normal parameters, thanks for checking in!"])


def on_click(event=None):
    # Get user input from the entry field
    input_str = entry.get().strip()

    # Clear the entry field
    entry.delete(0, tk.END)

    # Generate response and add it to the chat history
    response_str = respond(input_str)

    # Show typing animation
    chat_history.configure(state=tk.NORMAL)
    chat_history.insert(tk.END, f"User: {input_str}\n")
    for char in "Soil Monitor: " + response_str:
        chat_history.insert(tk.END, char)
        chat_history.see(tk.END)
        chat_history.update_idletasks()
        time.sleep(0.01)
    chat_history.insert(tk.END, "\n\n")
    chat_history.see(tk.END)
    chat_history.configure(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Soil Monitor Chatbot")

# Create the chat history text widget
chat_history = tk.Text(root, height=20, width=60, state=tk.DISABLED, wrap=tk.WORD)
chat_history.pack(side=tk.TOP, padx=10, pady=10)

# Create a label and entry field for user input
input_label = tk.Label(root, text="Text:")
input_label.pack(side=tk.LEFT, padx=10, pady=10)
entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Bind the entry field to the on_click function for both button click and "Enter" key press
entry.bind("<Return>", on_click)
button = tk.Button(root, text="Submit", command=on_click)
button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
