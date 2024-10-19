import pandas as pd
import streamlit as st
from utils.products_list import sample_data_table
from lib.apriori import use_apriori, input_params

file_path = './dataset/CountryLevelPurchasePattern.csv'

data = pd.read_csv(file_path)
data = pd.DataFrame(data)

st.title("Bộ dữ liệu Country Level Purchase")
st.subheader("Đây là bộ dữ liệu mua hàng từ nhiều quốc gia,...")

st.write("`Dữ liệu thô chưa xử lý:`", data)

st.write("Mô tả:")
left, right = st.columns(2)
with left: 
  st.write("`country (int):`")
  st.write("`clothing_model_page (str):`")
  st.write("`Total_Purchase (double):`")

with right:
  st.write("Chỉ số đại diện cho một quốc gia")
  st.write("Có thể hiểu là mã đơn hàng")
  st.write("Số lượng sản phẩm")
st.write("Mục tiêu:")
st.write("Chúng ta sẽ dựa vào các unique `clothing_model_page` để tìm xem các quốc gia đã mua hàng từ nó. Áp dụng thuật toán `Apriori` để tìm xem nếu quốc gia này mua hàng thì tỉ lệ quốc gia khác cũng mua hàng là bao nhiêu.")

st.write("Xử lý dữ liệu:")
st.write("Ta cần đưa dữ liệu về chuẩn dạng mẫu. Dữ liệu mẫu chuẩn:")
st.write("", pd.DataFrame(sample_data_table))

st.write("Ta nhận thấy chỉ cần lấy `country` và `clothing_model_page` để xử lý.")

st.write("Dữ liệu sau khi xử lý:")

data = data[['country', 'clothing_model_page']]

st.write("Ta cần gộp các `country` thành một chuỗi cho các `clothing_model_page` đã mua.")

data = data.groupby('clothing_model_page')['country'].unique()
data = pd.DataFrame(data)

data = data.reset_index()
data = data['country'].apply(lambda x: x.tolist())

st.write("Dữ liệu sau khi xử lý:")
st.write(data)

st.write("Áp dụng thuật toán Apriori để tìm ra các quy tắc kết hợp:")

if st.button("Kết quả thuật toán", key='apriori'):
  rules = use_apriori(data, min_support=0.8, target="lift", min_threshold=1)
  st.write(rules)







  

