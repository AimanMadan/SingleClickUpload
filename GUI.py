import requests 
import singleClickUpload  
import getArtwork  
import tkinter as tk  # creating GUI applications
from tkinterdnd2 import TkinterDnD, DND_FILES  # drag and drop functionality
from tkinter import ttk  # themed widgets
from PIL import Image, ImageTk  #handling and displaying images
from io import BytesIO  # used here to handle image data
import os

# global variables for file paths
wav_file_path = ""
stem_file_path = ""
track_title_name = ""
artwork_path = ""

# Drag & Drop related to .wav file
def drop_wav(event):
    global wav_file_path
    wav_file_path = event.data.strip('{}')
    wav_box.delete("1.0", tk.END)  # Clear the text box
    wav_box.insert(tk.END, wav_file_path)  # Insert the file path into the text box
    wav_box.config(state=tk.DISABLED)  # Disable the text box to make it read-only

# Drag & Drop related to .zip or .rar file
def drop_stem(event):
    global stem_file_path
    stem_file_path = event.data.strip('{}')
    stems_box.delete("1.0", tk.END)  # Clear the text box
    stems_box.insert(tk.END, stem_file_path)  # Insert the file path into the text box
    stems_box.config(state=tk.DISABLED)  # Disable the text box to make it read-only

# Function to save artwork
def save_current_image():
    global artwork_path
    img_data = requests.get(getArtwork.image_urls[image_index]).content
    img = Image.open(BytesIO(img_data))
    img = img.resize((3000, 3000), Image.LANCZOS)
    artwork_path = os.path.join(os.getcwd(), 'Files to upload', 'artwork.jpg')
    if os.path.exists(artwork_path):
        os.remove(artwork_path)  # Remove the existing file
    img.save(artwork_path, 'JPEG')

# Get File paths, track title, and artwork
def upload_files():
    global wav_file_path, stem_file_path, track_title_name, artwork_path
    track_title_name = track_title_entry.get()  # Get the track title from the entry field
    save_current_image()  # Save the current displayed image
    singleClickUpload.run_script(wav_file_path, stem_file_path, track_title_name, artwork_path)  # Call the upload script function

# Setup for main Window
def setup_single_Click():
    single_Click = TkinterDnD.Tk()
    single_Click.configure(bg='#EB0000')  # background color 
    single_Click.geometry("400x710")  # Window size
    single_Click.title("Single Click Upload")  # Window title
    return single_Click

