from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import Tool
from pathlib import Path
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_output.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    output_path = Path(__file__).parent / filename
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {output_path}"

save_tool = Tool(
    name='save_text_to_file',
    func=save_to_txt,
    description='Save the research output to a text file with a timestamp. Input should be a string.',
)

search = DuckDuckGoSearchRun()
search_tool = Tool(
    name='search',
    func=search.run,
    description='search the web for info',
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
