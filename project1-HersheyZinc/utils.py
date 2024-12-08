TEXT = "tx"
MB = "mb"
PHONETICS = "ph"
GLOSS = "ge"
POS = "ps"
FREE_TRANSLATE = "ft"
TAGS = [TEXT, MB, PHONETICS, GLOSS, POS, FREE_TRANSLATE]


def load_data(file_path, tags=TAGS):
    '''
    Loads and preprocesses data from a file

    Returns: list - list of 'blocks', each block is a dictionary containing tx,mb,ph,ge,ps,ft keys
    '''

    # Open data file
    with open(file_path, encoding="utf-8") as f:
        # Read file as string and split into individual blocks
        blocks = f.read().split("\\ref")


    data = []

    # Iterate through each block and assign them an id
    for block in blocks:
        block_dict = {}

        # Find and append relevant translations to output data
        lines = block.split("\n")
        for line in lines:
            # Iterate through each tag
            for tag in tags:

                # Check if the line corresponds to the tag
                if not line.startswith(f"\\{tag}"):
                    continue

                # Preprocess text
                translation = line[4:].lower().strip("`").strip("'").strip(".")
                # Skip if translation is empty
                if translation == "empty":
                    continue
                
                # Add translation to dictionary
                if tag not in block_dict:
                    block_dict[tag] = " ".join(translation.split())
                else:
                    block_dict[tag] = block_dict[tag] + " " + " ".join(translation.split())
                
                
                

        # Append dictionary if all translations are present
        if len(block_dict) == len(tags):
            data.append(block_dict)

    return data


def load_multi_data(data_paths:list):
    '''
    Loads and combines multiple data files

    Returns: list - list of 'blocks', each block is a dictionary containing tx,mb,ph,ge,ps,ft keys
    '''
    data = []
    for data_path in data_paths:
        data += load_data(data_path)

    return data


def search_gloss_block(block, gloss_query_list, preceding_pos=[], gloss_pos=[], post_pos=[]):
    '''
    Checks if a block matches the input gloss and pos queries

    Returns: Boolean - True if block matches query, False if no match found
    '''
    
    # Split gloss and pos into lists
    gloss = block[GLOSS].split(" ")
    pos = block[POS].split(" ")

    candidates = []
    # Check if query is empty
    if gloss_query_list == []:
        # Check all gloss if empty
        candidates = list(range(len(gloss)))
    else:
        # Iterate through gloss by index
        for i in range(len(gloss)):
            # Perform window search to find matching queries
            gloss_window = gloss[i:i+len(gloss_query_list)]
            # pos_window = pos[i:i+len(gloss_query_list)]

            # Check if gloss matches
            if gloss_window == gloss_query_list:
                candidates.append(i)




    # return False if no candidates found
    if len(candidates) == 0:
        return False
    # return true if candidates found and user does not want to check pos
    elif len(preceding_pos+gloss_pos+post_pos) == 0:
        return True

    query_len = len(gloss_query_list)
    if query_len == 0:
        query_len = len(gloss_pos)

    # Iterate through each candidate index
    for idx in candidates:
        # Get the starting and ending indexes to match
        start_idx = idx - len(preceding_pos)
        end_idx = idx + query_len + len(post_pos)

        # Skip if indexes are out of range
        if start_idx < 0 or end_idx > len(pos):
            continue
        
        # Check if preceding and post pos are matching
        prec_match = (pos[start_idx : idx] == preceding_pos)
        query_match = (pos[idx : idx + query_len] == gloss_pos)
        post_match = (pos[idx + query_len : end_idx] == post_pos)
        # print(pos[idx : idx + query_len])
        if prec_match and query_match and post_match:
            return True
    
    return False


def search_gloss_data(data, gloss_query, preceding_pos=[], gloss_pos=[], post_pos=[]):
    '''
    Finds all blocks that have matching gloss and pos queries

    Returns: list of indexes that match the queries
    '''
    results = []
    # Preprocess query 
    gloss_query_list = gloss_query.lower().strip().split(" ")
    if gloss_query == "":
        gloss_query_list = []

    for idx, block in enumerate(data):
        if search_gloss_block(block, gloss_query_list, preceding_pos, gloss_pos, post_pos):
            results.append(idx)

    return results


def search_text_block(block, text_query, tag=TEXT):
    '''
    Checks if a block matches the input text query

    Returns: Boolean - True if block matches query, False if no match found
    '''
    text = block[tag]
    if text_query in text:
        return True
    else:
        return False


def search_text_data(data, text_query):
    '''
    Finds all blocks that have matching text queries

    Returns: list of indexes that match the queries
    '''
    results = []

    if text_query == "":
        return list(range(len(data)))

    text_query = text_query.lower().strip()

    for idx, block in enumerate(data):
        if search_text_block(block, text_query):
            results.append(idx)
    
    return results


def combine_search_results(results):
    '''
    Convenience function to find overlapping indexes from multiple results
    '''
    intersections = set.intersection(*[set(list) for list in results])
    return sorted(list(intersections))


def blocks_to_string(data, indexes, line=False):
    '''
    UI function to format block as a string
    '''
    s = ""
    for idx in indexes:
        block = data[idx]
        for tag in block.keys():
            if tag == FREE_TRANSLATE:
                s += f"\n{tag.ljust(3)}: {block[tag]}"
            else:
                txt = " ".join([word.ljust(11) for word in block[tag].split(" ")])
                s += f"\n{tag.ljust(3)}: {txt}"
        
        if line: s += "\n" + "---"*40 + "\n"

    return s


def get_pos_tags(data):
    '''
    UI function to retrieve all unique pos tags from the data
    '''
    # Get all unique POS tags in the data
    tags = []
    for block in data:
        tags += block[POS].split(" ")
    tags = sorted(list(set(tags)))
    return tags


def write_output(data, results,file_path="output.txt"):
    '''
    Utility function to write search results to a text file
    '''
    s = blocks_to_string(data, results, line=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(s)