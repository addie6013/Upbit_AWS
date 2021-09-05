import pyupbit

access = "VohKIx6945AIHPrOq02PdzHmRqfdrLlRI7isu9ht"          # 본인 값으로 변경
secret = "OLSxQGiv0uZKWlQwxvx0W1nq9BYcxxG3WdO6n0eI"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-MLK"))     # KRW-MLK 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회sa