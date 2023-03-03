import solve
import datetime
import streamlit as st
# if clicked solve!
st.title("Get the words to todays NYT spelling bee")
if st.button(f"get answers for spelling bee {datetime.date.today()}"):
    st.write("solving the spelling bee")
    solve.solve()
