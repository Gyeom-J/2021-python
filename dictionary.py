book_one={'제목':'안드로이드앱개발','저자':'최전산','출판사':'PCB','가격':25000,'출판연도':2017}
book_two={'제목':'파이썬','저자':'강수라','출판사':'연두','가격':22000,'출판연도':2019}
book_thr={'제목':'자바스크립트','저자':'박정식','출판사':'SSS','가격':23000,'출판연도':2018}
book_fou={'제목':'HTML5','저자':'주환','출판사':'대한','가격':27500,'출판연도':2012}
book_fiv={'제목':'컴파일러','저자':'장진웅','출판사':'PCB','가격':19500,'출판연도':2011}
book_six={'제목':'C언어','저자':'홍말숙','출판사':'한국','가격':22000,'출판연도':2010}
book_sev={'제목':'프로그래밍언어','저자':'현정숙','출판사':'연두','가격':15000,'출판연도':2019}
lis=[book_one,book_two,book_thr,book_fou,book_fiv,book_six,book_sev]
while True:
    sel=int(input("도서검색키워드\n1. 도서명\n2. 저자명\n3. 출판사명\n선택(1,2,3):"))
    if sel==1:
        count=0
        name=input("제목 >>> ")
        for i in range(0,7):
            for key,value in lis[i].items():
                if key=='제목' and value==name:
                    count+=1
                    print('\n')
                    for k, v in lis[i].items():
                        print(k, ":", v)
                    print('\n')
        if count==0 :
            print("\n")
            print("검색한 도서가 없습니다")
            print("\n")

    elif sel==2:
        count=0
        name=input("저자 >>> ")
        for i in range(0,7):
            for key,value in lis[i].items():
                if key=='저자' and value==name:
                    count+=1
                    print('\n')
                    for k, v in lis[i].items():
                        print(k, ":", v)
                    print('\n')
        if count==0 :
            print("\n")
            print("검색한 도서가 없습니다")
            print("\n")


    elif sel==3:
        count=0
        name=input("출판사 >>> ")
        for i in range(0,7):
            for key,value in lis[i].items():
                if key=='출판사' and value==name:
                    count+=1
                    print('\n')
                    for k, v in lis[i].items():
                        print(k, ":", v)
                    print('\n')
        if count==0 :
            print("\n")
            print("검색한 도서가 없습니다")
            print("\n")