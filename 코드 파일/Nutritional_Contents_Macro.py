from tkinter import *
import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
root = Tk()
root.title("Nutritional_Contents_Macro.v1")
root.geometry("1250x770+500+100")
root.resizable(False, False) 
#====================================================================
# 데이터 베이스
import csv
import time



# 전체_리스트 외 리스트 품복20종
곡류_및_그_제품_리스트 = [] 
감자_및_전분류_리스트 = []
당류_리스트 = []
두류_리스트 = []
견과_및_종실류_리스트 = []
채소류_리스트 = []
버섯류_리스트 = []
과일류_리스트 = []
육류_리스트 = []
난류_리스트 = []
어패류_및_기타_수산물_리스트  = []
해조류_리스트  = []
우유류_및_유제품_리스트  = []
유지류_리스트  = []
차류_리스트  = []
음료류_리스트  = []
주류_리스트  = []
조미료류_리스트  = []
조리가공식품류_리스트 = []
기타_리스트  = []
now_path = os.getcwd()
DB_path = now_path + "\\build\\Nutritional_Contents_Macro\\" + "Nutritional_Contents_DB.csv"
with open(DB_path, "r", encoding ="cp949") as f:
    rows_read = csv.reader(f)
    전체_리스트 = [row for row in rows_read]
    for row in 전체_리스트:
        if row[0] == "곡류 및 그 제품":
           곡류_및_그_제품_리스트.append(list(row))
        elif row[0] == "감자 및 전분류":
            감자_및_전분류_리스트.append(list(row))
        elif row[0] == "당류":
            당류_리스트.append(list(row))
        elif row[0] == "두류":
            두류_리스트.append(list(row))
        elif row[0] == "견과 및 종실류":
            견과_및_종실류_리스트.append(list(row))
        elif row[0] == "채소류":
            채소류_리스트.append(list(row))
        elif row[0] == "버섯류":
            버섯류_리스트.append(list(row))
        elif row[0] == "과일류":
            과일류_리스트.append(list(row))
        elif row[0] == "육류":
            육류_리스트.append(list(row))
        elif row[0] == "난류":
            난류_리스트.append(list(row))
        elif row[0] == "어패류 및 기타 수산물":
            어패류_및_기타_수산물_리스트.append(list(row))
        elif row[0] == "해조류":
            해조류_리스트.append(list(row))
        elif row[0] == "우유류 및 유제품":
            우유류_및_유제품_리스트.append(list(row))
        elif row[0] == "유지류":
            유지류_리스트.append(list(row))
        elif row[0] == "차류":
            차류_리스트.append(list(row))
        elif row[0] == "음료류":
            음료류_리스트.append(list(row))
        elif row[0] == "주류":
            주류_리스트.append(list(row))
        elif row[0] == "조미료류":
            조미료류_리스트.append(list(row))
        elif row[0] == "조리가공식품류":
            조리가공식품류_리스트.append(list(row))
        elif row[0] == "기타":
            기타_리스트.append(list(row))

# 리스트 선택에 따라 리스트 박스에서 보여주는 항목이 다름


# 직접 검색 : 식품명에 입력한 글자가 포함되면 출력
#food_name = input("음식명 :")

#for food in 전체_리스트:
    #if food_name in food[1]:
        #print(food)
#----------------------------------------------------------------------
# 로그인 프레임, 선택화면 프레임, 결과화면 프레임 (화면 전환)
login_frame = Frame(root)
main_frame = Frame(root)
sub_frame = Frame(root)
login_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid(row=0, column=0, sticky="nsew")
sub_frame.grid(row=0, column=0, sticky="nsew")

now_path = os.getcwd()
# 메인화면
페페_path = now_path + "\\image\\" + "메인.png"
photo = PhotoImage(file=페페_path)
label_페페 = Label(login_frame, image=photo) 
label_페페.pack(side="top")

gap0 = Label(login_frame, text="       ")
gap0.pack(side="top")


# 사용자 정보 프레임
user_inf_frame = Frame(login_frame)
user_inf_frame.pack(side="top")
# 사용자 정보 : 성별, 나이, 키, 체중
label_sex = Label(user_inf_frame, text="성별 :")
label_sex.pack(side="left")
sex_var = IntVar()
btn_sex_male = Radiobutton(user_inf_frame, text="남", value=1, variable=sex_var) 
btn_sex_female = Radiobutton(user_inf_frame, text="여", value=2, variable=sex_var) 
btn_sex_male.pack(side="left")
btn_sex_female.pack(side="left")
btn_sex_male.select()

gap1 = Label(user_inf_frame, text="       ")
gap1.pack(side="left")

label_age1 = Label(user_inf_frame, text="나이 :")
label_age1.pack(side="left")
user_age = Entry(user_inf_frame, width=4)
user_age.pack(side="left")
label_age2 = Label(user_inf_frame, text="(세)")
label_age2.pack(side="left")

gap2 = Label(user_inf_frame, text="       ")
gap2.pack(side="left")

label_hight1 = Label(user_inf_frame, text="키 :")
label_hight1.pack(side="left")
user_hight = Entry(user_inf_frame, width=4)
user_hight.pack(side="left")
label_hight2 = Label(user_inf_frame, text="(cm)")
label_hight2.pack(side="left")

gap3 = Label(user_inf_frame, text="       ")
gap3.pack(side="left")

label_weight1 = Label(user_inf_frame, text="체중 :")
label_weight1.pack(side="left")
user_weight = Entry(user_inf_frame, width=4)
user_weight.pack(side="left")
label_weight2 = Label(user_inf_frame, text="(kg)")
label_weight2.pack(side="left")

# 옵션 프레임 
option_frame = Frame(login_frame)
option_frame.pack(side="top", pady=13)
# 식사량 기준 : 한끼/하루
one_three = Label(option_frame, text="식사량 기준 :")
one_three.pack(side="left")
values1 = ["한끼","하루"]
one_or_three = ttk.Combobox(option_frame, width=5, height=2, values=values1, state="readonly")
one_or_three.current(0) 
one_or_three.pack(side="left")

gap4 = Label(option_frame, text="       ")
gap4.pack(side="left")

# 식단 목적 : 린매스업/벌크/다이어트
goal = Label(option_frame, text="식단 목적 :")
goal.pack(side="left")
values2 = ["벌크업","다이어트","린매스업"]
goal_box = ttk.Combobox(option_frame, width=10, height=3, values=values2, state="readonly")
goal_box.current(0) 
goal_box.pack(side="left")

gap5 = Label(option_frame, text="       ")
gap5.pack(side="left")

# 활동량 
activity = Label(option_frame, text="활동량 :")
activity.pack(side="left")
values3 = ["거의 운동하지 않음", "가벼운 운동(주 1~3일)", "보통 수준","적극적으로 운동(주 6~7일)","매우 적극적으로 운동(주 6~7일)"]
activity_box = ttk.Combobox(option_frame, width=25, height=5, values=values3, state="readonly")
activity_box.current(0) 
activity_box.pack(side="left")



def openFrame(frame):  
        frame.tkraise()




def login_check(frame):
    if user_age.get() and user_hight.get() and user_weight.get():
        try:
            int(user_age.get())
            float(user_hight.get())
            float(user_weight.get())
            frame.tkraise()
        except Exception as err:
            msgbox.showerror("에러", "나이, 키, 몸무게는 실수여야 합니다.")
        
    else:
        msgbox.showerror("로그인 에러","입력 사항을 전부 입력하시오")

    

# "사용자 정보 등록" 버튼
btnTologin = Button(login_frame, 
    text="사용자 정보 등록", 
    padx=10, 
    pady=10, 
    command=lambda:[login_check(main_frame)])

btnTologin.pack(side="top",pady=8)






openFrame(login_frame)
#----------------------------------------------------------------------
# 원래 로그인화면 있던 자리 위로 옮김
#-------------------------------------------------------------------
# 리스트 목록
group_list_frame5 = Frame(main_frame)
group_list_frame5.pack(fill="x",side="bottom",pady=8)

search_list_box_frame = Frame(group_list_frame5)
search_list_box_frame.pack(fill="x",side="right",)

# 메인 화면의 리스트박스 2개
gap = Label(search_list_box_frame, text="      ")
gap.pack(side="right")
scrollbar_search_list = Scrollbar(search_list_box_frame)
scrollbar_search_list.pack(side="right",fill="y")
search_list_box = Listbox(search_list_box_frame, width=70, selectmode="single", height=25, yscrollcommand=scrollbar_search_list.set) 
search_list_box.pack()
scrollbar_search_list.config(command=search_list_box.yview)

# 음식 등록 리스트 박스, 음식 검색 결과 리스트 박스 프레임 


food_list_box_frame = Frame(group_list_frame5,width=700,height=380)
food_list_box_frame.pack(fill="x",side="left",padx=13)



#--------------------------------------------------------------------------------------------------------------------------
# 음식 등록
select_var1 = IntVar()
select_var2 = IntVar()
select_var3 = IntVar()
select_var4 = IntVar()
select_var5 = IntVar()
select_var6 = IntVar()
select_var7 = IntVar()
select_var8 = IntVar()
select_var9 = IntVar()
select_var10 = IntVar()
select_var11 = IntVar()
select_var12 = IntVar()
s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
s10 = 0
s11 = 0
s12 = 0

def select_func():
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    global s10
    global s11
    global s12
    if select_var1.get():
        s1 = 1
    else:
        s1=0
    if select_var2.get():
        s2 = 1
    else:
        s2=0
    if select_var3.get():
        s3 = 1
    else:
        s3=0
    if select_var4.get():
        s4 = 1
    else:
        s4=0
    if select_var5.get():
        s5 = 1
    else:
        s5=0
    if select_var6.get():
        s6 = 1
    else:
        s6=0
    if select_var7.get():
        s7 = 1
    else:
        s7=0
    if select_var8.get():
        s8 = 1
    else:
        s8=0
    if select_var9.get():
        s9 = 1
    else:
        s9=0
    if select_var10.get():
        s10 = 1
    else:
        s10=0
    if select_var11.get():
        s11 = 1
    else:
        s11=0
    if select_var12.get():
        s12 = 1
    else:
        s12=0
    total_s = s1+s2+s3+s4+s5+s6+s7+s8+s9+s10+s11+s12
    return total_s



food_list_frame0 = Frame(food_list_box_frame, relief="raised",bd=1)
food_list_frame0.pack(fill="x",side="top", pady=4)
selecetvar1= Checkbutton(food_list_frame0, text="음식 등록1", variable=select_var1)
selecetvar1.pack(side="left")
selecetvar1.select()
label0_1 = Label(food_list_frame0, text=" [식품명] :")
label0_1.pack(side="left")
e0_1 = Entry(food_list_frame0, width=50)
e0_1.pack(side="left")
label0_2 = Label(food_list_frame0, text="[무게] :")
label0_2.pack(side="left")
e0_2 = Entry(food_list_frame0, width=8)
e0_2.pack(side="left")
label0_3 = Label(food_list_frame0, text="(g)")
label0_3.pack(side="left")
e0_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")

    



