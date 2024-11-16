import pandas as pd
import streamlit as st
from utils.products_list import sample_data_table

from lib.apriori import use_apriori, input_params

st.header("Thuật toán Apriori:")
st.subheader("Tìm luật kết hợp dễ dàng với bộ dữ liệu của bạn.")

st.title("Hướng dẫn sử dụng")

left, right = st.columns(2)

with left:
    st.info("1. Import bộ dữ liệu với định dạng file .csv lên trang web.")
    st.warning("Lưu ý: File dữ liệu phải chuẩn theo format mẫu:")
with right:
    st.write(pd.DataFrame(sample_data_table))

st.info("2. Chọn các chỉ số tùy chỉnh:")
st.error("* min_support: phải được căn chỉnh phù hợp để tránh tình trạng bị crash app.")
st.error("* target: chỉ số mục tiêu cần phải tìm.")
st.error("* min_threshold: ngưỡng tối thiểu.")


st.write("Chọn các thông số cho thuật toán Apriori:")
min_support, target, min_threshold = input_params(add_min_support=True)
uploaded_file = st.file_uploader("Chọn một file CSV...", type="csv")

# Nếu người dùng đã chọn file dữ liệu, hãy hiển thị số lượng dòng dữ liệu trong file.
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file, low_memory=False, on_bad_lines='skip', encoding='utf-8')
    st.write('Số lượng dòng dữ liệu trong file:', data.shape[0])
    st.write('Dữ liệu đã tải lên của bạn:', data)

    columns = data.columns
    columns = columns.insert(0, 'None')
    col_name = st.selectbox('Chọn cột dữ liệu:', columns)

    split_char = st.text_input('Nhập kí tự bạn đã dùng để phân tách các sản phẩm:', value=', ')


    if st.button("Thực hiện thuật toán:"):
        if col_name != 'None':
            data = data[col_name]
            # loại bỏ giá trị nan
            data = data.dropna()
            data = data.apply(lambda row: str(row).split(split_char))

        else :
            data = data.apply(lambda row: row.dropna().tolist())
        st.write('Dữ liệu sau khi xử lý:', data)
        rules = use_apriori(data, min_support, target, min_threshold)
        st.write('Các quy tắc kết hợp:', rules)



    