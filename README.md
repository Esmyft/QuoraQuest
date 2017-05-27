# QuoraQuest

IN this problem, we try to match question pairs with the same intent to find _canonical_ questions for quora. 

## Data

We are given a dataset of about 400,000 question pairs and a final test set of similar size. Question pairs look like:

|id	|qid1	|qid2	|question1	|question2	|is_duplicate|
|---|---|---|---|---|---|
|5	|11	|12|	Astrology: I am a Capricorn Sun Cap moon and cap rising...what does that say about me?	|I'm a triple Capricorn (Sun, Moon and ascendant in Capricorn) What does this say about me?|1|
|6	|13	|14	|Should I buy tiago?	|What keeps childern active and far from phone and video games?	|0|
|7	|15	|16	|How can I be a good geologist?	|What should I do to be a great geologist? |1|
|8	|17	|18	|When do you use ã‚· instead of ã—?	|When do you use "&" instead of "and"? 	|0|


We are asked to minimize the log loss of a binary classification on the test set.