num=1
def update_food():
    # ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ왜 여기서 딕셔너리, while, len을 안써서 노가다를 쳐 했노;;ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ
    global num 
    global select_var
    global e1_1
    global e1_2
    global e2_1
    global e2_2
    global e3_1
    global e3_2
    global e4_1
    global e4_2
    global e5_1
    global e5_2
    global e6_1
    global e6_2
    global e7_1
    global e7_2
    global e8_1
    global e8_2
    global e9_1
    global e9_2
    global e10_1
    global e10_2
    global e11_1
    global e11_2
    if num == 1:
        global food_list_frame1
        food_list_frame1 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame1.pack(fill="x",side="top", pady=4)
        selecetvar2= Checkbutton(food_list_frame1, text="음식 등록2", variable=select_var2)
        selecetvar2.pack(side="left")
        label1_1 = Label(food_list_frame1, text=" [식품명] :")
        label1_1.pack(side="left")
        e1_1 = Entry(food_list_frame1, width=50)
        e1_1.pack(side="left")
        label1_2 = Label(food_list_frame1, text="[무게] :")
        label1_2.pack(side="left")
        e1_2 = Entry(food_list_frame1, width=8)
        e1_2.pack(side="left")
        label1_3 = Label(food_list_frame1, text="(g)")
        label1_3.pack(side="left")
        e1_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
        num+=1
    elif num == 2:
        global food_list_frame2
        food_list_frame2 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame2.pack(fill="x",side="top", pady=4)
        selecetvar3= Checkbutton(food_list_frame2, text="음식 등록3", variable=select_var3)
        selecetvar3.pack(side="left")
        label2_1 = Label(food_list_frame2, text=" [식품명] :")
        label2_1.pack(side="left")
        e2_1 = Entry(food_list_frame2, width=50)
        e2_1.pack(side="left")
        label2_2 = Label(food_list_frame2, text="[무게] :")
        label2_2.pack(side="left")
        e2_2 = Entry(food_list_frame2, width=8)
        e2_2.pack(side="left")
        label2_3 = Label(food_list_frame2, text="(g)")
        label2_3.pack(side="left")
        e2_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
        num+=1
    elif num == 3:
        global food_list_frame3
        food_list_frame3 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame3.pack(fill="x",side="top", pady=4)
        selecetvar4= Checkbutton(food_list_frame3, text="음식 등록4", variable=select_var4)
        selecetvar4.pack(side="left")
        label3_1 = Label(food_list_frame3, text=" [식품명] :")
        label3_1.pack(side="left")
        e3_1 = Entry(food_list_frame3, width=50)
        e3_1.pack(side="left")
        label3_2 = Label(food_list_frame3, text="[무게] :")
        label3_2.pack(side="left")
        e3_2 = Entry(food_list_frame3, width=8)
        e3_2.pack(side="left")
        label3_3 = Label(food_list_frame3, text="(g)")
        label3_3.pack(side="left")
        e3_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
        num+=1
    elif num == 4:
        global food_list_frame4
        food_list_frame4 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame4.pack(fill="x",side="top", pady=4)
        selecetvar5= Checkbutton(food_list_frame4, text="음식 등록5", variable=select_var5)
        selecetvar5.pack(side="left")
        label4_1 = Label(food_list_frame4, text=" [식품명] :")
        label4_1.pack(side="left")
        e4_1 = Entry(food_list_frame4, width=50)
        e4_1.pack(side="left")
        label4_2 = Label(food_list_frame4, text="[무게] :")
        label4_2.pack(side="left")
        e4_2 = Entry(food_list_frame4, width=8)
        e4_2.pack(side="left")
        label4_3 = Label(food_list_frame4, text="(g)")
        label4_3.pack(side="left")
        e4_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
        num+=1
    elif num == 5:
        global food_list_frame5
        food_list_frame5 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame5.pack(fill="x",side="top", pady=4)
        selecetvar6= Checkbutton(food_list_frame5, text="음식 등록6", variable=select_var6)
        selecetvar6.pack(side="left")
        label5_1 = Label(food_list_frame5, text=" [식품명] :")
        label5_1.pack(side="left")
        e5_1 = Entry(food_list_frame5, width=50)
        e5_1.pack(side="left")
        label5_2 = Label(food_list_frame5, text="[무게] :")
        label5_2.pack(side="left")
        e5_2 = Entry(food_list_frame5, width=8)
        e5_2.pack(side="left")
        label5_3 = Label(food_list_frame5, text="(g)")
        label5_3.pack(side="left")
        e5_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
        num+=1
    elif num == 6:
        global food_list_frame6
        food_list_frame6 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame6.pack(fill="x",side="top", pady=4)
        selecetvar7= Checkbutton(food_list_frame6, text="음식 등록7", variable=select_var7)
        selecetvar7.pack(side="left")
        label6_1 = Label(food_list_frame6, text=" [식품명] :")
        label6_1.pack(side="left")
        e6_1 = Entry(food_list_frame6, width=50)
        e6_1.pack(side="left")
        label6_2 = Label(food_list_frame6, text="[무게] :")
        label6_2.pack(side="left")
        e6_2 = Entry(food_list_frame6, width=8)
        e6_2.pack(side="left")
        label6_3 = Label(food_list_frame6, text="(g)")
        label6_3.pack(side="left")
        e6_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
        num+=1
    elif num == 7:
        global food_list_frame7
        food_list_frame7 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame7.pack(fill="x",side="top", pady=4)
        selecetvar8= Checkbutton(food_list_frame7, text="음식 등록8", variable=select_var8)
        selecetvar8.pack(side="left")
        label7_1 = Label(food_list_frame7, text=" [식품명] :")
        label7_1.pack(side="left")
        e7_1 = Entry(food_list_frame7, width=50)
        e7_1.pack(side="left")
        label7_2 = Label(food_list_frame7, text="[무게] :")
        label7_2.pack(side="left")
        e7_2 = Entry(food_list_frame7, width=8)
        e7_2.pack(side="left")
        label7_3 = Label(food_list_frame7, text="(g)")
        label7_3.pack(side="left")
        num+=1
        e7_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
    elif num == 8:
        global food_list_frame8
        food_list_frame8 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame8.pack(fill="x",side="top", pady=4)
        selecetvar9= Checkbutton(food_list_frame8, text="음식 등록9", variable=select_var9)
        selecetvar9.pack(side="left")
        label8_1 = Label(food_list_frame8, text=" [식품명] :")
        label8_1.pack(side="left")
        e8_1 = Entry(food_list_frame8, width=50)
        e8_1.pack(side="left")
        label8_2 = Label(food_list_frame8, text="[무게] :")
        label8_2.pack(side="left")
        e8_2 = Entry(food_list_frame8, width=8)
        e8_2.pack(side="left")
        label8_3 = Label(food_list_frame8, text="(g)")
        label8_3.pack(side="left")
        num+=1
        e8_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
    elif num == 9:
        global food_list_frame9
        food_list_frame9 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame9.pack(fill="x",side="top", pady=4)
        selecetvar10= Checkbutton(food_list_frame9, text="음식 등록10", variable=select_var10)
        selecetvar10.pack(side="left")
        label9_1 = Label(food_list_frame9, text=" [식품명] :")
        label9_1.pack(side="left")
        e9_1 = Entry(food_list_frame9, width=50)
        e9_1.pack(side="left")
        label9_2 = Label(food_list_frame9, text="[무게] :")
        label9_2.pack(side="left")
        e9_2 = Entry(food_list_frame9, width=8)
        e9_2.pack(side="left")
        label9_3 = Label(food_list_frame9, text="(g)")
        label9_3.pack(side="left")
        e9_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
        num+=1
    elif num == 10:
        global food_list_frame10
        food_list_frame10 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame10.pack(fill="x",side="top", pady=4)
        selecetvar11= Checkbutton(food_list_frame10, text="음식 등록11", variable=select_var11)
        selecetvar11.pack(side="left")
        label10_1 = Label(food_list_frame10, text=" [식품명] :")
        label10_1.pack(side="left")
        e10_1 = Entry(food_list_frame10, width=50)
        e10_1.pack(side="left")
        label10_2 = Label(food_list_frame10, text="[무게] :")
        label10_2.pack(side="left")
        e10_2 = Entry(food_list_frame10, width=8)
        e10_2.pack(side="left")
        label10_3 = Label(food_list_frame10, text="(g)")
        label10_3.pack(side="left")
        e10_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
        num+=1
    elif num == 11:
        global food_list_frame11
        food_list_frame11 = Frame(food_list_box_frame, relief="raised",bd=1)
        food_list_frame11.pack(fill="x",side="top", pady=4)
        selecetvar12= Checkbutton(food_list_frame11, text="음식 등록12", variable=select_var12)
        selecetvar12.pack(side="left")
        label11_1 = Label(food_list_frame11, text=" [식품명] :")
        label11_1.pack(side="left")
        e11_1 = Entry(food_list_frame11, width=50)
        e11_1.pack(side="left")
        label11_2 = Label(food_list_frame11, text="[무게] :")
        label11_2.pack(side="left")
        e11_2 = Entry(food_list_frame11, width=8)
        e11_2.pack(side="left")
        label11_3 = Label(food_list_frame11, text="(g)")
        label11_3.pack(side="left")
        e11_1.insert(0,"(직접 입력하지 말고 '음식 등록' 버튼으로 입력하시오)")
        num+=1
    elif num == 12:
        msgbox.showinfo(title="알림", message="음식은 최대 12종까지 \n등록할 수 있습니다.") 

# 삭제버튼 메서드
def delete_food():
    global num
    if num == 1:
        msgbox.showerror("에러","음식은 최소 1개여야 합니다.")
    elif num == 2:
        food_list_frame1.destroy()
        num = 1
    elif num == 3:
        food_list_frame2.destroy()
        num = 2
    elif num == 4:
        food_list_frame3.destroy()
        num = 3
    elif num == 5:
        food_list_frame4.destroy()
        num = 4
    elif num == 6:
        food_list_frame5.destroy()
        num = 5
    elif num == 7:
        food_list_frame6.destroy()
        num = 6
    elif num == 8:
        food_list_frame7.destroy()
        num = 7
    elif num == 9:
        food_list_frame8.destroy()
        num = 8
    elif num == 10:
        food_list_frame9.destroy()
        num = 9
    elif num == 11:
        food_list_frame10.destroy()
        num = 10
    elif num == 12:
        food_list_frame11.destroy()
        num = 11
# --------------------------------------------------------------------
# 리스트 목록 연동 메서드
def 곡류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 곡류제품 in 곡류_및_그_제품_리스트:
        search_list_box.insert(END, 곡류제품[1])

def 감자버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 감자제품 in 감자_및_전분류_리스트:
        search_list_box.insert(END, 감자제품[1])
def 당류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 당류제품 in 당류_리스트:
        search_list_box.insert(END, 당류제품[1])
def 두류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 두류제품 in 두류_리스트:
        search_list_box.insert(END, 두류제품[1])
def 견과버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 견과제품 in 견과_및_종실류_리스트:
        search_list_box.insert(END, 견과제품[1])
def 채소류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 채소류제품 in 채소류_리스트:
        search_list_box.insert(END, 채소류제품[1])
def 버섯류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 버섯류제품 in 버섯류_리스트:
        search_list_box.insert(END, 버섯류제품[1])
def 과일류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 과일류제품 in 과일류_리스트:
        search_list_box.insert(END, 과일류제품[1])
def 육류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 육류제품 in 육류_리스트:
        search_list_box.insert(END, 육류제품[1])
def 난류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 난류제품 in 난류_리스트:
        search_list_box.insert(END, 난류제품[1])
def 어패류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 어패류제품 in 어패류_및_기타_수산물_리스트:
        search_list_box.insert(END, 어패류제품[1])
def 해조류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 해조류제품 in 해조류_리스트:
        search_list_box.insert(END, 해조류제품[1])
def 우유류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 우유류제품 in 우유류_및_유제품_리스트:
        search_list_box.insert(END, 우유류제품[1])
def 유지류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 유지류제품 in 유지류_리스트:
        search_list_box.insert(END, 유지류제품[1])
