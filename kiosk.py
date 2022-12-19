# 참고: https://m.blog.naver.com/dukalee/221258336167
# 2022.12.17.(토) ~ 2022.12.17.(일) 넘어가는 새벽에. 
# 재현이의 과제를 도와주고자 만들었습니다.
# 키오스크 화면에는 9개의 메뉴와 각 메뉴의 정보가 나옵니다.
# 각 메뉴에는 +, - 버튼이 있고, + 버튼을 누르면 메뉴 하나를 고른 것이고 - 버튼을 누르면 선택 취소를 했다는 의미입니다.
# 메뉴를 선택하면, 메뉴의 가격 총합을 알려줍니다.

# tkinter 를 tk 라는 이름으로 가져옴.
import tkinter as tk

####################################################################
###################### 화면의 배경과 프로그램의 이름. #####################
####################################################################
# root window를 만들어준다.
root = tk.Tk()
root.title('재현이의 먹리스트')
# 프로그램 제목의 frame은 pack으로 설정한다.
labelFrame = tk.Frame(root)
labelFrame.pack(side="top")
# 배경색을 노란색으로 바꾼다.
root['bg'] = 'yellow'
# 창 크기는, root.geometry('AxB') 형식으로 맞춰야 한다.
# pixel 단위.
root.geometry('500x650')

##### 프로그램의 이름. 위젯 - 라벨. ######
# 사용할 폰트 설정.
FONT = ('Futura', 30, 'bold')
# 글의 색깔은 fg, 글의 배경색은 bg.
nameOfProgram = tk.Label(labelFrame, 
text='재현이의 먹리스트', 
fg = 'black',
bg='yellow',
font=FONT,
pady=20)
# pack 메서드로 화면에 뿌려주어야 함. 
nameOfProgram.pack(side="top")
####################################################################
####################################################################
####################################################################





# 메뉴의 가격을 딕셔너리 안에 넣어둘 것임.
priceMenuArray = dict()
# 메뉴의 이름들을 리스트 안에 넣어둘 것임.
labelArray = []
# 메뉴들의 개수를 모두 0으로 초기화 해둘 것임
countMenu = [ 0 for _ in range(9) ]




####################################################################
############################# 객체 ##################################
####################################################################
# 메뉴 정보 표시 오브젝트. (클래스)
class Menu:
    def __init__(self, frameArg, nameMenu, priceMenu, indexOfMenu):
        self.menu = tk.Label(frameArg, 
            text=nameMenu + '\n' + str(priceMenu) + '원',
            fg='black',
            bg='white',
            width=15,
            height=6
        )
        priceMenuArray[indexOfMenu] = priceMenu

# number 가 최종 가격이 된다.
number = 0


# '재현이의 출혈', 즉 총 합산된 가격을 계산하는 함수다. 
def click(priceArg, indexOfMenu):
        global number  # number 는 전역변수.
        # 만약 선택 메뉴 개수가 0인데 -를 눌렀다면 아무런 변화가 없어야함.
        if countMenu[indexOfMenu] == 0 and priceArg < 0:
            pass
        elif number + priceArg >= 0: # 총 합이 양수일 때는 합을 계산한 값을 그대로 출력.
            number += priceArg
        else:  # 합이 음수일 때는 음수를 출력하는 것이 아니라 합을 계산하지 않고 곧바로 0을 출력. 
            number = 0
        print(number)  # 콘솔에 출력.
        price.config(text=str(number))  # GUI 에 출력.


# + 버튼 오브젝트. (클래스)
class btnPlus:
    def __init__(self, frameArg, _indexOfMenu):
        self.indexOfMenu = _indexOfMenu
        self.btnPlus = tk.Button(frameArg,
            text="+",
            fg='black',
            bg='white',
            padx=5,
            command=lambda:[click(priceMenuArray[self.indexOfMenu], _indexOfMenu), self.plus()]
            # 버튼을 눌렀을 때 특정 기능을 수행하게 하려면, command를 써야한다. 
            # command 에서 수행할 함수나 파라미터가 여러 개 일 때는, lambda 를 써야 한다. 
        )

    def plus(self): # + 버튼을 누르면. 메뉴의 개수가 1 증가한다. 
        countMenu[self.indexOfMenu] += 1
        print(labelArray[self.indexOfMenu])
        labelArray[self.indexOfMenu].config(text=countMenu[self.indexOfMenu])


