from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb
from config.config_loader import load_config


def add_custom_functions():
    cfg = load_config()

    model = SentenceTransformer(cfg["embedding"]["model"])
    client = chromadb.PersistentClient(path=cfg["database"]["path"])
    col = client.get_or_create_collection(cfg["database"]["collection_name"])

    files = list(Path("data/custom_functions").glob("*.py"))

    texts, metas, ids = [], [], []
    start = col.count()

    for i, fp in enumerate(files, start=start):
        txt = fp.read_text(encoding="utf-8")

        texts.append(txt)
        metas.append({
            "func_name": fp.stem,
            "repo": "custom",
            "path": str(fp).replace("\\", "/"),
            "source": "custom"
        })
        ids.append(str(i))

    embs = model.encode(texts).tolist()

    col.add(
        ids=ids,
        documents=texts,
        embeddings=embs,
        metadatas=metas
    )








"""
from pathlib import Path
from sentence_transformers import SentenceTransformer
import chromadb
from config.config_loader import load_config
from pathlib import Path


def add_custom_functions():
    cfg = load_config()
    model = SentenceTransformer(cfg['embedding']['model'])
    client = chromadb.PersistentClient(path=cfg['database']['path'])
    col = client.get_or_create_collection(cfg['database']['collection_name'])

    files = list(Path('data/custom_functions').glob('*.py'))
    texts, metas, ids = [], [], []
    start = col.count()
    for i, fp in enumerate(files, start=start):
        txt = fp.read_text(encoding='utf-8')
        texts.append(txt)
        metas.append({'func_name': fp.stem, 'repo': 'custom', 'path': str(fp), 'source': 'custom'})
        ids.append(str(i))
    embs = model.encode(texts).tolist()
    col.add(ids=ids, documents=texts, embeddings=embs, metadatas=metas)"""