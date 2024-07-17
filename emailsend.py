import smtplib 
import os


email_id = os.environ.get('EMAIL_ADDR')
email_pass = os.environ.get("EMAIL_PASS")
with smtplib.SMTP('smtp.gmail.com' , 587) as smtp  :  # 587 is port number 
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()


    # ehlo is en alternative to helo for services that suppoert the smpt services extensions 
    #in eny case helo or ehlo is must command for the smpt clien tp commence a mail transfer 

    smtp.login(email_id , email_pass) 
    subject = 'fight againest corovirus' # subject which comes in email  
    body = " hey , hi let's fight against coronavirus by starying at home " 


    msg  = f"subject : {subject} \n\n\n\n{body}"

    smtp.sendmail(email_id , 'ramiferjani66@gmail.com' , msg ) 