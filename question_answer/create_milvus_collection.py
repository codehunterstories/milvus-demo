import common.milvus_v as mvar
from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection, utility

connections.connect(host=mvar.get_ip(), port=mvar.get_port())

def create_milvus_collection(collection_name, dim):
    if utility.has_collection(collection_name):
        utility.drop_collection(collection_name)
    
    fields = [
    FieldSchema(name='id', dtype=DataType.VARCHAR, description='ids', max_length=500, is_primary=True, auto_id=False),
    FieldSchema(name='embedding', dtype=DataType.FLOAT_VECTOR, description='embedding vectors', dim=dim)
    ]
    schema = CollectionSchema(fields=fields, description='Question Answering System')
    collection = Collection(name=collection_name, schema=schema)

    # create IVF_FLAT index for collection.
    index_params = {
        'metric_type':'L2',
        'index_type':"IVF_FLAT",
        'params':{"nlist":2048}
    }
    collection.create_index(field_name="embedding", index_params=index_params)
    return collection

collection = create_milvus_collection(mvar.get_collection_name(), mvar.get_collection_dim())
print('Total number of inserted data is {}.'.format(collection.num_entities))

