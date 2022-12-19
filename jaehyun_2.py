# 참고: https://m.blog.naver.com/dukalee/221258336167
# tkinter 를 tk 라는 이름으로 가져옴.
import tkinter as tk

# root window를 만들어준다.
root = tk.Tk()
root.title('재현이의 먹리스트')

# number 가 최종 가격이 될 터이다. 
number = 0

# 프로그램 제목의 frame은 pack 로 하겠습니다. 
labelFrame = tk.Frame(root)
labelFrame.pack(side="top")

# 배경색을 노란색으로 바꿈.
root['bg'] = 'yellow'

# 창 크기는, root.geometry('AxB') 형식으루다가.
# pixel 단위임.
root.geometry('500x600')


# 메뉴의 이름들을 배열 안에다가 집어 넣어둘 것임.
labelArray = []
# 메뉴들의 개수를 모두 0으로 초기화해 넣을 것임.
countMenu = [ 0 for _ in range(9) ]


##### 프로그램의 이름. 위젯 - 라벨. ######
# 사용할 폰트 설정.
FONT = ('Futura', 30, 'bold')
# 글의 색깔은 fg, 글의 배경색은 bg.
nameOfProgram = tk.Label(labelFrame, 
text='재현이의 먹리스트', 
fg = 'black',
bg='yellow',
font=FONT,
pady=30)
# pack 메서드로 화면에 뿌려주어야 함. 
nameOfProgram.pack(side="top")

#############################################
################# OBJECT ####################
#############################################

class amountMenu:  # +, - 버튼과 메뉴의 개수 정보가 표시 되어 있는 오브젝트.
    def __init__(self,indexOfMenu, frameArg):
        btnPlus = tk.Button(frameArg,
            text="+",
            fg='black',
            bg='white',
            padx=5,
            command=lambda:[self.click(labelArray[indexOfMenu]), self.plus(indexOfMenu)]
        )
        #btnPlus.grid(row=0,column=0)
        labelPrice = tk.Label(frameArg,
            fg='black',
            bg='white',
            padx=10,
        )
        labelPrice.config(text="0")
        labelArray.append(labelPrice)
        #labelPrice.grid(row=0,column=1)
        btnMinus = tk.Button(frameArg,
            text="-",
            fg='black',
            bg='white',
            padx=5,
            command=lambda:[self.click(labelArray[indexOfMenu]), self.minus(indexOfMenu)]
        )
        #btnMinus.grid(row=0, column=2)

    def show(start):
        self.btnPrice.grid(row=0, column=start)
        self.labelPrice.grid(row=0, column=end)

    ################################################
    ################## FUNCTIONS ###################
    ################################################
    # 버튼을 클릭할 때마다, 해당 가격이
    # 총 가격인 [재현이의 출혈]에서 더해져야 한다. 
    def click(priceArg):
        global number 
        if number + priceArg >= 0:
            number += priceArg
        else:
            number = 0
        print(number)
        price.config(text=str(number))
    
    # + 버튼을 누르면. 
    def plus(indexOfMenu): 
        countMenu[indexOfMenu] += 1
        labelArray[indexOfMenu].config(text=countMenu[indexOfMenu])

    # - 버튼을 누르면. 
    def minus(indexOfMenu):
        if countMenu[indexOfMenu] > 0:
            countMenu[indexOfMenu] -= 1
        labelArray[indexOfMenu].config(text=countMenu[indexOfMenu])




##############################################
##############################################
##############################################

######## 메뉴, 첫번째 row. 
##### 메뉴에 대한 정보가 label로 표현된다.
##### 3개의 column 이 있다. 
###################################
##### 각 메뉴에 대한 정보와
##### + (개수, 가격이 증가) 버튼
##### - (개수, 가격이 감소) 버튼

# 메뉴 1번 줄의 frame은 grid로 하겠습니다. 
menuFrame1 = tk.Frame(root)
menuFrame1.pack()

##### 음식 레이블을 6개 정도만 만들어볼게.
# 음식 이름으로 해볼게. 이건 나중에 재현이가 바꾸면 돼.
# 음식 - 1. 한양식당 제육볶음 7000원, 2. 쪼매 떡볶이 3500원, 3. 무봉리 국밥 9000원, 
# 4. 맘스터치 싸이버거 6400원, 5. 몽키 파스타 7800원 6. 사나이뚝배기 우렁이 강된장 5700원

# padx = x축의 padding (좌우)
# pady = y축의 padding (상하)

# 첫번째 메뉴. 한양식당 제육볶음, 7000원
btnHanyang = tk.Label(menuFrame1, 
text='한양식당 제육볶음\n7000원',
fg='black',
bg='white',
width=15,
height=6
) # 참고로 mac OS 에서는 버튼의 배경색이 바뀌지 않는다...
# 하나의 프레임 내에서 Place/ Pack/ Grid를 동시에 사용할 수 없다. 
#btnHanyang.pack(side="left", anchor='center')
#btnHanyang.place(x=25, y=110)
btnHanyang.grid(row = 0, column = 0)

# 두번째 메뉴. 쪼매 떡볶이, 3500원.
btnJjomae = tk.Label(menuFrame1,
text='쪼매 떡볶이\n3500원',
fg='black',
bg='white',
width=15,
height=6
)
#btnJjomae.pack(side="right", anchor='center')
#btnJjomae.place(x=300, y=110)
btnJjomae.grid(row = 0, column = 1)

# 세번째 메뉴. 무봉리 국밥, 9000원.
btnMubongni = tk.Label(menuFrame1,
text='무봉리 국밥\n9000원',
fg='black',
bg='white',
width=15,
height=6
)
btnMubongni.grid(row = 0, column = 2)



###### +, - 버튼이 들어갈 frame. grid 입니다.
###### [+][메뉴의 개수][-]가 한쌍이고, 
###### 한 줄에 총 3개의 메뉴가 있으므로.
###### 이 frame 에는 9 개의 column이 있습니다.

## 클래스의 인자들:
## def __init__(self,indexOfMenu, plusFrameArg, labelFrameArg, minusFrameArg):
amountFrame1 = tk.Frame(root)
amountFrame1.pack()

btnOne = amountMenu(0, amountFrame1)
btnOne.show(0)

labelPrice.grid(row = 0, column = 1)

btnMinus1.grid(row=0, column=2)
#####################################################
#####################################################

#################################
# 메뉴 2번 줄의 frame은 grid로 하겠습니다. 
menuFrame2 = tk.Frame(root)
menuFrame2.pack()


# 네번째 메뉴. 맘스터치 싸이버거, 6400원.
btnMomstouch = tk.Label(menuFrame2,
text='맘스터치 싸이버거\n6400원',
fg='black',
bg='white',
width=15,
height=6
)
btnMomstouch.grid(row = 1, column = 0)

# 다섯번째 메뉴. 몽키 파스타, 7800원.
btnMonkeyPasta = tk.Label(menuFrame2,
text='몽키 파스타\n7800원',
fg='black',
bg='white',
width=15,
height=6
)
btnMonkeyPasta.grid(row = 1, column = 1)

# 여섯번째 메뉴. 사나이뚝배기 우렁이 강된장, 5700원.
btnSanai = tk.Label(menuFrame2,
text='사나이뚝배기 우렁이 강된장\n5700원',
fg='black',
bg='white',
width=15,
height=6
)
btnSanai.grid(row = 1, column = 2)



priceLabelFrame = tk.Frame(root)
priceLabelFrame.pack()





####################################
####################################
###### 가격의 총합이 나타나는 라벨을 입니다!! 
FONT = ('맑은 고딕', 20, 'roman')

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

#실행
root.mainloop()