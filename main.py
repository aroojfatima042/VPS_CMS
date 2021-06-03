# Adding Libraries
import streamlit as st
import pandas as pd
import hashlib
from PIL import Image
import sqlite3

# Function to make password hashes
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

# Function to check those password hashes
def check_hashes(password, hashed_text):
    if make_hashes(password) != hashed_text:
        return False
    return hashed_text

# Building connection with sqlite3
conn = sqlite3.connect('Project2.db')
c = conn.cursor()

# Public table data
def create_public_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS public_userstable(new_user1 TEXT, new_password1 TEXT, mobile INT, email NVARCHAR)')


# Public User data insertion
def add_public_userdata(new_user1, new_password1, mobile, email):
    c.execute('INSERT INTO public_userstable(new_user1, new_password1, mobile, email) VALUES(?,?,?,?)',(new_user1, new_password1, mobile, email))
    conn.commit()


# Login Function
def login_public_user(new_user1, new_password1):
    c.execute('SELECT * FROM public_userstable WHERE new_user1 =? AND new_password1 = ?',(new_user1, new_password1))
    data = c.fetchall()
    return data

# Viewing all the public user data
def view_all_public_users():
    c.execute('SELECT new_user1 FROM public_userstable')
    data2 = c.fetchall()
    return  data2

# Defining the main function of this page
def main():
    """REGISTER YOURSELF HERE..."""
    # menu to choose the page
    menu = ["Home", "Login", "SignUp", "About Me"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Home Page 'Function
    if choice == "Home":

        # Main Heading
        st.success('------------ " Virtual Police Station and Crime Management System (VPS & CMS) " ------------')

        # Image Code
        image = Image.open('police line.jpg')
        st.image(image, width=700)

        # Other Heading
        st.warning('------------------------------------------ " HOME PAGE " ------------------------------------------')

        # Detail to register or login the accounts
        st.subheader("Are you a New User ?")
        st.text("If you are a new user and you need to use this effective application then you just need to")
        st.text("Register yourself by clicking the Signup option in the menu sidebar.")
        st.subheader("Are you an Existing User ?")
        st.text("If you are an existing user then you all need to just login in your account by clicking the")
        st.text("LoginIn option.")

        # Information about the project
        st.warning('--------------------------------------- " ABOUT PROJECT " ---------------------------------------')
        st.text("Crime is a part of illegal activities in human life. It is quite obvious that the rate of ")
        st.text("crimes is increasing day by day in all societies across the world, but we do believe that ")
        st.text("there is a lot which can be done by both the governments and the individuals to reduce the")
        st.text(" crimes in communities. The rise of population and complex society rises the range of anti")
        st.text("-social conducts that must be restricted by the government through the military and ")
        st.text("and different organizations particularly the Police Force. There are many current crime ")
        st.text("management systems which faces several difficulties, as there is no means to report crime ")
        st.text("instantly other than phone calls, messaging or face-to-face compliant filing. This crime")
        st.text("reporting and management system is a complete web based application that permits all ")
        st.text("aspects of any crime recording system. This will help us to record, analyze, file any ")
        st.text("complaint and check about any criminal in a meaningful manner, generating fast reports.")

    # Login Function choosed from the sidebar menu
    elif choice == "Login":

        # Another Heading
        st.success('------------ " Virtual Police Station and Crime Management System (VPS & CMS) " ------------')

        # Image Code
        image = Image.open('police line.jpg')
        st.image(image, width=700)

        # Another Heading
        st.warning('---------------------------------------- " LOGIN PAGE " ----------------------------------------')

        # Details to login
        st.subheader("Login below if you are an existing user. If not, then click on the SignUp from")
        st.subheader("sidebar menu.")
        st.text(" ")

        # Login Part
        st.text(" ")
        st.sidebar.subheader("LOG INTO AN ACCOUNT")

        menu1 = ["Select option", "Admin", "User"]
        choice1 = st.sidebar.selectbox("Login Selection", menu1)

        if choice1 == "Admin":
            st.subheader("Welcome")

            def authenticate(username, password):
                return username == "admin123" and password == "admin456"

            username = st.text_input('Admin_Name')
            password = st.text_input("password", type='password')

            if st.checkbox("Login", key=1):
                if authenticate(username, password):
                    st.success('You are Successfully Login as Admin !')

                    st.subheader("User Logins")
                    user_result = view_all_public_users()
                    clean_db = pd.DataFrame(user_result, columns=["Username"])
                    st.dataframe(clean_db)

                    import admindata

                    PAGES = {
                        "Profile": admindata
                    }
                    selection = st.radio("Go to", list(PAGES.keys()))
                    page = PAGES[selection]
                    page.app()

                else:
                    st.error('The username or password you have entered is invalid.')

        elif choice1 == "User":
            new_user1 = st.sidebar.text_input("Username")
            new_password1 = st.sidebar.text_input("Password", type='password')

            # Submitting public user form
            if st.sidebar.checkbox("Login"):
                create_public_usertable()
                hashed_pswd = make_hashes(new_password1)
                result = login_public_user(new_user1, check_hashes(new_password1, hashed_pswd))

                # If you are successfully login
                if result:
                    st.sidebar.success("Successful Login of {}".format(new_user1))

                    import publicdata

                    PAGES = {
                        "Profile": publicdata
                    }
                    selection = st.radio("Go to", list(PAGES.keys()))
                    page = PAGES[selection]
                    page.app()

                # If the information provided is wrong
                else:
                    st.warning("Incorrect Username/Password")

    # If you choose the Signup option
    elif choice == "SignUp":

        # Another Heading
        st.success('------------ " Virtual Police Station and Crime Management System (VPS & CMS) " ------------')

        # Image Code
        image = Image.open('police line.jpg')
        st.image(image, width=700)

        # Another Heading
        st.warning('--------------------------------------- " SIGNUP PAGE " ---------------------------------------')

        # Details
        st.subheader("Register yourself if you are a new user.")
        st.text(" ")

        # Registration Part
        st.error("Registration Section")
        st.text(" ")

        # Creating Account
        st.subheader("CREATE A NEW ACCOUNT")
        st.subheader("Welcome fellow, Fill the following information to register yourself.")
        new_user1 = st.text_input("Username")
        new_password1 = st.text_input("Password", type='password')
        mobile = st.text_input("Mobile Number")
        email = st.text_input("Email")

        # Submit Public User form
        if st.button("Signup"):
            create_public_usertable()
            add_public_userdata(new_user1, make_hashes(new_password1), mobile, email)
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")

    elif choice == "About Me":
        st.warning("PROJECT DETAILS")
        st.text(" ")
        st.subheader("Name : AROOJ FATIMA")
        st.subheader("Roll No. : Fa19/BS-DFCS/042")
        st.subheader("Subject : PYTHON PROGRAMMING")
        st.subheader("Teacher : SIR TASEER SUALEMAN")
        st.subheader("Project Name : VPS & CMS")
        st.subheader("Detail : SEMESTER PROJECT")


# Executing main function
if __name__ == '__main__':
    main()
