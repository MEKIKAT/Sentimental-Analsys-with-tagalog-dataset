#streamlit run main.py

from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
from PIL import Image
import time
import altair as alt
import numpy as np
from datetime import datetime
####---------------------------------------------------->
# CUSTOM TAGALOG DATA SETS
from textblob.classifiers import NaiveBayesClassifier

dataset = [
            ("Pogi", "Positive"),
            ("ganda", "Positive"),
            ("maganda", "Positive"),
            ("Magaling", "Positive"),
            ("Mabait", "Positive"),
            ("Matino", "Positive"),
            ("Nakabibighani", "Positive"),
            ("Bayani", "Positive"),
            ("Matalino", "Positive"),
            ("Maniwala", "Positive"),
            ("Pahimakas", "Positive"),
            ("Tadhana", "Positive"),
            ("Magkaugnay", "Positive"),
            ("Marahuyo", "Positive"),
            ("Mutya", "Positive"),
            ("Tinatangi", "Positive"),
            ("Dayang", "Positive"),
            ######## NEGATIVE
            ("tanga", "Negative"),
            ("bobo", "Negative"),
            ("hindi marunong", "Negative"),
            ("hindi nag tuturo", "Negative"),
            ("sakit ", "Negative"),
            ("nakaktakot", "Negative"),
            ("uto uto", "Negative"),
            ("hindi namamansin", "Negative"),
            ("nagagalit", "Negative"),
            ("panget", "Negative"),
        ######## NEURAL
            ("ok", "neutral")
        ]

# Train a classifier on the dataset   
cl = NaiveBayesClassifier(dataset)


st.sidebar.title("About")



tab1, tab2= st.tabs(["Evaluate Teacher", "Reuslt"])
with tab1: 
    name = st.text_input("Your name:")

    course = st.selectbox(
        'What Department are you in',
        ('CCSICT', 'CBAPA', 'EDU','CRIM'),
        index=0
        )

    if course == 'CCSICT':
        CCSIT_Teachers = st.selectbox(
        'Teacher you will be evaluating',
        ('CCSIT_Name1', 'CCSIT_Name2', 'CCSIT_Name3','CCSIT_Name4')
    )
    

    if course == 'CBAPA':
        CBAPA_Teachers = st.selectbox(
        'Teacher you will be evaluating',
        ('CBAPA_Name1', 'CBAPA_Name2', 'CCBAPA_Name3','CBAPA_Name4'),
    )
    if course == 'EDU':
        EDU_Teachers = st.selectbox(
        'Teacher you will be evaluating',
        ('EDU_Name1', 'EDU_Name2', 'EDU_Name3','EDU_Name4'),
    )

    if course == 'CRIM':
        CRIM_Teachers = st.selectbox(
        'Teacher you will be evaluating',
        ('CRIM_Name1', 'CRIM_Name2', 'CRIM_Name3','CRIM_Name4'),
    )
    
    #--------Evaluation Form START ------->
    #
    st.title("Evaluation Form")

    choices =  ["Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"]

    question1 = st.radio(
        "The instructor was well prepared for the class.",choices,index=1,
    horizontal=True
    )
    question2 = st.radio(
        "The instructor showed an interest in helping students learn.",choices,index=1,
    horizontal=True
    )
    question3 = st.radio(
        "I received useful feedback on my performance on tests, papers, etc.",choices,index=1,
    horizontal=True
    )
    question4 = st.radio(
        "The lectures, tests, and assignments complemented each other.",choices,index=1,
    horizontal=True
    )
    question5 = st.radio(
        "The instructional materials (i.e., books, readings, handouts, study guides, lab manuals, multimedia, software) increased my knowledge and skills in the subject matter.",choices,index=1,
    horizontal=True
    )
    question6 = st.radio(
        "The course was organized in a manner that helped me understand the underlying concepts.",choices,index=1,
    horizontal=True
    )
    question7 = st.radio(
        "The course gave me the confidence to do more advanced work in the subject",choices,index=1,
    horizontal=True
    )
    #--------Evaluation Form  END ------->
    text = st.text_area("Comments and suggestions: ",height=300)
    blob = TextBlob(text)
    with st.expander("Text Status"):
        if text:
            #Show Score
            st.write('Polarity: ' , round(blob.sentiment.polarity,2))
            st.write('Subjectivity: ' , round(blob.sentiment.subjectivity,2)) 

        #st.write('Tagalog Score: ' , cl.accuracy(dataset))
            

        

    #Drop Down UPLOAD .CSV
    with st.expander("Analyze a CSV folder"):
        upl = st.file_uploader("Upload File")
        #Upload File 
        
        def score(x):
            blob1 = TextBlob(x)
            return blob1.sentiment.polarity
        
        def analyze(x):
            if x >= 0.5:
                return 'Positive'
            elif x <= 0.5:
                return 'Negative'
            else :
                return 'Neutral'
            
        if upl:
            df =  pd.read_excel(upl)
            del df['Unnamed: 0 ']
            df['score'] = df['tweets'].apply(score)
            df['analysis'] = df[score].apply(analyze)
            st.write(df.head(10))

