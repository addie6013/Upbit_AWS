import pyupbit
import numpy as np

# OHLCV(open, high, low, close, volume)로 당일 시가, 고가, 저가, 종가, 거래량에 데이터

# KRW-BTC에 대해 7일간의 데이터 가져오기
df = pyupbit.get_ohlcv("KRW-BTC", count = 7)

# 변동폭 * k 계산, (고가 - 저가) * k 값
df['range'] = (df['high'] - df['low']) * 0.5 # range에 매수 타이밍 계산

# target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shift(1))
df['target'] = df['open'] + df['range'].shift(1) # 금일 시가의 range 더하기

# ror(수익율), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'],
                     1)

# 누적 곱 계산(cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Draw Down(하락폭) 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")