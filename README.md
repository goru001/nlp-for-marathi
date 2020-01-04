# NLP for Marathi

This repository contains State of the Art Language models
 and Classifier for Marathi, which is spoken predominantly by
  Marathi people of Maharashtra, India.
  
The models trained here have been used in [Natural Language Toolkit for Indic Languages
 (iNLTK)](https://github.com/goru001/inltk)
 

## Dataset

#### Created as part of this project
1. [Marathi Wikipedia Articles](https://www.kaggle.com/disisbig/marathi-wikipedia-articles)

2. [Marathi News Dataset](https://www.kaggle.com/disisbig/marathi-news-dataset)

## Results

#### Language Model Perplexity

| Architecture/Dataset | Marathi Wikipedia Articles |
|:--------:|:----:|
|   ULMFiT  |  18  |
|  TransformerXL |  17.42  |


#### Classification Metrics

##### ULMFiT

| Dataset | Accuracy | Kappa Score |
|:--------:|:----:|:----:|
| Marathi News Dataset |  93.55  |  87.50  |


#### Visualizations
 
##### Embedding Space

| Architecture | Visualization |
|:--------:|:----:|
| ULMFiT | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-marathi/master/language-model/embedding_projector_config.json) |
| TransformerXL | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-marathi/master/language-model/embedding_projector_transformer_config.json)  |

##### Sentence Encodings

| Architecture | Visualization |
|:--------:|:----:|
| ULMFiT | [Encodings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-marathi/master/language-model/sentence_encodings/encoding_projector_config.json) |


## Pretrained Language Model

Download pretrained Language Model from [here](https://drive.google.com/open?id=1b5gBQ-CmYoZGeOeOm7C_yT5jD3mW_rHr)


## Classifier

Download classifier from [here](https://drive.google.com/open?id=1F-3m1BVoBFdeYcJO2M9or6FBf-jUnGrP)


## Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1w_CtyeS0CfCsZgOcGQwx3q4B88PynKu0)