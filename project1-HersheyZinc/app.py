import streamlit as st
from utils import *
st.set_page_config(layout="wide")

# data = load_multi_data(["data/text1-Pnar15_LathadlabotStory3.txt","data/text2-Pnar05_DaloiofRaliang.txt"])
data = load_multi_data(["data/full_text.txt"])

pos_tags = ["NA"] + get_pos_tags(data)

st.subheader("HG2051 Project 1 - Multilingual Search")

input_container1 = st.container(border=True)
with input_container1:
    text_query = st.text_input("Text query")


input_container2 = st.container(border=True)
with input_container2:
    gloss_query = st.text_input("Gloss query")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        pos1 = st.selectbox("preceding pos", pos_tags, key=0)
    with c2:
        pos2 = st.selectbox("preceding pos", pos_tags, key=1)
    with c3:
        pos3 = st.selectbox("gloss pos", pos_tags, key=2)
    with c4:
        pos4 = st.selectbox("post pos", pos_tags, key=4)
    with c5:
        pos5 = st.selectbox("post pos", pos_tags, key=5)




r1 = search_text_data(data, text_query)

preceding_pos = [i for i in [pos1,pos2] if i != "NA"]
query_pos = [i for i in [pos3] if i != "NA"]
post_pos = [i for i in [pos4,pos5] if i != "NA"]


r2 = search_gloss_data(data, gloss_query, preceding_pos, query_pos, post_pos)

results = combine_search_results([r1, r2])


st.subheader(f"{len(results)} matches found:")
display_container = st.container(border=True)
with display_container:
    for r in results:
        txt = st.text(blocks_to_string(data, [r]))
        st.divider()

# print(blocks_to_string(data, results))
write_output(data, results, "output.txt")