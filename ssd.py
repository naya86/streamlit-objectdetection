import streamlit as st
import cv2
from PIL import Image
from ssd_model import ssd_img


def run_ssd() : 

    st.info('Image Object Detection 활용')
    
    sel_ssd = st.radio('Select', ['Image', 'Video'] )

    if sel_ssd == 'Image' :
        
        img = Image.open('data/images/image2.jpg')
        st.image(img)

        btn = st.button('Object Detection')

        if btn :

            ssd_img()
