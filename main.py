import streamlit as st


if __name__ == '__main__':
  pg = st.navigation([
    st.Page("./pages/introduce.py", title="Giới thiệu", default=True),
    st.Page("./pages/apriori_algorithm.py", title="Thuật toán Apriori"),
    st.Page("./pages/generate_sample_data.py", title="Tạo dữ liệu mẫu"),
    st.Page("./pages/apriori_on_datasets.py", title="Apriori trên các bộ dữ liệu"),
    st.Page("./pages/market_basket_dataset.py", title="Bộ dữ liệu market Basket Dataset"),
    st.Page("./pages/country_level_purchase_dataset.py", title="Country Level Purchase Dataset"),
    st.Page("./pages/brazilian_ecommerce.py", title="Brazilian E-commerce Dataset"),
    
])
pg.run()