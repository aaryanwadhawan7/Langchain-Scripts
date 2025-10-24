from langchain_community.document_loaders import TextLoader

loader = TextLoader(
    'Football.txt',
    'utf-8'
)

docs = loader.load()

## print (docs)
## print (type(docs))

print (type (docs[0]))
## <class 'langchain_core.documents.base.Document'>