with tab2:
    st.write("Result")
    col1_ ,col2_ = st.columns(2)
    with col1_ :
        if name:
            print(st.title(name))
        else:
            print(st.title("No Name Inserted"))
    
    with col2_ :
        print(st.title(course))
    
    now = datetime.now()

    current_time = now.strftime("%A : %d @:%I %M")
    st.write(current_time)

    with st.container():
    
       # ["Strongly Agree","Agree","Neutral","Disagree","Strongly Disagree"]#
        #print(st.write(question1))
        if question1 == 'Strongly Agree':
            points1 = 5
        elif question1 == "Agree":
            points1 = 4
        elif question1 == "Neutral":
            points1 = 3
        elif question1 == "Disagree":
            points1 = 2
        elif question1 == "Strongly Disagree":
            points1 = 1
        else:
            points1 = 0
        #print(st.write(question2))
        if question2 == 'Strongly Agree':
            points2 = 5
        elif question2 == "Agree":
            points2 = 4
        elif question2 == "Neutral":
            points2 = 3
        elif question2 == "Disagree":
            points2 = 2
        elif question2 == "Strongly Disagree":
            points2 = 1
        else:
            points1 = 0
        #print(st.write(question3))
        if question3 == 'Strongly Agree':
            points3 = 5
        elif question3 == "Agree":
            points3 = 4
        elif question3 == "Neutral":
            points3 = 3
        elif question3 == "Disagree":
            points3 = 2
        elif question3 == "Strongly Disagree":
            points3 = 1
        else:
            points1 = 0
        #print(st.write(question4))
        if question4 == 'Strongly Agree':
            points4 = 5
        elif question4 == "Agree":
            points4 = 4
        elif question4 == "Neutral":
            points4 = 3
        elif question4 == "Disagree":
            points4 = 2
        elif question4 == "Strongly Disagree":
            points4 = 1
        else:
            points1 = 0
        #print(st.write(question5))
        if question5 == 'Strongly Agree':
            points5 = 5
        elif question5 == "Agree":
            points5 = 4
        elif question5 == "Neutral":
            points5 = 3
        elif question5 == "Disagree":
            points5 = 2
        elif question5 == "Strongly Disagree":
            points5 = 1
        else:
            points5 = 0
        #print(st.write(question6))
        if question6 == 'Strongly Agree':
            points6 = 5
        elif question6 == "Agree":
            points6 = 4
        elif question6 == "Neutral":
            points6 = 3
        elif question6 == "Disagree":
            points6 = 2
        elif question6 == "Strongly Disagree":
            points6 = 1
        else:
            points6 = 0
        #print(st.write(question7))
        if question7 == 'Strongly Agree':
            points7 = 5
        elif question7 == "Agree":
            points7 = 4
        elif question7 == "Neutral":
            points7 = 3
        elif question7 == "Disagree":
            points7 = 2
        elif question7 == "Strongly Disagree":
            points7 = 1
        else:
            points7 = 0
        print(st.write('Polarity: ' , round(blob.sentiment.polarity,2)))
        print(st.write('Subjectivity: ' , round(blob.sentiment.subjectivity,2)) )

        #Tagalog
        #st.write(cl.classify(text))
        st.code( cl.accuracy(dataset))
        tag = cl.classify(text)

        PS = round(blob.sentiment.polarity,2)
        S = round(blob.sentiment.subjectivity,2)

        if PS <= 0:
            #st.error('NEGATIVE')
            st.write(cl.classify(text))
        elif S >= 0:
            #st.success("POSITIVE")
            st.write(cl.classify(text))
    
        else:   
            st.code("Neural")

        total = points1 + points2 + points3 + points4 + points5 + points6 + points7
        if CCSIT_Teachers :
            st.title(CCSIT_Teachers) 
        elif CBAPA_Teachers :
            st.title(CCSIT_Teachers)
        elif EDU_Teachers :
            st.title(CCSIT_Teachers) 
        elif CRIM_Teachers :
            st.title(CCSIT_Teachers) 
        else:
            st.title("Pick A Teacher")
        colscore1,colscore2  = st.columns(2)
        with colscore1:
            st.subheader("Points : ") 
        with colscore2:
            st.subheader(total)


