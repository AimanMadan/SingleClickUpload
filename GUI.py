import tkinter as tk
from tkinterdnd2 import TkinterDnD, DND_FILES
import singleClickUpload  # Import the upload script

# Initialize global variables for file paths
wav_file_path = ""
stem_file_path = ""

def drop_wav(event):
    global wav_file_path
    wav_file_path = event.data.strip('{}')
    wav_box.delete("1.0", tk.END)  # Clear the text box
    wav_box.insert(tk.END, wav_file_path)  # Insert the file path into the text box
    wav_box.config(state=tk.DISABLED)  # Disable the text box to make it read-only

def drop_stem(event):
    global stem_file_path
    stem_file_path = event.data.strip('{}')
    stems_box.delete("1.0", tk.END)  # Clear the text box
    stems_box.insert(tk.END, stem_file_path)  # Insert the file path into the text box
    stems_box.config(state=tk.DISABLED)  # Disable the text box to make it read-only

def upload_files():
    global wav_file_path, stem_file_path
    singleClickUpload.run_script(wav_file_path, stem_file_path)  # Call the upload script function

def setup_single_Click():
    single_Click = TkinterDnD.Tk()
    single_Click.configure(bg='#EB0000')  # Set the background color of the main single_Click
    single_Click.geometry("300x500")  # Set the size of the single_Click to 300x500 pixels
    single_Click.title("Beat Stars Single Click")  # Set the title of the single_Click
    return single_Click

def create_widgets(single_Click):
    # Add a title label with the text "Single click upload" and a bold font
    title = tk.Label(single_Click, text="Single click upload", font=('Ariel', 13, 'bold'), bg='#EB0000', fg='white')
    title.pack(padx=20, pady=20)  # Add some space around the label

    # Add a label to prompt users to drop .wav files
    wav_drop = tk.Label(single_Click, text="Drop track file below", font=('Ariel', 11), bg='#EB0000', fg='white')
    wav_drop.pack(padx=20, pady=10)  # Add some space around the label

    global wav_box
    # Add a text box for dropping .wav files
    wav_box = tk.Text(single_Click, height=3, width=30, bg="lightgrey", fg='black', state=tk.NORMAL)
    wav_box.pack(padx=20, pady=10)

    # Register the text box as a drop target for files and bind the drop event
    wav_box.drop_target_register(DND_FILES)
    wav_box.dnd_bind('<<Drop>>', drop_wav)

    # Add a label to prompt users to drop .zip or .rar files
    stems_drop = tk.Label(single_Click, text="Drop Stems file below", font=('Ariel', 11), bg='#EB0000', fg='white')
    stems_drop.pack(padx=20, pady=10)  # Add some space around the label

    global stems_box
    # Add a text box for dropping .zip or .rar files
    stems_box = tk.Text(single_Click, height=3, width=30, bg="lightgrey", fg='black', state=tk.NORMAL)
    stems_box.pack(padx=20, pady=10)

    # Register the text box as a drop target for files and bind the drop event
    stems_box.drop_target_register(DND_FILES)
    stems_box.dnd_bind('<<Drop>>', drop_stem)

    # Add an upload button for users to click when they're ready to upload
    upload_button = tk.Button(single_Click, text="Upload", font=('Ariel', 11), bg='#EB0000', fg='white', command=upload_files)
    upload_button.pack(padx=20, pady=5)  # Add some space around the button

def main():
    single_Click = setup_single_Click()
    create_widgets(single_Click)
    single_Click.mainloop()  # Start the Tkinter event loop so the single_Click remains open and responsive

if __name__ == "__main__":
    main()
