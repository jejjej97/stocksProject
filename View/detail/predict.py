import datetime
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import numpy as np
import pandas as pd
import time
import pandas_datareader as pdr
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense, Activation

def stock_predict(key):
    begin = time.time()

    try:
        # 회사명으로 주식 종목 코드를 획득할 수 있도록 하는 함수
        def get_code(df, name):
            code = df.query("name=='{}'".format(name))['code'].to_string(index=False)

            # 위와같이 code명을 가져오면 앞에 공백이 붙어있는 상황이 발생하여 앞뒤로 sript() 하여 공백 제거
            code = code.strip()
            return code
        # excel 파일을 다운로드하는거와 동시에 pandas에 load하기
        # 흔히 사용하는 df라는 변수는 data frame을 의미합니다.
        code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download', header=0)[0]
        # data frame정리
        code_df = code_df[['회사명', '종목코드']]
        # data frame title 변경 '회사명' = name, 종목코드 = 'code'
        code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
        # 종목코드는 6자리로 구분되기때문에 0을 채워 6자리로 변경
        code_df.code = code_df.code.map('{:06d}'.format)
        # ex) 삼성전자의의 코드를 구해보겠습니다.
        code = get_code(code_df, key)
        # yahoo의 주식 데이터 종목은 코스피는 .KS, 코스닥은 .KQ가 붙습니다.
        # 삼성전자의 경우 코스피에 상장되어있기때문에 '종목코드.KS'로 처리하도록 한다.
        # get_data_yahoo API를 통해서 yahho finance의 주식 종목 데이터를 가져온다.
        print(code)
        try:
            code = code + '.KS'
            df = pdr.get_data_yahoo(code)
            df.reset_index(inplace=True)
        except:
            code = code[:6] + '.KQ'
            df = pdr.get_data_yahoo(code)
            df.reset_index(inplace=True)

        print('마지막리턴df마지막리턴df마지막리턴df마지막리턴df마지막리턴df마지막리턴df')
        print(df, len(df))

        # ------------------------------lstm 시작-------------------------------------
        # 출처: https://woochan-autobiography.tistory.com/871

        data = df
        print(data.head())

        high_prices = data['High'].values
        low_prices = data['Low'].values
        mid_prices = (high_prices + low_prices) / 2

        start_date = data['Date'][0]
        y = start_date.year
        m = start_date.month
        d = start_date.day

        # 최근 50일 간의 데이터 확인
        seq_len = 50  # window size
        sequence_length = seq_len + 1

        result = []
        for index in range(len(mid_prices) - sequence_length):
            result.append(mid_prices[index: index + sequence_length])

        normalized_data = []
        for window in result:
            normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
            normalized_data.append(normalized_window)

        result = np.array(normalized_data)

        # split train and test data
        row = int(round(result.shape[0] * 0.9))
        train = result[:row, :]
        np.random.shuffle(train)  # training set shuffle

        x_train = train[:, :-1]
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        y_train = train[:, -1]

        x_test = result[row:, :-1]  # 앞에 50개
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
        y_test = result[row:, -1]  # 뒤에 1개

        x_train.shape, x_test.shape

        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=(50, 1)))
        model.add(LSTM(64, return_sequences=False))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse', optimizer='rmsprop')
        model.summary()

        model.fit(x_train, y_train,
                  validation_data=(x_test, y_test),
                  batch_size=10,
                  epochs=100) # epochs 인공 신경망 갯수 높일수록 정확성 올라감

        pred = model.predict(x_test)

        # fig = plt.figure(facecolor='white')
        # ax = fig.add_subplot(111)
        # ax.plot(y_test, label='True')
        # ax.plot(pred, label='Prediction')
        # ax.legend()
        # plt.show()
        l_pred = []
        for i in pred:
            l_pred.append(np.float64(i[0]))
        y_test = y_test.tolist()
        print('y_test len', y_test)
        # print('pred', pred)
        print('l_pred len ', l_pred)
        last_list = []
        last_list.append(y_test)
        last_list.append(l_pred)
        last_list.append(y)
        last_list.append(m)
        last_list.append(d)
        print('last_listlast_listlast_listlast_listlast_listlast_list', last_list)

        runtime = time.time() - begin
        print(runtime)

        return last_list, runtime

    except:
        print('데이터 불충분')