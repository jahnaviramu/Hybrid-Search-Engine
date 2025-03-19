import streamlit as st
from hybrid_search_module import hybrid_search

st.title('Hybrid Search Engine with AI and MongoDB')
query = st.text_input('Enter your query:')

if st.button('Search'):
    if query:
        results = hybrid_search(query)
        for result in results:
            st.subheader(result['title'])
            st.write(f"**Content:** {result['content']}")
            st.write(f"**Score:** {result['score']}")
    else:
        st.write('Please enter a query to search.')

