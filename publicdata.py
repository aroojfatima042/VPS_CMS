import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('Project2.db', check_same_thread=False)
c = conn.cursor()

# Register Complaints Table
def create_complaints_table():
    c.execute('CREATE TABLE IF NOT EXISTS complaints_table(crime_date INT, complaint_by TEXT, address NVARCHAR, phone INT, location NVARCHAR, comments NVARCHAR)')

# Public User data insertion
def add_complaints_data(crime_date, complaint_by, address, phone, location, comments):
    c.execute('INSERT INTO complaints_table(crime_date, complaint_by, address, phone, location, comments) VALUES(?,?,?,?,?,?)', (crime_date, complaint_by, address, phone, location, comments))
    conn.commit()

def create_missing_table():
    c.execute('CREATE TABLE IF NOT EXISTS missing_report_table(crime_date1 INT, complaint_by1 TEXT, address1 NVARCHAR, phone1 INT, last_location NVARCHAR, comments1 NVARCHAR)')

# Public User data insertion
def add_missing_data(crime_date1, complaint_by1, address1, phone1, last_location, comments1):
    c.execute('INSERT INTO missing_report_table(crime_date1, complaint_by1, address1, phone1, last_location, comments1) VALUES(?,?,?,?,?,?)', (crime_date1, complaint_by1, address1, phone1, last_location, comments1))
    conn.commit()

def create_feedback_table():
    c.execute('CREATE TABLE IF NOT EXISTS feedback_table(issue TEXT, opinion TEXT)')

# Public User data insertion
def add_feedback_data(issue, opinion):
    c.execute('INSERT INTO feedback_table(issue, opinion) VALUES(?,?)', (issue, opinion))
    conn.commit()

def view_all_complaints():
    c.execute('SELECT * FROM complaints_table')
    data4 = c.fetchall()
    return data4

    # Viewing all the usernames and password hashes
def view_all_missing():
    c.execute('SELECT * FROM missing_report_table')
    data5 = c.fetchall()
    return data5

def view_all_feedback():
    c.execute('SELECT * FROM feedback_table')
    data6 = c.fetchall()
    return data6

def app():
    # Other Heading
    st.warning('------------------------------------------- " USER " -------------------------------------------')
    st.text(" ")

    menu4 = ["-", "Register Complaints", "Missing Person Report", "My Complaints", "Feedback Form"]
    choice4 = st.selectbox("Select option", menu4)

    if choice4 == "Register Complaints":
        crime_date = st.text_input('Enter Crime Date (yyyy/mm/dd) : ')
        complaint_by = st.text_input('Enter Name of complainee : ')
        address = st.text_input('Enter Complainee Address :')
        phone = st.text_input('Enter Complainee Phone No :')
        location = st.text_input('Enter the location of crime :')
        comments = st.text_input('Any detailed information :')

        if st.button("Register"):
            create_complaints_table()
            add_complaints_data(crime_date, complaint_by, address, phone, location, comments)
            st.success("You have successfully register your complaint. ")

    elif choice4 == "Missing Person Report":
        crime_date1 = st.text_input('Enter Crime Date (yyyy/mm/dd) : ')
        complaint_by1 = st.text_input('Enter Name of complainee : ')
        address1 = st.text_input('Enter Complainee Address :')
        phone1 = st.text_input('Enter Complainee Phone No :')
        last_location = st.text_input('Enter the last location of the missing person :')
        comments1 = st.text_input('Any detailed information :')

        if st.button("Report"):
            create_missing_table()
            add_missing_data(crime_date1, complaint_by1, address1, phone1, last_location, comments1)
            st.success("Reported successfully.")

    elif choice4 == "My Complaints":
        task = st.selectbox("Complaints", ["General Reports", "Missing Reports"])
        if task == "General Reports":
            st.subheader("My All Complaints")
            user_result2 = view_all_complaints()
            clean_db_2 = pd.DataFrame(user_result2,
                                      columns=["crime_date", "complaint_by", "address", "phone", "location",
                                               "comments"])
            st.dataframe(clean_db_2)

        # Want to see all the profiles ?
        elif task == "Missing Reports":
            st.subheader("All Missing Reports")
            user_result_3 = view_all_missing()
            clean_db3 = pd.DataFrame(user_result_3,
                                     columns=["crime_date1", "complaint_by1", "address1", "phone1", "last_location",
                                              "comments1"])
            st.dataframe(clean_db3)

    elif choice4 == "Feedback Form":
        issue = st.text_input('Enter the issue here : ')
        opinion = st.text_input('Enter your opinion here : ')

        if st.button("Submit"):
            create_feedback_table()
            add_feedback_data(issue, opinion)
            st.success("Successful.")