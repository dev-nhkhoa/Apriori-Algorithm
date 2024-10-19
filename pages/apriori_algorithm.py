import pandas as pd
import streamlit as st

from lib.apriori import use_apriori, input_params

st.write("Chọn các thông số cho thuật toán Apriori:")
min_support, target, min_threshold = input_params()
uploaded_file = st.file_uploader("Chọn một file CSV...", type="csv")

# Nếu người dùng đã chọn file dữ liệu, hãy hiển thị số lượng dòng dữ liệu trong file.
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write('Số lượng dòng dữ liệu trong file:', data.shape[0])
    st.write('Dữ liệu đã tải lên của bạn:', data)

    columns = data.columns
    columns = columns.insert(0, 'None')
    col_name = st.selectbox('Chọn cột dữ liệu:', columns)

    split_char = st.text_input('Nhập kí tự bạn đã dùng để phân tách các sản phẩm:', value=',')


    if st.button("Thực hiện thuật toán:"):
        if col_name != 'None':
            data = data[col_name]
            data = data.apply(lambda row: str(row).split(split_char))
        st.write('Dữ liệu sau khi xử lý:', data)

        rules = use_apriori(data, min_support, target, min_threshold)
        st.write('Các quy tắc kết hợp:', rules)



    