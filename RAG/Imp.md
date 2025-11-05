### RAG

---

#### Document Loaders

```python
[
Document(page_content = 'Text from page 1', metadata = {'page' : 0, "source" : "file.pdf"}),
Document(page_content = 'Text from page 2', metadata = {'page' : 1, "source" : "file.pdf"})
]
```

---

- TextLoader
- PyPDFLoader
- WebBaseLoader (Needs beautifulsoup4 in requirements.txt)
- CSVLoader
- Directory Loader (We need to define glob here.)
- Load (Eager Loading : Load Everything at once) VS Lazy-Load (Loads on demand)

---

#### Text Splitters

---

#### Vector Store (Storage + Retrieval)

- Task

  - Generate vector embeddings
  - Store
  - Semantic Search

- Key Features

  - Storage (In-memory [RAM] and On-disk [Harddrive])
  - Similarity Search (Semantic Search)
  - Indexing (Clustering)

- Vector Store VS Vector Database
  - VS (Storage & Retrieval)
  - VD (VS + [Additional Features])
    - Distributed Architecture for auto-scaling
    - Durability and Persistence
    - Metadata handling
    - ACID Transactions
    - Authentication / Authorization

```python
from_documents(...) or from_text(...),
add_documents(...) or add_text(...),
similarity_search(query, k =...),
Metadata-Based Filtering
```

- Chroma Hierarchy
  [User -> Database -> Collection -> Doc (Embedding + Metadata)]

---

#### Retrievers

- Runnable : It has access to invoke function
- Retrievers are classified based on the type of data source and search strategy
-
