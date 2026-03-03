# AI Engineer

This repository contains various projects, notebooks, and resources for AI and Machine Learning engineering. It covers foundational libraries, Natural Language Processing (NLP), and Generative AI.

## Project Structure

The project is organized into the following modules:

- **[gen-ai](./gen-ai)**: A comprehensive collection of Generative AI projects, including chat models, embedding models, and applications like CineSage. 
- **[nlp](./nlp)**: Notebooks covering core NLP tasks such as text preprocessing, POS tagging, Named Entity Recognition (NER), and sentiment analysis.
- **[numpy](./numpy)**: Fundamental numerical computing with NumPy.
  - [1_1_numpy_basics.ipynb](./numpy/1_1_numpy_basics.ipynb): Basics, random generation, attributes.
  - [1_2_numpy_indexing_slicing.ipynb](./numpy/1_2_numpy_indexing_slicing.ipynb): Reshaping, indexing, and slicing.
  - [1_3_numpy_operations.ipynb](./numpy/1_3_numpy_operations.ipynb): Element-wise and advanced operations.
  - [1_4_numpy_exercises.ipynb](./numpy/1_4_numpy_exercises.ipynb): Practice problems and exercises.
- **[pandas](./pandas)**: Data manipulation and analysis using Pandas.
- **[python](./python)**: Foundations of Python programming.
  - [1_python_basics.ipynb](./python/1_python_basics.ipynb): Print, data types, variables, and literals.
  - [2_python_operators_loops.ipynb](./python/2_python_operators_loops.ipynb): Operators, if-else, modules, and loops.
  - [3_python_loops_strings.ipynb](./python/3_python_loops_strings.ipynb): Advanced loops and string manipulation.
  - [4_time_complexity.ipynb](./python/4_time_complexity.ipynb): Efficiency, Big O, and examples.
  - [5_python_lists.ipynb](./python/5_python_lists.ipynb): Memory management, methods, and comprehensions.
  - [6_python_tuples_sets_dicts.ipynb](./python/6_python_tuples_sets_dicts.ipynb): Immutability of tuples, unique sets, and key-value dictionaries.
  - [7_python_functions.ipynb](./python/7_python_functions.ipynb): Creation, scope, closures, and functional programming.
  - [8_python_oop_part1.ipynb](./python/8_python_oop_part1.ipynb): Classes, objects, 'self', and dunder methods.
  - [9_python_oop_part2.ipynb](./python/9_python_oop_part2.ipynb): Encapsulation, static members, and reference variables.
  - [10_python_oop_part3.ipynb](./python/10_python_oop_part3.ipynb): Aggregation, inheritance types, MRO, polymorphism, and abstraction.
- **[matplotlib](./matplotlib)**: Data visualization techniques using Matplotlib and Seaborn.

## Getting Started

Each directory contains specific notebooks or scripts related to the topic. Most of the content consists of Jupyter Notebooks (`.ipynb`), which can be run in any standard Jupyter environment or VS Code.

### Prerequisites

- Python 3.x
- Jupyter Notebook / JupyterLab or VS Code with Jupyter extension

### Setup Environment

To run the notebooks in this repository, it is recommended to use the provided virtual environment:

1. **Create and Activate Virtual Environment**:
   ```bash
   # Create the environment (if not already created)
   python3 -m venv .venv

   # Activate the environment
   # On macOS/Linux:
   source .venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install --upgrade pip
   pip install ipykernel numpy pandas matplotlib seaborn scikit-learn
   ```

3. **Select Kernel in VS Code**:
   When opening a `.ipynb` file, click on "Select Kernel" in the top right corner and choose the `.venv` environment.

Required libraries include:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `seaborn`
  - `scikit-learn`
  - `nltk` / `spacy` (for NLP)
  - `google-generativeai` / `langchain` (for Gen-AI)
