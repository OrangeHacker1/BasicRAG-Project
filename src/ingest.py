from datasets import load_dataset
from sentence_transformers import SentenceTransformer
import chromadb
from config.config_loader import load_config



def build_starter_collection(reset=False):
    cfg = load_config()
    client = chromadb.PersistentClient(path=cfg['database']['path'])

    name = cfg['database']['collection_name']
    if reset:
        try:
            client.delete_collection(name)
        except Exception:
            pass

    col = client.get_or_create_collection(name)
    model = SentenceTransformer(cfg['embedding']['model'])

    ds = load_dataset(
    "code_search_net",
    "python",
    split="train",
    streaming=True
)

    rows = []
    for i, row in enumerate(ds):
        rows.append(row)
        if len(rows) >= cfg['dataset']['starter_size']:
            break

    texts = []
    metas = []
    ids = []

    for idx, r in enumerate(rows):
        doc = r.get('func_documentation_string') or ''
        code = r.get('func_code_string') or ''
        text = doc + '\n' + code
        texts.append(text)
        metas.append({
            'func_name': r.get('func_name', ''),
            'repo': r.get('repository_name', ''),
            'path': r.get('func_path_in_repository', ''),
            'source': 'starter'
        })
        ids.append(str(idx))

    embs = model.encode(texts, show_progress_bar=True).tolist()
    col.add(ids=ids, documents=texts, embeddings=embs, metadatas=metas)
    return col