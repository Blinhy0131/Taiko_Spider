#########################################################################
# Taiko Spider 
# Version 1.01     2024/06/27
# Made by Hyblin    
# Github link = https://github.com/Blinhy0131/Taiko_Spider
#########################################################################
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import time
import sys
import getpass

def main():
    str1 = '#######################################################'
    str2 = '# Taiko Spider Version 1.01       2024/06/27          #'
    str3 = '# Made by Hyblin                                      #'
    str4 = '# Github link=                                        #'
    str5 = '#    https://github.com/Blinhy0131/Taiko_Spider       #'
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    print(str5)
    print(str1)
    # 
    if getattr(sys, 'frozen', False):
        # if its exe
        current_dir = os.path.dirname(sys.executable)
    else:
        # else
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
    chrome_driver_path = os.path.join(current_dir, 'chromedriver.exe')

    #print(chrome_driver_path)
    account=input('Enter the banapass account: ')
    password=getpass.getpass('Enter the banapass password: ')
    card=input('Please select the data number (1 or 2 or 3) :')


    # 初始化ChromeDriver
    service = Service(chrome_driver_path)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service)


    # 打開網站
    driver.get('https://donderhiroba.jp/')

    # wait the driver
    wait = WebDriverWait(driver, 10)

    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='ログイン' and @onclick=\"document.getElementById('login_form').submit();\"]")))
    login_button.click()


    # 等待表單
    time.sleep(2)
    email_field = wait.until(EC.visibility_of_element_located((By.ID, 'mail')))
    cookie=driver.find_element(By.ID,"onetrust-accept-btn-handler")
    cookie.click()
    
    # 輸入帳號

    email_field.click()
    email_field.send_keys(account) 

    # 輸入密碼
    password_field = driver.find_element(By.ID, 'pass')
    password_field.send_keys(password)  

    # 點擊登入按鈕
    login_submit_button = driver.find_element(By.ID, 'btn-idpw-login')
    login_submit_button.click()

    #USER
    user_card="//a[contains(@onclick, \"document.getElementById('form_user"+card+"').submit();\")]"
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, user_card)))
    time.sleep(2)
    cookie2 = driver.find_element(By.ID,"onetrust-accept-btn-handler")
    cookie2.click()
    login_button.click()


    xpath_expression = "(//div[contains(@class, 'buttonParentArea bunkatsu_3')]//a/img[@src='image/sp/640/btn_r_02_640.png']/ancestor::a)[3]"
    score_data_button = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_expression)))
    score_data_button.click()
    data = []

    dic={1:"Jpop",2:"Kids",3:"Anime",4:"Vocaloid",5:"Game Music",6:"Variety",7:"Classic",8:"Namco"}
    for kk in range(1,9):
        vv="//li[@class='selectTab"+str(kk)+"']/a"
        
        folder=dic.get(kk)
        #不同歌曲分類
        button = wait.until(EC.element_to_be_clickable((By.XPATH, vv)))
        button.click()

        # 獲取所有符合條件的按鈕
        buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, 'score_detail.php?song_no=') and (contains(@href, 'level=4') or contains(@href, 'level=5'))]")))

        num=len(buttons)



        for index in range(num):
            # click the button
            buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, 'score_detail.php?song_no=') and (contains(@href, 'level=4') or contains(@href, 'level=5'))]")))
            buttons[index].click()

            # song name score data....
            song_name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//li[@class='songNameTitleScore']/h2")))
            score_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='high_score']/span")))
            
            good_cnt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='good_cnt']/span")))
            ok_cnt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ok_cnt']/span")))
            ng_cnt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ng_cnt']/span")))
            combo_cnt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='combo_cnt']/span")))
            pound_cnt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='pound_cnt']/span")))
            
            stage_cnt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='stage_cnt']/span")))
            clear_cnt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='clear_cnt']/span")))
            full_combo_cnt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='full_combo_cnt']/span")))
            dondaful_combo_cnt = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='dondaful_combo_cnt']/span")))

            # 獲取歌曲名稱和分數
            song_name = song_name_element.text

            if  index !=0 and (song_name==data[-1][1]) :
                song_name=song_name+'(裏)'
                
            score = score_element.text
            score = int(score[:-1]) 
            good_cnt = int(good_cnt.text[:-1])
            ok_cnt = int(ok_cnt.text[:-1])
            ng_cnt = int(ng_cnt.text[:-1])
            combo_cnt = int(combo_cnt.text[:-1])
            pound_cnt = int(pound_cnt.text[:-1])

            stage_cnt = int(stage_cnt.text[:-1])
            clear_cnt = int(clear_cnt.text[:-1])
            full_combo_cnt = int(full_combo_cnt.text[:-1])
            dondaful_combo_cnt =int(dondaful_combo_cnt.text[:-1])

            if score !=0:
                
                #crown
                # scoreDetailStatus 內的 mydon_name
                mydon_name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='mydon_name']/div")))
                mydon_name = mydon_name_element.text

                # 獲取 scoreDetailStatus 內的 crown 的 src
                score_detail_status = driver.find_element(By.CLASS_NAME, "scoreDetailStatus")
                try:
                    crown_element = score_detail_status.find_element(By.XPATH, ".//img[@class='crown']")
                    crown_src = crown_element.get_attribute('src')
                    
                    if 'crown_large_1' in crown_src:
                        crown = '銀冠'
                    elif 'crown_large_2' in crown_src:
                        crown = '金冠'
                    elif 'crown_large_3' in crown_src:
                        crown = '彩冠'
                    else:
                        crown = '無'
                except NoSuchElementException:
                    crown = '無'
                    
                #icon
                try:
                    icon_element = score_detail_status.find_element(By.XPATH, "//img[@class='best_score_icon']")
                    icon_src = icon_element.get_attribute('src')
                    #print(icon_src)
                    if 'rank_2' in icon_src:
                        icon='白粹'
                    elif 'rank_3' in icon_src:
                        icon='銅粹'
                    elif 'rank_4' in icon_src:
                        icon='銀粹'
                    elif 'rank_5' in icon_src:
                        icon='金雅'
                    elif 'rank_6' in icon_src:
                        icon='粉雅'
                    elif 'rank_7' in icon_src:
                        icon='紫雅'
                    elif 'rank_8' in icon_src:
                        icon='彩極'  
                    else:
                        icon='無'
                except :
                    icon='無'
                
                ranking = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='ranking']/span")))
                rank=ranking.text[:-1]
                #print()
                try:
                    rank=int(rank)
                except:
                    rank='nan'
                    
            else:
                crown = '無'
                icon='無'
                rank='nan'
                
            print(folder,index,'/',num,' ',song_name)
            data.append([folder,song_name, score,crown,icon,rank,good_cnt,ok_cnt,ng_cnt,combo_cnt,pound_cnt,stage_cnt,clear_cnt,full_combo_cnt,dondaful_combo_cnt])
            #print()
            # 返回上衣業
            driver.back()

    #print(data)
    labels=['分類', '曲名', '最佳分數', '皇冠', '評級', '排名', '良數', '可數',
            '不可數', 'combo數', '連打數', '遊玩數', '過關次數', '全接數', '全良次數']

    import pandas as pd
    # 換為 DataFrame
    df = pd.DataFrame(data, columns=labels)

    # 保存Excel
    df.to_excel('output.xlsx', index=False)
    # 關閉WebDriver
    driver.quit()


if __name__ == '__main__':
    main()
