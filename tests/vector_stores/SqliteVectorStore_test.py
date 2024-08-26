import pytest
from swarmauri.standard.documents.concrete.Document import Document
from swarmauri.standard.vector_stores.concrete.SqliteVectorStore import SqliteVectorStore

@pytest.mark.unit
def test_ubc_resource():
	vs = SqliteVectorStore()
	assert vs.resource == 'VectorStore'
	assert vs.embedder.resource == 'Embedding'

@pytest.mark.unit
def test_ubc_type():
	vs = SqliteVectorStore()
	assert vs.type == 'SqliteVectorStore'

@pytest.mark.unit
def test_serialization():
	vs = SqliteVectorStore()
	assert vs.id == SqliteVectorStore.model_validate_json(vs.model_dump_json()).id

@pytest.mark.unit
def top_k_test():
	vs = SqliteVectorStore()
	documents = [Document(content="test"),
	     Document(content='test1'),
	     Document(content='test2'),
	     Document(content='test3')]

	vs.add_documents(documents)
	assert len(vs.retrieve(query='test', top_k=2)) == 2