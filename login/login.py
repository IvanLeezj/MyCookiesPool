import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class WeiboCookies():

    def __init__(self, username, password):
        self.url = 'https://passport.weibo.cn/signin/login?entry=mweibo&r=https://m.weibo.cn/'
        self.browser = webdriver.Chrome(executable_path='./chromedriver.exe')
        self.wait = WebDriverWait(self.browser,20)
        self.password = password
        self.username = username


    def open(self):
        self.browser.delete_all_cookies()
        self.browser.get(self.url)
        username = self.wait.until(EC.presence_of_element_located((By.ID, 'loginName')))
        password = self.wait.until(EC.presence_of_element_located((By.ID, 'loginPassword')))
        submit = self.wait.until(EC.element_to_be_clickable((By.ID, 'loginAction')))
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(1)
        submit.click()

    def vertify(self):
        get_code_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="vdVerify"]/div[1]/div/div/div[3]/a')))
        get_code_button.click()
        code = input("输入验证码")
        vertify_input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="verifyCode"]/div[1]/div/div/div[2]/div/div/div/span[1]/input')))
        vertify_input.send_keys(code)
        submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="verifyCode"]/div[1]/div/div/div[3]/a')))
        submit_button.click()


    def get_cookies(self):
        return self.browser.get_cookies()

    def close_browser(self):
        self.browser.close()

    def run(self):
        """
        模拟登录微博
        :return: 包含cookies的字典
        """
        # self.open()
        # self.vertify()
        # cookies = self.get_cookies()
        cookies = [{'domain': '.weibo.cn', 'expiry': 1625132118, 'httpOnly': False, 'name': 'MLOGIN', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.weibo.cn', 'httpOnly': True, 'name': 'WEIBOCN_FROM', 'path': '/', 'secure': False, 'value': '1110006030'}, {'domain': '.weibo.cn', 'expiry': 1625129118, 'httpOnly': True, 'name': 'M_WEIBOCN_PARAMS', 'path': '/', 'secure': False, 'value': 'uicode%3D20000174'}, {'domain': '.m.weibo.cn', 'expiry': 1625129718, 'httpOnly': False, 'name': 'XSRF-TOKEN', 'path': '/', 'secure': False, 'value': '6174f2'}, {'domain': '.weibo.cn', 'httpOnly': False, 'name': 'SSOLoginState', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1625128514'}, {'domain': '.weibo.cn', 'expiry': 1656664515, 'httpOnly': False, 'name': 'SUBP', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh.AFsoMF_Y0g7AdAjsmlq_5NHD95Qceo-fehnfeoBfWs4Dqcjci--ci-27iK.Ni--fi-82iK.7i--ci-2Ei-2Ri--fi-82iK.7i--Ni-2ci-iFi--fi-82iK.7'}, {'domain': '.weibo.cn', 'expiry': 1625155202, 'httpOnly': False, 'name': '_T_WM', 'path': '/', 'secure': False, 'value': '77927734588'}, {'domain': '.weibo.cn', 'expiry': 1656664516, 'httpOnly': True, 'name': 'SUB', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '_2A25N2Q4SDeRhGeBM7lcR-CvOzzmIHXVvJZJarDV6PUJbktB-LWHbkW1NRKnltlCV7-0-rY1KRb0CP6BEzWU7lkQo'}]
        # self.close_browser()

        return {
            'status': 1,
            'content': cookies
        }


if __name__ == '__main__':
    test = WeiboCookies('13226098983','ivan1997')
    cookies = test.run()
    # print(cookies)