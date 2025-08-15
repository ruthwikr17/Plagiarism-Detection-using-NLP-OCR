import re
import os
from tkinter import Tk, filedialog
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader
from docx import Document
from PIL import Image
import pytesseract


# Function for text preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text


# Function to extract text from different file types
def extract_text_from_file(filepath):
    ext = os.path.splitext(filepath)[1].lower()
    if ext == ".txt":
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    elif ext == ".pdf":
        reader = PdfReader(filepath)
        return " ".join([page.extract_text() or "" for page in reader.pages])
    elif ext == ".docx":
        doc = Document(filepath)
        return " ".join([para.text for para in doc.paragraphs])
    elif ext in [".jpg", ".jpeg", ".png"]:
        img = Image.open(filepath)
        custom_config = r"--oem 3 --psm 6"
        return pytesseract.image_to_string(img, config=custom_config)
    else:
        raise ValueError("Unsupported file type: " + ext)


# Function to open file dialog and load text
def load_document(prompt):
    print(prompt)
    filepath = filedialog.askopenfilename(
        filetypes=[("Supported Files", "*.txt *.pdf *.docx *.jpg *.jpeg *.png")]
    )
    if not filepath:
        raise ValueError("No file selected.")
    return preprocess_text(extract_text_from_file(filepath))


# Hide Tkinter root window
Tk().withdraw()

# Load and preprocess documents
text1 = load_document("Select the first document (original):")
text2 = load_document("Select the second document (to compare):")

# Load model
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# Generate embeddings
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)

# Compute cosine similarity
similarity_score = cosine_similarity([embedding1], [embedding2])[0][0]

# Output result
print(f"\nSimilarity Score: {similarity_score:.2f}")
if similarity_score > 0.8:
    print("High similarity - possible plagiarism.")
elif similarity_score > 0.6:
    print("Moderate similarity - check for paraphrasing.")
else:
    print("Low similarity - likely original content.")
