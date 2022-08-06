# 10911 박종상 과학탐구 실험 (요리속 과학) 프로그래밍 코드
    
    
def science_in_cooking():
    answer = input('달고나 속에있는 과학들 (물리,화학,생물,지구,모두 중 선택)')

    physics = '달고나 속의 물리는'
    chemistry = '달고나 속의 화학은'
    earth = '달고나 속의 지구는'
    living_things = '달고나 속의 생명은'

    if answer == '물리':
        print(physics)

    elif answer == '화학':
        print(chemistry)

    elif answer == '생물':
        print(living_things)

    elif answer == '지구':
        print(earth)
    
    elif answer == '모두':
        print(physics)
        print(chemistry)
        print(living_things)
        print(earth)

#달고나 속의 과학들을 설명해 주는 함수

def How_To_Make_Dalgona():
    print('달고나를 만들기 위한 재료 리스트 (1회분 기준) ')
    print('설탕 3 티스푼 (약 3g')
    print('베이킹 소다 약 1/8 티스푼 (약 1g) ')
    print('달고나를 만들기 위한 기타 재료들(스크래퍼,국자, 모양틀, 누름판')
    answer = input('달고나 만드는 방법을 보시겠습니까? (y/n 으로 응답)')
    
    if answer == 'y':
        print('1. 국자에 설탕 3 티스푼을 넣고 투명해질때 까지 약불로 녹여줍니다')
        print('2. 설탕이 녹아서 투명해지면 불에 잠시 국자를 멀리두고 베이킹 소다를 1/8 티스푼 정도 넣어줍니다')
        print('3. 녹인 설탕을 잠시 불에서 때고 황토색으로 변할때까지 마구 섞어줍니다.')
        print('4. 불을 끄고 종이 호일, 쟁반등에 달고나를 쏟고 잠시 식혀준후 모양틀을 찍습니다')
        print('(단 모양틀을 찍을때 모양틀에 베이킹 소다나 밀가루를 발라줍니다)')
        print('레시피 출처: 만개의 레시피 https://www.10000recipe.com/recipe/6954737')

    else:
        print('프로그램을 종료합니다.')

#달고나를 만드는 방법을 알려주는 함수

def Dalgona(sugar_gram):
    baking_soda = (sugar_gram //3) #설탕과 소다의 비는 3:1 이다 즉 소다의 필요량은 설탕량/3이다 
    making_dalgona = (baking_soda + sugar_gram) // 4 #만들어 지는 달고나의 량은 설탕 + 베이킹 소다 // 4이다
    dalgona_cal = 14.4
    print('달고나를 만드는데 필요한 소다의 량은',baking_soda,'입니다')
    print('현재 만들수 있는 달고나의 량은',making_dalgona,'입니다')
    print('이 달고나 하나의 칼로리는',dalgona_cal,'입니다.')
    print('이 달고나를 전부 섭취했을 경우',(dalgona_cal * making_dalgona),'만큼의 칼로리를 얻습니다.')


    dalgona_count = int(input('이 달고나를 개당 얼마에 판매 하시겠습니까?'))
    dalgona_price = dalgona_count * making_dalgona 
    print('현재 판매 예정인 달고나는 ',dalgona_count,'개이며 달고나 1개당',dalgona_count,'의 가격으로 판매한다면',dalgona_price,'만큼의 수익을 얻을수 있습니다.')
    

#여기 까지는 달고나를 만드는대 필요한 소다의 량, 칼로리, 달고나 판매 시뮬레이터 프로그램


def Dalgona_kit():
    kit_sugar_price = int(input('달고나 키트에 사용될 설탕의 단가를 입력하세요(1회용분) '))
    kit_soda_price = int(input('달고나 키트에 사용될 소다의 단가를 입력하세요 (1회용분)'))
    kit_tool_price = int(input('달고나 키트에 사용되는 도구들의 가격을 입력하세요(단가)'))
    kit_price = int(input('이 달고나 키트를 1개당 얼마에 판매하시겠습니까?'))
        
    Real_kit_price = (kit_sugar_price + kit_soda_price + kit_tool_price)
        
    kit_count = int(input('이 달고나 키트를 몇개 판매하시겠습니까?'))
        
    dalgona_kit_proceeds = (kit_count * kit_price) - (Real_kit_price * kit_count)
        
    if dalgona_kit_proceeds >= 0:
        print('달고나 키트 판매를 통해 얻은 수익은 ',dalgona_kit_proceeds,'입니다. (흑자)')
            
    elif dalgona_kit_proceeds < 0:
        print('달고나 키트 판매를 통해 얻은 손익은',dalgona_kit_proceeds,'입니다. (적자)')
            
#여기까지는 달고나 키트의 재료비와 개당 가격을 설정하고 이로인해 얻을수 있는 수익과 이 수익을 얻으면 적자인지 흑자인지 알수 있게 해주는 프로그램

def dalgona_history():
    print('')


print('10911 박종상 과학 탐구 실험 요리속 과학')
print('조장: 박종상, 조원:박준원, 허원준, 화태원')
print('진로 박종상(프로그래머), 박준원(생명을 사랑하는 사람), 허원준(세계적인 CEO), 화태원(역사 선생님)')
print('다음 항목들중 사용할것을 입력하세요')

print('달고나 속의 과학  (A)' )
print('달고나 만드는 방법  (B)')
print('설탕의 량으로 얼마나 많은 달고나를 만들수 있을까? (C)')
print('달고나 키트 판매 시뮬레이터 (D)')
print('달고나의 재료인 설탕속 역사 이야기 (E)')
answer = input('사용할 프로그램은? (A, B , C, D, E 중 선택)')

if answer == 'A':
    science_in_cooking()
    
elif answer == 'B':
    How_To_Make_Dalgona()

elif answer == 'C':
    sugar_gram = int(input('사용할 설탕의 량은?'))
    Dalgona(sugar_gram)

elif answer == 'D':
    Dalgona_kit()

elif answer == 'E':
    dalgona_history()

else: 
    print('응답안 답이 A, B, C, D 중 존재하지 않습니다. ')

#사용자에게 값을 받아서 해당하는 값의 함수를 실행한다
