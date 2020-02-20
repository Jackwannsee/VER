from selenium import webdriver
import time
import json
import smtplib

#password and username
with open ("credentials/credentials.json","r+") as jf:
    creds = json.load(jf)

b = webdriver.Chrome()
b.get("https://accounts.veracross.eu/asb/portals/login")

def SendEmail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(creds["YourEmailUsername"], creds["YourEmailPassword"])

    Subject = 'You have a new grades go check'
    Body = ('Hey you have received a new grade please go check https://accounts.veracross.eu/asb/portals/login\n' +
            "New Grades:\n\n" + ''.join(map(str, NamesGrades)))

    Email = f"subject: {Subject}\n\n{Body}"

    server.sendmail\
    (
        creds["YourEmailUsername"],
        creds["Recipient"],
        Email
    )

    print("Email Sent")

NamesGrades = []
def Run():
    Username = b.find_element_by_id("username")
    Username.send_keys(creds["username"])

    Password = b.find_element_by_id("password")
    Password.send_keys(creds["password"])

    Login = b.find_element_by_id("recaptcha")
    Login.click()

    b.implicitly_wait(3)

    CourseName = b.find_elements_by_class_name("course-name")
    Badges = b.find_elements_by_class_name("notification-badge")

    grades = 0
    Notification = 0
    for i in Badges:
        if i.text.split(' ')[0] != "0":
            print(CourseName[grades].text + " " + i.text.split(' ')[0])
            NamesGrades.append(CourseName[grades].text + " " + i.text.split(' ')[0] + "\n")
            Notification = 1

        grades = grades + 1

    if Notification != 0:
        SendEmail()
        b.close()

    else:
        b.close()


while True:
    Run()
    time.sleep(300)
