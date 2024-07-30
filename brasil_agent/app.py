import os

import pandas as pd
from dotenv import load_dotenv
from llama_index.experimental.query_engine import PandasQueryEngine
from tools.prompts import new_prompt, instruction_str

load_dotenv()

population_path = os.path.join("..", "data", "population.csv")
population = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(df=population, verbose=True, instruction_str=instruction_str)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})

population_query_engine.query("qual a população do brasil?")


