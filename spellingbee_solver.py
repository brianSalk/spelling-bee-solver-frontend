import solve
import datetime
import streamlit as st


if __name__ == "__main__":
    st.title("Get the words to todays NYT spelling bee")
    if st.button(f"get answers for spelling bee {datetime.date.today()}"):
        st.write("solving the spelling bee")
        solve.solve()
    with st.sidebar:
        st.title("created by Brian Salkas")
        st.header("Contribute")
        st.write("missing a word and/or contains invalid word?")
        st.write("open an issue or submit a pull request [here](https://github.com/brianSalk/spelling-bee-solver-frontend)")
