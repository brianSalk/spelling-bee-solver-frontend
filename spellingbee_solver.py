import solve
import datetime
import streamlit as st
import solve_custom

if __name__ == "__main__":
    st.title("Get the words to todays NYT spelling bee")
    if st.button(f"get answers for spelling bee {datetime.date.today()}"):
        st.write("solving the spelling bee")
        solve.solve()
    vert_space = '<div style="padding: 100px 5px;"></div>'
    st.markdown(vert_space, unsafe_allow_html=True)
    st.title("Get words for custom spelling bee")
    gl = st.text_input('good letters',max_chars=6)
    ml=st.text_input('middle letter', max_chars=1)
    gl += ml
    if st.button('get answers for custom'):
        solve_custom.solve(gl,ml)


    with st.sidebar:
        st.title("created by Brian Salkas")
        st.header("Contribute")
        st.write("missing a word and/or contains invalid word?")
        st.write("open an issue or submit a pull request [here](https://github.com/brianSalk/spelling-bee-solver-frontend)")

