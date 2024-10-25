import streamlit as st
import pandas as pd
from lib.apriori import use_apriori, input_params
import plotly.express as px

market_basket = pd.read_csv('./dataset/kaggle/Market_Basket_Optimisation.csv', header=None)

st.title("Bộ dữ liệu Market Basket Optimization từ Kaggle:")

st.write("Cũng là một bộ dữ liệu được lấy từ kaggle. Bộ dữ liệu này đại diện cho nhiều giao dịch mua hàng của một siêu thị nào đó.")
st.link_button(label="Thông tin chi tiết của dataset bạn có thể xem tại đây", url="https://www.kaggle.com/datasets/devchauhan1/market-basket-optimisationcsv")

st.write("Bắt đầu với việc xem dữ liệu: Ta thực hiện các lệnh sau:")
st.code("market_basket = pd.read_csv('./dataset/kaggle/Market_Basket_Optimisation.csv', header=None)")
st.code("st.write(pd.DataFrame(market_basket))")
st.write(pd.DataFrame(market_basket))
st.info("Bạn có thể thấy, dữ liệu của chúng ta chưa giống với định dạnh format yêu cầu. Vì vậy chúng ta cần một vài dòng code để chỉnh sửa nó.")

st.write("")
st.code("market_basket = market_basket.stack().groupby(level=0).apply(', '.join).reset_index()")
st.code("market_basket = market_basket.drop(columns=['index'])")
st.code("market_basket = market_basket[0].str.split(', ', expand=True)")
st.code("market_basket = market_basket.apply(lambda x: x.dropna().tolist(), axis=1).tolist()")
market_basket = market_basket.stack().groupby(level=0).apply(', '.join).reset_index()
market_basket = market_basket.drop(columns=['index'])

st.write("Dữ liệu sau khi được chuẩn hóa:")
st.write(market_basket)

market_basket = market_basket[0].str.split(', ', expand=True)

market_basket = market_basket.apply(lambda x: x.dropna().tolist(), axis=1).tolist()

min_support, target, min_threshold = input_params()
st.info("Tiếp theo chúng ta có thể áp dụng thuật toán Ariori để tìm luật kết hợp.")
st.error("* Vì tránh bị crash App nên min_support đã được cố định. Bạn chỉ tùy chỉnh được target và min_threshold.")
st.info("*  Min_support phù hợp với dataset này là: 0.05 = 5%")

if st.button("Thực hiện thuật toán"):
    rules = use_apriori(market_basket, min_support=0.05, target=target, min_threshold=min_threshold)
    st.write('Các quy tắc kết hợp:', rules)

    if not rules.empty:
        rules['antecedents'] = rules['antecedents'].apply(lambda x: str(x))
        rules['consequents'] = rules['consequents'].apply(lambda x: str(x))
        
        fig = px.bar(rules, x='antecedents', y='support', color='confidence',
                     title='Hỗ trợ của các quy tắc kết hợp',
                     labels={'support': 'Hỗ trợ', 'antecedents': 'Quy tắc tiền đề'},
                     color_continuous_scale=px.colors.sequential.Viridis)

        st.plotly_chart(fig)
