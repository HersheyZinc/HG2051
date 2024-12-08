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

    Returns: list - list of 'blocks', each block is a dictionary containing tx,mb,ph,ge,ps,ft keys. The keys to find are customizable with the 'tags' parameter
    '''

    # Open data file
    with open(file_path, encoding="utf-8") as f:
        # Read file as string and split into individual blocks
        blocks = f.read().split("\\tx")


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


def format_data(data):
    '''
    Function to format data for tagger
    '''
    output = []

    # Iterate through each line in the data
    for line in data:
        mb_str = line["mb"] # Get the mb string
        ps_str = line["ps"] # Get the POS string
        tags = [(mb, ps) for mb, ps in zip(mb_str.split(" "), ps_str.split(" "))] # Split both strings on spaces, and group them as tuples
        output.append(tags)

    return output