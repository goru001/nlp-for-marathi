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

#### Open Source Datasets
1. [iNLTK Headlines Corpus - Marathi](https://github.com/ai4bharat-indicnlp/indicnlp_corpus#publicly-available-classification-datasets) : Uses the Marathi News Dataset prepared above.

## Results

### Language Model Perplexity (on validation set)

| Architecture/Dataset | Marathi Wikipedia Articles |
|:--------:|:----:|
|   ULMFiT  |  18  |
|  TransformerXL |  17.42  |


### Classification Metrics

##### ULMFiT

| Dataset | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Marathi | 92.40 | 85.23 | [Link](https://github.com/goru001/nlp-for-marathi/blob/master/classification/Marathi_Classification_Model.ipynb) |
 
### Visualizations
 
##### Word Embeddings

| Architecture | Visualization |
|:--------:|:----:|
| ULMFiT | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-marathi/master/language-model/embedding_projector_config.json) |
| TransformerXL | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-marathi/master/language-model/embedding_projector_transformer_config.json)  |

##### Sentence Embeddings

| Architecture | Visualization |
|:--------:|:----:|
| ULMFiT | [Encodings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-marathi/master/language-model/sentence_encodings/encoding_projector_config.json) |


### Results of using Transfer Learning + Data Augmentation from iNLTK

##### On using complete training set (with Transfer learning)

| Dataset | Dataset size (train, valid, test) | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Marathi | (9672, 1210, 1210) | 92.40 | 85.23 | [Link](https://github.com/goru001/nlp-for-marathi/blob/master/classification/Marathi_Classification_Model.ipynb) |
 
##### On using 5% of training set (with Transfer learning)

| Dataset | Dataset size (train, valid, test) | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Marathi | (483, 1210, 1210) | 84.13 | 68.59 | [Link](https://github.com/goru001/nlp-for-marathi/blob/master/classification/Marathi_Classification_Model_without_aug.ipynb) |
 
##### On using 5% of training set (with Transfer learning + Data Augmentation)

| Dataset | Dataset size (train, valid, test) | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Marathi | (483, 1210, 1210) | 84.55 | 69.11 | [Link](https://github.com/goru001/nlp-for-marathi/blob/master/classification/Marathi_Classification_Model_with_aug.ipynb) |


## Pretrained Models

#### Language Models 
Download pretrained Language Model from [here](https://drive.google.com/open?id=1b5gBQ-CmYoZGeOeOm7C_yT5jD3mW_rHr)

#### Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1w_CtyeS0CfCsZgOcGQwx3q4B88PynKu0)