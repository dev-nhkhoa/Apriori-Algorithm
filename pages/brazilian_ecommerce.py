import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules 

st.header("Brazilian E-commerce Dataset:")
st.subheader("Bộ dữ liệu từ sàn thương mại điện tử của Brazil.")

st.image("./assets/brazilian_ecommerce_structure.png", caption="Cấu trúc của bộ dữ liệu Brazilian E-commerce.")

st.divider()

st.subheader("Dữ liệu thô:")

st.write("Tất cả các file của bộ dữ liệu:")
st.code(""" 
# Đường dẫn tới thư mục chứa các file
file_path = "./dataset/kaggle/brazilian_ecommerce"

# Tạo biến cho các file với đường dẫn đầy đủ
olist_customers_dataset = f"{file_path}/olist_customers_dataset.csv"
olist_geolocation_dataset = f"{file_path}/olist_geolocation_dataset.csv"
olist_order_items_dataset = f"{file_path}/olist_order_items_dataset.csv"
olist_order_payments_dataset = f"{file_path}/olist_order_payments_dataset.csv"
olist_order_reviews_dataset = f"{file_path}/olist_order_reviews_dataset.csv"
olist_orders_dataset = f"{file_path}/olist_orders_dataset.csv"
olist_products_dataset = f"{file_path}/olist_products_dataset.csv"
olist_sellers_dataset = f"{file_path}/olist_sellers_dataset.csv"
product_category_name_translation = f"{file_path}/product_category_name_translation.csv"


# Đọc dữ liệu từ file olist_customers_dataset.csv
customers = pd.read_csv(olist_customers_dataset)
customers.head()
# Đọc dữ liệu từ file olist_order_items_dataset.csv
order_items = pd.read_csv(olist_order_items_dataset)
order_items.head()
# Đọc dữ liệu từ file olist_products_dataset.csv
products = pd.read_csv(olist_products_dataset)
products.head()
# Đọc dữ liệu từ file olist_order_reviews_dataset.csv
order_reviews = pd.read_csv(olist_order_reviews_dataset)
order_reviews.head()
# Đọc dữ liệu từ file olist_orders_dataset.csv
orders = pd.read_csv(olist_orders_dataset)
orders.head()
# Đọc dữ liệu từ file olist_order_payments_dataset.csv
order_payments = pd.read_csv(olist_order_payments_dataset)
order_payments.head()
# Đọc dữ liệu từ file olist_sellers_dataset.csv
sellers = pd.read_csv(olist_sellers_dataset)
sellers.head()
# Đọc dữ liệu từ file product_category_name_translation.csv
product_category_name_translation = pd.read_csv(product_category_name_translation)
product_category_name_translation
""")

file_path = "./dataset/kaggle/brazilian_ecommerce"

# Tạo biến cho các file với đường dẫn đầy đủ
olist_customers_dataset = f"{file_path}/olist_customers_dataset.csv"
olist_geolocation_dataset = f"{file_path}/olist_geolocation_dataset.csv"
olist_order_items_dataset = f"{file_path}/olist_order_items_dataset.csv"
olist_order_payments_dataset = f"{file_path}/olist_order_payments_dataset.csv"
olist_order_reviews_dataset = f"{file_path}/olist_order_reviews_dataset.csv"
olist_orders_dataset = f"{file_path}/olist_orders_dataset.csv"
olist_products_dataset = f"{file_path}/olist_products_dataset.csv"
olist_sellers_dataset = f"{file_path}/olist_sellers_dataset.csv"
product_category_name_translation = f"{file_path}/product_category_name_translation.csv"


