import streamlit as st
import cv2
from PIL import Image
from ssd_model import ssd_img
import imutils
import pathlib
from input_image import input_image, input_image_yolo
from yolo_model import yolo_img



def run_yolo():
    menu = ['About YOLO', 'Play YOLO']
    select = st.sidebar.selectbox('SELECT', menu)
    
    # st.info('SSD Image Object Detection 활용')

    if select == 'About YOLO' :
        st.subheader('YOLO 란')
        st.write('''YOLO는 You Only Look Once의 약자로 Object detection 분야에서 많이 알려진 모델이다.
                    처음으로 one-stage-detection방법을 고안해 실시간으로 Object Detection이 가능하게 만들었다.''')
        ssd_cap_img1 = Image.open('data/images/ssd_capture1.PNG')
        ssd_cap_img1 = ssd_cap_img1.resize((600,400))
        st.image(ssd_cap_img1)

        st.write('YOLO는 기존의 Object Detection 모델과 비교 했을 때')  
        st.write('첫 번째로 간단한 처리 과정으로 속도가 매우 빠르며 기존의 실시간 Object Detection 모델들과 비교하면 2배 정도 높은 mAP를 보인다.') 
        st.write('두 번째는 이미지 전체를 한 번에 바라보는 방식을 이용하므로 class에 대한 맥락적 이해도가 다른 모델에 비해 높아 낮은 False-Positive를 보인다.') 
        st.write('세 번째로 일반화된 Object 학습이 가능하여 자연 이미지로 학습하고 이를 그림과 같은 곳에 테스트 해도 다른 모델에 비해 훨씬 높은 성능을 보여준다.') 
        st.write('하지만 다른 모델에 비해 낮은 정확도를 가지고 있다. 특히 작은 객체에 대해 정확도가 낮다.')
        
        yolo_cap_img1 = Image.open('data/images/yolo_capture1.PNG')
        yolo_cap_img1 = yolo_cap_img1.resize((600,400))
        st.image(yolo_cap_img1)
        st.write('(YOLO Structure)')

        yolo_cap_img2 = Image.open('data/images/yolo_capture2.PNG')
        yolo_cap_img2 = yolo_cap_img2.resize((600,400))
        st.image(yolo_cap_img2)

        st.write('YOLO 는 이미지를 S X S 의 그리드로 나눠 각각의 그리드에서 트레이닝 되어 있는 데이터를 기반으로 확률로 객체를 인식하고 , IOU를 이용하여 같은 객체임을 판단한다.')
        st.write('이때 여러개의 바운딩 박스가 생성되는데 , NMS 를 이용하여 하나만 남겨준다.')

        yolo_cap_img4 = Image.open('data/images/yolo_capture4.png')
        yolo_cap_img4 = yolo_cap_img4.resize((600,400))
        st.image(yolo_cap_img4)
        

        st.write('두개 이상의 객체가 겹쳐 있을때는 결과값의 벡터를 하나의 벡터로 처리(Anchor Boxes)하여 , 객체를 분류한다.')

        yolo_cap_img3 = Image.open('data/images/yolo_capture3.PNG')
        yolo_cap_img3 = yolo_cap_img3.resize((600,400))
        st.image(yolo_cap_img3)


        

    if select == 'Play YOLO' :
    
        sel_yolo = st.radio('Select', ['Image', 'Video'] )#'Input Image'뺌

        if sel_yolo == 'Image' :
            
            image_btn = st.selectbox('select image', ['image_1', 'image_2'] )
            
            if image_btn == 'image_1' : 
                
                img = Image.open('data/images/image1.jpg')
                img = img.resize( ( 800,600 ) )
                st.image(img)

                btn = st.button('Object Detection')

                if btn :
                    # EC2 문제로 결과 이미지만 가져오기로 함
                    # image_path = pathlib.Path('data\\images\\image1.jpg')
                    # st.subheader('Objecct Detection Image result')
                    # yolo_img(image_path)
                    img = Image.open('data/images/ch_yolo_image1.jpg')
                    img = img.resize( (800,600))
                    st.image(img)

            elif image_btn == 'image_2' :
                img = Image.open('data/images/image2.jpg')
                img = img.resize( ( 800,600 ) )
                st.image(img)

                btn = st.button('Object Detection')

                if btn :
                     # EC2 문제로 결과 이미지만 가져오기로 함
                    # image_path = pathlib.Path('data\\images\\image1.jpg')
                    # st.subheader('Objecct Detection Image result')
                    # yolo_img(image_path)
                    img = Image.open('data/images/ch_yolo_image2.jpg')
                    img = img.resize( (800,600))
                    st.image(img)
                    st.subheader('작은 물체는 인식이 잘 안되는 것을 볼 수 있다.')

            
        # EC2 문제로 없애기
        # if sel_yolo == 'Input Image' : 
        #     input_image_yolo()   

        
        if sel_yolo == 'Video' :

            st.subheader('Object Detection 처리 영상')
            st.info('AWS EC2의 프리티어 사용으로 실시간 처리가 힘들어 Local에서의 작업 후 결과 영상')

            video_file = open('data/videos/output_yolo.mp4', 'rb').read()
            # video_file = cv2.cvtColor(video_file, cv2.COLOR_BGR2RGB)
            
            # video_file = imutils.resize(video_file, width=800, height=600  )
            st.video(video_file)

            st.write('(Local에서의 Object Detection 처리 영상)')
            
            re_video_file = open('data/videos/record_yolo.mp4','rb').read()
            st.video(re_video_file)
