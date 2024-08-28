import selenium
import time
import sys
import word_proc
import streamlit as st
import format_words
from driver_stuff import get_chrome_webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def open_login_page(driver):
    driver.get('https://myaccount.nytimes.com/auth/enter-email?redirect_uri=https%3A%2F%2Fwww.nytimes.com%2Fpuzzles%2Fspelling-bee&amp;response_type=cookie&amp;client_id=games&amp;application=crosswords&amp;asset=navigation-bar')
    return driver 
def solve():
    driver = None
    try:
        driver = get_chrome_webdriver()
        url = 'https://www.nytimes.com/puzzles/spelling-bee'
        driver.get(url)
        # commented out section is for the purr-blocker, I think it is some anit-scraping thing
        """
        element = driver.find_element(By.XPATH,"//div[@class='purr-blocker-card pz-hide-games-app pz-hide-newsreader']")
        driver.execute_script("arguments[0].style.visibility='hidden'", element)
        """
    except Exception as e:
        print(f'Unable to open browser, please check your browser and try again. {e}')
        st.write('could not solve the wordle, sorry about that... :-(')
        return
    btns = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'button')))
    found = False
    for btn in btns:
        if btn.text.lower() == 'play':
            found = True
            driver.execute_script("arguments[0].click();",btn)
            
    if not found:
        print('unable to get todays spelling-bee, please try again')

    middle_letter = driver.find_element(By.XPATH,"//*[@class='cell-letter' or @class='center']")
    middle_letter = middle_letter.get_attribute('innerHTML')

    good_letters, btns = word_proc.get_good_letters_and_buttons(driver)
    bad_letters = word_proc.get_bad_letters(good_letters)
    # get list of english dictionary words
    words = word_proc.get_words()
    good_words = word_proc.get_good_words(bad_letters, words,middle_letter)
    # print hive
    outer_letters = ""
    for letter in good_letters:
        if letter != middle_letter:
            outer_letters += letter.upper()
            outer_letters += " "
    st.write(f'outerletters: :green[{outer_letters}]')

    st.write(f'middle letter: :orange[{middle_letter.upper()}]')
    format_words.format_words(good_words, good_letters, middle_letter)
    print(good_words)
    driver.close()
 
if __name__ == '__main__':
    solve()
