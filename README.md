Here's the updated `README.md` file with the included section to showcase the GUI using the provided image URL:

---

# BeatStars Single Click Upload Automation

This repository contains a Python script to automate the process of uploading tracks to BeatStars. The script utilizes Selenium WebDriver to interact with the BeatStars website, handling tasks such as logging in, uploading .wav files, filling in basic track information, and setting artwork.

## Features

- **Login Automation**: Automatically logs into BeatStars using credentials stored in a text file.
- **File Upload**: Uploads .wav files and optionally stem files (.zip or .rar).
- **Basic Info Entry**: Fills in the track's basic information, such as title, extracted from the file name.
- **Artwork Selection**: Fetches random images from Unsplash to use as artwork for the track.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (ensure it is compatible with your installed version of Chrome)
- BeatStars account with necessary permissions to upload tracks
- Unsplash API Key (saved in `UnsplashAPI.txt`)

## Setup

### Install Dependencies:

```bash
pip install selenium
pip install tkinterdnd2
pip install pillow
pip install requests
```

### Download Chrome WebDriver:

- Download the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
- Ensure the `chromedriver.exe` is placed in the same directory as the script or specify its path in the script.

### Prepare Credentials:

- The repository includes a `Login.txt` file. Replace the placeholder text with your actual BeatStars email and password.
- The repository includes a `UnsplashAPI.txt` file. Replace the placeholder text with your Unsplash API key.

```
your-email@example.com
yourpassword
your-unsplash-api-key
```

### Organize Files for Upload:

- Ensure at least one .wav file is present in the directory named `Files to Upload`.
- If you want to upload stems, place them in a compressed .zip or .rar file in the same directory.

## Usage

### Change Directory in Script:

- Update the directory path in the script to point to your project directory.

### Run the Script:

```bash
python main.py
```

### Script Workflow:

- The script will read the email and password from `Login.txt`.
- It will navigate to the BeatStars login page and log in using the provided credentials.
- The script will upload the .wav file (and stems if present).
- It will then fill in the basic information such as the track title.
- It will fetch a random image from Unsplash and use it as the track's artwork.

### GUI for Single Click Upload:

- The GUI allows users to drag and drop .wav and .zip/.rar files, enter the track title, and select artwork from Unsplash.
- Users can navigate through different images and save the selected image as `artwork.jpg`.
- If no track title is entered, the track title will default to the .wav file name.

## Showcase

![GUI Screenshot](https://github.com/user-attachments/assets/8cb2a4b9-eb57-4424-89eb-60fb22bb9a30)

## Important Notes

- Ensure the correct paths are specified for `chromedriver.exe` and the files to be uploaded.
- The current implementation includes `time.sleep` for upload waits. A more robust solution with explicit waits is recommended for production use.

## Contributions

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

