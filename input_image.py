import streamlit as st
import cv2
from PIL import Image
from ssd_model import ssd_img
import pathlib
import os

def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2.이제는 디렉토리가 있으니, 파일을 저장
    with open(os.path.join(directory, file.name), 'wb') as f:
        f.write(file.getbuffer())
    return st.success('Saved file : {} in {}'.format(file.name, directory))


def input_image() :
    
    image_file = st.file_uploader('Upload Image', type=['png', 'jpg', 'jpeg'], accept_multiple_files=True)

    if image_file is not None :
        
        # st.write( image_file.name )
                
        st.subheader('Image resized 800 X 600 (Original) ')

        image = Image.open(image_file)

        image = image.resize((800, 600) )

        st.image(image)

        save_file = save_uploaded_file('temp_files', image_file)

        print(save_file.name)


        # btn = st.button('Object Detection')

        # if btn :
            
        #     image_path = pathlib.Path('temp_file\\image3.jpeg')
        #     st.subheader('Objecct Detection Image result')
        #     ssd_img(image_path)         







        