# Đọc dữ liệu từ file olist_customers_dataset.csv
customers = pd.read_csv(olist_customers_dataset)
customers.head()
# Đọc dữ liệu từ file olist_order_items_dataset.csv
order_items = pd.read_csv(olist_order_items_dataset)
order_items.head()
# Đọc dữ liệu từ file olist_products_dataset.csv
products = pd.read_csv(olist_products_dataset)
products.head()
# Đọc dữ liệu từ file olist_order_reviews_dataset.csv
order_reviews = pd.read_csv(olist_order_reviews_dataset)
order_reviews.head()
# Đọc dữ liệu từ file olist_orders_dataset.csv
orders = pd.read_csv(olist_orders_dataset)
orders.head()
# Đọc dữ liệu từ file olist_order_payments_dataset.csv
order_payments = pd.read_csv(olist_order_payments_dataset)
order_payments.head()
# Đọc dữ liệu từ file olist_sellers_dataset.csv
sellers = pd.read_csv(olist_sellers_dataset)
sellers.head()
# Đọc dữ liệu từ file product_category_name_translation.csv
product_category_name_translation = pd.read_csv(product_category_name_translation)
st.write("Dữ liệu từ file product_category_name_translation.csv:")
st.write(product_category_name_translation)

st.divider()

st.subheader("Chuẩn hóa dữ liệu:")

st.write("""
# Bước 3: Chuẩn hóa dữ liệu:
#### Ta thấy được rằng có 3 file .csv chính liên quan đến các hóa đơn và mặt hàng. Cụ thể là:

- olist_order_items_dataset ( Danh sách hóa đơn )
- olist_products_dataset ( Danh sách các sản phẩm nhưng không có tên sản phẩm )
- product_category_name_translation ( Bản dịch phân loại từ tiếng Brazil sang Tiếng Anh)

#### * Vì không có tên sản phẩm trong database nên ta phải map danh mục sản phẩm theo id và chuyển đổi ngôn ngữ về Tiếng Anh.""")

st.code("""
# Dịch tên phân loại sản phẩm sang tiếng Anh
products = products.merge(product_category_name_translation, on='product_category_name', how="left")

products['product_category_name_english']
        """)

# Dịch tên phân loại sản phẩm sang tiếng Anh
products = products.merge(product_category_name_translation, on='product_category_name', how="left")

st.write(products['product_category_name_english'])

st.divider()

st.write("Từ product_id ta cần map chúng để ta có thể biết được tên phân loại của sản phẩm mục đích là dễ dàng trực quan hóa dữ liệu ở các bước sau.")

st.code("""
# Gộp dữ liệu từ các bảng order_items và products theo product_id để lấy thông tin về tên sản phẩm và danh mục sản phẩm 
order_items = order_items.merge(products[['product_id','product_category_name_english']], on='product_id', how='left')

order_items.head()""")

# Gộp dữ liệu từ các bảng order_items và products theo product_id để lấy thông tin về tên sản phẩm và danh mục sản phẩm 
order_items = order_items.merge(products[['product_id','product_category_name_english']], on='product_id', how='left')

st.write(order_items)

st.write("""
Loại bỏ dữ liệu không hợp lệ:
- Ta sẽ cần xóa các dòng dữ liệu mà chúng không có product_cagetory_name""")

st.code("""
# Loại bỏ các giá trị NaN từ cột product_category_name_english
order_items.dropna(inplace=True, subset=['product_category_name_english'])

len(order_items['product_id'].unique())""")

# Loại bỏ các giá trị NaN từ cột product_category_name_english
order_items.dropna(inplace=True, subset=['product_category_name_english'])

st.write(len(order_items['product_id'].unique()))

st.write("Đã hiểu được nguyên lý, chúng ta sẽ bắt đầu group tất cả các hóa đơn để biết các mặt hàng cụ thể hóa đơn đó đã mua.")

st.code("""# Tạo một dataframe mới với mỗi hàng là một đơn hàng và mỗi cột là một sản phẩm
transactions = order_items.groupby("order_id").product_category_name_english.unique()


transactions.value_counts()[:50].plot(kind='bar', figsize=(15,5))""")

# Tạo một dataframe mới với mỗi hàng là một đơn hàng và mỗi cột là một sản phẩm
transactions = order_items.groupby("order_id").product_category_name_english.unique()


st.write(transactions.value_counts()[:50].plot(kind='bar', figsize=(15,5)))

st.divider()

st.write("""# Bước 4: Luật kết hợp Apriori

## Chúng ta sẽ tiến hành áp dụng thuật toán để tìm ra quy luật và thói quen mua hàng từ khách hàng""")

