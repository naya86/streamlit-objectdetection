import streamlit as st
import cv2
from PIL import Image
from ssd_model import ssd_img
import pathlib
from input_image import input_image


def run_ssd() : 

    st.info('Image Object Detection 활용')
    
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
                ssd_img(image_path)        


    if sel_ssd == 'Input Image' : 
        input_image()

    
    
    
    
    # if sel_ssd == 'Video' :

    #     video_btn = st.selectbox('select video', ['video_1', 'video_2', 'video_3' ] )

    #     if video_btn == 'video_1' : 

    #         video_file = open('data/videos/video.mp4', 'rb').read()
    #         video_file = video.resize( ( 800,600 ) )
    #         st.video(video_file)


