from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import csv
#coding:utf-8

USERNAME = 'QQtestee'
PASSWORD = 'testaccountofqq'
CHROME_PATH = "/usr/local/bin/chromedriver"
CSV_FILE_PATH = "test.csv"
CSV_HEADER = ['No.',
              'Repo Name', 
              '#\{stargazer\}', 
              '#\{forks\}', 
              'contributor #1',
              'contributor #2',
              'contributor #3',
              'contributor #4',
              'contributor #5']
LOGGING_URL = "https://github.com/login"
TRENDING_URL = "https://github.com/trending/python?since=monthly&spoken_language_code=en"

class GithubSpider:

    def __init__(self, usr, pwd, browser):
        self.usr = usr
        self.pwd = pwd
        self.browser = browser
        self.links = {}
        self.csvRows = []
    
    def login(self):
        print('--开始尝试登录--')
        try:
            self.browser.get(LOGGING_URL)

            usrInputXpath = '/html/body/div[3]/main/div/div[4]/form/input[2]'
            pwdInputXpath = '/html/body/div[3]/main/div/div[4]/form/input[3]'
            submitXpath = '/html/body/div[3]/main/div/div[4]/form/input[14]'

            usrInput = self.browser.find_element_by_xpath(usrInputXpath)
            pwdInput = self.browser.find_element_by_xpath(pwdInputXpath)
            submit = self.browser.find_element_by_xpath(submitXpath)

            usrInput.send_keys(self.usr)
            pwdInput.send_keys(self.pwd)
            submit.click()
        except NoSuchElementException:
            print('报错：NoSuchElementException')
        finally:
            print('++登录操作完成++')
            #self.browser.close()
    
    def task1(self):
        print('--开始尝试获取所需信息--')
        try:
            self.links = {}
            self.browser.get(TRENDING_URL)

            targetClass = 'Box-row'
            targets = self.browser.find_elements_by_class_name(targetClass)

            count = 0

            for target in targets:
                child = target.find_element_by_tag_name('h1')
                if child and count < 10:
                    tmpRow = [count + 1]
                    childName = child.find_element_by_tag_name('a')
                    self.links[child.text] = childName.get_attribute('href')
                    tmpRow.append(child.text)

                    childProps = target.find_element_by_class_name('f6')

                    childPropsA = childProps.find_elements_by_tag_name('a')
                    tmpRow.append(childPropsA[0].text)
                    tmpRow.append(childPropsA[1].text)

                    childPropSpans = childProps.find_elements_by_class_name('mr-3')
                    if len(childPropSpans) > 3:
                        childPropContributor = childPropSpans[3]
                        persons = childPropContributor.find_elements_by_tag_name('a')
                        for personHref in persons:
                            personInfo = personHref.find_element_by_tag_name('img')
                            tmpRow.append(personInfo.get_attribute('alt'))

                    self.csvRows.append(tmpRow)
                    count += 1

            self.writeCSV()

        except NoSuchElementException:
            print('报错：NoSuchElementException')
        finally:
            print('++已完成获取所需信息的操作++')
            #self.browser.close()
    
    def writeCSV(self):
        print(f'--开始写入{CSV_FILE_PATH}文件的操作--')
        with open(CSV_FILE_PATH,'w')as f:
            f_csv = csv.writer(f)
            f_csv.writerow(CSV_HEADER)
            f_csv.writerows(self.csvRows)
        print(f'++已完成写入{CSV_FILE_PATH}文件的操作++')
    
    def task2(self):
        print('--开始对各个repo进行watch的操作--')
        try:

            for repoName in self.links:

                print(f'--开始对{repoName}进行watch的操作--')
                self.browser.get(self.links[repoName])
                
                butnXpath = '/html/body/div[4]/div/main/div[2]/div[1]/ul/li[1]/notifications-list-subscription-form/details'
                try:
                    watchButn = self.browser.find_element_by_xpath(butnXpath)
                    watchButn.click()
                except NoSuchElementException:
                    try:
                        self.browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[1]/ul/li[2]/notifications-list-subscription-form/details').click()
                        self.browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[1]/ul/li[2]/notifications-list-subscription-form/details/details-menu/div/div/button').click()
                        release = self.browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[1]/ul/li[2]/notifications-list-subscription-form/details/details-dialog/div/form/fieldset/div[3]/label/input')
                        if not release.is_selected():
                            release.click()
                        self.browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[1]/ul/li[2]/notifications-list-subscription-form/details/details-dialog/div/form/div/button[1]').click()
                    finally:
                        pass
                else:
                    customXpath = '/html/body/div[4]/div/main/div[2]/div[1]/ul/li[1]/notifications-list-subscription-form/details/details-menu/div/div/button'
                    custom = browser.find_element_by_xpath(customXpath)
                    custom.click()

                    releaseXpath = '/html/body/div[4]/div/main/div[2]/div[1]/ul/li[1]/notifications-list-subscription-form/details/details-dialog/div/form/fieldset/div[3]/label/input'
                    release = browser.find_element_by_xpath(releaseXpath)

                    if not release.is_selected():
                        release.click()

                    submitXpath = '/html/body/div[4]/div/main/div[2]/div[1]/ul/li[1]/notifications-list-subscription-form/details/details-dialog/div/form/div/button[1]'
                    submit = browser.find_element_by_xpath(submitXpath)
                    submit.click()
                    pass
                finally:
                    print(f'++完成对{repoName}进行watch的操作++')
                #self.browser.close()

        finally:
            print('++已完成对各个repo进行watch的操作++')
            #self.browser.close()

    def run(self):
        print("--开始爬虫操作--")
        try:
            self.login()
            self.task1()
            self.task2()
        finally:
            print("++完成爬虫操作++")

if __name__ == "__main__":

    def check():
        if not USERNAME or not PASSWORD or not CSV_FILE_PATH or not CHROME_PATH:
            return False
        return True
    
    if not check():
        print("请您先在代码首部配置好：Github账号名、密码、CSV文件名、CHROME Driver路径，谢谢！")
    else:
        try:
            browser = webdriver.Chrome(executable_path=CHROME_PATH)
            mySpider = GithubSpider(USERNAME, PASSWORD, browser)
            mySpider.run()
        finally:
            putmp = ''
            while (putmp != 'q'):
                putmp = input('请输入字母q来退出:')
            browser.quit()