# '선택한 메뉴의 개수' 레이블 오브젝트. (클래스)
class labelNumber:
    def __init__(self, frameArg, indexOfMenu):
        self.labelPrice = tk.Label(frameArg,
            fg='black',
            bg='white',
            padx=10,
        )
        self.labelPrice.config(text="0")
        labelArray.append(self.labelPrice)


# - 버튼 오브젝트. (클래스)
class btnMinus:
    def __init__(self, frameArg, _indexOfMenu):
        self.indexOfMenu = _indexOfMenu
        self.btnMinus = tk.Button(frameArg,
            text="-",
            fg='black',
            bg='white',
            padx=5,
            command=lambda:[click(-priceMenuArray[_indexOfMenu], _indexOfMenu), self.minus()]
        )

    def minus(self):  # - 버튼을 누르면. 메뉴의 개수가 1 감소한다. 
        if countMenu[self.indexOfMenu] > 0:
            countMenu[self.indexOfMenu] -= 1
        labelArray[self.indexOfMenu].config(text=countMenu[self.indexOfMenu])

####################################################################
####################################################################
####################################################################
    



####################################################################
############################ 객체 생성하기 #############################
####################################################################
######## 첫 번째 줄의 메뉴 정보.
firstRowMenu = tk.Frame(root)
firstRowMenu.pack()

menu0 = Menu(firstRowMenu, "한양식당 제육볶음", 7000, 0)
menu0.menu.grid(row=0, column=0)
menu1 = Menu(firstRowMenu, "쪼매 떡볶이", 3500, 1)
menu1.menu.grid(row=0, column=1)
menu2 = Menu(firstRowMenu, "무봉리 국밥", 9000, 2)
menu2.menu.grid(row=0, column=2)
######## 첫 번째 줄의 +, 메뉴의 개수, - 버튼 및 레이블 grid.
firstRow = tk.Frame(root)
firstRow.pack()

plusBtn0 = btnPlus(firstRow, 0)
plusBtn0.btnPlus.grid(row=0, column=0)
labelPrice0 = labelNumber(firstRow, 0)
labelPrice0.labelPrice.grid(row=0, column=1)
minusBtn0 = btnMinus(firstRow, 0)
minusBtn0.btnMinus.grid(row=0, column=2)

plusBtn1 = btnPlus(firstRow, 1)
plusBtn1.btnPlus.grid(row=0, column=3)
labelPrice1 = labelNumber(firstRow, 1)
labelPrice1.labelPrice.grid(row=0, column=4)
minusBtn1 = btnMinus(firstRow, 1)
minusBtn1.btnMinus.grid(row=0, column=5)

plusBtn2 = btnPlus(firstRow, 2)
plusBtn2.btnPlus.grid(row=0, column=6)
labelPrice2 = labelNumber(firstRow, 2)
labelPrice2.labelPrice.grid(row=0, column=7)
minusBtn2 = btnMinus(firstRow, 2)
minusBtn2.btnMinus.grid(row=0, column=9)


########## 두 번째 줄의 메뉴 정보. 
secondRowMenu = tk.Frame(root)
secondRowMenu.pack()

menu3 = Menu(secondRowMenu, "맘스터치 싸이버거", 6400, 3)
menu3.menu.grid(row=0, column=0)
menu4 = Menu(secondRowMenu, "몽키 파스타", 7800, 4)
menu4.menu.grid(row=0, column=1)
menu5 = Menu(secondRowMenu, "사나이뚝배기 우렁이 강된장", 5700, 5)
menu5.menu.grid(row=0, column=2)


######## 두 번째 줄의 +, 메뉴의 개수, - 버튼 및 레이블 grid.
secondRow = tk.Frame(root)
secondRow.pack()

