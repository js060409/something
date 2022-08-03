sugar_gram = int(input('달고나를 만드는데 사용될 설탕의 량을 입력하세요. Dalgona(설탕의 그램 단위 량) 으로 입력한다'))
dalgona_cal = 14.4

def Dalgona(sugar_gram):
    baking_soda = (sugar_gram //3) #설탕과 소다의 비는 3:1 이다 즉 소다의 필요량은 설탕량/3이다 
    making_dalgona = (baking_soda + sugar_gram) // 4 #만들어 지는 달고나의 량은 설탕 + 베이킹 소다 // 4이다
    
    print('달고나를 만드는데 필요한 소다의 량은',baking_soda,'입니다')
    print('현재 만들수 있는 달고나의 량은',making_dalgona,'입니다')
    print('이 달고나 하나의 칼로리는',dalgona_cal,'입니다.')
    print('이 달고나를 전부 섭취했을 경우',(dalgona_cal * making_dalgona),'만큼의 칼로리를 얻습니다.')


    dalgona_count = int(input('이 달고나를 개당 얼마에 판매 하시겠습니까?'))
    dalgona_price = dalgona_count * making_dalgona 
    print('현재 판매 예정인 달고나는 ',dalgona_count,'개이며 달고나 1개당',dalgona_count,'의 가격으로 판매한다면',dalgona_price,'만큼의 수익을 얻을수 있습니다.')
    
input()
#여기 까지는 달고나를 만드는대 필요한 소다의 량, 칼로리, 달고나 판매 시뮬레이터 프로그램


    def Dalgona_kit():
        kit_sugar_price = int(input('달고나 키트에 사용될 설탕의 단가를 입력하세요(1회용분) '))
        kit_tool_price = int(input('달고나 키트에 사용되는 도구들의 가격을 입력하세요(단가)'))
        kit_price = int(input('이 달고나 키트를 1개당 얼마에 판매하시겠습니까?'))
        realkit_price = (kit_price - kit_sugar_price - kit_tool_price)
        kit_count = int(input('이 달고나 키트를 몇개 판매하시겠습니까?'))
        dalgona_kit_proceeds = (kit_count * kit_price) - (realkit_price * kit_count)
        
        if dalgona_kit_proceeds > realkit_price:
            print('달고나 키트 판매를 통해 얻은 수익은 ',dalgona_kit_proceeds,'입니다. (흑자)')
        elif dalgona_kit_proceeds <= realkit_price:
            print('달고나 키트 판매를 통해 얻은 수익은',dalgona_kit_proceeds,'입니다. (적자)')
            
#여기까지는 달고나 키트의 재료비와 개당 가격을 설정하고 이로인해 얻을수 있는 수익과 이 수익을 얻으면 적자인지 흑자인지 알수 있게 해주는 프로그램