def 차류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 차류제품 in 차류_리스트:
        search_list_box.insert(END, 차류제품[1])
def 음료류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 음료류제품 in 음료류_리스트:
        search_list_box.insert(END, 음료류제품[1])
def 주류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 음료류제품 in 주류_리스트:
        search_list_box.insert(END, 음료류제품[1])
def 조미료류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 조미료류제품 in 조미료류_리스트:
        search_list_box.insert(END, 조미료류제품[1])
def 조리가공식품류버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 조리가공식품류제품 in 조리가공식품류_리스트:
        search_list_box.insert(END, 조리가공식품류제품[1])
def 기타버튼():
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for 기타제품 in 기타_리스트:
        search_list_box.insert(END, 기타제품[1])


def 음식_등록함수():
    if  select_func() == 1:
        search_food = search_list_box.curselection()
        if search_food:
            if select_var1.get():
                search_food = search_list_box.get(search_food)
                e0_1.delete(0, END)
                e0_1.insert(0,search_food)
            elif select_var2.get():
                search_food = search_list_box.get(search_food)
                e1_1.delete(0, END)
                e1_1.insert(0,search_food)
            elif select_var3.get():
                search_food = search_list_box.get(search_food)
                e2_1.delete(0, END)
                e2_1.insert(0,search_food)
            elif select_var4.get():
                search_food = search_list_box.get(search_food)
                e3_1.delete(0, END)
                e3_1.insert(0,search_food)
            elif select_var5.get():
                search_food = search_list_box.get(search_food)
                e4_1.delete(0, END)
                e4_1.insert(0,search_food)
            elif select_var6.get():
                search_food = search_list_box.get(search_food)
                e5_1.delete(0, END)
                e5_1.insert(0,search_food)
            elif select_var7.get():
                search_food = search_list_box.get(search_food)
                e6_1.delete(0, END)
                e6_1.insert(0,search_food)
            elif select_var8.get():
                search_food = search_list_box.get(search_food)
                e7_1.delete(0, END)
                e7_1.insert(0,search_food)
            elif select_var9.get():
                search_food = search_list_box.get(search_food)
                e8_1.delete(0, END)
                e8_1.insert(0,search_food)
            elif select_var10.get():
                search_food = search_list_box.get(search_food)
                e9_1.delete(0, END)
                e9_1.insert(0,search_food)
            elif select_var11.get():
                search_food = search_list_box.get(search_food)
                e10_1.delete(0, END)
                e10_1.insert(0,search_food)
            elif select_var12.get():
                search_food = search_list_box.get(search_food)
                e11_1.delete(0, END)
                e11_1.insert(0,search_food)
            
        else:
            msgbox.showerror("에러", "등록할 음식 항목을 선택하시오.")
    elif select_func() == 0:
        msgbox.showerror("에러", "체크된 음식등록 리스트가 없습니다.") 
    else:
        msgbox.showerror("에러", "체크된 음식등록 리스트가 2개 이상입니다.") 


       


#----------------------------------------------------------------------
# 분류 검색 프레임 : 실행되는 코드 주소/image/


group_list_frame1 = Frame(main_frame)
group_list_frame1.pack(fill="x",side="top")



group_list_frame2 = Frame(main_frame)
group_list_frame2.pack(fill="x",side="top")



# 그림 버튼 20개 + 글자

# 버튼 그림 주소
now_path = os.getcwd()

icon_frame_곡류 = Frame(group_list_frame1)
icon_frame_곡류.pack(ipadx=11,side="left")
곡류_path = now_path + "\\image\\" + "곡류.png"
곡류_photo = PhotoImage(file=곡류_path) 
btn_곡류 = Button(icon_frame_곡류, image=곡류_photo, command=곡류버튼)
btn_곡류.pack(side="bottom")
label1 = Label(icon_frame_곡류, text="<곡류 및 그 제품>")
label1.pack(side="top")

icon_frame_감자 = Frame(group_list_frame1)
icon_frame_감자.pack(ipadx=11,side="left")
감자_path = now_path + "\\image\\" + "감자.png"
감자_photo = PhotoImage(file=감자_path) 
btn_감자 = Button(icon_frame_감자, image=감자_photo, command=감자버튼)
btn_감자.pack(side="bottom")
label2 = Label(icon_frame_감자, text="<감자 및 전분류>")
label2.pack(side="top")

icon_frame_견과류 = Frame(group_list_frame1)
icon_frame_견과류.pack(ipadx=11,side="left")
견과류_path = now_path + "\\image\\" + "견과류.png"
견과류_photo = PhotoImage(file=견과류_path) 
btn_견과류 = Button(icon_frame_견과류, image=견과류_photo, command=견과버튼)
btn_견과류.pack(side="bottom")
label3 = Label(icon_frame_견과류, text="<견과 및 종실류>")
label3.pack(side="top")

icon_frame_과일류 = Frame(group_list_frame1)
icon_frame_과일류.pack(ipadx=15,side="left")
과일류_path = now_path + "\\image\\" + "과일류.png"
과일류_photo = PhotoImage(file=과일류_path) 
btn_과일류 = Button(icon_frame_과일류, image=과일류_photo, command=과일류버튼)
btn_과일류.pack(side="bottom")
label4 = Label(icon_frame_과일류, text="<과일류>")
label4.pack(side="top")

icon_frame_난류 = Frame(group_list_frame1)
icon_frame_난류.pack(ipadx=15,side="left")
난류_path = now_path + "\\image\\" + "난류.png"
난류_photo = PhotoImage(file=난류_path) 
btn_난류 = Button(icon_frame_난류, image=난류_photo, command=난류버튼)
btn_난류.pack(side="bottom")
label5 = Label(icon_frame_난류, text="<난류>")
label5.pack(side="top")

icon_frame_당류 = Frame(group_list_frame1)
icon_frame_당류.pack(ipadx=15,side="left")
당류_path = now_path + "\\image\\" + "당류.png"
당류_photo = PhotoImage(file=당류_path) 
btn_당류 = Button(icon_frame_당류, image=당류_photo, command=당류버튼)
btn_당류.pack(side="bottom")
label6 = Label(icon_frame_당류, text="<당류>")
label6.pack(side="top")

icon_frame_두류 = Frame(group_list_frame1)
icon_frame_두류.pack(ipadx=15,side="left")
두류_path = now_path + "\\image\\" + "두류.png"
두류_photo = PhotoImage(file=두류_path) 
btn_두류 = Button(icon_frame_두류, image=두류_photo, command=두류버튼)
btn_두류.pack(side="bottom")
label7 = Label(icon_frame_두류, text="<두류>")
label7.pack(side="top")

icon_frame_버섯 = Frame(group_list_frame1)
icon_frame_버섯.pack(ipadx=15,side="left")
버섯_path = now_path + "\\image\\" + "버섯.png"
버섯_photo = PhotoImage(file=버섯_path) 
btn_버섯 = Button(icon_frame_버섯, image=버섯_photo, command=버섯류버튼)
btn_버섯.pack(side="bottom")
label8 = Label(icon_frame_버섯, text="<버섯류>")
label8.pack(side="top")

icon_frame_어패류 = Frame(group_list_frame1)
icon_frame_어패류.pack(side="left")
어패류_path = now_path + "\\image\\" + "어패류.png"
어패류_photo = PhotoImage(file=어패류_path) 
btn_어패류 = Button(icon_frame_어패류, image=어패류_photo, command=어패류버튼)
btn_어패류.pack(side="bottom")
label9 = Label(icon_frame_어패류, text="<어패류 및 기타 수산물>")
label9.pack(side="top")

icon_frame_우유 = Frame(group_list_frame1)
icon_frame_우유.pack(side="left")
우유_path = now_path + "\\image\\" + "우유.png"
우유_photo = PhotoImage(file=우유_path) 
btn_우유 = Button(icon_frame_우유, image=우유_photo, command=우유류버튼)
btn_우유.pack(side="bottom")
label10 = Label(icon_frame_우유, text="<우유류 및 유제품>")
label10.pack(side="top")

icon_frame_유지류 = Frame(group_list_frame2)
icon_frame_유지류.pack(ipadx=19,side="left")
유지류_path = now_path + "\\image\\" + "유지류.png"
유지류_photo = PhotoImage(file=유지류_path) 
btn_유지류 = Button(icon_frame_유지류, image=유지류_photo, command=유지류버튼)
btn_유지류.pack(side="bottom")
label11 = Label(icon_frame_유지류, text="<유지류>")
label11.pack(side="top")

icon_frame_육류 = Frame(group_list_frame2)
icon_frame_육류.pack(ipadx=18,side="left")
육류_path = now_path + "\\image\\" + "육류.png"
육류_photo = PhotoImage(file=육류_path) 
btn_육류 = Button(icon_frame_육류, image=육류_photo, command=육류버튼)
btn_육류.pack(side="bottom")
label12 = Label(icon_frame_육류, text="<육류>")
label12.pack(side="top")

icon_frame_음료류 = Frame(group_list_frame2)
icon_frame_음료류.pack(ipadx=16,side="left")
음료류_path = now_path + "\\image\\" + "음료류.png"
음료류_photo = PhotoImage(file=음료류_path) 
btn_음료류 = Button(icon_frame_음료류, image=음료류_photo, command=음료류버튼)
btn_음료류.pack(side="bottom")
label13 = Label(icon_frame_음료류, text="<음료류>")
label13.pack(side="top")

icon_frame_조미료류 = Frame(group_list_frame2)
icon_frame_조미료류.pack(ipadx=17,side="left")
조미료류_path = now_path + "\\image\\" + "조미료류.png"
조미료류_photo = PhotoImage(file=조미료류_path) 
btn_조미료류 = Button(icon_frame_조미료류, image=조미료류_photo, command=조미료류버튼)
btn_조미료류.pack(side="bottom")
label14 = Label(icon_frame_조미료류 , text="<조미료류>")
label14.pack(side="top")

icon_frame_주류 = Frame(group_list_frame2)
icon_frame_주류.pack(ipadx=15,side="left")
주류_path = now_path + "\\image\\" + "주류.png"
주류_photo = PhotoImage(file=주류_path) 
btn_주류 = Button(icon_frame_주류, image=주류_photo, command=주류버튼)
btn_주류.pack(side="bottom")
label15 = Label(icon_frame_주류, text="<주류>")
label15.pack(side="top")

icon_frame_차류 = Frame(group_list_frame2)
icon_frame_차류.pack(ipadx=18,side="left")
차류_path = now_path + "\\image\\" + "차류.png"
차류_photo = PhotoImage(file=차류_path) 
btn_차류 = Button(icon_frame_차류, image=차류_photo, command=차류버튼)
btn_차류.pack(side="bottom")
label16 = Label(icon_frame_차류, text="<차류>")
label16.pack(side="top")

icon_frame_채소류 = Frame(group_list_frame2)
icon_frame_채소류.pack(ipadx=13,side="left")
채소류_path = now_path + "\\image\\" + "채소류.png"
채소류_photo = PhotoImage(file=채소류_path) 
btn_채소류 = Button(icon_frame_채소류, image=채소류_photo, command=채소류버튼)
btn_채소류.pack(side="bottom")
label17 = Label(icon_frame_채소류, text="<채소류>")
label17.pack(side="top")

icon_frame_해조류 = Frame(group_list_frame2)
icon_frame_해조류.pack(ipadx=16,side="left")
해조류_path = now_path + "\\image\\" + "해조류.png"
해조류_photo = PhotoImage(file=해조류_path) 
btn_해조류 = Button(icon_frame_해조류, image=해조류_photo, command=해조류버튼)
btn_해조류.pack(side="bottom")
label18 = Label(icon_frame_해조류, text="<해조류>")
label18.pack(side="top")

