# BeatStars Single Click Upload Automation

This repository contains a Python script to automate the process of uploading tracks to BeatStars. The script utilizes Selenium WebDriver to interact with the BeatStars website, handling tasks such as logging in, uploading .wav files, and filling in basic track information.

## Features

- **Login Automation**: Automatically logs into BeatStars using credentials stored in a text file.
- **File Upload**: Uploads .wav files and optionally stem files (.zip or .rar) and artwork (.jpeg, .jpg, or .png).
- **Basic Info Entry**: Fills in the track's basic information, such as title, extracted from the file name.

## Requirements

- Python 3.x
- Selenium WebDriver
- Chrome WebDriver (ensure it is compatible with your installed version of Chrome)
- BeatStars account with necessary permissions to upload tracks

## Setup

1. **Install Selenium**:
   ```bash
   pip install selenium
   ```

2. **Download Chrome WebDriver**:
   - Download the Chrome WebDriver from [here](https://sites.google.com/chromium.org/driver/).
   - Ensure the `chromedriver.exe` is placed in the same directory as the script or specify its path in the script.

3. **Prepare Credentials**:
   - The repository already includes a `Login.txt` file. Replace the placeholder text with your actual BeatStars email and password.
   ```txt
   your-email@example.com
   yourpassword
   ```

4. **Organize Files for Upload**:
   - Ensure at least one .wav file is present in the directory named `Files to Upload`.
   - If you want to upload stems, place them in a compressed .zip or .rar file in the same directory.

## Usage

1. **Change Directory in Script**:
   - Update the directory path in the script to point to your project directory.
   ```python
   # Get .wav, stem, and artwork files from the specified directory
   wav, stems, artwork, title = get_files('C:/BeatStarsSingleClick/Files To Upload')  # Change Directory to the Project's directory
   ```

2. **Run the Script**:
   ```bash
   python main.py
   ```

3. **Script Workflow**:
   - The script will read the email and password from `Login.txt`.
   - It will navigate to the BeatStars login page and log in using the provided credentials.
   - The script will upload the .wav file (and stems if present).
   - It will then fill in the basic information such as the track title.

## Important Notes

- Ensure the correct paths are specified for `chromedriver.exe` and the files to be uploaded.
- The script uses explicit waits to handle page loading times. Adjust these waits if necessary.
- The current implementation includes `time.sleep` for some waits. A more robust solution with explicit waits is recommended for production use.

## Contributions

Contributions are welcome! Please fork this repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

