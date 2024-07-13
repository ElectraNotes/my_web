import streamlit as st 
from PIL import Image

img = Image.open("logo.png")
st.image(img, width=80) 
st.title("Welcome to ElectraNotes")

st.sidebar.header("About")
st.sidebar.info("To learn Robotics in free fill following details:")
name = st.sidebar.text_input("name:")
age = st.sidebar.text_input("age:")
DOB = st.sidebar.date_input("D.O.B")
gender = st.sidebar.radio("Gender:", ('male','female','other'))
branch = st.sidebar.selectbox("Branch:",('ECE','EEE','CSE','ME','EE','CE','IT'))
college = st.sidebar.text_area("College name:")
lang = st.sidebar.multiselect("Programming languages you know",('Python','C','C++','java','html','css','R','java script'))
button = st.sidebar.button("Submit")
if button:
    st.sidebar.success("Submited successfully")
    # st.text(f'''You have entered:
    #             name: {name},
    #             age: {age},
    #             DOB: {DOB},
    #             Gender: {gender},
    #             branch: {branch},
    #             languages: {lang}
    #             ''')
    with open('web_data.txt','a') as f:
        f.write(f'''\nDetails:
                name: {name},
                age: {age},
                DOB: {DOB},
                Gender: {gender},
                branch: {branch},
                languages: {lang}
                ''')
    # print(f'''You have entered:
    #             name: {name},
    #             age: {age},
    #             DOB: {DOB},
    #             Gender: {gender},
    #             branch: {branch},
    #             languages: {lang}
    #             ''')
    
st.markdown("Introduction to Arduino & programming")
st.info("What is Arduino?")

st.write(""""Arduino is an open-source platform that is a combination of hardware and software. Arduino is easily 
accessible – even for those who don’t know much about electronics. Arduino boards are simple a type of 
microcontroller. They are able to read inputs from the sensors and turn those inputs into output. We 
can give some instructions to arduino and arduino performs operation according to given conditions or 
instructions.
        """)

img = Image.open("arduino.jpg")
st.image(img, width=350) 

st.info("What we can do using Arduino?")
st.write('''We can do so many things with arduino for example:\n
- We can fully automate our home with help of Arduino.\n
- We can build very interesting science or engineering projects.\n
- We can also use this in medical sector.\n
- We can make some interesting tools or projects for hacking with the help of arduino.\n
         ''')

st.info("Why do we need to use arduino?")
st.write('''
        For the following reasons we should use arduino:
        - It’s open source\n
        - It’s easy to program\n
        - It’s cheaper than other microcontroller\n
        - There are so many libraries available for arduino\n
        - We can build so many interesting projects using arduino for example: Robotic car, automatic
        light, Drones, fire fighting robots and radar.
         ''')

st.info("What is programming?")
st.write('''Programming is a way for us to deliver our instructions to arduino. In easy language, we can say 
programming is medium to tell arduino what to do? Now a question will can come in your mind why do 
we need of programming?\n
So the answer is arduino don’t know the language that we know (Hindi, English, etc). That’s why to 
communicate with the arduino or give instructions to arduino, we need to learn programming. Now the 
next question will come in your mind which programming language we need to learn for communicate 
with arduino
         ''')

st.info("What programming does Arduino use?")
st.write('''The arduino programming language is a modified version of C/C++. Usually, we program in C++ with the 
addition of methods and functions. A program written in arduino programming language called sketch 
and saved with .ino extension. You can even use Python to write an Arduino program. All these 
languages are text-based programming languages.
         ''')

st.sidebar.info("Link to buy my ebook  on arduino")
st.sidebar.markdown("https://imojo.in/electranotes_arduino")
