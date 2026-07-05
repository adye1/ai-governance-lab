import chromadb, sys
from sentence_transformers import SentenceTransformer
from openai import OpenAI

# Same embedding model, CPU (Maxwell/PyTorch limitation, same as ingest.py)
embed = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')

# Connect to the vector store we built with ingest.py
col = chromadb.PersistentClient(path='./chroma').get_collection('corpus')

# Talk to the LOCAL Ollama model via its OpenAI-compatible API
llm = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')

# The user's question comes from the command line
question = sys.argv[1]

# 1. RETRIEVE: find the 2 most relevant documents
hits = col.query(query_embeddings=[embed.encode(question).tolist()], n_results=2)
context = '\n\n'.join(hits['documents'][0])

# 2. AUGMENT: build a prompt that includes the retrieved context
prompt = f"""Answer the question using only the context below.

Context:
{context}

Question: {question}"""

# 3. GENERATE: ask the local model
resp = llm.chat.completions.create(
    model='llama3.1:8b',
    messages=[{'role': 'user', 'content': prompt}]
)
print(resp.choices[0].message.content)
