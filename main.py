import tkinter as tk
import openai

#! Load the API key from 'api_key.txt'
with open('api_key.txt', 'r') as file: # just get the api key and set it the the var "api_key"
    api_key = file.read().strip()
    openai.api_key = api_key

#! Create the main Tkinter window
root = tk.Tk() # inits the window i think
root.title("AI Scary Story") #defines the name of the window
root.geometry("1000x800") #defines the size of the window
#! Title label
label = tk.Label(root, text="AI Scary Story", font=("Arial", 16))
label.pack(pady=20)

#! Function to generate a story
def on_gen_click():
    prompt = user_input.get() #set the userinput to "prompt var"
    if not prompt: #checks if text has been entered or not
        Generated.config(text="Please enter a prompt.") #this just syas that text hasn't been input if there wasn't any input text
        return #returns var

    try: #trys to genrate text
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # defines what gpt model we will use 
            messages=[{"role": "user", "content": f"Write a short scary story that is PG13 about: {prompt} (reply with just the story)"}], #prompt that gpt is prompted with
            temperature=0.8 # chatgpt said to put this idk what it does lmao
        )
        story = response.choices[0].message['content'].strip() #sets the 'story' var to the 'response' var   
        Generated.config(text=story) #set the "generated" area to the story var
    except Exception as e: #error handleling
        Generated.config(text=f"Error: {e}")

#! Function to save the generated story to a file
def on_save_click(): 
    story = Generated.cget("text") #gets the story as plain text
    if not story or story == "generated text here": # see's if it can save or not but weather Generated area has text or the text is something else then "generated text here"
        Generated.config(text="No story to save.") 
        return

    try:
        with open("scary_story.txt", "w") as file: #writes to file
            file.write(story) 
        Generated.config(text="Story saved to 'scary_story.txt' rename file to not override last file.")
    except Exception as e: #error handleing
        Generated.config(text=f"Error saving story: {e}")

#! User input entry
user_input = tk.Entry(root, width=40)
user_input.pack(pady=5)

#! Generate button
Generate = tk.Button(root, text="Generate", command=on_gen_click)
Generate.pack(pady=10)

#! Label to display the generated story
Generated = tk.Label(root, text="generated text here", font=("Arial", 10), wraplength=800, justify="left", anchor="nw", relief="sunken", width=80, height=20)
Generated.pack(pady=20)  

#! Save button
save = tk.Button(root, text="Save", command=on_save_click)
save.pack(pady=10)

#! Start the Tkinter event loop
root.mainloop()