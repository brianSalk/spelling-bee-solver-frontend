import solve
import streamlit as st
# if clicked solve!
st.title("Get the words to todays NYT spelling bee")
if st.button("Solve todays spelling bee!"):
    st.write("solving the spelling bee")
    solve.solve()
