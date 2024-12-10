from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # Pillow library should be installed
import datetime

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")

        # Main frame
        main_frame = Frame(self.root, bd=4, bg='powder blue', width=610)
        main_frame.pack()

        # Load and resize the image
        img_chat = Image.open(r'college_images\bot1.jpg')
        img_chat = img_chat.resize((200, 70), Image.LANCZOS)
        self.phot = ImageTk.PhotoImage(img_chat)

        # Title label with image and text
        Title_label = Label(main_frame, bd=3, relief=RAISED, anchor='nw', compound=LEFT,
                            image=self.phot, text='CHAT ME', font=('arial', 30, 'bold'), 
                            fg='green', bg='white')
        Title_label.pack(side=TOP)

        # Scrollbar and Text widget
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=5, relief=RAISED, font=('arial', 14),
                         yscrollcommand=self.scroll_y.set)
        self.scroll_y.config(command=self.text.yview)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        # Button frame
        btn_frame = Frame(self.root, bd=4, bg='white', width=730)
        btn_frame.pack()

        label_1 = Label(btn_frame, text="Type Something", font=('arial', 14, 'bold'), fg='green', bg='white')
        label_1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = ttk.Entry(btn_frame, width=40, font=('times new roman', 16, 'bold'))
        self.entry.grid(row=0, column=1, padx=5, sticky=W)

        self.send = Button(btn_frame, text="Send>>", command=self.send, font=('arial', 15, 'bold'), width=8, bg='green')
        self.send.grid(row=0, column=2, padx=5, sticky=W)

        self.clear = Button(btn_frame, text="Clear Data", command=self.clear_text, font=('arial', 14, 'bold'), width=8, bg='yellow')
        self.clear.grid(row=1, column=0, padx=5, sticky=W)

        self.msg = ''
        self.label_l1 = Label(btn_frame, text=self.msg, font=('arial', 14, 'bold'), fg='red', bg='white')
        self.label_l1.grid(row=1, column=1, padx=5, sticky=W)

        # Greet the user based on time
        self.greet_user()


    # ============================FUNCTION DECLARATION===================================
    
    def greet_user(self):
        """Function to greet the user based on the current time."""
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            greeting = "Good Morning!"
        elif 12 <= hour < 18:
            greeting = "Good Afternoon!"
        else:
            greeting = "Good Evening!"
        
        self.text.insert(END, f"\nBot: {greeting} How can I assist you today?\n")

    def send(self):
        user_input = self.entry.get().strip()
        if user_input == '':
            self.msg = 'Enter some input'
            self.label_l1.config(text=self.msg, fg='red')
        else:
            self.msg = ''
            self.label_l1.config(text=self.msg, fg='red')
            self.text.insert(END, '\n\t\t\tYou: ' + user_input)

            # Check for specific responses
            if user_input.lower() in ['hello', 'hi']:
                self.text.insert(END, '\nBot: Hi! How can I assist you with the Smart Attendance system?')
            
            elif user_input.lower() == 'who created you':
                self.text.insert(END, '\nBot: I was created by Yuvraj Singh as part of a Smart Attendance project.')
            
            elif 'face recognition' in user_input.lower():
                self.text.insert(END, '\nBot: This system uses face recognition to mark attendance automatically by identifying registered faces in real-time.')

            elif 'attendance' in user_input.lower():
                self.text.insert(END, '\nBot: This project is designed to track attendance by detecting faces and matching them with a database and storing th attendance  in the CSV file .')

            elif 'project' in user_input.lower() and 'explain' in user_input.lower():
                self.text.insert(END, '\nBot: This Smart Attendance project uses machine learning and face recognition technology to mark attendance efficiently and accurately. It relies on OpenCV, SQL, and deep learning models to perform face recognition.')

            elif 'database' in user_input.lower() or 'store' in user_input.lower() or 'store' in user_input.lower():
                self.text.insert(END, '\nBot: The system stores attendance records in an SQL database. It keeps track of each entry and allows for easy retrieval.')

            elif 'accuracy' in user_input.lower():
                self.text.insert(END, '\nBot: The accuracy depends on factors like lighting and facial angle. Regular updates to the face data help improve accuracy.')

            elif 'real-time feedback' in user_input.lower():
                self.text.insert(END, '\nBot: The chatbot can give real-time feedback if a face is recognized or if there is an issue with recognition.')

            elif 'time' in user_input.lower() or 'what time is it' in user_input.lower():
                current_time = datetime.datetime.now().strftime('%I:%M %p')
                self.text.insert(END, f'\nBot: The current time is {current_time}.')

            else:
                self.text.insert(END, "\nBot: Sorry, I didn't understand that. Can you ask something related to the Smart Attendance project?")

            # Clear the entry box after sending
            self.entry.delete(0, END)

    def clear_text(self):
        """Function to clear the Text widget."""
        self.text.delete('1.0', END)

if __name__ == '__main__':
    root = Tk()
    obj = ChatBot(root)
    root.mainloop()
