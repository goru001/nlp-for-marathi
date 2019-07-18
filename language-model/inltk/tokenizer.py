from fastai.text import *
import sentencepiece as spm

class MarathiTokenizer(BaseTokenizer):
    def __init__(self, lang:str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load("/home/gaurav/PycharmProjects/nlp-for-marathi/tokenizer/marathi_lm.model")
        
    def tokenizer(self, t:str) -> List[str]:
        return self.sp.EncodeAsPieces(t)
