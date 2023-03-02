import solve
import streamlit as st
browser = st.radio('Please select your default browser:', ['firefox', 'chrome', 'edge'])

st.write(f'Solve todays spelling bee using {browser}')
has_loggin = st.checkbox('I have a NYT account')
if has_loggin:
    st.write("After you click \"Solve!\", you will be prompted to loggin in the new browser window that appears.")
else:
    st.write("without a NYT account I can only complete some of the puzzle")

# if clicked solve!
if st.button("Solve!"):
    try:
        driver = solve.create_driver(browser)
    except Exception:
        st.write(f'cannot find the binary path for {browser}, try using a different browser or reconfiguring your path to {browser}')
    try:
        solve.solve(driver,has_loggin)
    except Exception:
        st.write("how did I do?")
