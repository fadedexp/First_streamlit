import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

st.write("# My First App")


st.write("## Second Header")

df = pd.read_csv("ds_salaries_clean.csv")
st.line_chart(df["Salary_USD"])
st.dataframe(df)

sbin = st.select_slider(
    'select bin number',
    options=list(range(1, 26))
)
st.write('Bins', sbin)


fig, ax = plt.subplots()
sns.histplot(df['Salary_USD'], ax=ax, bins=sbin)
st.pyplot(fig)




genre = st.radio(
    label="Tajriba darajasini tanlang",
    options=df['Experience'].unique().tolist(),
    index=None,
)

if st.button("Jadvalni ko'rsat"):
    st.write("You selected:", genre)
    st.dataframe(df[df['Experience']==genre])


with st.sidebar:
    
    st.line_chart(df["Salary_USD"])
    
    with st.echo():
        st.write("This code will be printed to the sidebar.")

    with st.spinner("Loading..."):
        time.sleep(5)
    st.success("Done!")

tab1, tab2, tab3 = st.tabs(["Mushuk", "Kuchuk", "Boyo'gli (Boyqush)"])

imageSize = st.select_slider(
    'select image size',
    options=list(range(1, 21))
)
st.write('Image size', )

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=imageSize*50)
   
    # st.line_chart(df["Salary_USD"])

with tab2:

   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=imageSize*50)

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=imageSize*50)
