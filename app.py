import streamlit as st
import cv2
from ssd import run_ssd



def main():
    
    st.set_page_config(layout='wide', initial_sidebar_state='auto')

    st.title('Streamlit Object Detection')

    st.subheader('SSD , YOLO 를 활용한 Object Detection')

    menu = ['Home', 'SSD', 'YOLO']

    choice = st.sidebar.selectbox('MENU', menu)

    if choice == 'Home' :
        pass
    
    if choice == 'SSD' :
        
        run_ssd()

            















if __name__ == '__main__' :
    main()
