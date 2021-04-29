import streamlit as st
import cv2
from PIL import Image
from ssd_model import ssd_img

import pathlib
from input_image import input_image
from home import run_home


def run_ssd() : 

    menu = ['About SSD', 'SSD project']

    select = st.sidebar.selectbox('SELECT', menu)
    
    # st.info('SSD Image Object Detection 활용')

    if select == 'About SSD' :
        st.subheader('Object Detection이란')
        st.write('Object Detection은 Classification의 확장된 개념으로 볼 수 있다.')
        st.write('Classifictation는 사전에 학습된 데이터를 기반으로 어떤 이미지가 데이터로 들어오면 그 이미지가 무엇을 나타내는지 확률적 분석을 통해서 이미지 분류를 해준다.')
        img = Image.open('data/images/cat1.PNG')
        st.image(img)
        st.write('위와 같이 Classification은 하나의 이미지를 하나의 객체로 분류해주는 반면, Object Detection은 Localization이라는 개념을 포함하여')
        st.write('다중 객체 분류를 가능하게 해준다. 이러한 기능을 하게 하는 모델 중 하나가 SSD이다.')
        od_img = Image.open('data/images/object_detection1.PNG')
        st.image(od_img)
        st.write('기존에는 물체를 감지하는 커널을 가지고 , Sliding window방식으로 Convolution하며 , 나온 결과를 히스토그램으로 그려가며 물체를 인식한다.')
        st.write('이때 원본스케일과 다른 여러개의 다른 스케일을 가진 이미지로 반복하며, 크고 작은 물체들을 인식하게 되는것이다.')
        st.write('처리속도가 느리고, 복잡하여 개발된것이 SSD이다.')
        st.subheader('SSD란 Single Shot Detector 의 약자로 , ')
        st.write('말 그대로 사진의 변형 없이 그 한 장으로 훈련, 검출을 하는 Detector를 의미한다. ')


    elif select == 'SSD project' :
    
        sel_ssd = st.radio('Select', ['Image', 'Input Image','Video'] )

        if sel_ssd == 'Image' :
            
            image_btn = st.selectbox('select image', ['image_1', 'image_2', 'image_3' ] )
            
            if image_btn == 'image_1' : 
                
                img = Image.open('data/images/image1.jpg')
                img = img.resize( ( 800,600 ) )
                st.image(img)

                btn = st.button('Object Detection')

                if btn :
                    image_path = pathlib.Path('data\\images\\image1.jpg')
                    st.subheader('Objecct Detection Image result')
                    ssd_img(image_path)

            elif image_btn == 'image_2' :
                img = Image.open('data/images/image2.jpg')
                img = img.resize( ( 800,600 ) )
                st.image(img)

                btn = st.button('Object Detection')

                if btn :
                    image_path = pathlib.Path('data\\images\\image2.jpg')
                    st.subheader('Objecct Detection Image result')
                    ssd_img(image_path)

            elif image_btn == 'image_3' :
                img = Image.open('data/images/image3.jpeg')
                img = img.resize( ( 800,600 ) )
                st.image(img)

                btn = st.button('Object Detection')

                if btn :
                    image_path = pathlib.Path('data\\images\\image3.jpeg')
                    st.subheader('Objecct Detection Image result')
                    print(image_path)
                    ssd_img(image_path)        


        if sel_ssd == 'Input Image' : 
            input_image()
            
        
        
        
        
        if sel_ssd == 'Video' :

            st.subheader('출력되는 영상 실시간 Object Dection')

            video_btn = st.button('Play')
            
            if video_btn : 
            
                video_file = open('data/videos/output_ssd.mp4', 'rb').read()
                # video_file = cv2.cvtColor(video_file, cv2.COLOR_BGR2RGB)
                st.video(video_file)
    


