import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('Project2.db', check_same_thread=False)
c = conn.cursor()



def app():

    menu1 = ["-", "Admin", "User"]
    choice1 = st.selectbox("User Selection", menu1)

    if choice1 == "Admin":
        st.warning('------------------------------------------- " USER " -------------------------------------------')

        st.subheader("Fill below the requirements AGAIN.")

        #def authenticate(username, password):
            #return username == "admin123" and password == "admin456"

        def authenticate(password2):
            return password2 == "admin789"

        password2 = st.text_input("Passowrd", type="password", key=2)

        #username = st.text_input('Admin_Name')
        #password = st.text_input("password", type='password')

        if st.checkbox("Login"):
            #if authenticate(username, password):
            if authenticate(password2):
                st.success('You are Successfully Login as Admin !')

                st.text("")

                st.subheader("All Missing Reports")
                from publicdata import view_all_missing
                file1 = view_all_missing()
                clean_db8 = pd.DataFrame(file1,
                                         columns=["crime_date1", "complaint_by1", "address1", "phone1", "last_location",
                                                  "comments1"])
                st.dataframe(clean_db8)

                st.text("")

                st.subheader("All Complaints Reported")
                from publicdata import view_all_complaints
                file1 = view_all_complaints()
                clean_db9 = pd.DataFrame(file1,
                                         columns=["crime_date", "complaint_by", "address", "phone", "location",
                                                  "comments"])
                st.dataframe(clean_db9)

                st.text("")

                st.subheader("All Feedback Forms")
                from publicdata import view_all_feedback
                file1 = view_all_feedback()
                clean_db9 = pd.DataFrame(file1,
                                         columns=["issue", "opinion"])
                st.dataframe(clean_db9)

    elif choice1 == "User":
        # Other Heading
        st.warning('------------------------------------------- " USER " -------------------------------------------')
        st.text(" ")

        import publicdata

        PAGES = {
            "Profile": publicdata
        }
        selection = st.radio("Go to", list(PAGES.keys()))
        page = PAGES[selection]
        page.app()