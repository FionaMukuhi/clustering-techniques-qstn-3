import json
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import string

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Function to clean and lemmatize the text
def preprocess_text(text):
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize and lemmatize
    doc = nlp(text.lower())
    lemmatized = [token.lemma_ for token in doc if token.text not in STOP_WORDS and token.text.isalpha()]
    
    # Rejoin lemmatized text
    cleaned_text = ' '.join(lemmatized)
    
    return cleaned_text

# Load the image data
def load_image_data(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Preprocess descriptions
def preprocess_descriptions(image_data):
    for item in image_data:
        item['description'] = preprocess_text(item['description'])
    return image_data

if __name__ == '__main__':
    file_path = 'image_data.json'
    image_data = load_image_data(file_path)
    preprocessed_data = preprocess_descriptions(image_data)
    with open('preprocessed_image_data.json', 'w') as f:
        json.dump(preprocessed_data, f, indent=4)
    print('Preprocessed descriptions saved.')
