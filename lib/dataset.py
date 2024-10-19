import pandas as pd
import streamlit as st
from lib.apriori import use_apriori, input_params

class Dataset:
    def __init__(self, title, data):
        self.title = title
        self.data = data

    def display_data(self):
        if self.data is not None:
            st.write(self.data)
        else:
            st.write("Không có dữ liệu để hiển thị")

    def input_params(self):
        return input_params()
    
    def use_apriori(self, min_support, target, min_threshold):
        return use_apriori(self.data, min_support, target, min_threshold)