occur_mark = str(input('생성부호:'))
zero_num = len(occur_mark)  #4
zero_count = zero_num - 1

beta_send_data = str(input('전송 할 데이터:'))
send_data = beta_send_data + zero_count * "0"
cal_occur_mark = int(occur_mark)
cal_send_data = int(send_data)

# print(send_data)

#line 13 ~ 36 까지는 오류검출 부호 생성연산
idx = 0 
s1 = send_data[idx : idx + zero_num]
s2 = occur_mark

while idx < len(send_data) - zero_count:   
    if s1[0] != "0":
        l = [ord(a) ^ ord(b) for a,b in zip(s1,s2)]
        
    #print(s1)
    #print(l)
    l.pop(0)
    
    if idx+zero_num < len(send_data):
        l.append(int(send_data[idx+zero_num]))
        
    #print(l)
    #print("--------------------")
    strl = "".join(map(str, l))
    s1 = strl
    idx = idx +1
    
error_mark = s1
last_send_data = beta_send_data + s1


#line 39~59까지는 전송할 데이터 + 오류검출 부호를 생성 부호로 나누는 연산 (나머지 구하기)
idx = 0
s1 = last_send_data[idx : idx + zero_num]
s2 = occur_mark


while idx < len(last_send_data) - zero_count:
    if s1[0] != "0":
        l = [ord(a) ^ ord(b) for a,b in zip(s1,s2)]
        
    #print(s1)
    #print(l)
    l.pop(0)
    
    if idx+zero_num < len(last_send_data):
        l.append(int(last_send_data[idx+zero_num]))
        
    #print(l)
    #print("--------------------")
    strl = "".join(map(str, l))
    s1 = strl
    idx = idx +1

#print(s1)

#line 63 ~ 66까지는 오류 유무 확인    
if int(s1) != 0:
    print('오류가 있습니다.')
elif int(s1) == 0:
    print('데이터가 성공적으로 전송되었습니다.')
