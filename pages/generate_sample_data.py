import random
import pandas as pd
import utils.products_list as products_list
import streamlit as st

from utils.products_list import sample_data_table

from mlxtend.preprocessing import TransactionEncoder

# Tạo dữ liệu mẫu.

@st.cache_data
def convert_df(df):
  return df.to_csv(index=False).encode('utf-8')

def run(number_transctions):
  data = {
    'Items': []
  }

  for i in range(1, number_transctions + 1):
      # Random số lượng sản phẩm mua trong mỗi giao dịch.
    number_items = random.randint(1, 7)
    deviation = random.randint(0, 3)

    # Random các sản phẩm mua trong mỗi giao dịch.
    items = random.sample(products_list.products, number_items + deviation)

    # Chuyển list các sản phẩm thành một chuỗi.
    items = ', '.join(items)

    # Thêm giao dịch và các sản phẩm mua vào dữ liệu.
    data['Items'].append(items)

  data = pd.DataFrame(data)
  return data

data = pd.DataFrame(sample_data_table)
st.write('Dữ liệu mẫu:', data)

number_transactions = st.slider('Chọn số lượng giao dịch:', min_value=1000, max_value=1000000, value=1000, step=10000)

if st.button('Tạo dữ liệu mẫu'):
  try:
    data = run(number_transactions)
    st.write('Dữ liệu mẫu đã được tạo thành công.')
    csv = convert_df(data)
    # chart cho data hiển thị số lượng ở cột y và tên các sản phẩm ở cột x
    st.write('Dữ liệu vừa khởi tạo:', data)

    st.write('Dữ liệu sau khi đếm số lần mua của mỗi sản phẩm:')
    number_of_items = data['Items'].str.split(', ', expand=True).stack().value_counts().reset_index()

    number_of_items.columns = ['Items', 'Count']

    st.bar_chart(number_of_items.set_index('Items'), x_label='Sản phẩm', y_label='Số lần xuất hiện')

        # Đếm số sản phẩm trong mỗi giao dịch
    data['num_products'] = data['Items'].apply(lambda x: len(x.split(', ')))

    st.write('Dữ liệu sau khi đếm số lượng sản phẩm trong mỗi giao dịch:', data)

    # Đếm số giao dịch theo số lượng sản phẩm
    transaction_counts = data['num_products'].value_counts()

    # Vẽ biểu đồ
    st.bar_chart(transaction_counts, x_label='Số lượng sản phẩm', y_label='Số lượng giao dịch')

    st.download_button("Nhấn để tải xuống", csv, "sample_data.csv", "text/csv", key='download-csv')
  except:
      st.write("Có lỗi xảy ra!")









