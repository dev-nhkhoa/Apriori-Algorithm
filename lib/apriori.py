import streamlit as st
import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

def input_params(add_min_support=False, add_target=True, add_min_threshold=True):
    left, mid, right = st.columns(3)

    min_support = 1
    target = "lift"
    min_threshold = 1

    with left:
      if add_min_support:
        min_support = float(st.text_input('Nhập giá trị ngưỡng hỗ trợ:', '1'))
        st.write('Ngưỡng hỗ trợ:', min_support)
    with mid:
      if add_target:
        min_threshold = float(st.text_input('Nhập giá trị ngưỡng min_threshold:', '1'))
        st.write('Ngưỡng min_threshold:', min_threshold)
    with right:
      if add_min_threshold:
        target = st.selectbox('Chọn mục tiêu:', ['confidence', 'lift', 'leverage', 'conviction'])
        st.write('Mục tiêu đã chọn:', target)

    return min_support, target, min_threshold

def use_apriori(transactions, min_support, target, min_threshold):
    
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    
    st.write('Tập hợp các mặt hàng phổ biến:', frequent_itemsets)

    rules = association_rules(frequent_itemsets, metric=target, min_threshold=min_threshold)

    return rules