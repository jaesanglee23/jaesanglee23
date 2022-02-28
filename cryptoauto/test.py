import pyupbit

access = "LTfZox8aZICQw3fyBkfK5t2HVOjVj0AwY0ns76SP"          # 본인 값으로 변경
secret = "Hb0eEBsxTSo9splJz4ZnPkVNxxlgkH0M4sCWTbDq"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회