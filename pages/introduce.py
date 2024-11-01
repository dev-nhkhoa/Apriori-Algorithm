import streamlit as st
from streamlit_extras.grid import grid

st.header("Áp dụng thuật toán Apriori ( Luật kết hợp ) để dự đoán nhu cầu của khách hàng dựa trên lịch sử mua hàng.", anchor='1')

st.subheader("VLU - HK241 -Đồ án môn học phân tích dữ liệu.", anchor='2')

st.divider()

left, right = st.columns(2)

with left: 
  st.header("Nhóm thực hiện:", anchor='3')
  st.write("1. Trương Nguyễn Anh Khoa - 2274802010428")
  st.write("2. Lê Nguyễn Trúc My - 2274802010428")
  st.write("3. Nguyễn Huỳnh Thế Hiển - 2274802010428")
  st.write("4. Nguyễn Anh Vũ - 2274802010428")

with right:
  st.header("Giảng viên hướng dẫn:", anchor='4')
  st.subheader("Thầy Phan Hồ Viết Trường.")

st.divider()

st.header("Chương 1. Giới thiệu", anchor='5')
st.subheader("1.1.	Luật kết hợp là gì?", anchor='6')
my_grid = grid([0.6, 0.3], vertical_align='center')
my_grid.write("Apriori là một thuật toán do Rakesh Agrawal, Tomasz Imielinski, Arun Swami đề xuất lần đầu vào năm 1994. Khai phá luật kết hợp trong cơ sở dữ liệu (Association rule in data mining) là một kỹ thuật quan trọng trong lĩnh vực khai phá dữ liệu, mục tiêu nhằm phát hiện các mối quan hệ và quy luật giữa các mục dữ liệu trong cơ sở dữ liệu. Khai phá luận kết hợp giúp các nhà phân tích hiểu rõ hơn về cách các mục dữ liệu tương tác và liên kết với nhau.Khai phá Luật kết hợp bằng thuật toán Apriori - một ứng dụng quan trọng của Data Analytics.")
my_grid.image("./assets/apriori.png")
st.write(" Nó sẽ giúp chúng ta tìm ra quy luật kết hợp giữa các sản phẩm trong dữ liệu, từ đó đưa ra kết luận “Nếu…thì…”, ví dụ: Nếu mua A thì sẽ mua B. [3] Mô hình đầu tiên của bài toán KPLKH là mô hình nhị phân (hay còn gọi là mô hình cơ bản) được R. Agrawal, T. Imielinski và A. Swami đề xuất vào năm 1993, xuất phát từ nhu cầu phân tích dữ liệu của cơ sở dữ liệu giao tác, phát hiện các mối quan hệ giữa các tập mục hàng hóa (Itemsets) đã bán được tại các siêu thị.Việc xác định các quan hệ này không phân biệt vai trò khác nhau cũng như không dựa vào các đặc tính dữ liệu vốn có của các mục dữ liệu mà chỉ dựa vào sự xuất hiện cùng lúc của chúng.")

st.subheader('1.2.	Nguyên lý hoạt động và giải thuật Apriori:', anchor='7')
st.write('Bước đầu tiên để tạo các Luật kết hợp là xác định ngưỡng hỗ trợ (Min Support) và ngưỡng độ tin cậy (Min Confidence). [1] Do cơ sở dữ liệu có kích thước lớn và người dùng thường chỉ quan tâm tới một tập các phần tử nhất định, do vậy người ta đưa ra các ngưỡng giá trị cho độ hỗ trợ và độ tin cậy nhằm loại bỏ các luật không phù hợp với yêu cầu của người dùng hoặc các luật vô dụng. Công thức tính độ hỗ trợ và độ tin cậy của luật kết hợp X→Y ')
st.write('`Support (X → Y) = P (X∪Y) = (n (X∪Y))/N`')
st.write('`Confidence (X → Y) = P (X|Y)  = (n (X∪Y))/(n(X))`')
st.image("./assets/apriori-example.png")

st.divider()

st.header('Chương 2. Cấu trúc & Tính năng của hệ thống', anchor='8')
st.write("App được xây dựng dựa trên ngôn ngữ lập trình Python và sử dụng thư viện Streamlit để xây dựng giao diện người dùng. App bao gồm các chức năng chính sau:")
st.info("1.	Thực hiện thuật toán luật kết hợp lên các bộ dữ liệu có sẵn, các chỉ số người dùng có thể tùy chỉnh.")
st.info("2.	Thực hiện thuật toán do dữ liệu người dùng tự tải lên ( Yêu cầu phải đúng định dạng chuẩn của dữ liệu ).")
st.info("3.	Hiển thị kết quả thuật toán Apriori dưới dạng bảng và biểu đồ.")
st.info("4.	Tạo ra dữ liệu giả ( fake data ) về các giao dịch mua hàng để thực hiện thuật toán Apriori. `( Chưa hoàn thiện )`")
st.divider()

st.write("Nhược điểm của App:")
st.warning("1. Tùy thuộc vào ngưỡng `min_support` có thể App sẽ bị crash nếu ngưỡng này trả ra quá nhiều `frequent_itemsets`.")

st.divider()

st.header("Chương 3. Cấu trúc Web App", anchor='9')

st.write("Web App có những trang chính có các chức năng sau:")

st.write("`Trang chủ`: Giới thiệu về dự án, sơ lược về luật kết hợp và các nội dung lý thuyết khác.")
st.write("`Tạo dữ liệu giả`: Tạo ra dữ liệu giả về các giao dịch mua hàng để người dùng thử nghiệm thuật toán Apriori.")
st.write("`Sử dụng thuật toán`: Thực hiện thuật toán Apriori trên dữ liệu người dùng tự tải lên hoặc dữ liệu mẫu.")
st.write("Các bộ dữ liệu: Thực hiện và trình bày cụ thể các chuẩn hóa và áp dụng thuật toán Apriori.")
st.write("`Brazilian-Ecommerce`: Bộ dữ liệu về các giao dịch thương mại điện tử từ brazil.")
st.write("`Market-basket-dataset`: Bộ dữ liệu về các giao dịch mua hàng ở một siêu thị.")
st.write("`Country-level-purchase`: Bộ dữ liệu về các giao dịch mua hàng ở các quốc gia.")

st.divider()

left,right = st.columns(2)

with left:
  st.page_link(label="Tạo dữ liệu giả", page="pages/generate_sample_data.py", use_container_width=True)

with right:
  st.page_link(label="Sử dụng thuật toán", page="pages/apriori_algorithm.py", use_container_width=True)