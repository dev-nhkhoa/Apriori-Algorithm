import streamlit as st


if __name__ == '__main__':
  pg = st.navigation([
    st.Page("./pages/introduce.py", title="Giới thiệu", default=True),
    st.Page("./pages/apriori_algorithm.py", title="Thuật toán Apriori"),
    st.Page("./pages/generate_sample_data.py", title="Tạo dữ liệu mẫu"),
    st.Page("./pages/market_basket_dataset.py", title="Apriori trên các bộ dữ liệu"),
])
pg.run()