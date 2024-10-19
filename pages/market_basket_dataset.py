import streamlit as st
import pandas as pd
from lib.apriori import use_apriori, input_params

market_basket = pd.read_csv('./dataset/kaggle/Market_Basket_Optimisation.csv', header=None)

st.title("Bộ dữ liệu Market Basket Optimization từ Kaggle:")
market_basket = market_basket.stack().groupby(level=0).apply(', '.join).reset_index()
market_basket = market_basket.drop(columns=['index'])
st.write(market_basket)

market_basket = market_basket[0].str.split(', ', expand=True)

market_basket = market_basket.apply(lambda x: x.dropna().tolist(), axis=1).tolist()

min_support, target, min_threshold = input_params()

if st.button("Thực hiện thuật toán"):
    rules = use_apriori(market_basket, min_support=0.05, target=target, min_threshold=min_threshold)
    st.write('Các quy tắc kết hợp:', rules)