icon_frame_조리가공 = Frame(group_list_frame2)
icon_frame_조리가공.pack(ipadx=16,side="left")
조리가공_path = now_path + "\\image\\" + "조리가공.png"
조리가공_photo = PhotoImage(file=조리가공_path) 
btn_조리가공 = Button(icon_frame_조리가공, image=조리가공_photo, command=조리가공식품류버튼)
btn_조리가공.pack(side="bottom")
label19 = Label(icon_frame_조리가공, text="<조리가공식품류>")
label19.pack(side="top")

icon_frame_기타 = Frame(group_list_frame2)
icon_frame_기타.pack(ipadx=15,side="left")
기타_path = now_path + "\\image\\" + "기타.png"
기타_photo = PhotoImage(file=기타_path) 
btn_기타 = Button(icon_frame_기타, image=기타_photo, command=기타버튼)
btn_기타.pack(side="bottom")
label20 = Label(icon_frame_기타, text="기타")
label20.pack(side="top")

# "분석 시작" - 검색 입력 프레임
group_list_frame3 = Frame(main_frame)
group_list_frame3.pack(fill="x",side="top",pady=15)

# "분석 시작"버튼 - 검색 입력 객체
gap6 = Label(group_list_frame3, text="  ")
gap6.pack(side="right")

gap6 = Label(group_list_frame3, text='''                                                                                                                                                 
                                                                                                                                                                                     
                                                                                                                                                                                                                               ''')
gap6.pack(side="left")

gap6 = Label(group_list_frame3, text="[통합 검색] ")
gap6.pack(side="left")

food_name_search= Entry(group_list_frame3, width=30)
food_name_search.pack(side="left")


def 통합검색():
    input_food_search = food_name_search.get()
    if search_list_box.size() > 1:
        search_list_box.delete(0,END)
    for food in 전체_리스트:
        if input_food_search in food[1]:
            search_list_box.insert(END, food[1])


btn_search = Button(group_list_frame3, text="검색", command= 통합검색)
btn_search.pack(side="right")







# 검색한 음식 등록 버튼 프레임 
group_list_frame4 = Frame(main_frame)
group_list_frame4.pack(fill="x",side="top")

gap8 = Label(group_list_frame4, text="  ")
gap8.pack(side="right")






gap9 = Label(group_list_frame4, text=" 왼쪽의 체크된 음식 등록 항목에                                                             \n 아래에서 선택한 음식이 등록된다. (중복된 체크는 등록 불가)                      ")
gap9.pack(side="right")



#----------------------------------------------------------------------------------------------------------------------------


update_btn = Button(group_list_frame4, text=f"음식 등록",width=13,height=2, command=음식_등록함수)
update_btn.pack(side="right")

gap11 = Label(group_list_frame4, text="           ")
gap11.pack(side="right")

add_btn = Button(group_list_frame4, text=f"음식 삭제",width=13,height=2, command=delete_food)
add_btn.pack(side="right")

gap11_1 = Label(group_list_frame4, text=" ")
gap11_1.pack(side="right")

add_btn = Button(group_list_frame4, text=f"음식 추가",width=13,height=2, command=update_food)
add_btn.pack(side="right")

gap12 = Label(group_list_frame4, text="- 음식 추가 : 최대 12개              \n - 음식 삭제 : 마지막 항목부터 삭제")
gap12.pack(side="right")
# 결과

