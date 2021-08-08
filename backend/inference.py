from transformers import BertModel, BertTokenizer, BertConfig
import torch
from torch import nn

class SentimentClassifier(nn.Module):

    def __init__(self, freeze_bert = True):
        super(SentimentClassifier, self).__init__()

        # Instantiating the BERT model object
        self.bert_layer = BertModel(BertConfig())

        # Defining layers like dropout and linear
        self.dropout = nn.Dropout(0.1)
        self.classifier = nn.Linear(768, 1)

    def forward(self, seq, attn_masks):
        '''
        Inputs:
            -seq : Tensor of shape [B, T] containing token ids of sequences
            -attn_masks : Tensor of shape [B, T] containing attention masks to be used to avoid contibution of PAD tokens
        '''

        # Getting hidden states from BERT Layer
        hidden_states = self.bert_layer(seq, attention_mask = attn_masks).last_hidden_state

        # Obtaining the representation of [CLS] head
        cls_rep = hidden_states[:, 0]
        # print('CLS shape: ',cls_rep.shape)

        # Feeding cls_rep to the classifier layer
        logits = self.classifier(cls_rep)
        # print('Logits shape: ',logits.shape)

        return logits

class Predictor():

    def __init__(self, model):
        self.model = model
        self.maxlen = 64

    # Defining a preprocessing function
    def __preprocess(self, sentence):

        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

        # Tokenize the sentence
        tokens = tokenizer.tokenize(sentence)

        # Inserting the CLS and SEP token at the beginning and end of the sentence
        tokens = ['[CLS]'] + tokens + ['[SEP]']

        # Padding/truncating the sentences to the maximum length
        if len(tokens) < self.maxlen:
            tokens = tokens + ['[PAD]' for _ in range(self.maxlen - len(tokens))]
        else:
            tokens = tokens[:maxlen-1] + ['[SEP]']

        # Convert the sequence to ids with BERT Vocabulary
        tokens_ids = tokenizer.convert_tokens_to_ids(tokens)

        # Converting the list to a pytorch tensor
        tokens_ids_tensor = torch.tensor(tokens_ids).unsqueeze(0)

        # Obtaining the attention mask
        attn_mask = (tokens_ids_tensor != 0).long()

        return tokens_ids_tensor, attn_mask

    # Defining a prediction function for inference
    def predict(self, sentence):

        # preprocessing the sentence
        token_ids, attn_masks = self.__preprocess(sentence)

        device = 'cpu'
        # Setting model to evaluation mode
        self.model.eval()

        # Move inputs and targets to device
        token_ids, attn_masks = token_ids.to(device), attn_masks.to(device)

        # Get logit predictions
        p_logit = self.model(token_ids, attn_masks)

        probs = torch.sigmoid(p_logit.unsqueeze(-1))
        preds = (probs > 0.5).long().squeeze(0)


        return preds.item(), probs.item()
