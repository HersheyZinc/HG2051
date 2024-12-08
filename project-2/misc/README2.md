[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/aCf9Buv8)
# HG2051 (AY24/25) Project 2: Group assignment

##   Introduction

This project constitutes 30% of your final grade for HG2051. Please work on the
final program in groups of 2-3 and report together.

- The goal of this assignment is to demonstrate your programming and
problem-solving abilities through teamwork. If your team has an idea for
another project that you would like to do instead, talk to me for approval.

- This project involves developing a part of speech tagger for a low-resource
language. As with the individual project, your team will be required to submit
data, output, and annotated code along with a short writeup that describes your
goals, process, and results. Your code will be assessed based on its functionality
and simplicity.

> Github supports code collaboration via pull requests and merging. To
facilitate this, you should designate one person from your team as the
administrator and let me know who that is. This person will be responsible for
approving merges/changes from each group member's individual branch to the master
branch.

## Project 2: Part of speech tagging

Part of speech tagging is a way to automatically identify the word class of a
particular lexical item in a string of text. A decent part of speech tagger can
help to facilitate other downstream tasks such as machine translation. The
initial project code in this repository will help you to get started, along
the following lines:

1. There are two text files located in the `datasets` subfolder, corresponding
to the two files you used for Project 1 (if you chose to work on the Pnar
language). The first text will be used to train your POS-tagger, and the
second will be used to validate it.

2. Parse the first text `text1-Pnar15_LathadlabotStory3.txt` into word-POS
tuples using the `mb` and `ps` lines, and use them to train a POS-tagger. The
example `project2.py` script gives an example of using the NLTK library to do
this (with a POS-tagged sample of text 1), but you may want to use a different
library. Test your POS-tagger on the second text (`text2-Pnar05_DaloiofRaliang_test.txt`)
to see how well it performs - this second text has been edited to include only
POS-tagged sentences. The metric you will use to determine this is `accuracy`
as implemented by the example script.

3. The provided script gives a baseline accuracy using modules in the NLTK
library. Your accuracy should improve once you add more data to train your
POS-tagging model. The goal of your project is to improve on the existing
baseline, by additionally including rules or features for your POS-tagger. To
explore potential rules/features, you may want to do some research on the Pnar
language itself, or find some other methods for developing POS-taggers (you can
use [NLTK Ch 5](https://www.nltk.org/book/ch05.html) as a jumping-off point).

4. In order to improve your POS-tagger further, consider whether to incorporate
additional data from more Pnar sources, such as those linked in Project 1. You
may also want to train multiple POS-taggers and use them in combination to see
if you can improve your score.

5. This code is simply a starting point for exploration. What other features can
you think of and implement to improve accuracy? Are there other lexical
resources/corpora or algorithms within NLTK or from other sources that can
improve your results? What is the best accuracy you can get? How relevant are
these POS tags to other languages, i.e. would it be good to try and convert
them to something like the [Universal Tag Set](https://universaldependencies.org/u/pos/)?

6. With your group, write a roughly 5-page paper (no longer than 10 pages)
describing your goals, data, process, and results, and discussing some of the
concerns identified in point 5. This paper should include relevant linguistic
information and citations for your sources. Submit the paper as a PDF along with
your annotated/commented Python code in a Github repository. The PDF should also
be submitted via TurnItIn.

## Output

Your final updated repository should include the following items:

1. A `README.md` file (replace this one) with a brief summary of the project
and a list of the items in the repository along with short descriptions. See [this](https://github.com/lingdoc/praatscripts) and [this](https://github.com/lingdoc/V1_AA_project_scripts/tree/main/Toolbox_scripts)
for examples. The `.md` extension means the `README` file makes use of ['markdown'](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
code, which is commonly used for formatting text on GitHub and elsewhere.

2. A single python script or a set of scripts/folders containing code to build
your classifier and assess its performance on the test dataset. I should be able
to run a single script and get a similar result to what you report in your paper
and in the `output.txt` file. Bonus points if you use folders/modules in
developing your process. This does not include the `datasets` folder, which
should contain all of the data used to develop your classifier. **Your main
script should contain all names of the group and matriculation numbers!**

3. An `output.txt` file that contains the accuracy results of 10 runs of your
final classifier being trained on the dataset(s) and evaluated on the test
dataset. Code to do this is found in the initial project script.

4. A PDF of your 5-10 page paper describing your goals, data, process, and results.

> We will have a leaderboard that tracks progress of the projects via your
`output.txt` file. I will update the leaderboard every week with your most
recent results, so feel free to commit/push your code/output changes regularly.
