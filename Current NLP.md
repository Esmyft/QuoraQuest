# Current State of Natural Language Processing

What are the state of the art methods being used in natural language processing?

## A brief history

Handwritten rules
Decision trees -> If-then rules
Statistical models using part-of-speech tagging
Unsupervised learning

## General Tasks

A. **Syntax**
  1. Morphological segmentation
      - Identify smallest unit with meaning.
      - Free- : Independent meaning
      - Bound- : Dependent meaning
  2. Part-of-speech
      - Noun, verb, etc.
  3. Parse
      - Syntactic meaning
  4. Sentence/Word Breaking
      - Punctuations
  
B. **Semantics**
  1. Lexical semantics
      - Hierachy and relation of morphemes.
  2. Named Entity Recognition (NER)
      - Proper nouns

#### Useful Areas to look at

* Sentiment analysis
* Disambiguation (of words)
* Topic Segmentation

*General Methods*:
* SVD
* K-means
* Method of moments

*Modeling Methods*:
* Latent Dirichlet Allocation
* Bag-of-words 
  * tf-idf
  * BM25 family

## Current Quora Model

Random Forest with handcrafted features:
* Cosine similarity of average word2vec embedding
* Common topic labels
* Part-of-speech tags
ML Techniques:
* Recurrent Neural Networks (RNNs)
    * Long Short Term Memory (LSTM)
* Attention-based approach
    * Compared pairs of words from the two questions

## Question Answering    

A. Question Analysis
  1. Question Classification
      - Classifying questions by question type, i.e. math question, opinion question, definiton question
      - Identify puns, constraints, definitions
  2. Relation Database
      - A database of curated relationships helps marginally
  3. Decomposition
      - Parsing questions into sub-questions
  4. 