plusBtn3 = btnPlus(secondRow, 3)
plusBtn3.btnPlus.grid(row=0, column=0)
labelPrice3 = labelNumber(secondRow, 3)
labelPrice3.labelPrice.grid(row=0, column=1)
minusBtn3 = btnMinus(secondRow, 3)
minusBtn3.btnMinus.grid(row=0, column=2)

plusBtn4 = btnPlus(secondRow, 4)
plusBtn4.btnPlus.grid(row=0, column=3)
labelPrice4 = labelNumber(secondRow, 4)
labelPrice4.labelPrice.grid(row=0, column=4)
minusBtn4 = btnMinus(secondRow, 4)
minusBtn4.btnMinus.grid(row=0, column=5)

plusBtn5 = btnPlus(secondRow, 5)
plusBtn5.btnPlus.grid(row=0, column=6)
labelPrice5 = labelNumber(secondRow, 5)
labelPrice5.labelPrice.grid(row=0, column=7)
minusBtn5 = btnMinus(secondRow, 5)
minusBtn5.btnMinus.grid(row=0, column=9)


########## 세 번째 줄의 메뉴 정보. 
thirdRowMenu = tk.Frame(root)
thirdRowMenu.pack()

menu6 = Menu(thirdRowMenu, "일상다반 사케동", 11000, 6)
menu6.menu.grid(row=0, column=0)
menu7 = Menu(thirdRowMenu, "백소정 치즈 돈까스", 13000, 7)
menu7.menu.grid(row=0, column=1)
menu8 = Menu(thirdRowMenu, "맛닭꼬", 12900, 8)
menu8.menu.grid(row=0, column=2)


######## 세 번째 줄의 +, 메뉴의 개수, - 버튼 및 레이블 grid.
thirdRow = tk.Frame(root)
thirdRow.pack()

plusBtn6 = btnPlus(thirdRow, 6)
plusBtn6.btnPlus.grid(row=0, column=0)
labelPrice6 = labelNumber(thirdRow, 6)
labelPrice6.labelPrice.grid(row=0, column=1)
minusBtn6 = btnMinus(thirdRow, 6)
minusBtn6.btnMinus.grid(row=0, column=2)

plusBtn7 = btnPlus(thirdRow, 7)
plusBtn7.btnPlus.grid(row=0, column=3)
labelPrice7 = labelNumber(thirdRow, 7)
labelPrice7.labelPrice.grid(row=0, column=4)
minusBtn7 = btnMinus(thirdRow, 7)
minusBtn7.btnMinus.grid(row=0, column=5)

plusBtn8 = btnPlus(thirdRow, 8)
plusBtn8.btnPlus.grid(row=0, column=6)
labelPrice8 = labelNumber(thirdRow, 8)
labelPrice8.labelPrice.grid(row=0, column=7)
minusBtn8 = btnMinus(thirdRow, 8)
minusBtn8.btnMinus.grid(row=0, column=9)




####################################
####################################
###### 가격의 총합이 나타나는 라벨 입니다!! 
priceLabelFrame = tk.Frame(root)
priceLabelFrame.pack()
FONT = ('맑은 고딕', 20, 'bold')
priceLabel = tk.Label(priceLabelFrame, 
text='재현이의 출혈',
fg = "#3373FF" ,
bg='yellow',
font=FONT,
pady=20)
priceLabel.pack()



priceFrame = tk.Frame(root)
priceFrame.pack()
FONT = ('맑은 고딕', 50, 'bold')
price = tk.Label(priceFrame,
fg = "#FF3333",
bg = 'yellow',
font = FONT
)
price.pack()
price.config(text="0")


finalLabel = tk.Frame(root)
finalLabel.pack()
FONT = ('맑은 고딕', 20, 'bold')
label = tk.Label(finalLabel, 
text='원',
fg = "#3373FF" ,
bg='yellow',
font=FONT,
pady=20)
label.pack()



# 프로그램 실행. 
root.mainloop()