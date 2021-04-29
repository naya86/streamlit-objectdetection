import streamlit as st
import cv2
from PIL import Image 
import imutils





def run_home() :
    st.subheader('SSD 와 YOLO를 이용한 Object Detection 과 E-NET 을 이용한 Semantic Segmentation에 대해 알아보려 한다.')
    st.write('자율주행과 관련이 있고 , 그것이 아니더라도 모든 분야에서 사물을 인식하는 기술은')
    st.write('접목되고 있어 중요한 기술로 자리 잡고 있다.')

    home_od_img = Image.open('data/images/object_detection2.PNG')
    home_od_img = home_od_img.resize((600,400))
    st.image(home_od_img)

    st.write('위는 Object Detection 모델의 발전과정을 나타내고 있고, 초기모델부터 현재까지 처리 속도 및 정확도를 향상하며')
    st.write('계속 발전되며 개발되고 있다.')

    st.write('이번 프로젝트는 모델의 이해와 이미지 및 영상 Detection , Segmentation을 직접 처리한다.')
    
    img = Image.open('data/images/home_image.png')
    img = img.resize((600,400))
    st.image(img)
    

    