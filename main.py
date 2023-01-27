#streamlit run main.py

from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
from PIL import Image
import time
####---------------------------------------------------->
# CUSTOM TAGALOG DATA SETS
from textblob.classifiers import NaiveBayesClassifier

dataset = [
            ("Pogi", "positive"),
            ("ganda", "positive"),
            ("maganda", "positive"),
            ("Magaling", "positive"),
            ("Mabait", "positive"),
            ("Matino", "positive"),
            ("Nakabibighani", "positive"),
            ("Bayani", "positive"),
            ("Matalino", "positive"),
            ("Maniwala", "positive"),
            ("Pahimakas", "positive"),
            ("Tadhana", "positive"),
            ("Magkaugnay", "positive"),
            ("Marahuyo", "positive"),
            ("Mutya", "positive"),
            ("Tinatangi", "positive"),
            ("Dayang", "positive"),
            ######## NEGATIVE
            ("tanga", "negative"),
            ("bobo", "negative"),
            ("hindi marunong", "negative"),
            ("hindi nag tuturo", "negative"),
            ("sakit ", "negative"),
            ("nakaktakot", "negative"),
            ("uto uto", "negative"),
            ("hindi namamansin", "negative"),
            ("nagagalit", "negative"),
            ("panget", "negative"),
        ######## NEURAL
            ("ok", "neutral")
        ]

# Train a classifier on the dataset   
cl = NaiveBayesClassifier(dataset)



###---------------------------------------------------->
#SIDE BAR ------------------------------------------------------------->
st.sidebar.title("About")
#valueIamge 
wdt = 35
#Images
ccsict = Image.open("res\logo\ccsict.jpg")
isulogo = Image.open("res\logo\Isabela_State_University_Seal.png")

st.sidebar.write('A Thesis project Developed By BSCS 4 Students')
st.sidebar.image(isulogo,width=wdt,use_column_width="never")

st.sidebar.image(ccsict,width=wdt,use_column_width="never")
#SIDE BAR ------------------------------------------------------------->
#END

imageLogo = Image.open("res\logo\logo.png")

#Main Window
#text File and Expander 
col1 , col2 = st.columns([3,2])
with col1 :
    st.title('Sentimental Analysis')
with col2 :
    st.image(imageLogo,width=90)


text = st.text_area("Paste Your Text Here : ",height=300)

##my_bar = st.progress(0)
#for percent_complete in range(100):
#    time.sleep(0.1)
#    my_bar.progress(percent_complete + 1)
st.write("Ready to go ")

with st.expander("Text Status"):
    if text:
        blob = TextBlob(text)
        #Show Score
        st.write('Polarity: ' , round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ' , round(blob.sentiment.subjectivity,2)) 

       #st.write('Tagalog Score: ' , cl.accuracy(dataset))
        st.write(cl.classify(text))
        st.write( cl.accuracy(dataset))

        tag = cl.classify(text)

        PS = round(blob.sentiment.polarity,2)
        S = round(blob.sentiment.subjectivity,2)

        if PS <= 0:
            st.error('NEGATIVE')
        elif S >= 0:
            st.success("POSITIVE")
     
        else:
            st.code("Neural")

        st.code(cleantext.clean(text, clean_all=False, extra_spaces=True,
                                    stopwords=True,lowercase=True,numbers=True,punct=True))

    

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
    #