import streamlit as st
import cv2
from PIL import Image
from ssd_model import ssd_img
import imutils
import pathlib
from input_image import input_image, input_image_yolo
from yolo_model import yolo_img



def run_yolo():
    
    st.info('YOLO Image Object Detection 활용')

    sel_yolo = st.radio('Select', ['Image', 'Input Image','Video'] )

    if sel_yolo == 'Image' :
        
        image_btn = st.selectbox('select image', ['image_1', 'image_2', 'image_3' ] )
        
        if image_btn == 'image_1' : 
            
            img = Image.open('data/images/image1.jpg')
            img = img.resize( ( 800,600 ) )
            st.image(img)

            btn = st.button('Object Detection')

            if btn :
                image_path = pathlib.Path('data\\images\\image1.jpg')
                st.subheader('Objecct Detection Image result')
                yolo_img(image_path)

        elif image_btn == 'image_2' :
            img = Image.open('data/images/image2.jpg')
            img = img.resize( ( 800,600 ) )
            st.image(img)

            btn = st.button('Object Detection')

            if btn :
                image_path = pathlib.Path('data\\images\\image2.jpg')
                st.subheader('Objecct Detection Image result')
                yolo_img(image_path)

        elif image_btn == 'image_3' :
            img = Image.open('data/images/image3.jpeg')
            img = img.resize( ( 800,600 ) )
            st.image(img)

            btn = st.button('Object Detection')

            if btn :
                image_path = pathlib.Path('data\\images\\image3.jpeg')
                st.subheader('Objecct Detection Image result')
                print(image_path)
                yolo_img(image_path)    

    if sel_yolo == 'Input Image' : 
        input_image_yolo()   

    
    if sel_yolo == 'Video' :

        st.subheader('출력되는 영상 실시간 Object Dection')

        video_btn = st.button('Play')
        
        if video_btn : 
           
            video_file = open('data/videos/output_yolo.mp4', 'rb').read()
            # video_file = cv2.cvtColor(video_file, cv2.COLOR_BGR2RGB)
            
            # video_file = imutils.resize(video_file, width=800, height=600  )
            st.video(video_file)

