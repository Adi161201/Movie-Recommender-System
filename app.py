# import streamlit as st 
# import pickle
# import pandas as pd
# import requests
# import io
# from PIL import Image
# import json
# # api_key=<<api_key>>&language=en-US

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=cf8c8bade8ed9dffab24cbe12cfe6a6e&language=en-US'.format(movie_id))
#     data = response.json()
#     if data['poster_path']==None: return 
#     return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# movies_list = pickle.load(open('movies.pkl','rb'))
# # movies= pd.DataFrame(movies_list)
# # movies_list = movies_list['title'].values

# similarity = pickle.load(open('similarity.pkl','rb'))

# def recommend(movie):
#     movie_ind = movies_list[movies_list['title']==movie].index[0]
#     dist = similarity[movie_ind]
#     movie_list = sorted(list(enumerate(dist)) , reverse=True , key=lambda x: x[1])[1:6]

#     recom_movies=[]
#     recom_posters=[]

#     for i in movie_list:
#         movie_id = i[0]
#         #fetch poster from API
#         recom_movies.append(movies_list.iloc[i[0]].title )
#         recom_posters.append(fetch_poster(movie_id))

#     return recom_movies, recom_posters



# st.title('Movie Recommendation System')
# selected_movie_name = st.selectbox(
#     'How would you like to be contacted?',
#     (movies_list['title'].values))

# # st.write('You selected:', selected_movie_name)

# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
    
#     # col1, col2, col3 , col4, col5 = st.columns(5, gap="medium")

#     # with col1:
#     #     st.subheader(names[0])
#     #     st.image(posters[0])

#     # with col2:
#     #     st.subheader(names[1])
#     #     st.image(posters[1])

#     # with col3:
#     #     st.subheader(names[2])
#     #     st.image(posters[2])

#     # with col4:
#     #     st.subheader(names[3])
#     #     st.image(posters[3])

#     # with col5:
#     #     st.subheader(names[4])
#     #     st.image(posters[4])

import pandas as pd
import streamlit as st
import pickle
import requests

# background-image: url("https://cdn.arstechnica.net/wp-content/uploads/2022/07/netflix.jpg");

page_bg_img = '''
<style>
.appview-container {
background: linear-gradient(rgb(0, 0, 0, 0.7), rgb(0, 0, 0, 0.7)) , url("https://www.lifesavvy.com/p/uploads/2020/03/20d96ddc.jpg");




background-size: cover;
}

# .block-container{
# background: linear-gradient(rgb(0, 0, 0, 0.5), rgb(0, 0, 0, 0.5));
# height: 100vh;
# }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=020b311fe0559698373a16008dc6a672&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def fetch_overview(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=020b311fe0559698373a16008dc6a672&language=en-US'.format(movie_id))
    data = response.json()
    return data['overview']

def fetch_date(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=020b311fe0559698373a16008dc6a672&language=en-US'.format(movie_id))
    data = response.json()
    return str(data['release_date'])


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_overview=[]
    recommended_movies_date=[]


    for x in movies_list:
        movie_id = movies.iloc[x[0]].id
        recommended_movies.append(movies.iloc[x[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_overview.append(fetch_overview(movie_id))
        recommended_movies_date.append(fetch_date(movie_id))

    return recommended_movies, recommended_movies_posters , recommended_movies_overview , recommended_movies_date


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


with st.container():

    st.title('Movie Recommender System')

    selected_movie_name = st.selectbox(
        'Please select movie',
        movies['title'].values , 
    )



    if st.button('Recommend'):
        
        names, posters ,overview ,date= recommend(selected_movie_name)
        tab1, tab2, tab3 ,tab4, tab5 = st.tabs([x for x in names])

        with tab1:
            with st.container():
                st.header(names[0])

            col1, col2= st.columns(2)

            with col1:
                # st.header(names[0])
                st.image(posters[0])
            
            with col2:
                st.subheader('Overview')
                st.write(overview[0])
                st.subheader('Release date :')
                st.write(date[0])

            # st.header(names[0])
            # st.image(posters[0], width=200)
            


        with tab2:
            with st.container():
                st.header(names[1])

            col1, col2= st.columns(2)

            with col1:
                
                # st.header(names[0])
                st.image(posters[1])
            
            with col2:
                st.subheader('Overview')
                st.write(overview[1])
                st.subheader('Release date :')
                st.write(date[1])
        
        with tab3:
            with st.container():
                st.header(names[2])

            col1, col2= st.columns(2)

            with col1:
                # st.header(names[0])
                st.image(posters[2])
            
            with col2:
                st.subheader('Overview')
                st.write(overview[2])
                st.subheader('Release date :')
                st.write(date[0])
        
        with tab4:
            with st.container():
                st.header(names[3])

            col1, col2= st.columns(2)

            with col1:
                # st.header(names[0])
                st.image(posters[3])
            
            with col2:
                st.subheader('Overview')
                st.write(overview[3])
                st.subheader('Release date :')
                st.write(date[0])

        with tab5:
            with st.container():
                st.header(names[4])

            col1, col2= st.columns(2)

            with col1:
                # st.header(names[0])
                st.image(posters[4])
            
            with col2:
                st.subheader('Overview')
                st.write(overview[4])
                st.subheader('Release date :')
                st.write(date[0])




