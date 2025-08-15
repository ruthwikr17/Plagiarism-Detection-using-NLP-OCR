**Plagiarism Detection using NLP & OCR**<br>

This project detects text similarity between two documents to identify potential plagiarism.
It supports text files, Word documents, PDFs, and images using OCR (Tesseract).  <br><br>

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

**Features**<br>

	•	Supports .txt, .docx, .pdf, and image formats (.png, .jpg, .jpeg) <br>
	•	Text preprocessing (tokenization, stopword removal, normalization) <br>
	•	OCR integration with Tesseract for extracting text from images <br>
	•	Cosine Similarity to calculate plagiarism percentage <br>
	•	Simple file selection using Tkinter <br><br>


**Usage**<br>

Run the script:
  *python plagiarism_detection.py*

  1.	Select the first document (original). <br>
  2.	Select the second document (to check for plagiarism). <br>
  3.	View the plagiarism percentage in the terminal. <br><br>


**Requirements**<br>
	•	Python 3 <br>
	•	pytesseract <br>
	•	python-docx <br>
	•	PyPDF2 (fitz) <br>
	•	scikit-learn <br>
	•	nltk <br>
	•	tkinter <br>
