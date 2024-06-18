from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import glob

# Setup Chrome WebDriver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

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
    
# Function to get .wav, stem files (.zip or .rar), and artwork (.jpeg or .jpg or.png) files
def get_files(directory):
    wav = glob.glob(os.path.join(directory, "*.wav"))
    stems = glob.glob(os.path.join(directory, "*.zip")) + glob.glob(os.path.join(directory, "*.rar"))
    artwork = glob.glob(os.path.join(directory, "*.jpeg")) + glob.glob(os.path.join(directory, "*.jpg")) + glob.glob(os.path.join(directory, "*.png"))
    
    if not wav:
        raise FileNotFoundError("No .wav files found in the specified directory.")
    
    return wav, stems, artwork
    
#Upload a track with the attached files(Must have .wav at least)
def upload_track(driver, wav, stems):
    wait = WebDriverWait(driver, 50)
    
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
    drag_and_drop_input.send_keys(wav)
    print(f"Uploaded wav file")
    
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
        drag_and_drop_input_stems.send_keys(stems) 
        print(f"Uploaded stems file")
    else:
        print("No stems found. Skipping stem upload.")
        
     # Wait for the play button to turn blue (example of checking for a specific class change)
    def is_play_button_blue(driver):
        play_button = driver.find_element(By.XPATH, "//*[@id='cdk-drop-list-2']/studio-form-file-box/div/div/div[2]/studio-button-play-item/div/bs-square-button")
        return 'ng-star-inserted' in play_button.get_attribute('class')  # Change 'blue-class' to the actual class name

    wait.until(is_play_button_blue)
    print("Done creating a tagged audio")
    
    # Sleep to observe the final state
    time.sleep(50)  # Sleep for 10 seconds


"""# Function to add basic info and Metadata
def basic info:
    #check if user wants to add basic info 
    if yes
        #fill title 
        #fill description
    
    """
    
    
"""# Function to publish track
def publish_track(driver):
    
    # Wait for the "Publish" button to be clickable using the provided XPath
    publish_button_input = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/studio-root/div/ng-component/studio-page-container/div/form/studio-inventory-form-holder/div/studio-panel/div/div/div/bs-square-button[2]/button")))
    print("Publish input located, attempting to Publish file...")
    
    
    # Sleep to observe the final state
    time.sleep(50)  # Sleep for 10 seconds"""
    

try:
    # Get email and password from Login.txt
    email, password = get_credentials('Login.txt')
    
    # Get .wav, stem, and artwork files from the specified directory
    wav, stems, artwork = get_files('C:/Users/aiman/Documents/BeatStarsSingleClick/Files To Upload') 
    
    # Call the login function
    beatstars_sign_in(driver, email, password)
    
    # Call the function to upload the track
    upload_track(driver, wav, stems)
    
    # Call the function to publish the track
    #publish_track(driver)
    
finally:
    # Quit the driver
    driver.quit()
