warn_invest_list = ["microsoft", "google", "naver", "kakao", "samsung", "lg"]
print(f"경고 종목 리스트 : {warn_invest_list}")
item = input("투자종목이 무엇입니까? : ")

if item.lower in warn_invest_list:
    print("투자 경고 종목입니다.")
else:
    print ("투자 경고 종목이 아닙니다.") 