from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import time

browser = webdriver.Chrome(r"C:\Users\mikg2\Desktop\project\chromedriver.exe")
url = "http://koreanfood.rda.go.kr/kfi/fct/fctFoodSrch/list"
browser.get(url)

filename = "Nutritional_Contents2.csv"
f = open(filename,"w",encoding="cp949",newline="") 
writer = csv.writer(f)

title = "식품명 무게(g) 칼로리(kcal) 단백질(g) 지방(g) 탄수화물(g)".split()
writer.writerow(title)
start_time = time.time()

for i in range(1,329): 
    if i == 1: # 1 페이지
        for j in range(1,11):
            browser.find_element(By.XPATH,f"//*[@id='gridArea']/div[2]/div[1]/ul/li[{j}]/a").click()
            elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[2]/th[2]")))
            elem_name_gm = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[2]/th[2]").text
            elem_name = elem_name_gm.split("기본")[0].replace("\n","")
            elem_gm = elem_name_gm.split("기본")[1][2:-2] 
            elem_kcal = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[3]/td[2]").text
            elem_protein = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[5]/td[2]").text
            elem_fat = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[6]/td[2]").text
            elem_car = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[8]/td[2]").text
            row_lst = [elem_name, elem_gm, elem_kcal, elem_protein, elem_fat, elem_car]
            writer.writerow(row_lst)
            browser.find_element(By.XPATH,"//*[@id='wrap']/div[2]/div[1]/a").click() # 도표창 닫기
          

    elif i == 2: # 2 페이지
        # 페이지에 접속하고 다음 페이지 버튼을 처음 누를 때 time.sleep 해줘도 한번 씹혀서 다음 페이지로 안넘어가 첫 페이지의 항목 10개가 중복으로 두번 쓰였다.
        # 따라서 다음 페이지 버튼 클릭하는 코드를 두번 입력하니 됨. 이후로 문제 없음
        browser.find_element(By.XPATH,"//*[@id='gridArea']/div[3]/a[12]").click()
        browser.find_element(By.XPATH,"//*[@id='gridArea']/div[3]/a[12]").click() # 다음 페이지 클릭
        for j in range(1,11):
            browser.find_element(By.XPATH,f"//*[@id='gridArea']/div[2]/div[1]/ul/li[{j}]/a").click()
            elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[2]/th[2]")))
            elem_name_gm = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[2]/th[2]").text
            elem_name = elem_name_gm.split("기본")[0].replace("\n","")
            elem_gm = elem_name_gm.split("기본")[1][2:-2] 
            elem_kcal = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[3]/td[2]").text
            elem_protein = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[5]/td[2]").text
            elem_fat = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[6]/td[2]").text
            elem_car = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[8]/td[2]").text
            row_lst = [elem_name, elem_gm, elem_kcal, elem_protein, elem_fat, elem_car] 
            writer.writerow(row_lst)
            browser.find_element(By.XPATH,"//*[@id='wrap']/div[2]/div[1]/a").click() # 도표창 닫기
            
            

    elif 2<i<328:  # 3 페이지 ~ 327 페이지
        browser.find_element(By.XPATH,"//*[@id='gridArea']/div[3]/a[12]").click() # 다음 페이지 클릭
        for j in range(1,11):
            browser.find_element(By.XPATH,f"//*[@id='gridArea']/div[2]/div[1]/ul/li[{j}]/a").click()
            elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[2]/th[2]")))
            elem_name_gm = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[2]/th[2]").text
            elem_name = elem_name_gm.split("기본")[0].replace("\n","")
            elem_gm = elem_name_gm.split("기본")[1][2:-2] 
            elem_kcal = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[3]/td[2]").text
            elem_protein = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[5]/td[2]").text
            elem_fat = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[6]/td[2]").text
            elem_car = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[8]/td[2]").text
            row_lst = [elem_name, elem_gm, elem_kcal, elem_protein, elem_fat, elem_car] 
            writer.writerow(row_lst)
            browser.find_element(By.XPATH,"//*[@id='wrap']/div[2]/div[1]/a").click() # 도표창 닫기
            
           

    elif i == 328: # 마지막 328 페이지 
        browser.find_element(By.XPATH,"//*[@id='gridArea']/div[3]/a[12]").click() # 다음 페이지 클릭
        for j in range(1,3):
            browser.find_element(By.XPATH,f"//*[@id='gridArea']/div[2]/div[1]/ul/li[{j}]/a").click()
            elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[2]/th[2]")))
            elem_name_gm = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[2]/th[2]").text
            elem_name = elem_name_gm.split("기본")[0].replace("\n","")
            elem_gm = elem_name_gm.split("기본")[1][2:-2] 
            elem_kcal = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[3]/td[2]").text
            elem_protein = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[5]/td[2]").text
            elem_fat = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[6]/td[2]").text
            elem_car = browser.find_element(By.XPATH,"//*[@id='frmDeatil']/div/div[1]/table[1]/tbody/tr[8]/td[2]").text
            row_lst = [elem_name, elem_gm, elem_kcal, elem_protein, elem_fat, elem_car]
            writer.writerow(row_lst)
            browser.find_element(By.XPATH,"//*[@id='wrap']/div[2]/div[1]/a").click() # 도표창 닫기
            

end_time = time.time()
load_time = end_time - start_time
print("걸린 시간(초) :",load_time)


# 321 페이지부터 페이지 버튼 개수가 달라서 다음 버튼의 XPATH 까지도 달라진다
# 316 페이지 중간부터 멈췄는데 왜 멈춘건지는 모르겠다. 일시적 오류인듯. 과부하나
# 원래 행의 총 개수가 제목 합쳐서 3273개가 나와야 되는데 3283이 나옴. 한 페이지가 중복 된 것 같은데...
# -> 첫 페이지 10개 항목이 중복됨. 해결법은 위에 주석으로 설명해놓음