import streamlit as st
import cv2
from PIL import Image
from ssd_model import ssd_img

import pathlib
from input_image import input_image_seg




def run_seg() : 
   
   menu = ['About Semantic Segmentation', 'E-NET project']

   select = st.sidebar.selectbox('SELECT', menu)
   # input_image_seg()
   
   if select == 'About Semantic Segmentation' :
        pass

   elif select == 'E-NET project' :
    
      # EC2 문제로 없애기
      # sel_seg = st.radio('Select', ['Input Image','Video'] )

      
      # if sel_seg == 'Input Image' : 
      #    input_image_seg()
         
         
      # if sel_seg == 'Video' :

      st.subheader('출력되는 영상 실시간 Object Dection')
                  
         
      video_file = open('data/videos/output_seg.mp4', 'rb').read()
      # video_file = cv2.cvtColor(video_file, cv2.COLOR_BGR2RGB)
      st.video(video_file)

      st.write('(실시간 영상을 출력하려 했으나 , EC2 프리티어 문제로, LOCAL작업 후 올린 영상)')
      st.write('(LOCAL에서의 DETECTION 처리 영상)')
      
      re_video_file = open('data/videos/record_seg.mp4','rb').read()
      st.video(re_video_file)



