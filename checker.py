from selenium import webdriver
from selenium.webdriver.common.by import By


def fragment_checker(username):
    try:
        driver = webdriver.Firefox()
        try:
            driver.get(f'https://fragment.com/username/{username}')
            content = driver.find_element(By.CLASS_NAME, 'tm-section-header-status')
            if content.text == 'Taken':
                print(f'@{username} is taken')
            elif content.text in ['Available','On auction','For sale']:
                price = driver.find_element(By.CLASS_NAME, 'table-cell-value.tm-value.icon-before.icon-ton')
                print(f'@{username} is {content.text.lower()} for {price}')
            elif content.text == 'Sold':
                price = driver.find_element(By.CLASS_NAME, 'table-cell-value.tm-value.icon-before.icon-ton')
                print(f'@{username} has been sold for {price}')
        except:
            driver.get(f'https://fragment.com/?query={username}')
            print(f'@{username} is not used / not available')
    except Exception as e:
        print(e)
    finally:
        driver.quit()
