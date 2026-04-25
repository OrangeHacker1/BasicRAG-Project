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

PART 2 RESULTS:


# REFLECTION
Upon completing this project, I found that the RAG created was capable of handiling simple tasks. There were no extremely complicated or niche quesstions askeed for this experiment. The model was able to answer questions while siting the RAG, thus ensuring that the python methods are in fact grounded and would work. The only issue was when a custom method was prioritized over a better already existing method.    
During part 2, I found that the custom method would end up taking the top spot, even when it doesn't acctually complete the task. This wasn't an issue for unrelated tasks though. There seemed to be an elivated priority for the newest items added to this RAG.    
If I was given more time to play around with this project, I would have liked to further test more advanced questions. Perhaps I could add comments to the methods to see how that would impact the project. Asking more questions with similar topics but different essense could also help see how accurate the code is. It would also be interesting to explore different models to see the impact.    