# Display image URL 
def fetch_and_display_image(url=None):
    try:
        global image_index
        if url:
            getArtwork.image_urls.append(url)
            image_index += 1
        elif image_index == -1:
            url = getArtwork.fetch_and_store_image()
            image_index = 0
        else:
            url = getArtwork.image_urls[image_index]

        # Load the image directly from the URL
        img_data = requests.get(url).content
        img = Image.open(BytesIO(img_data))
        img = img.resize((250, 250), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        artwork_display.config(image=img)
        artwork_display.image = img
    except Exception as e:
        print(f"Error fetching or displaying image: {e}")

image_index = -1  # keep track of the current image index

# Previous button functionalty 
def fetch_previous_image():
    global image_index
    if image_index > 0:
        image_index -= 1
        fetch_and_display_image()

# Next button functionalty 
def fetch_next_image():
    global image_index
    if image_index < len(getArtwork.image_urls) - 1:
        image_index += 1
        fetch_and_display_image()
    else:
        new_url = getArtwork.fetch_and_store_image()
        fetch_and_display_image(new_url)

# GUI Elements 
def create_widgets(single_Click):
    # Add a title label with the text "Single click upload" and a bold font
    title = tk.Label(single_Click, text="Single click upload", font=('Ariel', 13, 'bold'), bg='#EB0000', fg='white')
    title.pack(padx=20, pady=20)  # Add some space around the label

    # Add a label to prompt users to drop .wav files
    wav_drop = tk.Label(single_Click, text="Drag & Drop .wav file below", font=('Ariel', 11), bg='#EB0000', fg='white')
    wav_drop.pack(padx=20, pady=2)  # Add some space around the label

    global wav_box
    # Add a text box for dropping .wav files
    wav_box = tk.Text(single_Click, height=2.5, width=30, bg="lightgrey", fg='black', state=tk.NORMAL)
    wav_box.pack(padx=20, pady=10)

    # Register the text box as a drop target for files and bind the drop event
    wav_box.drop_target_register(DND_FILES)
    wav_box.dnd_bind('<<Drop>>', drop_wav)

    # Add a label to prompt users to drop .zip or .rar files
    stems_drop = tk.Label(single_Click, text="Drag & Drop Stems(.zip or .rar) file below", font=('Ariel', 11), bg='#EB0000', fg='white')
    stems_drop.pack(padx=20, pady=2)  # Add some space around the label

    global stems_box
    # Add a text box for dropping .zip or .rar files
    stems_box = tk.Text(single_Click, height=2.5, width=30, bg="lightgrey", fg='black', state=tk.NORMAL)
    stems_box.pack(padx=20, pady=10)

    # Register the text box as a drop target for files and bind the drop event
    stems_box.drop_target_register(DND_FILES)
    stems_box.dnd_bind('<<Drop>>', drop_stem)
    
    # Create a frame for the track title label and entry
    track_title_frame = tk.Frame(single_Click, bg='#EB0000')
    track_title_frame.pack(pady=10)  # Add some space around the frame

    # Add a label for the track title
    track_title_label = tk.Label(track_title_frame, text="Track title:", font=('Ariel', 11), bg='#EB0000', fg='white')
    track_title_label.pack(side=tk.LEFT)  # Place the label to the left

    global track_title_entry
    # Add an entry field where users can type the track title
    track_title_entry = tk.Entry(track_title_frame, font=('Ariel', 11), bg='lightgrey', fg='black')
    track_title_entry.pack(side=tk.LEFT)  # Place the entry field to the right of the label
    
    # Add a label with the text "Single click upload" and a bold font
    artwork_title = tk.Label(single_Click, text="Choose an Artwork", font=('Ariel', 11), bg='#EB0000', fg='white')
    artwork_title.pack(padx=20, pady=20)  # Add some space around the label

    # Add a label to display artwork
    global artwork_display
    artwork_display = tk.Label(single_Click, text="Artwork will be displayed here", font=('Ariel', 11), bg='#EB0000', fg='white')
    artwork_display.pack(padx=20, pady=0)  # Add some space around the label

    # Add Previous and Next buttons
    button_frame = tk.Frame(single_Click, bg='#EB0000')
    button_frame.pack(pady=10)

    # Create a style for the rounded button
    style = ttk.Style()
    style.configure("RoundedButton.TButton", font=('Ariel', 11), background='#EB0000', foreground='black', borderwidth=1, relief="solid")
    style.map("RoundedButton.TButton",
              background=[('active', '#EB0000'), ('disabled', '#000000')],
              foreground=[('active', 'white'), ('disabled', 'grey')],
              relief=[('pressed', 'flat'), ('!pressed', 'solid')])

    prev_button = ttk.Button(button_frame, text="Previous", style="RoundedButton.TButton", command=fetch_previous_image)
    prev_button.pack(side=tk.LEFT, padx=10)

    next_button = ttk.Button(button_frame, text="Next", style="RoundedButton.TButton", command=fetch_next_image)
    next_button.pack(side=tk.LEFT, padx=10)

    # Fetch and display the first image
    fetch_and_display_image()
    
    # Add an upload button for users to click when they're ready to upload
    upload_button = ttk.Button(single_Click, text="Upload", style="RoundedButton.TButton", command=upload_files)
    upload_button.pack(padx=20, pady=5)  # Add some space around the button

def main():
    single_Click = setup_single_Click()
    create_widgets(single_Click)
    single_Click.mainloop()  # single_Click remains open and responsive

if __name__ == "__main__":
    main()