#---------------------------------------------------------------------------------------------------------------------------------
# 사용자가 입력한 데이터들 획득
def get_data(frame):
    # # =========================================================================================================================================
    # 사용자 데이터 파트
    # 성별
    user_sex_fi = sex_var.get()
    # 나이
    user_age_fi = int(user_age.get())
    # 키
    user_hight_fi =  float(user_hight.get())
    # 체중
    user_weight_fi = float(user_weight.get())
    # 식사량 기준
    one_or_three_fi = one_or_three.get()
    # 식단 목적
    goal_box_fi = goal_box.get()
    # 활동량
    activity_box_fi = activity_box.get()
    # 식품명, 무게
    
    result_analysis= LabelFrame(sub_frame,text="맞춤 통합 분석 결과", relief="solid", bd=1)
   


    result_analysis_user= Frame(result_analysis)
    result_analysis_user_label1 = Label(result_analysis_user, text=f"사용자 정보 : 성별 {user_sex_fi} / 나이 {user_age_fi}세 / 키 {user_hight_fi}cm / 체중 {user_weight_fi}kg")
    result_analysis_user_label2 = Label(result_analysis_user, text=f"식사량 기준 : {one_or_three_fi}")
    result_analysis_user_label3 = Label(result_analysis_user, text=f"식단 목적 : {goal_box_fi} ")
    result_analysis_user_label4 = Label(result_analysis_user, text=f"활동량  : {activity_box_fi}")
    result_analysis_user.pack(side="top")
    result_analysis_user_label1.pack(side="top")
    result_analysis_user_label2.pack(side="top")
    result_analysis_user_label3.pack(side="top")
    result_analysis_user_label4.pack(side="top")

    result_analysis_food= Frame(result_analysis) 
    result_analysis_food.pack(side="bottom")
    result_analysis_실제= LabelFrame(result_analysis_food,text="실제 섭취", relief="solid", bd=1)
    result_analysis_실제.pack(side="left", padx=10, pady=10)
    식단목적_값= one_or_three.get()
    result_analysis_권장= LabelFrame(result_analysis_food,text=f"권장 {식단목적_값}섭취", relief="solid", bd=1)
    result_analysis_권장.pack(side="left", padx=10, pady=10)
    result_analysis_분석= LabelFrame(result_analysis_food,text="분석 결과", relief="solid", bd=1)
    result_analysis_분석.pack(side="left", padx=10, pady=10)

    # "메인 화면으로" 버튼

    def openFrame_back(frame):  
        frame.tkraise()
        result_analysis.destroy()
        btnTo_remain.destroy()
        btnTo_relogin.destroy()
        
    btnTo_remain = Button(sub_frame, 
    text="뒤로", 
    padx=10, 
    pady=10, 
    command=lambda:openFrame_back(main_frame))

    

    # "로그인 화면으로" 버튼
    def openFrame_re(frame):  
        frame.tkraise()
        result_analysis.destroy()
        btnTo_remain.destroy()
        btnTo_relogin.destroy()

    btnTo_relogin = Button(sub_frame, 
    text="로그인 화면으로", 
    padx=10, 
    pady=10, 
    command=lambda:openFrame_re(login_frame))
     
    btnTo_relogin.pack(pady=10)
    btnTo_remain.pack(pady=10)
    result_analysis.pack(pady=20)



    # =========================================================================================================================================
    # 권장 칼로리, 단백질, 탄수화물, 지방
    if activity_box_fi == "거의 운동하지 않음":
        active_mul = 1.2
    elif activity_box_fi == "가벼운 운동(주 1~3일)":
        active_mul = 1.375
    elif activity_box_fi == "보통 수준":
        active_mul = 1.55
    elif activity_box_fi == "적극적으로 운동(주 6~7일)":
        active_mul = 1.75
    elif activity_box_fi == "매우 적극적으로 운동(주 6~7일)":
        active_mul = 1.9
    # 기초 대사량 
    if user_sex_fi ==1:
        기초대사량 = 66.47 + (13.75 * user_weight_fi) + (5*user_hight_fi) - (6.76*user_age_fi )
    elif user_sex_fi ==2:
        기초대사량 = 655.1 + (9.56 * user_weight_fi) + (1.85*user_hight_fi) - (4.68*user_age_fi )

    권장칼로리_basic = active_mul * 기초대사량
    # 권장 칼로리, 탄단지

    if  goal_box_fi == "벌크업":
        권장칼로리_max = 권장칼로리_basic + 300
        권장칼로리_min = 권장칼로리_basic + 200
        권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%권장칼로리_min} ~ {'%.1f'%권장칼로리_max} kcal"

        권장평균단백질= user_weight_fi*1.8
        권장최대단백질= user_weight_fi*2
        권장최소단백질= user_weight_fi*1.6
        단백질오차 = (권장최대단백질-권장최소단백질)/2

        권장평균탄수화물= 권장평균단백질*5/3
        권장최대탄수화물= 권장최대단백질*5/3
        권장최소탄수화물= 권장최소단백질*5/3
        탄수화물오차 = (권장최대탄수화물-권장최소탄수화물)/2

        권장평균지방= 권장평균단백질*2/3
        권장최대지방= 권장최대단백질*2/3
        권장최소지방= 권장최소단백질*2/3
        지방오차 = (권장최대지방-권장최소지방)/2

        권장단백질 = f"권장 섭취 단백질 : {'%.1f'%권장평균단백질} ± {'%.1f'%단백질오차} g"
        권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%권장평균탄수화물} ± {'%.1f'%탄수화물오차} g"
        권장지방 =  f"권장 섭취 지방 : {'%.1f'%권장평균지방} ± {'%.1f'%지방오차} g"

    elif goal_box_fi == "다이어트":
        권장칼로리_max = 권장칼로리_basic - 500
        권장칼로리_min = 권장칼로리_basic - 700
        권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%권장칼로리_min} ~ {'%.1f'%권장칼로리_max} kcal"

        권장평균단백질= user_weight_fi*1.8
        권장최대단백질= user_weight_fi*2
        권장최소단백질= user_weight_fi*1.6
        단백질오차 = (권장최대단백질-권장최소단백질)/2

        권장평균탄수화물= 권장평균단백질*3/5
        권장최대탄수화물= 권장최대단백질*3/5
        권장최소탄수화물= 권장최소단백질*3/5
        탄수화물오차 = (권장최대탄수화물-권장최소탄수화물)/2

        권장평균지방= 권장평균단백질*2/5
        권장최대지방= 권장최대단백질*2/5
        권장최소지방= 권장최소단백질*2/5
        지방오차 = (권장최대지방-권장최소지방)/2

        권장단백질 = f"권장 섭취 단백질 : {'%.1f'%권장평균단백질} ± {'%.1f'%단백질오차} g"
        권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%권장평균탄수화물} ± {'%.1f'%탄수화물오차} g"
        권장지방 =  f"권장 섭취 지방 : {'%.1f'%권장평균지방} ± {'%.1f'%지방오차} g"

    elif goal_box_fi == "린매스업": 
        권장칼로리_max = 권장칼로리_basic + 200
        권장칼로리_min = 권장칼로리_basic - 200
        권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%권장칼로리_min} ~ {'%.1f'%권장칼로리_max} kcal"

        권장평균단백질= user_weight_fi*1.8
        권장최대단백질= user_weight_fi*2
        권장최소단백질= user_weight_fi*1.6
        단백질오차 = (권장최대단백질-권장최소단백질)/2

        권장평균탄수화물= 권장평균단백질*1
        권장최대탄수화물= 권장최대단백질*1
        권장최소탄수화물= 권장최소단백질*1
        탄수화물오차 = (권장최대탄수화물-권장최소탄수화물)/2

        권장평균지방= 권장평균단백질*2/4
        권장최대지방= 권장최대단백질*2/4
        권장최소지방= 권장최소단백질*2/4
        지방오차 = (권장최대지방-권장최소지방)/2

        권장단백질 = f"권장 섭취 단백질 : {'%.1f'%권장평균단백질} ± {'%.1f'%단백질오차} g"
        권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%권장평균탄수화물} ± {'%.1f'%탄수화물오차} g"
        권장지방 =  f"권장 섭취 지방 : {'%.1f'%권장평균지방} ± {'%.1f'%지방오차} g"
    # # =========================================================================================================================================
    # 실제 섭취 ㅡ 권장, 분석
    #------------------------------------------------------------------------------------------------------------------------------------------1  
    if num == 1:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        if food1_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                 
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%섭취칼로리_1}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%섭취탄수화물_1}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%섭취단백질_1}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%섭취지방_1}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1
                총_섭취탄수화물 = 섭취탄수화물_1
                총_섭취단백질 = 섭취단백질_1
                총_섭취지방 = 섭취지방_1
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print("1:",err)
    

    #------------------------------------------------------------------------------------------------------------------------------------------2            
    if num == 2:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        if food1_weight == "" or food2_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2
                총_섭취지방 = 섭취지방_1 + 섭취지방_2
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)
    #------------------------------------------------------------------------------------------------------------------------------------------3            
    if num == 3:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)
    #------------------------------------------------------------------------------------------------------------------------------------------4            
    if num == 4:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        food4_name = e3_1.get()
        food4_weight = e3_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == ""or food4_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                food4_weight = float(e3_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                for food in 전체_리스트:
                    if food4_name == food[1]:
                        food4_kcal = float(food[3])
                        food4_car = float(food[4])
                        food4_pro = float(food[5])
                        food4_fat = float(food[6])
                        섭취칼로리_4 = food4_kcal * food4_weight
                        섭취탄수화물_4 = food4_car * food4_weight
                        섭취단백질_4 =food4_pro * food4_weight
                        섭취지방_4 =food4_fat * food4_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3+섭취칼로리_4)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3+섭취탄수화물_4)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3+섭취단백질_4)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3+섭취지방_4)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 + 섭취칼로리_4
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3 + 섭취탄수화물_4
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3 + 섭취단백질_4
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3 + 섭취지방_4
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)
    #------------------------------------------------------------------------------------------------------------------------------------5
    if num == 5:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        food4_name = e3_1.get()
        food4_weight = e3_2.get()
        food5_name = e4_1.get()
        food5_weight = e4_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == ""or food4_weight == ""or food5_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                food4_weight = float(e3_2.get())
                food5_weight = float(e4_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                for food in 전체_리스트:
                    if food4_name == food[1]:
                        food4_kcal = float(food[3])
                        food4_car = float(food[4])
                        food4_pro = float(food[5])
                        food4_fat = float(food[6])
                        섭취칼로리_4 = food4_kcal * food4_weight
                        섭취탄수화물_4 = food4_car * food4_weight
                        섭취단백질_4 =food4_pro * food4_weight
                        섭취지방_4 =food4_fat * food4_weight
                for food in 전체_리스트:
                    if food5_name == food[1]:
                        food5_kcal = float(food[3])
                        food5_car = float(food[4])
                        food5_pro = float(food[5])
                        food5_fat = float(food[6])
                        섭취칼로리_5 = food5_kcal * food5_weight
                        섭취탄수화물_5 = food5_car * food5_weight
                        섭취단백질_5 =food5_pro * food5_weight
                        섭취지방_5 =food5_fat * food5_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3+섭취칼로리_4+섭취칼로리_5)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3+섭취탄수화물_4+섭취탄수화물_5)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3+섭취단백질_4+섭취단백질_5)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3+섭취지방_4+섭취지방_5)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 + 섭취칼로리_4 + 섭취칼로리_5
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3 + 섭취탄수화물_4 + 섭취탄수화물_5
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3 + 섭취단백질_4 + 섭취단백질_5
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3 + 섭취지방_4 + 섭취지방_5
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)

    #------------------------------------------------------------------------------------------------------------------------------------6
    if num == 6:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        food4_name = e3_1.get()
        food4_weight = e3_2.get()
        food5_name = e4_1.get()
        food5_weight = e4_2.get()
        food6_name = e5_1.get()
        food6_weight = e5_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == ""or food4_weight == ""or \
            food5_weight == ""or food6_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                food4_weight = float(e3_2.get())
                food5_weight = float(e4_2.get())
                food6_weight = float(e5_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                for food in 전체_리스트:
                    if food4_name == food[1]:
                        food4_kcal = float(food[3])
                        food4_car = float(food[4])
                        food4_pro = float(food[5])
                        food4_fat = float(food[6])
                        섭취칼로리_4 = food4_kcal * food4_weight
                        섭취탄수화물_4 = food4_car * food4_weight
                        섭취단백질_4 =food4_pro * food4_weight
                        섭취지방_4 =food4_fat * food4_weight
                for food in 전체_리스트:
                    if food5_name == food[1]:
                        food5_kcal = float(food[3])
                        food5_car = float(food[4])
                        food5_pro = float(food[5])
                        food5_fat = float(food[6])
                        섭취칼로리_5 = food5_kcal * food5_weight
                        섭취탄수화물_5 = food5_car * food5_weight
                        섭취단백질_5 =food5_pro * food5_weight
                        섭취지방_5 =food5_fat * food5_weight
                for food in 전체_리스트:
                    if food6_name == food[1]:
                        food6_kcal = float(food[3])
                        food6_car = float(food[4])
                        food6_pro = float(food[5])
                        food6_fat = float(food[6])
                        섭취칼로리_6 = food6_kcal * food6_weight
                        섭취탄수화물_6 = food6_car * food6_weight
                        섭취단백질_6 =food6_pro * food6_weight
                        섭취지방_6 =food6_fat * food6_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3+섭취칼로리_4+섭취칼로리_5+섭취칼로리_6)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3+섭취탄수화물_4+섭취탄수화물_5+섭취탄수화물_6)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3+섭취단백질_4+섭취단백질_5+섭취단백질_6)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3+섭취지방_4+섭취지방_5+섭취지방_6)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 + 섭취칼로리_4 + 섭취칼로리_5 + 섭취칼로리_6
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3 + 섭취탄수화물_4 + 섭취탄수화물_5 + 섭취탄수화물_6
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3 + 섭취단백질_4 + 섭취단백질_5 + 섭취단백질_6
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3 + 섭취지방_4 + 섭취지방_5 + 섭취지방_6
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)

    #------------------------------------------------------------------------------------------------------------------------------------
    if num == 7:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        food4_name = e3_1.get()
        food4_weight = e3_2.get()
        food5_name = e4_1.get()
        food5_weight = e4_2.get()
        food6_name = e5_1.get()
        food6_weight = e5_2.get()
        food7_name = e6_1.get()
        food7_weight = e6_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == ""or food4_weight == ""or \
            food5_weight == ""or food6_weight == "" or food7_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                food4_weight = float(e3_2.get())
                food5_weight = float(e4_2.get())
                food6_weight = float(e5_2.get())
                food7_weight = float(e6_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                for food in 전체_리스트:
                    if food4_name == food[1]:
                        food4_kcal = float(food[3])
                        food4_car = float(food[4])
                        food4_pro = float(food[5])
                        food4_fat = float(food[6])
                        섭취칼로리_4 = food4_kcal * food4_weight
                        섭취탄수화물_4 = food4_car * food4_weight
                        섭취단백질_4 =food4_pro * food4_weight
                        섭취지방_4 =food4_fat * food4_weight
                for food in 전체_리스트:
                    if food5_name == food[1]:
                        food5_kcal = float(food[3])
                        food5_car = float(food[4])
                        food5_pro = float(food[5])
                        food5_fat = float(food[6])
                        섭취칼로리_5 = food5_kcal * food5_weight
                        섭취탄수화물_5 = food5_car * food5_weight
                        섭취단백질_5 =food5_pro * food5_weight
                        섭취지방_5 =food5_fat * food5_weight
                for food in 전체_리스트:
                    if food6_name == food[1]:
                        food6_kcal = float(food[3])
                        food6_car = float(food[4])
                        food6_pro = float(food[5])
                        food6_fat = float(food[6])
                        섭취칼로리_6 = food6_kcal * food6_weight
                        섭취탄수화물_6 = food6_car * food6_weight
                        섭취단백질_6 =food6_pro * food6_weight
                        섭취지방_6 =food6_fat * food6_weight
                for food in 전체_리스트:
                    if food7_name == food[1]:
                        food7_kcal = float(food[3])
                        food7_car = float(food[4])
                        food7_pro = float(food[5])
                        food7_fat = float(food[6])
                        섭취칼로리_7 = food7_kcal * food7_weight
                        섭취탄수화물_7 = food7_car * food7_weight
                        섭취단백질_7 =food7_pro * food7_weight
                        섭취지방_7 =food7_fat * food7_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3+섭취칼로리_4+섭취칼로리_5+섭취칼로리_6+섭취칼로리_7)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3+섭취탄수화물_4+섭취탄수화물_5+섭취탄수화물_6+섭취탄수화물_7)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3+섭취단백질_4+섭취단백질_5+섭취단백질_6+섭취단백질_7)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3+섭취지방_4+섭취지방_5+섭취지방_6+섭취지방_7)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 + 섭취칼로리_4 + 섭취칼로리_5 + 섭취칼로리_6 + 섭취칼로리_7
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3 + 섭취탄수화물_4 + 섭취탄수화물_5 + 섭취탄수화물_6 + 섭취탄수화물_7
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3 + 섭취단백질_4 + 섭취단백질_5 + 섭취단백질_6 + 섭취단백질_7
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3 + 섭취지방_4 + 섭취지방_5 + 섭취지방_6 + 섭취지방_7
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)

    #------------------------------------------------------------------------------------------------------------------------------------8
    if num == 8:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        food4_name = e3_1.get()
        food4_weight = e3_2.get()
        food5_name = e4_1.get()
        food5_weight = e4_2.get()
        food6_name = e5_1.get()
        food6_weight = e5_2.get()
        food7_name = e6_1.get()
        food7_weight = e6_2.get()
        food8_name = e7_1.get()
        food8_weight = e7_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == ""or food4_weight == ""or \
            food5_weight == ""or food6_weight == "" or food7_weight == ""or food8_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                food4_weight = float(e3_2.get())
                food5_weight = float(e4_2.get())
                food6_weight = float(e5_2.get())
                food7_weight = float(e6_2.get())
                food8_weight = float(e7_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                for food in 전체_리스트:
                    if food4_name == food[1]:
                        food4_kcal = float(food[3])
                        food4_car = float(food[4])
                        food4_pro = float(food[5])
                        food4_fat = float(food[6])
                        섭취칼로리_4 = food4_kcal * food4_weight
                        섭취탄수화물_4 = food4_car * food4_weight
                        섭취단백질_4 =food4_pro * food4_weight
                        섭취지방_4 =food4_fat * food4_weight
                for food in 전체_리스트:
                    if food5_name == food[1]:
                        food5_kcal = float(food[3])
                        food5_car = float(food[4])
                        food5_pro = float(food[5])
                        food5_fat = float(food[6])
                        섭취칼로리_5 = food5_kcal * food5_weight
                        섭취탄수화물_5 = food5_car * food5_weight
                        섭취단백질_5 =food5_pro * food5_weight
                        섭취지방_5 =food5_fat * food5_weight
                for food in 전체_리스트:
                    if food6_name == food[1]:
                        food6_kcal = float(food[3])
                        food6_car = float(food[4])
                        food6_pro = float(food[5])
                        food6_fat = float(food[6])
                        섭취칼로리_6 = food6_kcal * food6_weight
                        섭취탄수화물_6 = food6_car * food6_weight
                        섭취단백질_6 =food6_pro * food6_weight
                        섭취지방_6 =food6_fat * food6_weight
                for food in 전체_리스트:
                    if food7_name == food[1]:
                        food7_kcal = float(food[3])
                        food7_car = float(food[4])
                        food7_pro = float(food[5])
                        food7_fat = float(food[6])
                        섭취칼로리_7 = food7_kcal * food7_weight
                        섭취탄수화물_7 = food7_car * food7_weight
                        섭취단백질_7 =food7_pro * food7_weight
                        섭취지방_7 =food7_fat * food7_weight
                for food in 전체_리스트:
                    if food8_name == food[1]:
                        food8_kcal = float(food[3])
                        food8_car = float(food[4])
                        food8_pro = float(food[5])
                        food8_fat = float(food[6])
                        섭취칼로리_8 = food8_kcal * food8_weight
                        섭취탄수화물_8 = food8_car * food8_weight
                        섭취단백질_8 =food8_pro * food8_weight
                        섭취지방_8 =food8_fat * food8_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3+섭취칼로리_4+섭취칼로리_5+섭취칼로리_6+섭취칼로리_7+섭취칼로리_8)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3+섭취탄수화물_4+섭취탄수화물_5+섭취탄수화물_6+섭취탄수화물_7+섭취탄수화물_8)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3+섭취단백질_4+섭취단백질_5+섭취단백질_6+섭취단백질_7+섭취단백질_8)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3+섭취지방_4+섭취지방_5+섭취지방_6+섭취지방_7+섭취지방_8)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 + 섭취칼로리_4 + 섭취칼로리_5 + 섭취칼로리_6 + 섭취칼로리_7 + 섭취칼로리_8
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3 + 섭취탄수화물_4 + 섭취탄수화물_5 + 섭취탄수화물_6 + 섭취탄수화물_7 + 섭취탄수화물_8
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3 + 섭취단백질_4 + 섭취단백질_5 + 섭취단백질_6 + 섭취단백질_7 + 섭취단백질_8
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3 + 섭취지방_4 + 섭취지방_5 + 섭취지방_6 + 섭취지방_7 + 섭취지방_8
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)

    #------------------------------------------------------------------------------------------------------------------------------------9
    if num == 9:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        food4_name = e3_1.get()
        food4_weight = e3_2.get()
        food5_name = e4_1.get()
        food5_weight = e4_2.get()
        food6_name = e5_1.get()
        food6_weight = e5_2.get()
        food7_name = e6_1.get()
        food7_weight = e6_2.get()
        food8_name = e7_1.get()
        food8_weight = e7_2.get()
        food9_name = e8_1.get()
        food9_weight = e8_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == ""or food4_weight == ""or \
            food5_weight == ""or food6_weight == "" or food7_weight == ""or food8_weight == "" or\
                food9_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                food4_weight = float(e3_2.get())
                food5_weight = float(e4_2.get())
                food6_weight = float(e5_2.get())
                food7_weight = float(e6_2.get())
                food8_weight = float(e7_2.get())
                food9_weight = float(e8_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                for food in 전체_리스트:
                    if food4_name == food[1]:
                        food4_kcal = float(food[3])
                        food4_car = float(food[4])
                        food4_pro = float(food[5])
                        food4_fat = float(food[6])
                        섭취칼로리_4 = food4_kcal * food4_weight
                        섭취탄수화물_4 = food4_car * food4_weight
                        섭취단백질_4 =food4_pro * food4_weight
                        섭취지방_4 =food4_fat * food4_weight
                for food in 전체_리스트:
                    if food5_name == food[1]:
                        food5_kcal = float(food[3])
                        food5_car = float(food[4])
                        food5_pro = float(food[5])
                        food5_fat = float(food[6])
                        섭취칼로리_5 = food5_kcal * food5_weight
                        섭취탄수화물_5 = food5_car * food5_weight
                        섭취단백질_5 =food5_pro * food5_weight
                        섭취지방_5 =food5_fat * food5_weight
                for food in 전체_리스트:
                    if food6_name == food[1]:
                        food6_kcal = float(food[3])
                        food6_car = float(food[4])
                        food6_pro = float(food[5])
                        food6_fat = float(food[6])
                        섭취칼로리_6 = food6_kcal * food6_weight
                        섭취탄수화물_6 = food6_car * food6_weight
                        섭취단백질_6 =food6_pro * food6_weight
                        섭취지방_6 =food6_fat * food6_weight
                for food in 전체_리스트:
                    if food7_name == food[1]:
                        food7_kcal = float(food[3])
                        food7_car = float(food[4])
                        food7_pro = float(food[5])
                        food7_fat = float(food[6])
                        섭취칼로리_7 = food7_kcal * food7_weight
                        섭취탄수화물_7 = food7_car * food7_weight
                        섭취단백질_7 =food7_pro * food7_weight
                        섭취지방_7 =food7_fat * food7_weight
                for food in 전체_리스트:
                    if food8_name == food[1]:
                        food8_kcal = float(food[3])
                        food8_car = float(food[4])
                        food8_pro = float(food[5])
                        food8_fat = float(food[6])
                        섭취칼로리_8 = food8_kcal * food8_weight
                        섭취탄수화물_8 = food8_car * food8_weight
                        섭취단백질_8 =food8_pro * food8_weight
                        섭취지방_8 =food8_fat * food8_weight
                for food in 전체_리스트:
                    if food9_name == food[1]:
                        food9_kcal = float(food[3])
                        food9_car = float(food[4])
                        food9_pro = float(food[5])
                        food9_fat = float(food[6])
                        섭취칼로리_9 = food9_kcal * food9_weight
                        섭취탄수화물_9 = food9_car * food9_weight
                        섭취단백질_9 =food9_pro * food9_weight
                        섭취지방_9 =food9_fat * food9_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3+섭취칼로리_4+섭취칼로리_5+섭취칼로리_6+섭취칼로리_7+섭취칼로리_8+섭취칼로리_9)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3+섭취탄수화물_4+섭취탄수화물_5+섭취탄수화물_6+섭취탄수화물_7+섭취탄수화물_8+섭취탄수화물_9)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3+섭취단백질_4+섭취단백질_5+섭취단백질_6+섭취단백질_7+섭취단백질_8+섭취단백질_9)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3+섭취지방_4+섭취지방_5+섭취지방_6+섭취지방_7+섭취지방_8+섭취지방_9)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 + 섭취칼로리_4 + 섭취칼로리_5 + 섭취칼로리_6 + 섭취칼로리_7 + 섭취칼로리_8 + 섭취칼로리_9
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3 + 섭취탄수화물_4 + 섭취탄수화물_5 + 섭취탄수화물_6 + 섭취탄수화물_7 + 섭취탄수화물_8 + 섭취탄수화물_9
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3 + 섭취단백질_4 + 섭취단백질_5 + 섭취단백질_6 + 섭취단백질_7 + 섭취단백질_8 + 섭취단백질_9
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3 + 섭취지방_4 + 섭취지방_5 + 섭취지방_6 + 섭취지방_7 + 섭취지방_8 + 섭취지방_9
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)

    #------------------------------------------------------------------------------------------------------------------------------------10
    if num == 10:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        food4_name = e3_1.get()
        food4_weight = e3_2.get()
        food5_name = e4_1.get()
        food5_weight = e4_2.get()
        food6_name = e5_1.get()
        food6_weight = e5_2.get()
        food7_name = e6_1.get()
        food7_weight = e6_2.get()
        food8_name = e7_1.get()
        food8_weight = e7_2.get()
        food9_name = e8_1.get()
        food9_weight = e8_2.get()
        food10_name = e9_1.get()
        food10_weight = e9_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == ""or food4_weight == ""or \
            food5_weight == ""or food6_weight == "" or food7_weight == ""or food8_weight == "" or\
                food9_weight == "" or food10_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                food4_weight = float(e3_2.get())
                food5_weight = float(e4_2.get())
                food6_weight = float(e5_2.get())
                food7_weight = float(e6_2.get())
                food8_weight = float(e7_2.get())
                food9_weight = float(e8_2.get())
                food10_weight = float(e9_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                for food in 전체_리스트:
                    if food4_name == food[1]:
                        food4_kcal = float(food[3])
                        food4_car = float(food[4])
                        food4_pro = float(food[5])
                        food4_fat = float(food[6])
                        섭취칼로리_4 = food4_kcal * food4_weight
                        섭취탄수화물_4 = food4_car * food4_weight
                        섭취단백질_4 =food4_pro * food4_weight
                        섭취지방_4 =food4_fat * food4_weight
                for food in 전체_리스트:
                    if food5_name == food[1]:
                        food5_kcal = float(food[3])
                        food5_car = float(food[4])
                        food5_pro = float(food[5])
                        food5_fat = float(food[6])
                        섭취칼로리_5 = food5_kcal * food5_weight
                        섭취탄수화물_5 = food5_car * food5_weight
                        섭취단백질_5 =food5_pro * food5_weight
                        섭취지방_5 =food5_fat * food5_weight
                for food in 전체_리스트:
                    if food6_name == food[1]:
                        food6_kcal = float(food[3])
                        food6_car = float(food[4])
                        food6_pro = float(food[5])
                        food6_fat = float(food[6])
                        섭취칼로리_6 = food6_kcal * food6_weight
                        섭취탄수화물_6 = food6_car * food6_weight
                        섭취단백질_6 =food6_pro * food6_weight
                        섭취지방_6 =food6_fat * food6_weight
                for food in 전체_리스트:
                    if food7_name == food[1]:
                        food7_kcal = float(food[3])
                        food7_car = float(food[4])
                        food7_pro = float(food[5])
                        food7_fat = float(food[6])
                        섭취칼로리_7 = food7_kcal * food7_weight
                        섭취탄수화물_7 = food7_car * food7_weight
                        섭취단백질_7 =food7_pro * food7_weight
                        섭취지방_7 =food7_fat * food7_weight
                for food in 전체_리스트:
                    if food8_name == food[1]:
                        food8_kcal = float(food[3])
                        food8_car = float(food[4])
                        food8_pro = float(food[5])
                        food8_fat = float(food[6])
                        섭취칼로리_8 = food8_kcal * food8_weight
                        섭취탄수화물_8 = food8_car * food8_weight
                        섭취단백질_8 =food8_pro * food8_weight
                        섭취지방_8 =food8_fat * food8_weight
                for food in 전체_리스트:
                    if food9_name == food[1]:
                        food9_kcal = float(food[3])
                        food9_car = float(food[4])
                        food9_pro = float(food[5])
                        food9_fat = float(food[6])
                        섭취칼로리_9 = food9_kcal * food9_weight
                        섭취탄수화물_9 = food9_car * food9_weight
                        섭취단백질_9 =food9_pro * food9_weight
                        섭취지방_9 =food9_fat * food9_weight
                for food in 전체_리스트:
                    if food10_name == food[1]:
                        food10_kcal = float(food[3])
                        food10_car = float(food[4])
                        food10_pro = float(food[5])
                        food10_fat = float(food[6])
                        섭취칼로리_10 = food10_kcal * food10_weight
                        섭취탄수화물_10 = food10_car * food10_weight
                        섭취단백질_10 =food10_pro * food10_weight
                        섭취지방_10 =food10_fat * food10_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3+섭취칼로리_4+섭취칼로리_5+섭취칼로리_6+섭취칼로리_7+섭취칼로리_8+섭취칼로리_9+섭취칼로리_10)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3+섭취탄수화물_4+섭취탄수화물_5+섭취탄수화물_6+섭취탄수화물_7+섭취탄수화물_8+섭취탄수화물_9+섭취탄수화물_10)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3+섭취단백질_4+섭취단백질_5+섭취단백질_6+섭취단백질_7+섭취단백질_8+섭취단백질_9+섭취단백질_10)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3+섭취지방_4+섭취지방_5+섭취지방_6+섭취지방_7+섭취지방_8+섭취지방_9+섭취지방_10)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 + 섭취칼로리_4 + 섭취칼로리_5 + 섭취칼로리_6 + 섭취칼로리_7 + 섭취칼로리_8 + 섭취칼로리_9 + 섭취칼로리_10
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3 + 섭취탄수화물_4 + 섭취탄수화물_5 + 섭취탄수화물_6 + 섭취탄수화물_7 + 섭취탄수화물_8 + 섭취탄수화물_9 + 섭취탄수화물_10
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3 + 섭취단백질_4 + 섭취단백질_5 + 섭취단백질_6 + 섭취단백질_7 + 섭취단백질_8 + 섭취단백질_9 + 섭취단백질_10
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3 + 섭취지방_4 + 섭취지방_5 + 섭취지방_6 + 섭취지방_7 + 섭취지방_8 + 섭취지방_9 + 섭취지방_10
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)

    #------------------------------------------------------------------------------------------------------------------------------------11
    if num == 11:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        food4_name = e3_1.get()
        food4_weight = e3_2.get()
        food5_name = e4_1.get()
        food5_weight = e4_2.get()
        food6_name = e5_1.get()
        food6_weight = e5_2.get()
        food7_name = e6_1.get()
        food7_weight = e6_2.get()
        food8_name = e7_1.get()
        food8_weight = e7_2.get()
        food9_name = e8_1.get()
        food9_weight = e8_2.get()
        food10_name = e9_1.get()
        food10_weight = e9_2.get()
        food11_name = e10_1.get()
        food11_weight = e10_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == ""or food4_weight == ""or \
            food5_weight == ""or food6_weight == "" or food7_weight == ""or food8_weight == "" or\
                food9_weight == "" or food10_weight == ""or food11_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                food4_weight = float(e3_2.get())
                food5_weight = float(e4_2.get())
                food6_weight = float(e5_2.get())
                food7_weight = float(e6_2.get())
                food8_weight = float(e7_2.get())
                food9_weight = float(e8_2.get())
                food10_weight = float(e9_2.get())
                food11_weight = float(e10_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                for food in 전체_리스트:
                    if food4_name == food[1]:
                        food4_kcal = float(food[3])
                        food4_car = float(food[4])
                        food4_pro = float(food[5])
                        food4_fat = float(food[6])
                        섭취칼로리_4 = food4_kcal * food4_weight
                        섭취탄수화물_4 = food4_car * food4_weight
                        섭취단백질_4 =food4_pro * food4_weight
                        섭취지방_4 =food4_fat * food4_weight
                for food in 전체_리스트:
                    if food5_name == food[1]:
                        food5_kcal = float(food[3])
                        food5_car = float(food[4])
                        food5_pro = float(food[5])
                        food5_fat = float(food[6])
                        섭취칼로리_5 = food5_kcal * food5_weight
                        섭취탄수화물_5 = food5_car * food5_weight
                        섭취단백질_5 =food5_pro * food5_weight
                        섭취지방_5 =food5_fat * food5_weight
                for food in 전체_리스트:
                    if food6_name == food[1]:
                        food6_kcal = float(food[3])
                        food6_car = float(food[4])
                        food6_pro = float(food[5])
                        food6_fat = float(food[6])
                        섭취칼로리_6 = food6_kcal * food6_weight
                        섭취탄수화물_6 = food6_car * food6_weight
                        섭취단백질_6 =food6_pro * food6_weight
                        섭취지방_6 =food6_fat * food6_weight
                for food in 전체_리스트:
                    if food7_name == food[1]:
                        food7_kcal = float(food[3])
                        food7_car = float(food[4])
                        food7_pro = float(food[5])
                        food7_fat = float(food[6])
                        섭취칼로리_7 = food7_kcal * food7_weight
                        섭취탄수화물_7 = food7_car * food7_weight
                        섭취단백질_7 =food7_pro * food7_weight
                        섭취지방_7 =food7_fat * food7_weight
                for food in 전체_리스트:
                    if food8_name == food[1]:
                        food8_kcal = float(food[3])
                        food8_car = float(food[4])
                        food8_pro = float(food[5])
                        food8_fat = float(food[6])
                        섭취칼로리_8 = food8_kcal * food8_weight
                        섭취탄수화물_8 = food8_car * food8_weight
                        섭취단백질_8 =food8_pro * food8_weight
                        섭취지방_8 =food8_fat * food8_weight
                for food in 전체_리스트:
                    if food9_name == food[1]:
                        food9_kcal = float(food[3])
                        food9_car = float(food[4])
                        food9_pro = float(food[5])
                        food9_fat = float(food[6])
                        섭취칼로리_9 = food9_kcal * food9_weight
                        섭취탄수화물_9 = food9_car * food9_weight
                        섭취단백질_9 =food9_pro * food9_weight
                        섭취지방_9 =food9_fat * food9_weight
                for food in 전체_리스트:
                    if food10_name == food[1]:
                        food10_kcal = float(food[3])
                        food10_car = float(food[4])
                        food10_pro = float(food[5])
                        food10_fat = float(food[6])
                        섭취칼로리_10 = food10_kcal * food10_weight
                        섭취탄수화물_10 = food10_car * food10_weight
                        섭취단백질_10 =food10_pro * food10_weight
                        섭취지방_10 =food10_fat * food10_weight
                for food in 전체_리스트:
                    if food11_name == food[1]:
                        food11_kcal = float(food[3])
                        food11_car = float(food[4])
                        food11_pro = float(food[5])
                        food11_fat = float(food[6])
                        섭취칼로리_11 = food11_kcal * food11_weight
                        섭취탄수화물_11 = food11_car * food11_weight
                        섭취단백질_11 =food11_pro * food11_weight
                        섭취지방_11 =food11_fat * food11_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3+섭취칼로리_4+섭취칼로리_5+섭취칼로리_6+섭취칼로리_7+섭취칼로리_8+섭취칼로리_9+섭취칼로리_10+섭취칼로리_11)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3+섭취탄수화물_4+섭취탄수화물_5+섭취탄수화물_6+섭취탄수화물_7+섭취탄수화물_8+섭취탄수화물_9+섭취탄수화물_10+섭취탄수화물_11)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3+섭취단백질_4+섭취단백질_5+섭취단백질_6+섭취단백질_7+섭취단백질_8+섭취단백질_9+섭취단백질_10+섭취단백질_11)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3+섭취지방_4+섭취지방_5+섭취지방_6+섭취지방_7+섭취지방_8+섭취지방_9+섭취지방_10+섭취지방_11)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 + 섭취칼로리_4 + 섭취칼로리_5 + 섭취칼로리_6 + 섭취칼로리_7 + 섭취칼로리_8 + 섭취칼로리_9 + 섭취칼로리_10 + 섭취칼로리_11
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3 + 섭취탄수화물_4 + 섭취탄수화물_5 + 섭취탄수화물_6 + 섭취탄수화물_7 + 섭취탄수화물_8 + 섭취탄수화물_9 + 섭취탄수화물_10 + 섭취탄수화물_11
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3 + 섭취단백질_4 + 섭취단백질_5 + 섭취단백질_6 + 섭취단백질_7 + 섭취단백질_8 + 섭취단백질_9 + 섭취단백질_10 + 섭취단백질_11
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3 + 섭취지방_4 + 섭취지방_5 + 섭취지방_6 + 섭취지방_7 + 섭취지방_8 + 섭취지방_9 + 섭취지방_10 + 섭취지방_11
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)

    #------------------------------------------------------------------------------------------------------------------------------------11
    if num == 12:
        food1_name = e0_1.get()
        food1_weight = e0_2.get()
        food2_name = e1_1.get()
        food2_weight = e1_2.get()
        food3_name = e2_1.get()
        food3_weight = e2_2.get()
        food4_name = e3_1.get()
        food4_weight = e3_2.get()
        food5_name = e4_1.get()
        food5_weight = e4_2.get()
        food6_name = e5_1.get()
        food6_weight = e5_2.get()
        food7_name = e6_1.get()
        food7_weight = e6_2.get()
        food8_name = e7_1.get()
        food8_weight = e7_2.get()
        food9_name = e8_1.get()
        food9_weight = e8_2.get()
        food10_name = e9_1.get()
        food10_weight = e9_2.get()
        food11_name = e10_1.get()
        food11_weight = e10_2.get()
        food12_name = e11_1.get()
        food12_weight = e11_2.get()
        if food1_weight == "" or food2_weight == "" or food3_weight == ""or food4_weight == ""or \
            food5_weight == ""or food6_weight == "" or food7_weight == ""or food8_weight == "" or\
                food9_weight == "" or food10_weight == ""or food11_weight == ""or food11_weight == "":
            msgbox.showerror("음식 무게 에러","음식 무게를 입력하시오.")
        else:
            try:
                food1_weight = float(e0_2.get())
                food2_weight = float(e1_2.get())
                food3_weight = float(e2_2.get())
                food4_weight = float(e3_2.get())
                food5_weight = float(e4_2.get())
                food6_weight = float(e5_2.get())
                food7_weight = float(e6_2.get())
                food8_weight = float(e7_2.get())
                food9_weight = float(e8_2.get())
                food10_weight = float(e9_2.get())
                food11_weight = float(e10_2.get())
                food12_weight = float(e11_2.get())
                for food in 전체_리스트:
                    if food1_name == food[1]:
                        food1_kcal = float(food[3])
                        food1_car = float(food[4])
                        food1_pro = float(food[5])
                        food1_fat = float(food[6])
                        섭취칼로리_1 = food1_kcal * food1_weight
                        섭취탄수화물_1 = food1_car * food1_weight
                        섭취단백질_1 =food1_pro * food1_weight
                        섭취지방_1 =food1_fat * food1_weight
                for food in 전체_리스트:
                    if food2_name == food[1]:
                        food2_kcal = float(food[3])
                        food2_car = float(food[4])
                        food2_pro = float(food[5])
                        food2_fat = float(food[6])
                        섭취칼로리_2 = food2_kcal * food2_weight
                        섭취탄수화물_2 = food2_car * food2_weight
                        섭취단백질_2 =food2_pro * food2_weight
                        섭취지방_2 =food2_fat * food2_weight
                for food in 전체_리스트:
                    if food3_name == food[1]:
                        food3_kcal = float(food[3])
                        food3_car = float(food[4])
                        food3_pro = float(food[5])
                        food3_fat = float(food[6])
                        섭취칼로리_3 = food3_kcal * food3_weight
                        섭취탄수화물_3 = food3_car * food3_weight
                        섭취단백질_3 =food3_pro * food3_weight
                        섭취지방_3 =food3_fat * food3_weight
                for food in 전체_리스트:
                    if food4_name == food[1]:
                        food4_kcal = float(food[3])
                        food4_car = float(food[4])
                        food4_pro = float(food[5])
                        food4_fat = float(food[6])
                        섭취칼로리_4 = food4_kcal * food4_weight
                        섭취탄수화물_4 = food4_car * food4_weight
                        섭취단백질_4 =food4_pro * food4_weight
                        섭취지방_4 =food4_fat * food4_weight
                for food in 전체_리스트:
                    if food5_name == food[1]:
                        food5_kcal = float(food[3])
                        food5_car = float(food[4])
                        food5_pro = float(food[5])
                        food5_fat = float(food[6])
                        섭취칼로리_5 = food5_kcal * food5_weight
                        섭취탄수화물_5 = food5_car * food5_weight
                        섭취단백질_5 =food5_pro * food5_weight
                        섭취지방_5 =food5_fat * food5_weight
                for food in 전체_리스트:
                    if food6_name == food[1]:
                        food6_kcal = float(food[3])
                        food6_car = float(food[4])
                        food6_pro = float(food[5])
                        food6_fat = float(food[6])
                        섭취칼로리_6 = food6_kcal * food6_weight
                        섭취탄수화물_6 = food6_car * food6_weight
                        섭취단백질_6 =food6_pro * food6_weight
                        섭취지방_6 =food6_fat * food6_weight
                for food in 전체_리스트:
                    if food7_name == food[1]:
                        food7_kcal = float(food[3])
                        food7_car = float(food[4])
                        food7_pro = float(food[5])
                        food7_fat = float(food[6])
                        섭취칼로리_7 = food7_kcal * food7_weight
                        섭취탄수화물_7 = food7_car * food7_weight
                        섭취단백질_7 =food7_pro * food7_weight
                        섭취지방_7 =food7_fat * food7_weight
                for food in 전체_리스트:
                    if food8_name == food[1]:
                        food8_kcal = float(food[3])
                        food8_car = float(food[4])
                        food8_pro = float(food[5])
                        food8_fat = float(food[6])
                        섭취칼로리_8 = food8_kcal * food8_weight
                        섭취탄수화물_8 = food8_car * food8_weight
                        섭취단백질_8 =food8_pro * food8_weight
                        섭취지방_8 =food8_fat * food8_weight
                for food in 전체_리스트:
                    if food9_name == food[1]:
                        food9_kcal = float(food[3])
                        food9_car = float(food[4])
                        food9_pro = float(food[5])
                        food9_fat = float(food[6])
                        섭취칼로리_9 = food9_kcal * food9_weight
                        섭취탄수화물_9 = food9_car * food9_weight
                        섭취단백질_9 =food9_pro * food9_weight
                        섭취지방_9 =food9_fat * food9_weight
                for food in 전체_리스트:
                    if food10_name == food[1]:
                        food10_kcal = float(food[3])
                        food10_car = float(food[4])
                        food10_pro = float(food[5])
                        food10_fat = float(food[6])
                        섭취칼로리_10 = food10_kcal * food10_weight
                        섭취탄수화물_10 = food10_car * food10_weight
                        섭취단백질_10 =food10_pro * food10_weight
                        섭취지방_10 =food10_fat * food10_weight
                for food in 전체_리스트:
                    if food11_name == food[1]:
                        food11_kcal = float(food[3])
                        food11_car = float(food[4])
                        food11_pro = float(food[5])
                        food11_fat = float(food[6])
                        섭취칼로리_11 = food11_kcal * food11_weight
                        섭취탄수화물_11 = food11_car * food11_weight
                        섭취단백질_11 =food11_pro * food11_weight
                        섭취지방_11 =food11_fat * food11_weight
                for food in 전체_리스트:
                    if food12_name == food[1]:
                        food12_kcal = float(food[3])
                        food12_car = float(food[4])
                        food12_pro = float(food[5])
                        food12_fat = float(food[6])
                        섭취칼로리_12 = food12_kcal * food12_weight
                        섭취탄수화물_12 = food12_car * food12_weight
                        섭취단백질_12 =food12_pro * food12_weight
                        섭취지방_12 =food12_fat * food12_weight
                #------------------------------------------------------------------------------------------
                # 프레임3개: result_analysis_실제, result_analysis_권장, result_analysis_분석
                # result_analysis_실제 프레임
                label실제_칼로리= Label(result_analysis_실제, text=f"실제 총 섭취 칼로리 : {'%.1f'%(섭취칼로리_1+섭취칼로리_2+섭취칼로리_3+섭취칼로리_4+섭취칼로리_5+섭취칼로리_6+섭취칼로리_7+섭취칼로리_8+섭취칼로리_9+섭취칼로리_10+섭취칼로리_11+섭취칼로리_12)}kcal")
                label실제_칼로리.pack(side="top")
                label실제_탄수화물= Label(result_analysis_실제, text=f"실제 총 섭취 탄수화물 : {'%.1f'%(섭취탄수화물_1+섭취탄수화물_2+섭취탄수화물_3+섭취탄수화물_4+섭취탄수화물_5+섭취탄수화물_6+섭취탄수화물_7+섭취탄수화물_8+섭취탄수화물_9+섭취탄수화물_10+섭취탄수화물_11+섭취탄수화물_12)}g")
                label실제_탄수화물.pack(side="top")
                label실제_단백질= Label(result_analysis_실제, text=f"실제 총 섭취 단백질 : {'%.1f'%(섭취단백질_1+섭취단백질_2+섭취단백질_3+섭취단백질_4+섭취단백질_5+섭취단백질_6+섭취단백질_7+섭취단백질_8+섭취단백질_9+섭취단백질_10+섭취단백질_11+섭취단백질_12)}g")
                label실제_단백질.pack(side="top")
                label실제_지방= Label(result_analysis_실제, text=f"실제 총 섭취 지방 : {'%.1f'%(섭취지방_1+섭취지방_2+섭취지방_3+섭취지방_4+섭취지방_5+섭취지방_6+섭취지방_7+섭취지방_8+섭취지방_9+섭취지방_10+섭취지방_11+섭취지방_12)}g")
                label실제_지방.pack(side="top")
                # result_analysis_권장 프레임
                if one_or_three.get() == "한끼":
                    권장칼로리 =  f"권장 섭취 칼로리 : {'%.1f'%(권장칼로리_min/3)} ~ {'%.1f'%(권장칼로리_max/3)} kcal"
                    권장단백질 = f"권장 섭취 단백질 : {'%.1f'%(권장평균단백질/3)} ± {'%.1f'%(단백질오차/3)} g"
                    권장탄수화물 =  f"권장 섭취 탄수화물 : {'%.1f'%(권장평균탄수화물/3)} ± {'%.1f'%(탄수화물오차/3)} g"
                    권장지방 =  f"권장 섭취 지방 : {'%.1f'%(권장평균지방/3)} ± {'%.1f'%(지방오차/3)} g"
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                elif one_or_three.get() == "하루":
                    label권장_칼로리= Label(result_analysis_권장, text=권장칼로리)
                    label권장_칼로리.pack(side="top")
                    label권장_탄수화물= Label(result_analysis_권장, text=권장탄수화물)
                    label권장_탄수화물.pack(side="top")
                    label권장_단백질= Label(result_analysis_권장, text=권장단백질)
                    label권장_단백질.pack(side="top")
                    label권장_지방= Label(result_analysis_권장, text=권장지방)
                    label권장_지방.pack(side="top")
                # result_analysis_분석 프레임
                총_섭취칼로리 = 섭취칼로리_1 + 섭취칼로리_2 + 섭취칼로리_3 + 섭취칼로리_4 + 섭취칼로리_5 + 섭취칼로리_6 + 섭취칼로리_7 + 섭취칼로리_8 + 섭취칼로리_9 + 섭취칼로리_10 + 섭취칼로리_11 + 섭취칼로리_12
                총_섭취탄수화물 = 섭취탄수화물_1 + 섭취탄수화물_2 + 섭취탄수화물_3 + 섭취탄수화물_4 + 섭취탄수화물_5 + 섭취탄수화물_6 + 섭취탄수화물_7 + 섭취탄수화물_8 + 섭취탄수화물_9 + 섭취탄수화물_10 + 섭취탄수화물_11 + 섭취탄수화물_12
                총_섭취단백질 = 섭취단백질_1 + 섭취단백질_2 + 섭취단백질_3 + 섭취단백질_4 + 섭취단백질_5 + 섭취단백질_6 + 섭취단백질_7 + 섭취단백질_8 + 섭취단백질_9 + 섭취단백질_10 + 섭취단백질_11 + 섭취단백질_12
                총_섭취지방 = 섭취지방_1 + 섭취지방_2 + 섭취지방_3 + 섭취지방_4 + 섭취지방_5 + 섭취지방_6 + 섭취지방_7 + 섭취지방_8 + 섭취지방_9 + 섭취지방_10 + 섭취지방_11 + 섭취지방_12
                if one_or_three.get() == "한끼":
                    if 권장칼로리_min/3 <= 총_섭취칼로리 <= 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max/3)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min/3:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min/3 - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물/3-탄수화물오차/3 <= 총_섭취탄수화물 <= 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물/3+탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물/3+탄수화물오차/3))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물/3-탄수화물오차/3:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물/3-탄수화물오차/3 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질/3-단백질오차/3 <= 총_섭취단백질 <= 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질/3+단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질/3+단백질오차/3))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질/3-단백질오차/3:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질/3-단백질오차/3 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방/3-지방오차/3 <= 총_섭취지방 <= 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방/3+지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방/3+지방오차/3))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방/3-지방오차/3:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방/3-지방오차/3 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")

                elif one_or_three.get() == "하루":
                    if 권장칼로리_min <= 총_섭취칼로리 <= 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text="칼로리 : 충족")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 > 권장칼로리_max:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(총_섭취칼로리 - 권장칼로리_max)}kcal 초과")
                        분석_칼로리.pack(side="top")
                    elif 총_섭취칼로리 < 권장칼로리_min:
                        분석_칼로리= Label(result_analysis_분석, text=f"칼로리 : {'%.1f'%(권장칼로리_min - 총_섭취칼로리)}kcal 부족")
                        분석_칼로리.pack(side="top")

                    if 권장평균탄수화물-탄수화물오차 <= 총_섭취탄수화물 <= 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text="탄수화물 : 충족")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 > 권장평균탄수화물+탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(총_섭취탄수화물- (권장평균탄수화물+탄수화물오차))}g 초과")
                        분석_탄수화물.pack(side="top")
                    elif 총_섭취탄수화물 < 권장평균탄수화물-탄수화물오차:
                        분석_탄수화물= Label(result_analysis_분석, text=f"탄수화물 : {'%.1f'%(권장평균탄수화물-탄수화물오차 - 총_섭취탄수화물)}g 부족")
                        분석_탄수화물.pack(side="top")

                    if 권장평균단백질-단백질오차 <= 총_섭취단백질 <= 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text="단백질 : 충족")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 > 권장평균단백질+단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(총_섭취단백질- (권장평균단백질+단백질오차))}g 초과")
                        분석_단백질.pack(side="top")
                    elif 총_섭취단백질 < 권장평균단백질-단백질오차:
                        분석_단백질= Label(result_analysis_분석, text=f"단백질 : {'%.1f'%(권장평균단백질-단백질오차 - 총_섭취단백질)}g 부족")
                        분석_단백질.pack(side="top")
                            
                    if 권장평균지방-지방오차 <= 총_섭취지방 <= 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text="지방 : 충족")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 > 권장평균지방+지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(총_섭취지방- (권장평균지방+지방오차))}g 초과")
                        분석_지방.pack(side="top")
                    elif 총_섭취지방 < 권장평균지방-지방오차:
                        분석_지방= Label(result_analysis_분석, text=f"지방 : {'%.1f'%(권장평균지방-지방오차 - 총_섭취지방)}g 부족")
                        분석_지방.pack(side="top")
                #------------------------------------------------------------------------------------------------------------------------------------------------
                frame.tkraise()                   # 음식 무게를 정확히 입력해야 분석 프레임으로 넘어갈 수 있다.
            
            

            except Exception as err:
                msgbox.showerror("입력에러","음식명 또는 음식무게를 정확히 등록하시오.")
                print(err)
    
    
    


    
    

    
    # =========================================================================================================================================
    




# 계산
btnTostart = Button(group_list_frame4, 
    text="분석 시작", 
    padx=10, 
    pady=10, 
    command=lambda:get_data(sub_frame))
btnTostart.pack(side="left", padx=15)

#---------------------------------------------------------------------------------------------------------------------------------
root.mainloop()

