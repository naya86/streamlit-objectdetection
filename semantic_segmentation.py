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
        
      st.subheader('Semantic Segmentation은')
      st.write('자율주행시스템의 첫번째는 객체인식, 객체 위치 파악 및 의미세분화를 기반으로 한다.')
      st.write('최근 지속해서 자동차 주변을 식별하도록 설계된 수많은 기술 시스템이 등장하였고, 우리 주변의 장면을 이해하는 것은')
      st.write('중요한 연구 영역으로 밝혀졌다. Semantic Segmentation은 이미지의 개별 픽셀에 레이블을 할당하는 효과적인 방법이고,')
      st.write('ADAS(Advanced Driving Assistance System)에서 활용, 운전자의 성능을 향상 시킬 수 있다.')
      st.write('(ADAS에서 활용의 레이블은 사람, 거리, 도로, 하늘, 나무, 자동차 등이 될 수 있다.)')
      
      seg_cap_img1 = Image.open('data/images/seg_capture1.PNG')
      seg_cap_img1= seg_cap_img1.resize((600,400))
      st.image(seg_cap_img1)

      st.write('Semantic Segmentation의 입력값은 컬러이미지 또는 흑백이미지고,')
      st.write('출력값은 각 픽셀의 예측된 클래스를 나태내는 segmentation map이고, 이 값을 얻는 것이 실질적 목표이다.')

      st.subheader('E-NET')
      st.write('E-NET은 기존 대비 18배 이상 빠르며 75배 보다 적은 FLOPS, 79배 적은 파라미터값으로')
      st.write('기존 모델에 비해 더 나은 정확도를 보인다.')
         
      seg_cap_img2 = Image.open('data/images/seg_capture2.PNG')
      seg_cap_img2 = seg_cap_img2.resize((600,400))
      st.image(seg_cap_img2)

      st.write('(E-NET Architecture)')
      st.write('E-NET의 아웃풋은 512 X 512를 가진다.')
   elif select == 'Play E-NET' :
    
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
      st.write('(LOCAL에서의  SEGMENTATION 처리 영상)')
      
      re_video_file = open('data/videos/record_seg.mp4','rb').read()
      st.video(re_video_file)



