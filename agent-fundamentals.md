# Agent Fundamentals

_Taken from [Tech with Tim vid](https://www.youtube.com/watch?v=OKwDzKY_WN8&list=PL3lRs2q5QYyQSZEhAKpRnW5NKuwALGEsE)_

## Agent Building Blocks

- **LLM** to handle language and understanding responses (eg. OpenAI's GPT-4)
- **Prompt Template**: Clearly explains the task, provides context, specifies the format that you want for the particular response
- **Reasoning Strategies**:
  - ReAct -> thinks through problem step by step before taking action
  - Plan-and-Execute -> Similar to ReAct but it separates the planning phase from the execution phase
  - Reflexion: encourages agent to reflect on past actions to improve performance
- **Tools & Actions**: Tools give your agent the ability to make API calls, access the web, execute code, run file operations. Otherwise all it can do is generate text
- **Memory and State Management**: Memory systems store information from past interactions. Without this your agent is a goldfish.
- **Control Loop**: decision making progress that determines what the agent does next (Observe, Decide, Act, Repeat)

## Python Frameworks

- **LangChain**: Best for full programmatic control, API calls, complex reasoning tasks, memory management
- **LangGraph**: Best for state management, complex workflows, multi-step processes, synchronous branching logic conditions
- **LangFlow**: visual drag and drop framework, minimal coding, good for prototyping quickly and experimenting quickly with different...agent archetecture
- **LlamaIndex**: designed to connect external data sources like PDF's, websites, and databases to LLMs. Go to choice for data-centric AI agents
- **crewai**: ideal for multiple agents working together

### Additional Python Tools

- **Streamlit**: Python tool for building UI
- **DATASTAX and chromaDB**: vector database solutions for storing and retrieving embeddings
- **pandas**: data manipulation and analysis within your agent workflow

## Design Patterns

### ReAct

- Standard approach for tool-using agents
- Step 1 -> Reason (thinks through what it knows and what it needs to find out)
- Step 2 -> Act (Selects appropriate action)
- Step 3 -> Observes result
- Step 4 -> Repeats for whatever it needs to do
- Best for tool heavy tasks, step by step exploration, info gathering

### Plan and Execute

- You have two components: Planner Agent and Executor Agent
- Planner Agent develops step by step plan
- Executor executes the plan
- Ideal for complex tasks where mistakes will be costly like a coding agent

### Multi Agent Collaboration

- Teams of agents that work together on complex problems
- You assign specific roles based on different expertise

### RAG (Retrieval Augmented Generation)

- Agent searches some kind of documentation before answering (eg. a customer service bot that needs to review company docs before answering a customer's question)
- Ensures more accurate responses

## Picking your Stack

- Start by creating one agent with one clear goal and no complex memory requirements
- You can gradually add more complexity, such as memory and tools as needed

### Frameworks

- If you need full control -> LangChain or LangGraph
- Collab between agents -> crewAI/AutoGen
- Quick demo -> LangFlow/Streamlit
- Privacy concerns -> Ollama/Llama.cpp

## Final Word

- Start with a simple prolem statement, choose the simplest stack that addresses your needs, and iterate from there
