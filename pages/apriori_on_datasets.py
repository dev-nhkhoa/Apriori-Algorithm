import streamlit as st

st.header("Sử dụng thuật toán Apriori vào các datasets có sẵn.")
st.subheader("Các bước chi tiết từ chuẩn hóa dữ liệu đến kết luận rút ra khi áp dụng thuật toán apriori trên các bộ dữ liệu có sẵn")

st.divider()

st.write("Bộ dữ liệu `Market Basket Dataset` từ `Kaggle`", )
st.page_link(label="Xem chi tiết tại đây", page="pages/market_basket_dataset.py", use_container_width=True)

st.divider()

st.write("Bộ dữ liệu `Country Level Purchase Dataset` từ `Kaggle`", )
st.page_link(label="Xem chi tiết tại đây", page="pages/country_level_purchase_dataset.py", use_container_width=True)

st.divider()

st.write("Bộ dữ liệu `Brazilian Ecommerce Dataset` từ `Kaggle`", )
st.page_link(label="Xem chi tiết tại đây", page="pages/brazilian_ecommerce_dataset.py", use_container_width=True)