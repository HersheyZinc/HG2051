## Please enter your name and matric number as a comment below
## Name: Lim Zhe Xun
## Matric number: U2121481J
## For this project you will need to create a multilingual search tool that
## reads an interlinear corpus from raw text and allows you to search on
## multiple levels. Keep in mind that the raw text will first need to be
## processed and stored in some format before you can develop a search function.
## Below are ten steps using a simple example to get you started. There is an
## exit statement following the first step. Delete or comment out the exit
## statement and place it after each succeeding step to proceed and observe how
## the code progresses as you run it in your terminal.

from utils import *

'''MODIFY SEARCH TERMS BELOW'''

SOURCE_FILES = ["data/text1-Pnar15_LathadlabotStory3.txt","data/text2-Pnar05_DaloiofRaliang.txt"]

TEXT_QUERY = "" # Query to search in original text

GLOSS_QUERY = "bus" # Query to search in gloss
QUERY_POS = "" # POS corresponding to GLOSS_QUERY

PRECEDING_POS = "" # POS query to search immediately before GLOSS_QUERY
POST_POS = "" # POS query to search immediately after GLOSS_QUERY

OUTPUT_FILE_PATH = "output.txt"

''''MODIFY SEARCH TERMS ABOVE'''




if __name__ == "__main__":
    # Load data
    data = load_multi_data(SOURCE_FILES)

    # Perform text lookup
    r1 = search_text_data(data, TEXT_QUERY)

    # Perform gloss and POS lookup
    preceding_pos = [PRECEDING_POS] if PRECEDING_POS else []
    query_pos = [QUERY_POS] if QUERY_POS else []
    post_pos = [POST_POS] if POST_POS else []
    r2 = search_gloss_data(data, GLOSS_QUERY, preceding_pos, query_pos, post_pos)

    # Combine matching results
    results = combine_search_results([r1, r2])

    # Print results
    if len(results) == 0:
        print("Sorry, no matches found!")
    else:
        print(blocks_to_string(data, results, line=True))
        write_output(data, results, OUTPUT_FILE_PATH)

    