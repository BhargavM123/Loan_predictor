import streamlit as st
import preprocessor
import pickle
import base64
import numpy as np

# @st.cache_data

st.sidebar.title("LOAN PREDICTOR")
st.title('LOAN PREDICTION :')

# app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

def get_fvalue(val):
    # feature_dict = {"No":1,"Yes":2}
    Sec_account = {"0": 0, "1": 1}
    for key,value in Sec_account.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

Sec_account = {"0":0, "1":1}


Age = st.sidebar.slider('Age', 1, 120, 0, )
Income = st.sidebar.slider('Income', 0, 250, 0, )
CCAvg = st.sidebar.slider('CCAvg', 0.0, 10.0, 0.0, 0.1)
Mortgage = st.sidebar.slider('Mortgage', 0, 500, 0, )
# Family = st.sidebar.radio('Family', options=['2', '3','4'])
Family = st.sidebar.text_input("Family '2', '3','4'")
# Education = st.sidebar.radio('Education', options=['1: Undergrad','2: Graduate','3: Advanced/Professional'])
Education = st.sidebar.text_input('1: Undergrad,2: Graduate,3: Advanced/Professional')
SecuritiesAccount = st.sidebar.radio('Securities Account', tuple(Sec_account.keys()))
CDAccount = st.sidebar.radio('CD Account', tuple(Sec_account.keys()))
Online_1 = st.sidebar.radio('Online', tuple(Sec_account.keys()))
CreditCard = st.sidebar.radio('Credit Card', tuple(Sec_account.keys()))
zipcode = st.sidebar.number_input("zipcode", min_value=10000, max_value=99999, step=1)


data = {
        'Age': Age,
        'Income': Income,
        'CCAvg': CCAvg,
        'Mortgage': Mortgage,
        'Family': Family,
        'Education': Education,
        'SecuritiesAccount_1': SecuritiesAccount,
        'CDAccount_1': CDAccount,
        'Online_1': Online_1,
        'CreditCard_1': CreditCard,
        'ZIPCode': zipcode
     }

if st.sidebar.button("Predict"):
    feature_list = preprocessor.preprocess(data)
    # print(feature_list)

    # st.dataframe(feature_list)

    # imp_features = preprocessor.pred(feature_list)

    single_sample = np.array(feature_list).reshape(1, -1)

    loaded_model = pickle.load(open('Desicion_tree.sav', 'rb'))
    prediction = loaded_model.predict(single_sample)

    file_ = open("money-rain.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    file = open("loan_denied.gif", "rb")
    contents = file.read()
    data_url_no = base64.b64encode(contents).decode("utf-8")
    file.close()


    if prediction[0] == 0:
        st.error('According to our Calculations, you will not get the loan from Bank')
        st.markdown(f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">', unsafe_allow_html=True, )
    elif prediction[0] == 1:
        st.success('Congratulations!! you will get the loan from Bank')
        st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">', unsafe_allow_html=True, )

