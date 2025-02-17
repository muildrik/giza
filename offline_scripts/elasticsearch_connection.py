
from elasticsearch import Elasticsearch

# TODO: this needs to come from settings
ELASTICSEARCH_URL = 'localhost:9200'

# Connect to elasticsearch db
def get_connection():
    return Elasticsearch(ELASTICSEARCH_URL, timeout=30, max_retries=10, retry_on_timeout=True)

# Gets the content of an item, returns JSON
def get_item(item_id, source, index):
    return es.get(index=index, doc_type=source, id=item_id)["_source"]

# Inserts JSON document into elasticsearch with the given item_id
# Either adds new document or replaces existing document
def add_or_update_item(item_id, document, source, index):
    es.index(index=index, doc_type=source, id=item_id, body=document)

# Checks if item exists in elasticsearch, returns boolean
def item_exists(item_id, source, index):
    if (item_id is None or source is None):
        return False
    return es.exists(index=index, doc_type=source, id=item_id)

def delete(item_id, source, index):
    return es.delete(index=index, doc_type=source, id=item_id)

es = get_connection()
