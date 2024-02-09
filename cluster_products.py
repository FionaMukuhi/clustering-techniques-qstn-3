import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Load preprocessed descriptions and URLs
def load_preprocessed_data(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    descriptions = [item['description'] for item in data]
    urls = [item['url'] for item in data]
    return descriptions, urls

# Generate TF-IDF vectors
def generate_tfidf_vectors(descriptions):
    vectorizer = TfidfVectorizer(max_features=1000)
    tfidf_matrix = vectorizer.fit_transform(descriptions)
    return tfidf_matrix

# Save clustered data with URLs
def save_clustered_data(cluster_labels, urls):
    clustered_data = {}
    for label, url in zip(cluster_labels, urls):
        cluster_key = str(label)
        if cluster_key not in clustered_data:
            clustered_data[cluster_key] = []
        clustered_data[cluster_key].append(url)
    
    with open('clustered_image_data.json', 'w') as f:
        json.dump(clustered_data, f, indent=4)

if __name__ == "__main__":
    descriptions, urls = load_preprocessed_data('preprocessed_image_data.json')
    tfidf_matrix = generate_tfidf_vectors(descriptions)
    kmeans = KMeans(n_clusters=5, random_state=42)
    cluster_labels = kmeans.fit_predict(tfidf_matrix)
    save_clustered_data(cluster_labels, urls)
    print("Clustered image data saved.")
