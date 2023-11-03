def process_message(message):
  from transformers import AutoTokenizer, AutoModelForSequenceClassification
  from scipy.special import softmax
  import numpy as np
  roberta = "cardiffnlp/twitter-roberta-base-sentiment"
  model = AutoModelForSequenceClassification.from_pretrained(roberta)
  tokenizer = AutoTokenizer.from_pretrained(roberta)
  labels = ['Negative', 'Neutral', 'Positive']

  encoded_message = tokenizer(message, return_tensors='pt')
  output = model(**encoded_message)

  scores = output[0][0].detach().numpy()
  scores = softmax(scores)
  max_index = np.argmax(scores)
  print('this message is mostly', labels[max_index])
  return  labels[max_index]