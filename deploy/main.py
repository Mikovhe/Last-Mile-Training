import streamlit as st


def main():
    """function that puts together the streamlit app"""

    page = st.sidebar.selectbox("Choose a page",["About app","Data Explorer","Machine Learning"])

    if page =="About app":
        st.title("The Last Mile Training Streamlit App")

        st.markdown(""" The purpose of this app is to showcase some streamlit usecases. We have a movie rating 
        system built and have to deploy it. Go Crazy!
        """)

    if page =="Data Explorer":
        st.title("build a mini data explorer here and show some EDA!")
if __name__== "__main__":
    main()