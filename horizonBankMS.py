import json
import random
import re
import string
import tkinter as tk
from tkinter import messagebox

class BankManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Horizon Bank Management System")
        self.root.geometry("600x500")

        self.customer_details = {"name": "","gender":"", "dob": "", "ads": "", "phno": 0, "id": "", "username": "",
                             "password": "", "balance": 0, "account_number": ""}
        # Create a frame for the main window
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        self.main_frame.pack_forget()
        #create frame for login form
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()
        self.login_frame.pack_forget()

        # create frame for register form
        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack()
        self.register_frame.pack_forget()

        # create frame for reset-password form
        self.new_login_frame = tk.Frame(self.root)
        self.new_login_frame.pack()
        self.new_login_frame.pack_forget()

        #create frame for card
        self.card_frame = tk.Frame(self.root)
        self.card_frame.pack()
        self.card_frame.pack_forget()

        # create frame for personal loan
        self.loan_frame = tk.Frame(self.root)
        self.loan_frame.pack()
        self.loan_frame.pack_forget()

        self.operations_frame = tk.Frame(self.root)
        self.operations_frame.pack()
        self.operations_frame.pack_forget()

        self.deposit_frame = tk.Frame(self.root)
        self.deposit_frame.pack()
        self.deposit_frame.pack_forget()

        self.withdraw_frame = tk.Frame(self.root)
        self.withdraw_frame.pack()
        self.withdraw_frame.pack_forget()

        #create buttons for menu items in main frame

        self.main_menu()
        # Start the mainloop
        self.root.mainloop()
    def main_menu(self):
        self.main_frame.pack()
        title_label = tk.Label(self.main_frame, text="Welcome to Horizon Bank Online", font=("Helvetica", 14, "bold"))
        title_label.pack(pady=20)
        button1 = tk.Button(self.main_frame, text="Internet Banking", command=self.setup_login)
        button1.pack(pady=5)
        button2 = tk.Button(self.main_frame, text="Credit Card", command=self.card)
        button2.pack(pady=5)
        button3 = tk.Button(self.main_frame, text="Personal Loan", command=self.get_loan)
        button3.pack(pady=5)

        self.exit_button = tk.Button(self.main_frame, text="Logout", command=self.on_window_close)
        self.exit_button.pack(pady=5)

    def register(self):
        self.login_frame.pack_forget()
        self.register_frame.pack()
        customer_details = {}
        uname = ''
        def submit_register():
            nonlocal customer_details
            nonlocal uname
            customer_details["name"] = name_entry.get()
            customer_details["gender"] = gender.get()
            dob = match_dob(dob_entry.get())
            customer_details["dob"] = dob
            customer_details["ads"] = ads_entry.get()
            phno = match_phno(phno_entry.get())
            customer_details["phno"] = phno
            aadhaar_no = match_aadhaar(id_entry.get())
            customer_details["id"] = aadhaar_no
            customer_details["username"] = username_entry.get()
            uname = customer_details["username"]
            #print(uname)
            customer_details["password"] = password_entry.get()

            acc_num = ''.join(random.choices(string.digits, k=10))
            customer_details["account_number"] = acc_num

            customer_details["balance"] = 1000

            flag = True
            while flag:
                with open("users", "a+") as file2:
                    file2.seek(0)
                    names = [line.strip() for line in file2.readlines()]
                    if uname.lower() in names:
                        messagebox.showwarning("Registration","USERNAME EXIST!! PLEASE CHOOSE ANOTHER NAME")
                        flag = False
                    elif dob is None :
                        messagebox.showwarning("Error","Dob must be in dd/mm/yyyy format")
                        flag = False
                    elif aadhaar_no is None:
                        messagebox.showwarning("Error","Incorrect Aadhaar Number")
                        flag = False
                    elif phno is None:
                        messagebox.showwarning("Error","Incorrect phone number")
                        flag = False
                    else:
                        file2.write(uname +"\n")
                        file_path = f"{uname}.json"
                        with open(file_path, "w") as jsonfile:
                            json.dump(customer_details, jsonfile)
                            messagebox.showinfo("Registration","Successfully Created your registration")
                            flag = False

        name_label = tk.Label(self.register_frame, text="Name")
        name_label.grid(row=0, column=0,pady = 5)
        name_entry = tk.Entry(self.register_frame)
        name_entry.grid(row=0, column=1,pady = 5)

        gender_label = tk.Label(self.register_frame,text = "Gender")
        gender_label.grid(row = 1,column = 0,pady = 5)
        gender = tk.IntVar()
        radiobutton_male = tk.Radiobutton(self.register_frame,text = "Male",variable = gender, value=1)
        radiobutton_male.grid(row = 1,column = 1,pady = 5)
        radiobutton_female = tk.Radiobutton(self.register_frame,text = "Female",variable=gender,value = 2)
        radiobutton_female.grid(row = 1,column = 2,pady = 5)


        dob_label = tk.Label(self.register_frame, text="Date of birth(dd/mm/yyyy)")
        dob_label.grid(row=2, column=0,pady = 5)
        dob_entry = tk.Entry(self.register_frame)
        dob_entry.grid(row=2, column=1,pady = 5)

        ads_label = tk.Label(self.register_frame, text="Address")
        ads_label.grid(row=3, column=0,pady = 5)
        ads_entry = tk.Entry(self.register_frame)
        ads_entry.grid(row=3, column=1,pady = 5)

        phno_label = tk.Label(self.register_frame, text="Phone Number")
        phno_label.grid(row=4, column=0,pady = 5)
        phno_entry = tk.Entry(self.register_frame)
        phno_entry.grid(row=4, column=1,pady = 5)

        id_label = tk.Label(self.register_frame, text="Aadhaar Number(XXXX XXXX XXXX)")
        id_label.grid(row=5, column=0,pady = 5)
        id_entry = tk.Entry(self.register_frame)
        id_entry.grid(row=5, column=1,pady = 5)

        username_label = tk.Label(self.register_frame, text="Username")
        username_label.grid(row=6, column=0,pady = 5)
        username_entry = tk.Entry(self.register_frame)
        username_entry.grid(row=6, column=1,pady = 5)

        password_label = tk.Label(self.register_frame, text="Password")
        password_label.grid(row=7, column=0,pady = 5)
        password_entry = tk.Entry(self.register_frame)
        password_entry.grid(row=7, column=1,pady = 5)

        acc_num = ''.join(random.choices(string.digits, k=10))
        customer_details["account_number"] = acc_num

        info_label = tk.Label(self.register_frame, text="You have to pay Rs.1000/- for open an account.")
        info_label.grid(row = 8,column = 1,pady = 5)

        register_submit_button = tk.Button(self.register_frame, text="Submit", command=submit_register)
        register_submit_button.grid(row = 9,column = 1,pady = 5)

        back_button = tk.Button(self.register_frame,text = "Back",command = self.__init__ )
        back_button.grid(row = 10,column = 1,pady = 5)

        def match_dob(dob):
            pattern = r"(0[1-9]|[12][0-9]|3[01])\/(0[1-9]|1[1,2])\/(19\d{2}|20[0-2][0-3])"
            match = re.search(pattern,dob)
            if match:
                return dob
        def match_aadhaar(id):
            id_pattern = r"(\d{4}) (\d{4}) (\d{4})"
            id_match = re.search(id_pattern,id)
            if id_match:
                return id
        def match_phno(phno):
            phno_pattern = r"(\d{10})"
            phno_match = re.search(phno_pattern,phno)
            if phno_match:
                return phno


    def setup_login(self):
        self.main_frame.pack_forget()
        self.card_frame.pack_forget()
        self.login_frame.pack()
        def login():
            username = username_entry.get()
            password = password_entry.get()
            if not username or not password:
                messagebox.showerror("Empty Fields", "Please enter both username and password.")
                return
            file_name = f"{username}.json"
            try:
                with open(file_name, "r") as file:
                    data = json.load(file)
                    stored_password = data.get("password")
                    if stored_password != password or password is None:
                        messagebox.showerror("Incorrect password","Password is Incorrect")
                    else:
                        messagebox.showinfo("Login Successfull","Welcome, {}".format(username))
                        self.operations(username)
                        self.login_frame.pack_forget()
                        self.main_frame.pack_forget()
                        self.register_frame.pack_forget()
                        return username
                        #self.operations_frame.pack_forget()
            except Exception as e:
                print("exception",e)

        register_label = tk.Label(self.login_frame, text="New User? Click Register.")
        register_label.pack(pady=5)
        register_button = tk.Button(self.login_frame, text="Register", command=self.register)
        register_button.pack(pady=5)

        username_label = tk.Label(self.login_frame, text="Username:")
        username_label.pack(pady=5)

        # Create an entry widget for the username field
        username_entry = tk.Entry(self.login_frame)
        username_entry.pack(pady=5)

        # Create a label for the password field
        password_label = tk.Label(self.login_frame, text="Password:")
        password_label.pack(pady=5)

        # Create an entry widget for the password field
        password_entry = tk.Entry(self.login_frame, show="*")
        password_entry.pack(pady=5)
        login_button = tk.Button(self.login_frame, text="Login", command=login)
        login_button.pack(pady= 5)

        forgot_pword_button = tk.Button(self.login_frame,text = "Forgot Password",command= self.forgot_password)
        forgot_pword_button.pack(pady = 5)

    def forgot_password(self):
        self.login_frame.pack_forget()
        self.new_login_frame.pack()
        uname_label = tk.Label(self.new_login_frame,text = "Username")
        uname_label.pack(pady = 5)
        uname_entry = tk.Entry(self.new_login_frame)
        uname_entry.pack(pady = 5)
        new_pword_label = tk.Label(self.new_login_frame,text = "New Password")
        new_pword_label.pack(pady = 5)
        new_pword_entry = tk.Entry(self.new_login_frame)
        new_pword_entry.pack(pady = 5)
        reset_button = tk.Button(self.new_login_frame,text = "Reset",command=lambda :self.reset(uname_entry.get(),new_pword_entry.get()))
        reset_button.pack(pady = 5)

    def reset(self,uname,pword):
        if not uname or not pword:
            messagebox.showerror("Empty Fields", "Please enter both username and password.")
            return
        else:
            filename = f"{uname}.json"
            try:
                with open(filename, "r") as file:
                    data = json.load(file)
                    data["password"] = pword
                with open(filename, "w") as file1:
                    json.dump(data, file1)
                    messagebox.showinfo("Success","Password reset successfully")
            except:
                messagebox.showerror("Error","Password reset failed!! Try Again")
            login_button = tk.Button(self.new_login_frame,text="Login",command=self.setup_login)
            login_button.pack(pady=5)


    def operations(self,username):
        self.main_frame.pack_forget()
        self.login_frame.pack_forget()
        self.operations_frame.pack()


        button_balance = tk.Button(self.operations_frame, text="Check Your Balance", command=lambda: self.get_balance(username))
        button_balance.pack(pady=10)
        button_deposit = tk.Button(self.operations_frame, text="Deposit", command=lambda: self.deposit(username))
        button_deposit.pack(pady=10)
        button_withdraw = tk.Button(self.operations_frame, text="Withdraw", command=lambda: self.withdraw(username))
        button_withdraw.pack(pady=10)
        button_credit = tk.Button(self.operations_frame, text = "Credit Card", command=lambda: self.get_card(username))
        button_credit.pack(pady=10)
        #tk.Button(self.operations_frame, text="Logout", command=self.login).pack(pady=5)
        Logout_button = tk.Button(self.operations_frame, text="Logout", command=self.on_window_close)
        Logout_button.pack(pady=10)

    def get_balance(self,username):
        file_name = f"{username}.json"
        try:
            with open(file_name, "r") as file:
                data = json.load(file)
                messagebox.showinfo("Balance", f"Your Account balance is Rs. {data['balance']} /- only")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Error:", e)
        '''Logout_button = tk.Button(self.operations_frame, text="Logout", command = self.root.destroy)
        Logout_button.pack(pady=10)'''

    def deposit(self, username):
        self.operations_frame.pack_forget()
        self.deposit_frame.pack()

        file_name = f"{username}.json"
        with open(file_name, "r") as file_read:
            data = json.load(file_read)
            acno = data["account_number"]
        label_acno = tk.Label(self.deposit_frame, text=f"Account Number : {acno}")
        label_acno.pack(pady=5)
        label_amount = tk.Label(self.deposit_frame, text="Amount(Rs)")
        label_amount.pack(pady=5)
        entry_amount = tk.Entry(self.deposit_frame)
        entry_amount.pack(pady=5)
        submit_button = tk.Button(self.deposit_frame, text="Submit",command=lambda: self.submit_deposit(username, entry_amount))
        submit_button.pack(pady=5)
        button_back = tk.Button(self.deposit_frame, text="Back", command=self.__init__)
        button_back.pack(pady=5)
    def submit_deposit(self,username,entry_amount):
        if not window_closed:
            amnt = entry_amount.get()
            if not amnt.isdigit():
                messagebox.showerror("Invalid Amount","Please enter a valid amount.")
                return
            file_name = f"{username}.json"
            try:
                with open(file_name, "r") as file:
                    data = json.load(file)
                    data["balance"] += float(amnt)
                    new_balance = data["balance"]
                with open(file_name, "w") as file1:
                    json.dump(data, file1)
                label_balance = tk.Label(self.deposit_frame, text=f"Balance Amount : {new_balance}")
                label_balance.pack(pady=5)
                messagebox.showinfo("Balance", f"Deposit Successfull")
            except Exception as e:
                print(f"<<<ERROR FOUND>>>{e}")
        else:
            messagebox.showwarning("Session Out","Please login again")

    def withdraw(self, username):
        self.operations_frame.pack_forget()
        self.withdraw_frame.pack()

        file_name = f"{username}.json"
        with open(file_name, "r") as file_read:
            data = json.load(file_read)
            acno = data["account_number"]
        label_acno = tk.Label(self.withdraw_frame, text=f"Account Number : {acno}")
        label_acno.pack(pady=5)
        label_amount = tk.Label(self.withdraw_frame, text="Amount(Rs)")
        label_amount.pack(pady=5)
        entry_amount = tk.Entry(self.withdraw_frame)
        entry_amount.pack(pady=5)
        submit_button = tk.Button(self.withdraw_frame, text="Submit",command=lambda: self.submit_withdraw(username, entry_amount))
        submit_button.pack(pady=5)
        button_back = tk.Button(self.withdraw_frame, text="Back", command=self.__init__)
        button_back.pack(pady=5)
        '''Logout_button = tk.Button(self.operations_frame, text="Logout", command=self.main_menu)
        Logout_button.pack(pady=10)'''
        #self.operations_frame.pack_forget()
    def submit_withdraw(self,username,entry_amount):
        if not window_closed:
            amnt = entry_amount.get()
            file_name = f"{username}.json"
            with open(file_name, "r") as file_read:
                data = json.load(file_read)
                if data["balance"] >= 1000 + int(amnt):
                    data["balance"] -= float(amnt)

                    with open(file_name, "w") as file_write:
                        json.dump(data, file_write)
                        new_balance = data["balance"]
                        label_balance = tk.Label(self.withdraw_frame, text=f"Balance Amount : {new_balance}")
                        label_balance.pack(pady=5)
                        messagebox.showinfo("Balance",f"Withdrawal is Successfull")

                        #print("Your Account balance is ", data["balance"])
                else:
                    messagebox.showerror("Withdrawal Error", "Insufficient balance for withdrawal")
        else:
            messagebox.showwarning("Session Out","Please login again")
    def card(self):
        self.main_frame.pack_forget()
        self.card_frame.pack()
        card_head_label = tk.Label(self.card_frame,text = "Credit Card:Apply online",font=("Helvetica", 12, "bold"), fg="white",bg = "pink")
        card_head_label.grid(row=0,column=0,pady = 10)
        card_line2_label = tk.Label(self.card_frame,text = "A credit card is a payment card that allows you to"
                                                     " borrow money to pay for goods and services")
        card_line2_label.grid(row = 1,column = 0,pady = 5)
        apply_button = tk.Button(self.card_frame,text = "Apply",command=self.setup_login)
        apply_button.grid(row = 3,column =0,pady = 5)
    def get_card(self,username):
        self.login_frame.pack_forget()
        self.operations_frame.pack_forget()
        self.card_frame.pack()
        income_label = tk.Label(self.card_frame,text = "Select your income")
        income_label.grid(row = 4,column = 0)
        income_list = ["<1000","1000-10000","10000-100000",">100000"]
        self.selected_option = tk.StringVar()
        self.dropdown = tk.OptionMenu(self.card_frame,self.selected_option,*income_list)
        self.dropdown.grid(row = 5,column = 0)
        card_submit_button = tk.Button(self.card_frame,text = "Submit",command=lambda :self.submit_card(username,income_list))
        card_submit_button.grid(row = 6,column = 0)
    def submit_card(self,username,income_list):
        income = self.selected_option.get()
        filename = f"{username}.json"
        with open(filename,"r") as file_read:
            data = json.load(file_read)
            current_balance = data["balance"]
        if income == income_list[0] or current_balance <= 1000:
            messagebox.showwarning("CreditCard","Sorry, Your income is low to afford a credit card")
        elif income == income_list[1] or (10000 <= current_balance >1000):
            card_label = tk.Label(self.card_frame,text = "Congrats..You are eligible for Silver Credit card")
            card_label.grid(row = 7,column = 0)
        elif income == income_list[2] and (10000 < current_balance >=100000):
            card_label = tk.Label(self.card_frame, text="Congrats..You are eligible for Gold Credit card")
            card_label.grid(row = 7,column = 0)
        elif income == income_list[3] or (100000 < current_balance >=1000000):
            card_label = tk.Label(self.card_frame, text="Congrats..You are eligible for Platinum Credit card")
            card_label.grid(row = 7,column = 0)
        else:
            card_label = tk.Label(self.card_frame, text="Please directly contact bank")
            card_label.grid(row = 7,column = 0)



    def get_loan(self):
        self.operations_frame.pack_forget()
        self.main_frame.pack_forget()
        self.loan_frame.pack()
        info_label = tk.Label(self.loan_frame,text="Please visit our nearest branch...")
        info_label.grid(row=0,column=0)
        back_button = tk.Button(self.loan_frame,text = "Back",command=self.__init__)
        back_button.grid(row=1,column = 0)

    def on_window_close(self):
        global window_closed
        window_closed = True
        self.root.destroy()
if __name__ == '__main__':
    BankManagementSystem()



