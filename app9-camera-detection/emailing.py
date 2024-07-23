import smtplib
from email.message import EmailMessage
from PIL import Image


SENDER = "yourgmail@gmail.com"
password = "yourpassword"
receiver = "yourgmail@gmail.com"


def send_email(image_path):
    print("send_email func started")
    email_message = EmailMessage()
    email_message["Subject"] = "Person detected"
    email_message["From"] = SENDER
    email_message["To"] = receiver
    # email_message.set_content("New person detected in your house")

    with open(image_path, "rb") as file:
        content = file.read()

    image_type = Image.open(image_path).format.lower()
    email_message.add_attachment(content, maintype="image", subtype=image_type)


    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, password)
    gmail.send_message(email_message)
    print("Email sent")
    gmail.quit()
    print("send_email func ended")


if __name__ == "__main__":
    send_email(image_path="images/4.png")