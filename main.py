import streamlit as st

if __name__ == '__main__':
  st.title('Web App sử dụng thuật toán luật kết hợp Apriori')
  st.subheader('Luật kết hợp là gì?')
  st.write('Khai phá luật kết hợp trong cơ sở dữ liệu (Association rule in data mining) là một kỹ thuật quan trọng trong lĩnh vực khai phá dữ liệu, mục tiêu nhằm phát hiện các mối quan hệ và quy luật giữa các mục dữ liệu trong cơ sở dữ liệu. Khai phá luận kết hợp giúp các nhà phân tích hiểu rõ hơn về cách các mục dữ liệu tương tác và liên kết với nhau.Khai phá Luật kết hợp bằng thuật toán Apriori - một ứng dụng quan trọng của Data Analytics. Nó sẽ giúp chúng ta tìm ra quy luật kết hợp giữa các sản phẩm trong dữ liệu, từ đó đưa ra kết luận “Nếu…thì…”, ví dụ: Nếu mua A thì sẽ mua B. [3] Mô hình đầu tiên của bài toán KPLKH là mô hình nhị phân (hay còn gọi là mô hình cơ bản) được R. Agrawal, T. Imielinski và A. Swami đề xuất vào năm 1993, xuất phát từ nhu cầu phân tích dữ liệu của cơ sở dữ liệu giao tác, phát hiện các mối quan hệ giữa các tập mục hàng hóa (Itemsets) đã bán được tại các siêu thị.Việc xác định các quan hệ này không phân biệt vai trò khác nhau cũng như không dựa vào các đặc tính dữ liệu vốn có của các mục dữ liệu mà chỉ dựa vào sự xuất hiện cùng lúc của chúng.')
  st.subheader('2.2.	Nguyên lý hoạt động và giải thuật Apriori')
  st.write('Apriori là một thuật toán do Rakesh Agrawal, Tomasz Imielinski, Arun Swami đề xuất lần đầu vào năm 1994 [1]. Bước đầu tiên để tạo các Luật kết hợp là xác định ngưỡng hỗ trợ (Min Support) và ngưỡng độ tin cậy (Min Confidence). [1] Do cơ sở dữ liệu có kích thước lớn và người dùng thường chỉ quan tâm tới một tập các phần tử nhất định, do vậy người ta đưa ra các ngưỡng giá trị cho độ hỗ trợ và độ tin cậy nhằm loại bỏ các luật không phù hợp với yêu cầu của người dùng hoặc các luật vô dụng. Công thức tính độ hỗ trợ và độ tin cậy của luật kết hợp X→Y ')
  st.write('`Support (X → Y) = P (X∪Y) = (n (X∪Y))/N`')
  st.write('`Confidence (X → Y) = P (X|Y)  = (n (X∪Y))/(n(X))`')

