# NLP for Marathi

This repository contains State of the Art Tokenizer, Language model
 and Classifier for Marathi, which is spoken predominantly by
  Marathi people of Maharashtra, India.

## Dataset

* Download [Marathi Wikipedia Articles Dataset](https://drive.google.com/open?id=1YA49yoymRKKsJiSllCJIc7SV29BTVNe9) (85,537 articles) which I scraped, cleaned and
used to train the language model

* Download [Marathi News classification Dataset](https://drive.google.com/open?id=1sssR43ao9UV_lDBdHff01Wh6ASM2XVUX) which I scraped and used to train 
the classifier

## Results

#### Language Model

`on 30% validation set`

* Perplexity of language model: ~18

#### Classifier

* Accuracy of classification model: ~91%
* Kappa score of classification model: ~84

## Pretrained Language Model

Download pretrained Language Model from [here](https://drive.google.com/open?id=1b5gBQ-CmYoZGeOeOm7C_yT5jD3mW_rHr)


## Classifier

Download classifier from [here](https://drive.google.com/open?id=1F-3m1BVoBFdeYcJO2M9or6FBf-jUnGrP)


## Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1w_CtyeS0CfCsZgOcGQwx3q4B88PynKu0)