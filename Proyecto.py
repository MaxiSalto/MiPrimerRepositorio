#Importing Libraries
import pandas as pd  
import numpy as np  
import streamlit as st  
import sqlite3  
#Generating Random Business Data
def generate_data():  
 np.random.seed(0)  
 data = pd.DataFrame({  
 'Date': pd.date_range(start='1/1/2020', periods=100),  
 'Revenue': np.random.randint(1000, 5000, size=100),  
 'Expenses': np.random.randint(500, 3000, size=100)  
 })  
 return data  
#Database Architecture
def create_database(data):  
 conn = sqlite3.connect('business_data.db')  
 data.to_sql('finance', conn, if_exists='replace', index=False)  
 conn.close()  
#Streamlit Dashboard
def create_dashboard(data):  
 st.title('Business Finance Dashboard')  
 st.line_chart(data.set_index('Date')[['Revenue', 'Expenses']])  
 st.write("### Revenue and Expenses over Time")  
 st.write(data)  
#Main Function
def main():  
 data = generate_data()  
 create_database(data)  
 create_dashboard(data)  
  
if __name__ == '__main__':  
 main()  