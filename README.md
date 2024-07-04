### Single Click Upload Automation

This repository contains a Python project to automate the process of uploading tracks to BeatStars. The project utilizes Selenium WebDriver to interact with the BeatStars website, handling tasks such as logging in, uploading .wav files, and filling in basic track information. It now includes a GUI built with Tkinter for a more user-friendly experience and an integrated feature to fetch and display artwork from Unsplash.

#### Features

- **Login Automation:** Automatically logs into BeatStars using credentials stored in a text file.
- **File Upload:** Uploads .wav files and optionally stem files (.zip or .rar) and artwork (.jpeg, .jpg, or .png).
- **Basic Info Entry:** Fills in the track's basic information, such as title, extracted from the file name.
- **GUI Interface:** User-friendly interface for file selection, artwork display, and upload initiation.
- **Artwork Fetching:** Fetches and displays random artwork images from Unsplash based on a specified category, which can be used later as the artwork for the uploaded beat.

#### Requirements

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (ensure it is compatible with your installed version of Chrome)
- BeatStars account with necessary permissions to upload tracks
- TkinterDnD2
- PIL (Python Imaging Library)
- Requests module

#### Setup

##### Install Dependencies:

Install Selenium, TkinterDnD2, PIL, and Requests:
```bash
pip install selenium tkdnd pillow requests
```

##### Download Chrome WebDriver:

1. Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/).
2. Ensure the `chromedriver.exe` is placed in the same directory as the script or specify its path in the script.

##### Prepare Credentials:

1. The repository includes a `Login.txt` file. Replace the placeholder text with your actual BeatStars email and password.
    ```
    your-email@example.com
    yourpassword
    ```

##### Organize Files for Upload:

1. Ensure at least one .wav file is present in the directory named `Files to Upload`.
2. If you want to upload stems, place them in a compressed .zip or .rar file in the same directory.
3. Create a file named `UnsplashAPI` and place your Unsplash API key inside it.

#### Usage

##### Run the GUI:
```bash
python main.py
```
1. Use the GUI to drop the .wav and stem files.
2. Click the "Upload" button to start the automation process.
3. Navigate through artwork using the "Previous" and "Next" buttons.
4. The displayed images can later be used as the artwork for the beat uploaded to BeatStars.

##### Script Workflow:
1. The script will read the email and password from `Login.txt`.
2. It will navigate to the BeatStars login page and log in using the provided credentials.
3. The script will upload the .wav file (and stems if present).
4. It will then fill in the basic information such as the track title.
5. The GUI will fetch and display random artwork images from Unsplash, which can be used as the beat's artwork.

#### Important Notes

- Ensure the correct paths are specified for `chromedriver.exe` and the files to be uploaded.
- The script uses explicit waits to handle page loading times. Adjust these waits if necessary.
- The current implementation includes `time.sleep` for some waits. A more robust solution with explicit waits is recommended for production use.
- When running in headless mode, ensure that the user data directory is correctly specified to avoid two-step verification prompts.

#### Contributions

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

#### License

This project is licensed under the MIT License. See the LICENSE file for more details.
