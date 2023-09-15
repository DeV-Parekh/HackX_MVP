from tkinter import filedialog, ttk
import tkinter as tk
# Create main window
root = tk.Tk()
root.title("Upload Folder")
root.geometry("600x400")  # Set window size
root.configure(bg="#F8F8FF")  # Set background color

checkbox_frame = tk.Frame(root)
checkbox_frame.pack()

# Create a boolean variable to hold the state of the checkbox
checked_invalid = tk.BooleanVar()

# Create the checkbox
checkbox = tk.Checkbutton(
    checkbox_frame, text="Create folder for invalid marksheet", variable=checked_invalid
)
checkbox.pack(side=tk.LEFT)

checked_preprocess = tk.BooleanVar()

#Create the checkbox
checkbox = tk.Checkbutton(
    checkbox_frame, text="Preprocess", variable=checked_preprocess
)
checkbox.pack(side=tk.LEFT)

# Create label for displaying selected folder path
folder_path_label = tk.Label(root, text="No folder selected", font=("Arial", 12))
folder_path_label.configure(
    bg="#F8F8FF", fg="#4B0082"
)  # Set background and foreground color
folder_path_label.pack(pady=10)

# Create browse button
browse_button = tk.Button(
    root,
    text="Start",
    command=browse_folder,
    bg="#6495ED",
    fg="white",
    font=("Arial", 12),
)
browse_button.pack(pady=10)

# Run the application
root.mainloop()
