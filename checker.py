from selenium import webdriver
from selenium.webdriver.common.by import By


def fragment_checker(username):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_options)
        try:
            driver.get(f'https://fragment.com/username/{username}')
            status = driver.find_element(By.CLASS_NAME, 'tm-section-header-status')
            if status.text == 'Taken':
                print(f'@{username} is taken')
            elif status.text in ['Available','On auction','For sale']:
                price = driver.find_element(By.CLASS_NAME, 'table-cell-value.tm-value.icon-before.icon-ton')
                print(f'@{username} is {status.text.lower()} for {price.text} TON')
            elif status.text == 'Sold':
                price = driver.find_element(By.CLASS_NAME, 'table-cell-value.tm-value.icon-before.icon-ton')
                print(f'@{username} has been sold for {price.text} TON')
        except:
            driver.get(f'https://fragment.com/?query={username}')
            print(f'@{username} is not used / not available')
    except Exception as e:
        print(e)
    finally:
        driver.quit()

