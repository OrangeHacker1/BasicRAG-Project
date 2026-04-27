TRACK: B

# Methodology
For this assignment, the code is designed to create a local RAG for a callable LLM model. In order to reproduce this code, you will need to store the following variables within a '.env' file within the project: GENERATOR_BASE_URL; GENERATOR_MODEL; GENERATOR_API_KEY.

To run the code for this project, two files were created. The first is 'run_part1.py'. This is designed to create the initial RAG memory and populate the memmory with python methods. The amount of methods can be specified within the config file. After completing the initial RAG, this projeect aims to test how adding additional methods will impact the RAG. The 'run_part2.py' file will achieve this task by adding methods stored within the 'data\custom_functions' folder into the RAG storage space.    

In order to ensure that this works correctly and is reproducable, you will need to delete the chroma_code folder every time you run this code. If the folder is not deleted, you will end up duplicating methods within the RAG's memory. When looking at the top methods to accomplish each task, you will find duplicates of the best matches. This is an important consideration to ensure the RAG is working correctly.    

For my code, I used the following LLM:

    GENERATOR_BASE_URL=http://149.165.173.247:8888/v1
    GENERATOR_MODEL=meta-llama/Llama-3.1-8B-Instruct
    GENERATOR_API_KEY=<REDACTED>

REDULTS:

Part 1 RESULTS:    

| Query ID | Query | Top 4 | Answer Given | Judgement |
|----------|-------|-------|--------------|-----------|
| 1 | 'How do I decode JSON?' | [1] repo: DataMedSci/mcpartools, path: mcpartools/mcengine/shieldhit.py, func: ShieldHit._decrypt_icru_files; [2] repo: teaearlgraycold/puni, path: puni/base.py, func: UserNotes.get_json; [3] repo: elifesciences/elife-tools, path: elifetools/json_rewrite.py, func: rewrite_elife_body_json; [4] repo: canonical-ols/acceptable, path: acceptable/__main__.py, func: load_metadata | `json.load(stream, encoding='utf8', object_pairs_hook=OrderedDict)` Source: canonical-ols/acceptable::acceptable/__main__.py::load_metadata",manual_review | Yes |
| 2 | 'How do I sort a list?' | [1] repo: canonical-ols/acceptable, path: acceptable/util.py, func: _sort_schema; [2] repo: canonical-ols/acceptable, path: acceptable/_build_doubles.py, func: render_value; [3] repo: frostming/atoml, path: atoml/decoder.py, func: contains_list; [4] repo: elifesciences/elife-tools, path: elifetools/parseJATS.py, func: map_equal_contributions | You can use the `sorted()` function in Python to sort a list. Here's an example: ```python my_list = [3, 1, 2] sorted_list = sorted(my_list) print(sorted_list)  # Output: [1, 2, 3] ``` | Yes |
| 3 | 'How do I make an HTTP request?' | [1] repo: quantmind/agile-toolkit, path: agiletoolkit/api/components.py, func: RepoComponents.create; [2] repo: fredrike/pypoint, path: pypoint/__init__.py, func: PointSession._request_devices; [3] repo: fredrike/pypoint, path: pypoint/__init__.py, func: PointSession._register_webhook; [4] repo: quizl/quizler, path: quizler/lib.py, func: api_call | You can make an HTTP request using the `requests` library. 

Here's an example of how to make a GET request: ```python
import requests
url = 'https://example.com'
response = requests.get(url)
print(response.status_code)
print(response.json()) ``` | No |
| 4 | 'How do I parse command line arguments?' |
| 5 | 'How do I read a file line by line?' |
| 6 | 'How do I remove duplicates from a list?' |
| 7 | 'How do I convert bytes to string?' |
| 8 | 'How do I run a factorial?' |
| 9 | 'How do I retry failed operations?' |
| 10 | 'How do I work with URLs?' |

PART 2 RESULTS:     


# REFLECTION
Upon completing this project, I found that the RAG created was capable of handiling simple tasks. The questions did not always use the methods for the top K. However, the LLM would grab methods within the top K. This can be debated about whether it is grounded since the methods being used are listed within the top K. However, not all of the responses were properly citing there sources. If the method is show within the top K and cited, it will be considered grounded. However, the methods will need to be show. This is likely due to the fact that better methods are shown being used within the top K. The RAG didn't have the best solutions.      
Another factor playing into the results are likely due to the methods saved within the RAG having high complexity and being niche. While the LLM does its best to find the best k matches, there are subparts that can be used better. This could have also been dealt with better if more complex questions were asked. I am assuming that the methods that the submethods, like json.load() was not in the RAG. I did not have time to go through and check to make sure the items were not being missed.    
Looking at the results for part, I found that the results were much better for the targetted questions. This furthur proves that the retrieval method for the top K is working correctly.   
During part 2, I found that the custom method would end up taking the top spot, even when it doesn't acctually complete the task. This wasn't an issue for unrelated tasks though. There seemed to be an elivated priority for the newest items added to this RAG.    
If I was given more time to play around with this project, I would have liked to further test more advanced questions. Perhaps I could add comments to the methods to see how that would impact the project. Asking more questions with similar topics but different essense could also help see how accurate the code is. It would also be interesting to explore different models to see the impact.    
