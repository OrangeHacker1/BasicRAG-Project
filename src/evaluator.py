import pandas as pd
from src.retriever import retrieve
from src.generator import generate_answer


def run_queries(queries, output_path):
    rows = []

    for i, query in enumerate(queries, start=1):
        result = retrieve(query)

        prompt, answer = generate_answer(query, result)

        metas = result["metadatas"][0]
        dists = result["distances"][0]

        sources = []
        for m in metas:
            repo = m.get("repo", "")
            path = m.get("path", "").replace("\\", "/")
            func = m.get("func_name", "")
            sources.append(f"{repo}/{path}::{func}")

        rows.append({
            "query_id": i,
            "query": query,
            "sources": " | ".join(sources),
            "scores": " | ".join(map(str, dists)),
            "prompt": prompt,
            "answer": answer,
            "grounded": "manual_review"
        })

    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)
    return df
"""
import pandas as pd
from src.retriever import retrieve
from src.generator import generate_answer


def run_queries(queries, output_path):
    rows = []
    for i, query in enumerate(queries, start=1):
        result = retrieve(query)
        answer = generate_answer(query, result)
        metas = result['metadatas'][0]
        dists = result['distances'][0]
        sources = [f"{m['repo']}/{m['path']}::{m['func_name']}" for m in metas]
        rows.append({
            'query_id': i,
            'query': query,
            'sources': ' | '.join(sources),
            'scores': ' | '.join(map(str, dists)),
            'answer': answer[:500],
            'grounded': 'manual_review'
        })
    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False)
    return df"""