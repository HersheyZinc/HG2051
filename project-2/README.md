# HG2051 (AY24/25) Project 2: Group assignment

## Introduction
A core task in Natural Language Processing (NLP) is part of speech tagging, which refers to the task of identifying the word class of a particular lexical item in a sentence. Part of speech tagging serves as an important link between language and downstream tasks such as machine translation, named entity recognition, and information extraction. This project aims to develop an automatic part of speech tagger for the Pnar language, a low-resource language originating from India.

## Objectives
This project aims to achieve the following objectives:
1. Process and perform simple analysis on the Pnar dataset
2. Develop and evaluate part of speech taggers
3. Implement rules/features to improve on the baseline tagger

## Results
Overall, we achieved our best test accuracy of 0.948, using a custom bigram tagger built on ntlk's BigramTagger class.
![Accuracy of different taggers implemented](/misc/results.png)

## Repository Structure

- **Report.pdf** - PDF paper describing our goals, data, process, and results
- **utils.py** - A python file containing utility functions for loading and preprocessing data
- **project2.py** - Python code to implement and evaluate our best performing tagger
- **project2.ipynb** - Notebook containing implementations, results, and analysis of different taggers
- **datasets** - Directory containing the train and test data

## Instructions
To reproduce our results, follow the instructions below:
1. Install libraries\
```pip install -r requirements.txt```

2. To generate output.txt and reproduce the results of the final tagger:\
```python project2.py```

3. To view data analysis:\
```open project2.ipynb and run all cells```

