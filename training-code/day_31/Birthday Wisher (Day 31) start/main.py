import smtplib

my_email = "sudheerbaditha@gmail.com"
password = "ovjq jbgu lqxq imf"

try:
    # Set up the connection with Gmail's SMTP server
    connection = smtplib.SMTP(smtp_server, port) # type: ignore
    connection.starttls()  # Secure the connection
    connection.login(user=my_email, password=password)  # Log in to your email account
    
    # Send the email
    connection.sendmail(
        from_addr=my_email,
        to_addrs="sudheerbaditha0931@gmail.com",
        msg="Subject:Hello\n\nHello there"  # Include a subject line
    )
    print("Email sent successfully!")

except Exception as e:
    print(f"Error: {e}")

finally():
    connection.close()  # Close the connection

#"ovjq jbgu lqxq imf




