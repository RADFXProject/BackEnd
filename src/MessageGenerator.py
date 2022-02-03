import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class MessageGenerator():
    radfx_Address = "RadFxProject@hotmail.com"
    #adjust this to actual password when not on github
    radfx_Password = "dummy password"

    def generateMessage(tar_address, text, text_subject):
        radfx_Address = MessageGenerator.radfx_Address       
        radfx_Password = MessageGenerator.radfx_Password      
        target_Address = tar_address  

        host_Address = 'smtp-mail.outlook.com'
        host_Port = 587             

        server = smtplib.SMTP(host=host_Address, port=host_Port)
        server.starttls()
        server.login(radfx_Address, radfx_Password)

        message = MIMEMultipart("alternative")

        message['From'] = radfx_Address
        message['To'] = target_Address
        message['Subject'] = text_subject

        html = text

        htmlPart = MIMEText(html, 'html')

        message.attach(htmlPart)

        server.send_message(message)
        server.quit()
        return


    def updateTester():
        t_subject = "Schedule Change Alert"
        m_text = """<html>
            <head>Good evening,</head>
            <body>
                <p style='color:black;'>A change has been made to your testing submission. Log into https://radfx-radfxproject.vercel.app/ to check and verify any changes. If you have any issues with the new testing date please notify us at RadFxProject@hotmail.com at your earliest convience.</p>
                <p>Sincerily,</p>
                <p>RadFx Team</p>
            </body>
        </html>"""
        t_address = "RadFxProject@hotmail.com"   

        MessageGenerator.generateMessage(t_address, m_text, t_subject)
        return

    def welcomeTester(target):
        t_subject = "Welcome To RADFX"
        m_text = """<html>
            <head>Good evening,</head>
            <body>
                <p style='color:black;'>Thank you for creating a tester account with RADFX.</p>
                <p>Sincerily,</p>
                <p>RadFx Team</p>
            </body>
        </html>"""
        t_address = target  

        MessageGenerator.generateMessage(t_address, m_text, t_subject)
        return

    def notifyTester():
        t_subject = "Submission Notification"
        m_text = """<html>
            <head>Good evening,</head>
            <body>
                <p style='color:black;'>Thank you for submitting a test to RADFX. You will be notified shortly when you have been placed on the schedule.</p>
                <p>Sincerily,</p>
                <p>RadFx Team</p>
            </body>
        </html>"""
        t_address = "RadFxProject@hotmail.com"   

        MessageGenerator.generateMessage(t_address, m_text, t_subject)
        return
