import solve
import streamlit as st
browser = st.radio('browser used to solve spellingbee', ['firefox', 'chrome'])
st.write(f'Sove todays spelling bee using {browser}')
login = st.checkbox('I have a NYT account')
if login:
    st.write(f'you will be redirected to the NYT loggin page in a new {browser} window')
if st.button('Solve todays spelling bee'):
    if login:
        st.write(f'Once you log into your account in the new {browser} window, click the checkbox below')
        res = st.checkbox('I am logged in')
    solve.solve(browser,login)
