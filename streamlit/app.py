from qdrant_client import QdrantClient
from io import BytesIO
import streamlit as st
import base64
collection_name = "cat_embeddings"

# set up a state variable that will reuse through out the app
if 'selected_record' not in st.session_state:
    st.session_state['selected_record'] = None

def set_selected_record(record):
    """
    Set the selected record in the session state.

    Args:
        record (Any): The record to be set as the selected record.

    Returns:
        None
    """
    st.session_state['selected_record'] = record    

@st.cache_resource
def get_client():
    """
    Returns a QdrantClient instance with the specified URL and API key.

    This function is decorated with `@st.cache_resource`, which means that the client instance will be cached and reused
    for subsequent function calls.

    Returns:
        QdrantClient: A QdrantClient instance with the specified URL and API key.
    """
    return QdrantClient(url=st.secrets["QDRANT_URL"], api_key=st.secrets["QDRANT_API_KEY"])

def get_initial_records():
    """
    Retrieves the initial records from the Qdrant collection.

    Returns:
        list: A list of records retrieved from the Qdrant collection.
    """
    client = get_client()
    records, _ = client.scroll(collection_name=collection_name, with_vectors=False, limit=12)
    return records

def get_similar_records():
    """
    Retrieves similar records based on the provided embedding.

    Parameters:
        embedding: The embedding used to find similar records.

    Returns:
        The recommended similar records from the Qdrant collection.
    """
    client = get_client()
    if st.session_state['selected_record'] is not None:
        return client.recommend(
            collection_name=collection_name,
            positive = [st.session_state.selected_record.id],
            limit = 12
        )
    return records   
def get_bytes_from_base64(base64_string):
    """
    A function that converts a base64 string to bytes using utf-8 encoding.

    Parameters:
        base64_string (str): The base64 encoded string to be converted to bytes.

    Returns:
        BytesIO: A BytesIO object containing the bytes representation of the base64 string.
    """
    return BytesIO(base64.b64decode(base64_string)) 

# get selected records
records = get_initial_records() if st.session_state['selected_record'] is None else get_similar_records()
# render the selected image
if st.session_state['selected_record'] is not None:
    image_bytes = get_bytes_from_base64(st.session_state['selected_record'].payload['base64'])
    st.header("find similar cats")
    st.image(image=image_bytes)
    st.divider()
   
# set up grid to render the images    
column = st.columns(3)
# iterate through all the fetchedrecords and render the images using base64 string in the document's payload
for idx, record in enumerate(records):
    col_idx = idx % 3
    image_bytes = get_bytes_from_base64(record.payload['base64'])
    with column[col_idx]:
        st.image(image=image_bytes)
        st.button(label="find similar images", key=record.id, on_click=set_selected_record, args=[record])
   
    