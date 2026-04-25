from openai import OpenAI
from config.config_loader import load_config
from config.env_loader import load_environment

cfg = load_config()
env = load_environment()

client = OpenAI(
    api_key=env["generator_key"],
    base_url=env["generator_base"]
)


def build_prompt(query, retrieved):
    docs = retrieved["documents"][0]
    metas = retrieved["metadatas"][0]

    context_blocks = []

    for i, (doc, meta) in enumerate(zip(docs, metas), start=1):
        repo = meta.get("repo", "")
        path = meta.get("path", "").replace("\\", "/")
        func = meta.get("func_name", "")

        block = (
            f"[{i}] repo: {repo}, "
            f"path: {path}, "
            f"func: {func}\n"
            f"{doc.strip()}\n"
        )

        context_blocks.append(block)

    joined = "\n".join(context_blocks)

    prompt = f"""System: Answer using only the provided code. Cite sources as repo/path::func_name.

Context:
{joined}

User query: {query}
"""

    return prompt


def generate_answer(query, retrieved):
    prompt = build_prompt(query, retrieved)

    resp = client.chat.completions.create(
        model=env["generator_model"],
        messages=[{"role": "user", "content": prompt}],
        temperature=cfg["generation"]["temperature"],
        max_tokens=cfg["generation"]["max_tokens"]
    )

    return prompt, resp.choices[0].message.content



"""

from openai import OpenAI
from config.config_loader import load_config
from config.env_loader import load_environment

cfg = load_config()
env = load_environment()
client = OpenAI(api_key=env['generator_key'], base_url=env['generator_base'])


def build_prompt(query, retrieved):
    docs = retrieved['documents'][0]
    metas = retrieved['metadatas'][0]
    context = []
    for i, (doc, meta) in enumerate(zip(docs, metas), start=1):
        context.append(f"[{i}] repo: {meta['repo']}, path: {meta['path']}, func: {meta['func_name']}{doc}")
        joined = "".join(context)
    return f""System: Answer using only the provided code. Cite sources as repo/path::func_name.

Context:
{joined}

User query: {query}""


def generate_answer(query, retrieved):
    prompt = build_prompt(query, retrieved)
    resp = client.chat.completions.create(
        model=env['generator_model'],
        messages=[{'role': 'user', 'content': prompt}],
        temperature=cfg['generation']['temperature'],
        max_tokens=cfg['generation']['max_tokens']
    )
    return resp.choices[0].message.content"""