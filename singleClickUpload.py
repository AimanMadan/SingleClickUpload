import os
import glob
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to get .wav, stem files, and artwork files from provided paths
def get_files(wav_path, stem_path):
    wav = [wav_path]
    stems = [stem_path] if stem_path else []
    title = os.path.splitext(os.path.basename(wav[0]))[0] if wav else None
    return wav, stems, title

# Function to get email and password from a text file
def get_credentials(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"The file {filename} does not exist.")
    with open(filename, 'r') as file:
        lines = file.readlines()
        if len(lines) < 2:
            raise ValueError("The file should contain at least two lines: the email and the password.")
        email = lines[0].strip()
        password = lines[1].strip()
    return email, password

# Function to log into Beatstars
def beatstars_sign_in(driver, email, password):
    # Open BeatStars website
    driver.get("https://www.beatstars.com/dashboard")

    wait = WebDriverWait(driver, 10)
    
    '''
    SINCE COOKIES ARE CREATED THIS TIME YOU DO NOT NEED TO KEEP SINGNING IN
    DOING TWO STEP VERIFICATION
    JUST DO IT ONCE WITH YOUR BROWSER!
    
    
    # Wait for the email input to be present and visible, then enter email
    email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type your email or username']")))
    print(f"Located email input with placeholder: {email_input.get_attribute('placeholder')}")
        
    # Clear the input field before entering text
    email_input.clear()
        
    # Enter the email
    email_input.send_keys(email)
    print(f"Entered email: {email}")

    # Wait for the "Continue" button to be clickable using the provided XPath
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='btn-submit-oath']")))
    print("Continue button located, attempting to click...")
    # Click the "Continue" button
    continue_button.click()

    # Wait for the password input to be present and visible, then enter password
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='userPassword']")))
    print(f"Located password input with placeholder: {password_input.get_attribute('placeholder')}")
        
    # Clear the input field before entering text
    password_input.clear()
        
    # Enter the password
    password_input.send_keys(password)

    # Check if password was entered correctly
    entered_password = password_input.get_attribute('value')
    if entered_password != password:
        raise Exception("Password was not entered correctly")
        
    # Wait for the "Continue" button to be clickable using the provided XPath
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='btn-submit-oath']")))
    print("Continue button located, attempting to click...")
    # Click the "Continue" button
    continue_button.click()
    '''
#Upload a track with the attached files (Must have .wav at least)
def upload_track(driver, wav, stems):
    wait = WebDriverWait(driver, 10)
    
    # Wait for the "Create +" button to be clickable using the provided XPath
    create_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app-body']/mp-root/mp-main-menu-top-nav/header/div/bs-container-grid[1]/div/div[3]/div/bs-menu-more-options/div/bs-square-button/button")))
    print("Create + button located, attempting to click...")
    # Click the "Create +" button
    create_button.click()

    # Wait for the "Create Track" button to be clickable using the provided XPath
    create_track_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='mat-menu-panel-9']/div/bs-external-action-option[1]/button")))
    print("Create Track button located, attempting to click...")
    # Click the "Create Track" button
    create_track_button.click()
        
    # Wait for the "Upload wav" button to be clickable using the provided XPath
    upload_wav_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cdk-drop-list-0']/studio-form-file-box/div/div/div[2]/bs-upload-button/bs-universal-upload-button/div/div/bs-square-button/button")))
    print("Upload wav button located, attempting to click...")
    # Click the "Upload" button
    upload_wav_button.click()
    
    # Wait for the "Drag & Drop" button to be clickable using the provided XPath
    drag_and_drop_input = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='uppy-drag-drop']/div/button/input")))
    print("Drag & Drop input located, attempting to upload file...")
    
    # Upload the .wav file
    drag_and_drop_input.send_keys(wav[0])
    print(f"Uploaded wav file: {wav[0]}")
    
    # Check if stems are present and upload them
    if stems:
        # Wait for the "Upload stems" button to be clickable using the provided XPath
        upload_stems_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='cdk-drop-list-40']/studio-form-file-box/div/div/div[2]/bs-upload-button/bs-universal-upload-button/div/div/bs-square-button/button")))
        print("Upload stems button located, attempting to click...")
        # Click the "Upload" button
        upload_stems_button.click()
        
        # Wait for the "Drag & Drop" input to be present using the provided XPath
        drag_and_drop_input_stems = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='uppy-drag-drop']/div/button/input")))
        print("Drag & Drop input for stems located, attempting to upload file...")

        # Upload the stem file
        drag_and_drop_input_stems.send_keys(stems[0])
        print(f"Uploaded stems file: {stems[0]}")
    else:
        print("No stems found. Skipping stem upload.")
    
    # Sleep to wait for the upload to finish #Need to find a better way!!!
    print("Waiting for the upload process to complete...")
    time.sleep(20)  # Sleep for 20 seconds

# Function to add basic info and Metadata
def basic_info(driver, title):
    wait = WebDriverWait(driver, 10)
    
    # Use the full XPath to locate the "Basic Info" tab
    basic_info_tab = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/studio-root/div/ng-component/studio-page-container/div/form/studio-inventory-form-holder/div/studio-panel/div/mat-tab-group/mat-tab-header/div/div/div/div[2]")))
    print("Basic Info tab located, attempting to click...")
    basic_info_tab.click()
    print("Filling Basic Info...")
    
    # Use the full XPath to locate the title input
    title_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/studio-root/div/ng-component/studio-page-container/div/form/studio-inventory-form-holder/div/studio-panel/div/studio-wrapper-track-basic-info/studio-inventory-form-basic-info/div/div[2]/div/div[1]/bs-text-input/input")))
    print(f"Located title input with placeholder: {title_input.get_attribute('placeholder')}")
    
    # Clear the input field before entering text
    title_input.clear()

    # Enter the title
    title_input.send_keys(title)
    print(f"Entered track title: {title}")
    
    time.sleep(10)  # Sleep for 10 seconds

def run_script(wav_path, stem_path):
    try:
        # Get email and password from Login.txt
        email, password = get_credentials('Login.txt')
        
        # Get .wav, stem, and title from the provided file paths
        wav, stems, title = get_files(wav_path, stem_path)
        
        # Setup Chrome WebDriver with headless option
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')  # Necessary for Windows

        # Create a custom user data directory
        user_data_dir = os.path.join(os.getcwd(), 'user_data')
        os.makedirs(user_data_dir, exist_ok=True)
        options.add_argument(f'--user-data-dir={user_data_dir}')

        # Setup Chrome WebDriver
        service = Service(executable_path="chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=options)
        
        # Call the login function
        beatstars_sign_in(driver, email, password)
        
        # Call the function to upload the track
        upload_track(driver, wav, stems)
        
        # Call the function to fill basic info
        basic_info(driver, title)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_script('path_to_wav', 'path_to_stem')