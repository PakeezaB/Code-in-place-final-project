import tkinter as tk
from tkinter import ttk

# Function to generate the story based on user inputs
def generate_story():
    plot_type = plot_type_var.get()
    story_theme = story_theme_var.get()
    main_character = main_character_var.get()
    profession = profession_var.get()
    has_villain = has_villain_var.get()

    # Generating story based on inputs
    story = f"Once upon a time in a {plot_type.lower()} tale, there was a {profession.lower()} named {main_character}.\n"
    story += f"The story was a {story_theme.lower()} where {main_character} faced many challenges.\n"
    
    if has_villain:
        story += f"One day, a sinister villain appeared, causing trouble for {main_character}.\n"
    
    story += f"Through wit and determination, {main_character} navigated through the ups and downs of their profession as a {profession.lower()}.\n"
    
    if has_villain:
        story += f"In the end, {main_character} overcame the villain and triumphed, making the {plot_type.lower()} story a memorable one.\n"
    else:
        story += f"In the end, {main_character} achieved great success, making the {plot_type.lower()} story a memorable one.\n"

    # Split story into pages (for simplicity, let's assume each sentence is a page)
    global book_content
    book_content = story.split('\n')
    page_var.set(0)  # Reset to first page
    update_page()

# Function to update the displayed page
def update_page():
    current_page = page_var.get()
    story_canvas.delete("all")  # Clear previous content
    # Draw rectangle (simulating a page)
    story_canvas.create_rectangle(50, 50, 450, 300, fill="white", outline="black")
    # Display the text content
    if current_page < len(book_content):
        story_canvas.create_text(250, 175, text=book_content[current_page], width=380, font=("Arial", 14))

# Function to go to the next page
def next_page():
    if page_var.get() < len(book_content) - 1:
        page_var.set(page_var.get() + 1)
        update_page()

# Function to go to the previous page
def prev_page():
    if page_var.get() > 0:
        page_var.set(page_var.get() - 1)
        update_page()

# Function to draw a realistic book on the canvas
def draw_realistic_book(canvas):
    # Draw the book title text
    canvas.create_text(100, 50, font=("Times New Roman", 16), text="Book Plot Generator", fill="brown")
    
    # Draw the book cover with shading for a 3D effect
    canvas.create_rectangle(50, 100, 150, 200, fill='saddle brown', outline='black')
    canvas.create_line(50, 100, 150, 100, fill='black', width=1)  # Top edge
    canvas.create_line(150, 100, 150, 200, fill='black', width=1)  # Right edge
    canvas.create_polygon(50, 100, 60, 90, 160, 90, 150, 100, fill='saddle brown', outline='black')  # Top cover
    canvas.create_polygon(150, 100, 160, 90, 160, 190, 150, 200, fill='sienna', outline='black')  # Side cover

    # Draw the spine of the book with a lighter color
    canvas.create_line(50, 100, 50, 200, fill='wheat', width=5)

    # Draw pages with lines and slight curvature to represent pages
    for i in range(105, 195, 3):
        canvas.create_arc(50, i-2, 150, i+1, start=0, extent=-180, style=tk.ARC)

# Create main window
root = tk.Tk()
root.title("Short Story Generator & Canvas Book")
root.configure(bg="lightyellow")  # Set background color to light yellow

# Create a Canvas widget for the book and story display
book_canvas = tk.Canvas(root, width=210, height=300, bg="lightgrey")
book_canvas.grid(row=0, column=0, padx=10, pady=10)

# Draw realistic book on the book_canvas
draw_realistic_book(book_canvas)

# Create another Canvas widget for the story pages
story_canvas = tk.Canvas(root, width=500, height=350, bg="white")
story_canvas.grid(row=0, column=1, padx=10, pady=10)

# Frame for story generator options
options_frame = ttk.LabelFrame(root, text="Story Generator Options", width=200, height=300)
options_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=tk.NW)
options_frame.configure(style="My.TLabelframe")  # Apply style to the LabelFrame

# Plot Type
plot_type_label = ttk.Label(options_frame, text="Select Plot Type:")
plot_type_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

plot_types = ["Thrilling", "Adventurous", "Romantic", "Mystery"]
plot_type_var = tk.StringVar()
plot_type_var.set(plot_types[0])  # Default value

plot_type_dropdown = ttk.Combobox(options_frame, textvariable=plot_type_var, values=plot_types)
plot_type_dropdown.grid(row=0, column=1, padx=5, pady=5)

# Story Theme
story_theme_label = ttk.Label(options_frame, text="Select Story Theme:")
story_theme_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

story_themes = ["Friends Story", "Hero-Heroine", "Family Theme", "Rags to Riches"]
story_theme_var = tk.StringVar()
story_theme_var.set(story_themes[0])  # Default value

story_theme_dropdown = ttk.Combobox(options_frame, textvariable=story_theme_var, values=story_themes)
story_theme_dropdown.grid(row=1, column=1, padx=5, pady=5)

# Main Character
main_character_label = ttk.Label(options_frame, text="Main Character:")
main_character_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

main_character_var = tk.StringVar()
main_character_entry = ttk.Entry(options_frame, textvariable=main_character_var)
main_character_entry.grid(row=2, column=1, padx=5, pady=5)

# Profession
profession_label = ttk.Label(options_frame, text="Profession:")
profession_label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)

professions = ["Artist", "Musician", "Violinist", "Baker"]
profession_var = tk.StringVar()
profession_var.set(professions[0])  # Default value

profession_dropdown = ttk.Combobox(options_frame, textvariable=profession_var, values=professions)
profession_dropdown.grid(row=3, column=1, padx=5, pady=5)

# Has Villain
has_villain_var = tk.BooleanVar()
has_villain_checkbutton = ttk.Checkbutton(options_frame, text="Include a Villain", variable=has_villain_var)
has_villain_checkbutton.grid(row=4, columnspan=2, padx=5, pady=5)

# Generate Story Button
generate_button = ttk.Button(options_frame, text="Generate Story", command=generate_story)
generate_button.grid(row=5, columnspan=2, padx=5, pady=10)

# Apply style to the LabelFrame
style = ttk.Style()
style.configure("My.TLabelframe", background="lightyellow")
style.configure("TLabel", background="lightyellow")

# Navigation buttons
prev_button = ttk.Button(root, text="Previous", command=prev_page)
prev_button.grid(row=2, column=0, padx=5, pady=10, sticky=tk.SW)

page_var = tk.IntVar(value=0)  # Variable to track current page
page_label = ttk.Label(root, textvariable=page_var, background="lightyellow")
page_label.grid(row=2, column=1, padx=5, pady=10, sticky=tk.S)

next_button = ttk.Button(root, text="Next", command=next_page)
next_button.grid(row=2, column=1, padx=5, pady=10, sticky=tk.SE)

# Start GUI main loop
root.mainloop()
