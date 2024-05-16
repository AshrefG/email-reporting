import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = sender_entry.get()
    receiver_email = receiver_entry.get()
    password = "your_email_password"
    
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Daily Report"
    body = "Your daily report content here."
    message.attach(MIMEText(body, "plain"))
    
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
    messagebox.showinfo("Success", "Email sent successfully!")

def launch_gui():
    global sender_entry, receiver_entry
    root = tk.Tk()
    root.title("Email Report Sender")
    
    sender_label = tk.Label(root, text="Sender Email:")
    sender_label.pack()
    sender_entry = tk.Entry(root)
    sender_entry.pack()
    
    receiver_label = tk.Label(root, text="Receiver Email:")
    receiver_label.pack()
    receiver_entry = tk.Entry(root)
    receiver_entry.pack()
    
    send_button = tk.Button(root, text="Send Email", command=send_email)
    send_button.pack()
    
    root.mainloop()

# Schedule the email to be sent daily at a specific time (e.g., 8:00 AM)
schedule.every().day.at("08:00").do(send_email)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)

# Uncomment the line below to launch the GUI
launch_gui()