st.code("""# Xây dựng một one-hot encoded DataFrame từ list của các giao dịch
from mlxtend.preprocessing import TransactionEncoder

# khởi tạo encoder
encoder = TransactionEncoder()

# fit encoder với dữ liệu
encoder.fit(transactions)

# transform dữ liệu
onehot = encoder.transform(transactions)

# Convert one-hot encoded data thành DataFrame
onehot = pd.DataFrame(onehot, columns = encoder.columns_)

onehot.head()""")

# Xây dựng một one-hot encoded DataFrame từ list của các giao dịch
from mlxtend.preprocessing import TransactionEncoder

# khởi tạo encoder
encoder = TransactionEncoder()

# fit encoder với dữ liệu
encoder.fit(transactions)

# transform dữ liệu
onehot = encoder.transform(transactions)

# Convert one-hot encoded data thành DataFrame
onehot = pd.DataFrame(onehot, columns = encoder.columns_)

st.write(onehot)

st.code("""# Áp dụng thuật toán Apriori để tìm các sản phẩm phổ biến ( support >= 0.00005 )
frequent_itemsets = apriori(onehot, min_support = 0.00005, use_colnames = True)

frequent_itemsets""")

# Áp dụng thuật toán Apriori để tìm các sản phẩm phổ biến ( support >= 0.00005 )
frequent_itemsets = apriori(onehot, min_support = 0.00005, use_colnames = True)

st.write(frequent_itemsets)

st.write("Mô tả: Tìm các sản phẩm với độ phổ biến trong tất cả các giao dịch ( số lần số hiện trong tất cả giao dịch) >= 0.005%")

st.code("""# Kết hợp các sản phẩm phổ biến thành các luật kết hợp với lift >= 1
rules = association_rules(frequent_itemsets, metric = 'lift', min_threshold = 1)

rules.head()""")

# Kết hợp các sản phẩm phổ biến thành các luật kết hợp với lift >= 1
rules = association_rules(frequent_itemsets, metric = 'lift', min_threshold = 1)

st.write(rules)

st.write("""Mô tả: lift (độ tăng) là một chỉ số quan trọng được sử dụng để đánh giá sức mạnh của mối quan hệ giữa hai mục. Lift cho biết mức độ tăng trưởng của xác suất xảy ra của một mục B khi mục A đã xảy ra, so với xác suất mà B xảy ra một cách độc lập.

Giả sử bạn có quy tắc "Nếu khách hàng mua bed_bath_table (A), họ có khả năng home_confort (B)". Nếu:

Support(A ∪ B) = 0.000442 (0.0442% giao dịch có cả bed_bath_table và home_confort)
Support(A) = 0.096827	 (9.6827% giao dịch có bed_bath_table)
Support(B) = 0.004082 (0.4082% giao dịch có home_confort)

Lift = 1.11 cho thấy rằng việc mua bed_bath_table có thể làm tăng khả năng mua home_confort lên gấp 1.11 lần so với khi không có bed_bath_table. Lift là một chỉ số hữu ích trong việc phân tích mối quan hệ giữa các sản phẩm trong tiếp thị và kinh doanh.""")


st.code("""# Kết hợp các sản phẩm phổ biến thành các luật kết hợp với confidence >= 0.95
rules = association_rules(frequent_itemsets, metric = 'confidence', min_threshold = 0.95)

# Print rules.
rules""")

rules = association_rules(frequent_itemsets, metric = 'confidence', min_threshold = 0.95)

# Print rules.
st.write(rules)

st.write("""confidence (độ tin cậy) là một chỉ số được sử dụng để đo lường độ mạnh mẽ của một quy tắc kết hợp (association rule). Độ tin cậy cho biết xác suất mà một mục (hoặc tập hợp các mục) sẽ xuất hiện trong một giao dịch, khi một mục khác đã được biết là xuất hiện.
- Nếu độ tin cậy cao (ví dụ > 0.7), điều này cho thấy rằng khi mục A xuất hiện, mục B cũng có khả năng xuất hiện cao.
- Độ tin cậy thấp có thể chỉ ra rằng không có mối quan hệ mạnh mẽ giữa A và B.

confidence = 1, điều này có nghĩa là mỗi khi sản phẩm A được mua, sản phẩm B cũng sẽ được mua. Nói cách khác, có 100% khả năng rằng sản phẩm B sẽ xuất hiện khi sản phẩm A đã được mua.""")