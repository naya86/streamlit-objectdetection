import streamlit as st
import cv2
from PIL import Image 





def run_home() :
    st.subheader('SSD 와 YOLO를 이용한 Object Detection 과 E-NET 을 이용한 Semantic Segmentation에 대해 알아보려 한다.')
    st.write('자율주행과 관련이 있고 , 그것이 아니더라도 모든 분야에서 사물을 인식하는 기술은')
    st.write('접목되고 있어 중요한 기술로 자리 잡고 있다.')

    st.write('이번 프로젝트는 각 모델의 이해와 이미지 및 영상 Detection , Segmentation이다.')
    
    img = Image.open('data/images/home_image.png')
    st.image(img,width=800)
    

    