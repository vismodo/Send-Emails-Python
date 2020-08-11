import smtplib, ssl
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showinfo
def signin():
    global sender_email
    global password
    sender_email = username_entry.get()
    password = password_entry.get()
    global smtp_server
    global port
    server = server_name.get()
    if (server == 'Gmail'):
        smtp_server = 'smtp.gmail.com'
        port = 587
    elif (server == 'Outlook'):
        smtp_server = 'smtp.outlook.com'
        port = 587
    elif (server == 'Office 365'):
        smtp_server = 'smtp.office365.com'
        port = 587
    elif (server == 'Yahoo! Mail'):
        smtp_server = 'smtp.mail.yahoo.com'
        port = 465
    elif (server == 'Yahoo! Mail Plus'):
        smtp_server = 'plus.smtp.mail.yahoo.com'
        port = 465
    else:
        smtp_server = 'imap.mail.me.com'
        port = 993
    login.destroy()
    mail_window = tk.Tk()
    mail_window.title('Send Mail')
    global subject_box
    global message_box
    global receiver_email_entry
    reciever_label = tk.Label(mail_window, text = 'Recipients: (Separate with spaces)')
    receiver_email_entry = tk.Entry(mail_window)
    message_label = tk.Label(mail_window, text = 'Message')
    message_box = ScrolledText(mail_window)
    subject_label = tk.Label(mail_window, text = 'Subject:')
    subject_box = tk.Entry(mail_window)
    send_button = tk.Button(mail_window, text = 'Send Email', command = sendmail)
    reciever_label.pack()
    receiver_email_entry.pack()
    subject_label.pack()
    subject_box.pack()
    message_label.pack()
    message_box.pack()
    send_button.pack()
    mail_window.mainloop()
def sendmail():
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(sender_email, password)
            message = message_box.get('1.0', 'end-1c')
            receiver_email = receiver_email_entry.get().split(' ')
            server.sendmail(sender_email, receiver_email, ('Subject: ' + subject_box.get() + '\n' + message) + '\n \nSent with Python smtplib and ssl modules' )
    except Exception as e:
        showinfo('Error while sending', e)
login = tk.Tk()
login.title('Login')
username_label = tk.Label(login, text = 'Your username:')
username_entry = tk.Entry(login)
password_label = tk.Label(login, text = 'Your password:')
password_entry = tk.Entry(login)
server_label = tk.Label(login, text = 'Your SMTP server:')
list_of_servers = ['Gmail', 'Outlook', 'Office 365', 'Yahoo! Mail', 'Yahoo! Mail Plus', 'iCloud']
server_name = tk.StringVar(login)
servers_menu = tk.OptionMenu(login, server_name, *list_of_servers)
login_button = tk.Button(login, text = 'Login', command = signin)
username_label.pack()
username_entry.pack()
password_label.pack()
password_entry.pack()
server_label.pack()
server_name.set(list_of_servers[0])
servers_menu.config(width=40, font=('Helvetica', 12))
servers_menu.pack()
login_button.pack()
login.mainloop()

