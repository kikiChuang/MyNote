from selenium import webdriver  # selenium 的用法可參見 5-7 節
from time import sleep    # 匯入 time 模組的 sleep() 函式

def input_ticket_info(driver):
    driver.find_element_by_id('btn-confirm').click() #關閉個人資料使用訊息框
    driver.find_element_by_xpath('//select[@name="selectStartStation"]' +
                                 '//option[@value="2"]').click() # 起站：台北
    driver.find_element_by_xpath('//select[@name="selectDestinationStation"]' +
                                 '//option[@value="11"]').click() # 到站：台南
    driver.find_element_by_id('trainCon:trainRadioGroup_1').click()  #商務車廂
    e = driver.find_element_by_id('toTimeInputField')   # 日期欄
    e.clear()                  # 先清除內容
    e.send_keys("2018/12/05")  # 輸入日期
    driver.find_element_by_xpath('//option[@value="430P"]').click() # 下午4點30
    driver.find_element_by_xpath('//option[@value="2F"]').click()   # 買 2 張票

def input_train_and_person(driver):
    driver.find_element_by_name('SubmitButton').click()  #按【確認車次】鈕
    sleep(1)   # 等待換到下一頁
    driver.find_element_by_id('idNumber').send_keys('K122365XXX')    #輸入身分證字號
    driver.find_element_by_id('mobileInputRadio').click()  #選行動電話單選鈕
    driver.find_element_by_id('mobilePhone').send_keys('090854XXXX') #輸入行動電話
    driver.find_element_by_name('agree').click()  # 按下我已明確了解..高鐵約定事項
    driver.find_element_by_id("isSubmit").click()  # 按下完成訂位按鈕


url = 'https://irs.thsrc.com.tw/IMINT'   # 高鐵訂票網址
driver=webdriver.Chrome()  # 建立瀏覽器物件
driver.get(url)            # 連線到高鐵購票網頁
driver.maximize_window()   # 將視窗最大化

input_ticket_info(driver)  # 填寫購票資料
e = driver.find_element_by_id('BookingS1Form_homeCaptcha_passCode')
e.screenshot('captcha.png')  # 將驗證圖存檔

code = input('請輸入驗證碼：')
driver.find_element_by_name('homeCaptcha:securityCode').send_keys(code) #填入驗證碼
driver.find_element_by_name('SubmitButton').click()  #按【開始查詢】鈕
sleep(1)
input_train_and_person(driver) #填寫第 2、3 頁的資料, 完成訂票