import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES

def drop_wav(event):
    wav_file_path = event.data
    wav_box.delete("1.0", tk.END)  # Clear the text box
    wav_box.insert(tk.END, wav_file_path)  # Insert the file path into the text box
    wav_box.config(state=tk.DISABLED)  # Disable the text box to make it read-only

def drop_stem(event):
    stem_file_path = event.data
    stems_box.delete("1.0", tk.END)  # Clear the text box
    stems_box.insert(tk.END, stem_file_path)  # Insert the file path into the text box
    stems_box.config(state=tk.DISABLED)  # Disable the text box to make it read-only

def setup_window():
    window = TkinterDnD.Tk()
    window.configure(bg='#EB0000')  # Set the background color of the main window
    window.geometry("300x500")  # Set the size of the window to 300x500 pixels
    window.title("Beat Stars Single Click")  # Set the title of the window
    return window

def create_widgets(window):
    # Add a title label with the text "Single click upload" and a bold font
    title = tk.Label(window, text="Single click upload", font=('Ariel', 13, 'bold'), bg='#EB0000', fg='white')
    title.pack(padx=20, pady=20)  # Add some space around the label

    # Add a label to prompt users to drop .wav files
    wav_drop = tk.Label(window, text="Drop track file below", font=('Ariel', 11), bg='#EB0000', fg='white')
    wav_drop.pack(padx=20, pady=10)  # Add some space around the label

    global wav_box
    # Add a text box for dropping .wav files
    wav_box = tk.Text(window, height=3, width=30, bg="lightgrey", fg='black', state=tk.NORMAL)
    wav_box.pack(padx=20, pady=10)

    # Register the text box as a drop target for files and bind the drop event
    wav_box.drop_target_register(DND_FILES)
    wav_box.dnd_bind('<<Drop>>', drop_wav)

    # Add a label to prompt users to drop .zip or .rar files
    stems_drop = tk.Label(window, text="Drop Stems file below", font=('Ariel', 11), bg='#EB0000', fg='white')
    stems_drop.pack(padx=20, pady=10)  # Add some space around the label

    global stems_box
    # Add a text box for dropping .zip or .rar files
    stems_box = tk.Text(window, height=3, width=30, bg="lightgrey", fg='black', state=tk.NORMAL)
    stems_box.pack(padx=20, pady=10)

    # Register the text box as a drop target for files and bind the drop event
    stems_box.drop_target_register(DND_FILES)
    stems_box.dnd_bind('<<Drop>>', drop_stem)

    # Create a frame for the track title label and entry
    track_title_frame = tk.Frame(window, bg='#EB0000')
    track_title_frame.pack(pady=10)  # Add some space around the frame

    # Add a label for the track title
    track_title_label = tk.Label(track_title_frame, text="Track title:", font=('Ariel', 11), bg='#EB0000', fg='white')
    track_title_label.pack(side=tk.LEFT)  # Place the label to the left

    # Add an entry field where users can type the track title
    track_title = tk.Entry(track_title_frame, font=('Ariel', 11), bg='lightgrey', fg='black')
    track_title.pack(side=tk.LEFT)  # Place the entry field to the right of the label

    # Add an upload button for users to click when they're ready to upload
    upload_button = tk.Button(window, text="Upload", font=('Ariel', 11), bg='#EB0000', fg='white')
    upload_button.pack(padx=20, pady=5)  # Add some space around the button

def main():
    window = setup_window()
    create_widgets(window)
    window.mainloop()  # Start the Tkinter event loop so the window remains open and responsive

if __name__ == "__main__":
    main()
