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
        pass

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
    


