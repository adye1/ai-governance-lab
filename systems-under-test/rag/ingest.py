import chromadb, glob, os
from sentence_transformers import SentenceTransformer

# Force CPU: the M4000 (Maxwell/sm_52) isn't supported by modern PyTorch.
# Embedding a few small docs on CPU is instant anyway.
print("Loading embedding model (CPU)...")
embed = SentenceTransformer('all-MiniLM-L6-v2', device='cpu')

client = chromadb.PersistentClient(path='./chroma')
col = client.get_or_create_collection('corpus')

files = glob.glob('corpus/*.txt')
for path in files:
    text = open(path).read()
    col.add(
        ids=[os.path.basename(path)],
        embeddings=[embed.encode(text).tolist()],
        documents=[text]
    )
    print(f"  ingested: {path}")

print(f"\nDone. {col.count()} documents in the vector store.")
