import streamlit as st

def format_words(words, good_letters, middle_letter):

    middle_letter = middle_letter.lower()
    for word in words:
        word = word.lower()
        is_pangram = True
        for good_letter in good_letters: 
            if good_letter not in word:
                is_pangram = False
                break
        formatted_word = ""
        padding = ''
        if is_pangram:
            padding = '***' # pangrams appear bold and italic
        for letter in word:
            if letter == middle_letter:
                formatted_word += f':orange[{padding+letter+padding}]'
            else:
                formatted_word += f':green[{padding+letter+padding}]'
        st.write(formatted_word)

                



if __name__ == "__main__":
    words = ['UNIX', 'UNTILL', 'UNITE', 'ALTINX']
    good_letters = ['U', 'N', 'I', 'X', 'L','T', 'A']
    middle_letter = 'U'

