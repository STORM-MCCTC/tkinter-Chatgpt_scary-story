import tkinter as tk
import openai

# Load the API key from 'api_key.txt'
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()
    openai.api_key = api_key

# Create the main Tkinter window
root = tk.Tk()
root.title("AI Scary Story")
root.geometry("1000x800")

# Title label
label = tk.Label(root, text="AI Scary Story", font=("Arial", 16))
label.pack(pady=20)

# Function to generate a story
def on_gen_click():
    prompt = user_input.get()
    if not prompt:
        Generated.config(text="Please enter a prompt.")
        return

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": f"Write a short scary story that is PG13 about: {prompt} (reply with just the story)"}],
            temperature=0.8
        )
        story = response.choices[0].message['content'].strip()
        Generated.config(text=story)
    except Exception as e:
        Generated.config(text=f"Error: {e}")

# Function to save the generated story to a file
def on_save_click():
    story = Generated.cget("text")
    if not story or story == "generated text here":
        Generated.config(text="No story to save.")
        return

    try:
        with open("scary_story.txt", "w") as file:
            file.write(story)
        Generated.config(text="Story saved to 'scary_story.txt' rename file to not override last file.")
    except Exception as e:
        Generated.config(text=f"Error saving story: {e}")

# User input entry
user_input = tk.Entry(root, width=40)
user_input.pack(pady=5)

# Generate button
Generate = tk.Button(root, text="Generate", command=on_gen_click)
Generate.pack(pady=10)

# Label to display the generated story
Generated = tk.Label(root, text="generated text here", font=("Arial", 10), wraplength=800, justify="left", anchor="nw", relief="sunken", width=80, height=20)
Generated.pack(pady=20)

# Save button
save = tk.Button(root, text="Save", command=on_save_click)
save.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
