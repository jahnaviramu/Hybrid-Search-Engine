HYBRID SEARCH ENGINE 

DESCRIPTION  
The Hybrid Search Engine is an AI-powered application that combines keyword-based search with semantic search for accurate and relevant results. It uses MongoDB for database management, sentence-transformers for semantic similarity, and Streamlit for the web interface. This hybrid approach enhances the search accuracy by ranking results based on both text matching and contextual relevance.  

TECH STACK  
Backend: Python 3.8+, MongoDB  
Frontend: Streamlit for interactive web interface  
Database: MongoDB local or remote  
Libraries:  
pymongo: For MongoDB interaction  
nltk: For text processing tokenization  
transformers and sentence-transformers: For embedding generation and semantic similarity  
numpy: For numerical operations  
Environment Manager: Conda  
Operating System: Compatible with Linux, Windows, and macOS  

PRODUCTION SERVER IF DEPLOYING  
Cloud Service: AWS, GCP, Azure, or on-premise server  
Minimum Specifications:  
RAM: 8GB  
CPU: 4 cores  
Storage: 20GB SSD  
GPU: Optional, based on query volume and model usage  

PROPOSED PROTOCOL  

SYSTEM INITIALIZATION  
Hardware Setup:  
Multi-core CPU e.g., Intel i5 or AMD Ryzen  
RAM: 8GB minimum 16GB recommended  
Storage: SSD with at least 10GB free space  
Optional GPU: NVIDIA GTX 1050 or better for transformer efficiency  
Software Setup:  
Install and configure MongoDB locally or remotely  
Install Python >=3.8  

ENVIRONMENT SETUP  
Create a Python virtual environment:  
python -m venv env  
source env/bin/activate  Linux/Mac  
env\Scripts\activate  Windows  

Install dependencies:  
pip install pymongo nltk transformers sentence-transformers numpy streamlit  

NLTK setup:  
import nltk  
nltk.download('punkt')  

MONGODB DATABASE INITIALIZATION  
Start the MongoDB server  
Create a database:  
Name: search_db  
Collection: documents  
Insert sample data into the documents collection  
Create a text index on the title and content fields for keyword-based search  

HYBRID SEARCH IMPLEMENTATION  
Keyword Search:  
Uses MongoDB’s $text query for keyword matching  
AI-Based Semantic Search:  
Uses sentence-transformers to generate embeddings for both the query and documents  
Computes similarity scores using cosine similarity  
Integration:  
Combines both methods to provide hybrid search results ranked by relevance  

WEB INTERFACE  
Streamlit-based interactive front-end:  
Input field for user queries  
Displays ranked results with titles, content excerpts, and similarity scores  
Start the application:  
streamlit run app.py  

INSTALLATION AND USAGE  
Clone the repository:  
git clone <repository_url>  
cd hybrid-search-engine  

Install dependencies:  
pip install -r requirements.txt  

Start MongoDB server and Streamlit application:  
python app.py  
streamlit run app.py  

Open in the browser:  
http://localhost:8501  

CONTRIBUTIONS  
Contributions are welcome! Feel free to submit a pull request or create an issue.  

LICENSE  
This project is licensed under the MIT License.  

HYBRID SEARCH ENGINE → Combining keyword-based and AI-powered semantic search for accurate and relevant results.
