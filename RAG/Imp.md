### RAG

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

#### Vector Databases

#### Retrievers
