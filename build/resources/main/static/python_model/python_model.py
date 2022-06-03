#!/usr/bin/env python
# coding: utf-8

# # 민원 모델 학습 설정

# In[4]:

import pandas as pd
df = pd.read_excel('/Users/yuganghyeon/IdeaProjects/boot/src/main/resources/static/fileupload/class_ex.xlsx')
df.to_csv("/Users/yuganghyeon/IdeaProjects/boot/src/main/resources/static/fileupload/class_ex.xlsx", index=False)

# In[5]:


import pandas as pd
# 훈련용 데이터 읽어오기
df = pd.read_csv('/Users/yuganghyeon/IdeaProjects/boot/src/main/resources/static/fileupload/class_ex.xlsx')


# In[6]:


# 카테고리 분류 데이터 읽어오기
df = df.loc[:, ["소분류", "민원제목"]]

# 카테고리 정수 인코딩
# 훈련용 데이터
category_list = pd.factorize(df['소분류'])[1]
df['소분류'] = pd.factorize(df['소분류'])[0]

# 정규표현식 사용
df['민원제목'] = df['민원제목'].str.replace("[^\w]", " ")


# In[7]:


#df["민원제목"]


# 뉴스 카테고리 데이터를 활용한다. (https://www.kaggle.com/rmisra/news-category-dataset)
# 
# lines=True로 주어 각 줄별로 데이터를 받아올 수 있도록 한다.
# 
# 우리는 headline을 기반으로 category를 분류하는 기능을 만들 것이기 때문에 그 둘만 받아온다.
# 
# 판다스의 factorize는 시리즈데이터를 받아 그를 기반으로 [[인덱싱데이터],[각 인덱싱의 의미]]를 반환한다. 신경망학습에 문자열데이터를 사용하기란 매우 어렵다. 따라서 인덱싱한 데이터를 사용하도록 한다. 각 인덱싱의 의미도 추후 확인을 위해 필요하므로 category_list에 따로 저장해놓는다.
# 
# headline에 구별이 어려운 문자(이모티콘 등)이 존재할 수 있으므로 문자열이 아닌 데이터(^\w)는 정규표현식을 활용해 공백으로 만든다.
# 
# 
# 참고 링크 : https://inuplace.tistory.com/577

# In[8]:


from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import numpy as np


# In[9]:


# split하면서 shuffle 적용
news_train, news_test, y_train, y_test = train_test_split(df['민원제목'], df['소분류'], test_size=0.2, shuffle=True, random_state=23)

# 원핫벡터로 만들어줍시다! (num_classes로 카테고리 수 명시 가능)
y_train = to_categorical(y_train,83)
y_test = to_categorical(y_test,83)


# train_test_split를 활용해 학습 데이터와 테스트 데이터로 분류한다.
# 
# category를 인덱싱하여 숫자화했지만, 아직 데이터로 활용하기엔 부적절하다. 신경망이 각 인덱싱에 의미를 부여하여 제대로된 학습을 수행하기란 어렵기 때문이다.
# 
# 따라서 이를 원핫벡터화한다. to_categorical() 메소드가 이를 간단하게 수행해준다. (인덱싱된 데이터를 모두 원핫벡터화)

# In[10]:


# 입력데이터(headline) 토큰화
# 토큰화 진행
stopwords = ['a', 'an']

X_train = []
for stc in news_train:
    token = []
    words = stc.split()
    for word in words:
        if word not in stopwords:
            token.append(word)
    X_train.append(token)

X_test = []
for stc in news_test:
    token = []
    words = stc.split()
    for word in words:
        if word not in stopwords:
            token.append(word)
    X_test.append(token)


# 입력데이터도 문자열 그대로인 상태여선 처리할 수 없다.
# 
# 결과데이터와 마찬가지로 인덱싱화를 해주어야하는데, 입력데이터인 headline은 문장이기 때문에 그대로 인덱싱화해선 안된다.
# 
# 따라서 각 데이터를 split하여 단어로 나누고, stopwords를 제거한다. (임의로 a와 an만 넣었지만 더 많은 stopword를 제대로 설정해주는 것이 좋다.)
# 

# In[11]:


