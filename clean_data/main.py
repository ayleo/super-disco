import os
import re

path = "PATH_HERE" 
# Replace this with the path to the directory containing the folders
finished_path = "PATH_HERE"
# Replace this with the path to the directory where you want the finished.txt file to be saved,
# make sure it isn't in the same directory as the folders

url_pattern = r'URL:\s*([^\s]+)'
email_pattern = r'Login:\s*([^\s]+)'
password_pattern = r'Password:\s*([^\s]+)'

# Loop through the files in the directory and print the content of the file that starts with "passwords"
for file in os.listdir(path):
    os.chdir(path + "/" + file)
    print(os.getcwd())
    for i in os.listdir():
        if i.startswith("passwords"):
            with open(i, "r") as files:
                logs = files.read()
                urls = re.findall(url_pattern, logs)
                emails = re.findall(email_pattern, logs)
                passwords = re.findall(password_pattern, logs)
                combined_lists = [f"{urls}:{emails}:{passwords}"
                                  for urls, emails, passwords in zip(urls, emails, passwords)]
                with open(finished_path, "a") as filess:
                    for item in combined_lists:
                        filess.write(f"{item}\n")
