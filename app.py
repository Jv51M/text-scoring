import streamlit as st
import spacy
import regex
import nltk
from nltk.corpus import stopwords
try:
	nlp = spacy.load('en_core_web_sm')
except OSError:
    print("Downloading language model for spaCy...")
    from spacy.cli import download
    download('en_core_web_sm')
    nlp = spacy.load('en_core_web_sm')
    
Criterias = ['Language', 'Clarity & Rate', 'Content', 'Grammar', 'Speech', 'Structure', 'Engagement']

def ContentNstructure(data):
    text=data
    score=0
    #part 1: Salutation
    normal =['Hi', 'Hello']
    good = ['Good Morning', 'Good Afternoon', ' Good Evening', ' Good Day', ' Hello everyone']
    great = ['I am excited to introduce','Feeling great']
    if any(word in text for word in great):
        score += 5
    elif any(word in text for word in good):
        score += 4
    elif any(word in text for word in normal):
        score += 2
    else:
        score += 0
    salutation = normal+good+great
    #part2: Keywords
    musthaves= [['name','family'],
                ['age','years old'],
                ['school','class'],
                [
                    "hobby",
                    "interest",
                    "like to do",
                    "activity",
                    "favorite activity",
                    "pastime",
                    "thing I enjoy",
                    "free-time activity",
                    "fun activity",
                    "what I love doing",
                    "regular activity",
                    "personal interest",
                    "after-school interest",
                    "something I enjoy",
                    "thing I like"
                ]]
    goodtohave=[
    [
        "Family",
        "Parents",
        "Siblings",
        "Home",
        "Relatives",
        "Background"
    ],
    [
        "Hometown",
        "Birthplace",
        "Where I live",
        "Where I grew up",
        "Parents’ hometown",
        "Country",
        "State/City"
    ],
    [
        "Goal",
        "Dream",
        "Aim",
        "Future plan",
        "Career choice",
        "Life goal"
    ],
    [
        "Fun fact",
        "Special thing",
        "Unique point",
        "Hobby",
        "Hidden talent",
        "Cool thing"
    ],
    [
        "Strengths",
        "Skills",
        "Achievements",
        "Talents",
        "Awards",
        "Good qualities"
    ]
]
    for musts in musthaves:
        if any(i in text for i in musts): score += 4
    for goods in goodtohave:
        if any(j in text for j in goods): score += 2
    #part3: Flow
    sections={
        'salutation': salutation,
        'basic' :musthaves,
        'goodtohave': goodtohave,
        "closing": ["thank you", "thanks", "that's all"]
    }
    def get_sec(doc2,keywords):
        for token in doc2:
            if token.lower in keywords:
                return token.i
        return 0
    doc2 = nlp(text)
    pos={
        'salutation': get_sec(doc2,sections['salutation']),
        'basic': get_sec(doc2,sections['basic']),
        'goodtohave': get_sec(doc2,sections['goodtohave']),
        "closing":get_sec(doc2,sections['closing'])
    }
    positions = list(pos.values())
    if positions == sorted(positions):
        score+= 5
    return score

def Speechrate(data):
    text=nlp(data)
    toks = [token.text for token in text]
    total = len(toks)
    if total > 0.9:
        return 10
    elif 0.7 <= total <= 0.89:
        return 8
    elif 0.5 <= total <= 0.69:
        return 6
    elif 0.3 <= total <= 0.49:
        return 4
    else:
        return 2


def Scoring(data):
    stop_words = stopwords.words('english')
    stop_words = r'\b(?:%s)\b'%'|'.join(map(regex.escape,stop_words))
    data = regex.sub(stop_words, ' ', data)
    data = regex.sub('\s+', ' ', data)
    doc = nlp(data)
    cleaned = ' '.join([token.text for token in doc if not token.is_punct])

    score = 0
    score += ContentNstructure(cleaned)
    score += Speechrate(cleaned)
    return (score)
    #Clarity & Rate
    #Content
    #Grammar
    #Speech
    #Structure
    #Engagement

    #print(cleaned)




st.title("Text Scoring")

# File uploader (accept only .txt)
uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

# Initialize text input content
text_content = ""

if uploaded_file is not None:
    # Read the file as string
    text_content = uploaded_file.read().decode("utf-8")
    st.success("File loaded successfully!")

# Text area with uploaded file content (or empty if no upload)
user_input = st.text_area("Enter your text here:", value=text_content, height=200)

if st.button("Generate"):
    if user_input.strip() == "":
        st.warning("Please enter some text or upload a file.")
    else:
        st.success(f"You entered:\n\n{user_input}")
        with st.spinner('Generating score..'):
            Score=Scoring(user_input)
            st.success(f"Your score is: {Score}")