# 입력데이터 인덱싱
from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(25000)
tokenizer.fit_on_texts(X_train)

X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)


# 빈도수별로 25000개의 단어를 인덱싱화한다. (데이터를 살펴보고 일정 빈도수 이상의 단어만 인덱싱되도록 적절한 숫자를 설정해준 것이다.)
# 
# X_train만 fit하여 이를 기준으로 학습 데이터와 테스트 데이터를 인덱싱화한다.

# In[12]:


from tensorflow.keras.preprocessing.sequence import pad_sequences

# 입력 데이터 패딩
max_len = 15
X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen=max_len)


# ## 여기까지 실행하고 모델을 불러와서 사용하면 된다!!

# headline은 모두 단어갯수가 달라 학습에 어려움이 있다.
# 
# 따라서 그를 맞춰준다. max_len보다 더 긴 문장은 잘려지고, 더 짧은 문장은 데이터를 0으로 채운다.

# # 학습된 민원 모델 사용하기

# In[13]:


# 0. 사용할 패키지 불러오기
from keras.utils import np_utils
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np
from numpy import argmax
import pandas as pa
import tensorflow as tf


# In[15]:


# 2. 모델 불러오기
from keras.models import load_model
model = load_model('/Users/yuganghyeon/IdeaProjects/boot/src/main/resources/static/python_model/category_model.h5')


# In[16]:


import pandas as pd
# 훈련용 데이터 읽어오기
df_test = pd.read_csv('/Users/yuganghyeon/IdeaProjects/boot/src/main/resources/static/fileupload/class_ex.xlsx',     names=['민원제목'])


# In[17]:


# 카테고리 분류 데이터 읽어오기
df_test_values = df_test.values
# 추출한 값의 타입을 리스트로 변경하기 위해 tolist()를 수행해준다.
df_test_list = df_test_values.tolist()
# 첫 번째 필요없는 데이터 삭제
df_test_list.pop(0)


# In[18]:


from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
import numpy as np
# split하면서 shuffle 적용
news_train, news_test = train_test_split(df_test['민원제목'], test_size=0.2, shuffle=True, random_state=23)


# In[19]:


# 입력데이터(headline) 토큰화
# 토큰화 진행
stopwords = ['a', 'an']

X_train = []
for stc in news_train:
    token = []
    words = stc.split()
    for word in words:
        if word not in stopwords:
            token.append(word)
    X_train.append(token)

X_test = []
for stc in news_test:
    token = []
    words = stc.split()
    for word in words:
        if word not in stopwords:
            token.append(word)
    X_test.append(token)


# In[20]:


# 입력데이터 인덱싱
from tensorflow.keras.preprocessing.text import Tokenizer

tokenizer = Tokenizer(25000)
tokenizer.fit_on_texts(X_train)

X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)


# In[21]:


from tensorflow.keras.preprocessing.sequence import pad_sequences

# 입력 데이터 패딩
max_len = 15
X_train = pad_sequences(X_train, maxlen=max_len)
X_test = pad_sequences(X_test, maxlen=max_len)


# In[22]:


category_result_list = []
category_acc_list = []
minwon_list = []
for i in df_test_list:
    # 결과 확인
    sentence = i[0]
    token_stc = sentence.split()
    encode_stc = tokenizer.texts_to_sequences([token_stc])
    pad_stc = pad_sequences(encode_stc, maxlen=15)

    score = model.predict(pad_stc)
    print(category_list[score.argmax()], score[0, score.argmax()])
    minwon_list.append(i[0])
    category_result_list.append(category_list[score.argmax()])
    category_acc_list.append(score[0, score.argmax()])


# In[23]:


# csv와 excel로 결과값 저장
import pandas as pd
from collections import OrderedDict

data_ordered_dict = OrderedDict(
    [
        ('민원제목', minwon_list),
        ('카테고리', category_result_list),
        ('모델 정확도', category_acc_list)
    ]
)

dataframe = pd.DataFrame.from_dict(data_ordered_dict)
#dataframe.to_csv("C:/Users/user/Desktop/categoy_classification.csv", index=False)
dataframe.to_excel("/Users/yuganghyeon/IdeaProjects/boot/src/main/resources/static/downfile/download_file.xlsx", index=False)

