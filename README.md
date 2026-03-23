# AI Engineer

This repository contains various projects, notebooks, and resources for AI and Machine Learning engineering. It covers foundational libraries, Natural Language Processing (NLP), and Generative AI.

## Project Structure

The project is organized into the following modules:

- **[python](./python)**: Foundations of Python programming.

  | Notebook | Description |
  | :--- | :--- |
  | [1_python_basics.ipynb](./python/1_python_basics.ipynb) | Print, data types, variables, and literals. |
  | [2_python_operators_loops.ipynb](./python/2_python_operators_loops.ipynb) | Operators, if-else, modules, and loops. |
  | [3_python_loops_strings.ipynb](./python/3_python_loops_strings.ipynb) | Advanced loops and string manipulation. |
  | [4_time_complexity.ipynb](./python/4_time_complexity.ipynb) | Efficiency, Big O, and examples. |
  | [5_python_lists.ipynb](./python/5_python_lists.ipynb) | Memory management, methods, and comprehensions. |
  | [6_python_tuples_sets_dicts.ipynb](./python/6_python_tuples_sets_dicts.ipynb) | Immutability of tuples, unique sets, and key-value dictionaries. |
  | [7_python_functions.ipynb](./python/7_python_functions.ipynb) | Creation, scope, closures, and functional programming. |
  | [8_python_oop_part1.ipynb](./python/8_python_oop_part1.ipynb) | Classes, objects, 'self', and dunder methods. |
  | [9_python_oop_part2.ipynb](./python/9_python_oop_part2.ipynb) | Encapsulation, static members, and reference variables. |
  | [10_python_oop_part3.ipynb](./python/10_python_oop_part3.ipynb) | Aggregation, inheritance types, MRO, polymorphism, and abstraction. |
  | [11_python_exception_handling.ipynb](./python/11_python_exception_handling.ipynb) | Robust error management with try-except. |
  | [12_python_decorators.ipynb](./python/12_python_decorators.ipynb) | Function wrapping and LEGB scope rules. |
  | [13_python_iterators.ipynb](./python/13_python_iterators.ipynb) | Traversal protocols and custom iteration logic. |
  | [14_python_generators.ipynb](./python/14_python_generators.ipynb) | Memory-efficient data processing with yield. |

- **[numpy](./numpy)**: Fundamental numerical computing with NumPy.

  | Notebook | Description |
  | :--- | :--- |
  | [1_numpy_basics.ipynb](./numpy/1_numpy_basics.ipynb) | Basics, random generation, attributes. |
  | [2_numpy_indexing_slicing.ipynb](./numpy/2_numpy_indexing_slicing.ipynb) | Reshaping, indexing, and slicing. |
  | [3_numpy_operations.ipynb](./numpy/3_numpy_operations.ipynb) | Element-wise and advanced operations. |
  | [4_numpy_exercises.ipynb](./numpy/4_numpy_exercises.ipynb) | Practice problems and exercises. |

- **[pandas](./pandas)**: Data manipulation and analysis using Pandas.

  | Notebook | Description |
  | :--- | :--- |
  | [1_pandas.ipynb](./pandas/1_pandas.ipynb) | Data cleaning, transformation, and analysis. |

- **[matplotlib](./matplotlib)**: Data visualization techniques using Matplotlib and Seaborn.

  | Notebook | Description |
  | :--- | :--- |
  | [3_matplotib_seaborn.ipynb](./matplotlib/3_matplotib_seaborn.ipynb) | Data visualization with Matplotlib and Seaborn. |

- **[statistics](./statistics)**: Statistical hypothesis testing and outlier detection.

  | Notebook | Description |
  | :--- | :--- |
  | [central-tendency.ipynb](./statistics/central-tendency.ipynb) | Mean, median, and mode implementation. |
  | [chi-square.ipynb](./statistics/chi-square.ipynb) | Chi-Square test implementation. |
  | [outliers.ipynb](./statistics/outliers.ipynb) | Outlier detection techniques. |
  | [t-test.ipynb](./statistics/t-test.ipynb) | T-Test implementation. |
  | [z-test.ipynb](./statistics/z-test.ipynb) | Z-Test implementation. |

- **[machine-learning](./machine-learning)**: Practical machine learning projects and applications.
  - **Algorithms**:
    - [linear-regression.ipynb](./machine-learning/algorithms/linear-regression.ipynb): Implementation of Linear Regression.
    - [logistic-regression.ipynb](./machine-learning/algorithms/logistic-regression.ipynb): Implementation of Logistic Regression.
  - [ford-car-price-prediction](./machine-learning/ford-car-price-prediction): Predicting car prices based on features.
  - [heart-disease-prediction](./machine-learning/heart-disease-prediction): Classification of heart disease risk.
  - [insurance-coverage-prediction](./machine-learning/insurance-coverage-prediction): Predicting insurance coverage costs.

- **[nlp](./nlp)**: Comprehensive NLP modules covering text processing and analysis.

  | Module | Notebook | Description |
  | :--- | :--- | :--- |
  | **Text Preprocessing** | [nlp_text_preprocessing.ipynb](./nlp/text-preprocessing/nlp_text_preprocessing.ipynb) | Lowercasing, stop words, regex, and tokenization. |
  | **POS & NER** | [nlp_identify_pos_and_names_entities.ipynb](./nlp/identify-pos-and-names-entities/nlp_identify_pos_and_names_entities.ipynb) | Parts-of-speech tagging and Named Entity Recognition. |
  | **Sentiment Analysis** | [nlp_sentiment_analysis.ipynb](./nlp/sentiment-analysis/nlp_sentiment_analysis.ipynb) | Analyzing text sentiment and emotions. |

- **[opencv](./opencv)**: Computer vision and image processing with OpenCV.

  | Notebook | Description |
  | :--- | :--- |
  | [1_opencv_basics.ipynb](./opencv/1_opencv_basics.ipynb) | Installation and basic image I/O. |
  | [2_opencv_transformations.ipynb](./opencv/2_opencv_transformations.ipynb) | Resizing, cropping, rotation, and flipping. |
  | [3_opencv_processing.ipynb](./opencv/3_opencv_processing.ipynb) | Blurring, edge detection, and thresholding. |
  | [4_opencv_drawing.ipynb](./opencv/4_opencv_drawing.ipynb) | Drawing shapes (lines, rectangles, circles) and text. |
  | [5_opencv_video.ipynb](./opencv/5_opencv_video.ipynb) | Video capture and processing basics. |
  | [6_gesture_control.ipynb](./opencv/6_gesture_control.ipynb) | Hand gesture control using MediaPipe. |
  | [7_motion_detector.ipynb](./opencv/7_motion_detector.ipynb) | Real-time motion detection implementation. |

- **[langchain](./langchain)**: A comprehensive collection of Generative AI projects, including:
  - **[chat-models](./langchain/chat-models)**: Various LLM chat implementations.
  - **[embedding-models](./langchain/embedding-models)**: Vector embedding generation.
  - **[cine-sage](./langchain/cine-sage)**: Structured movie metadata extraction.
  - **[rag](./langchain/rag)**: Retrieval Augmented Generation components.

- **[fastapi](./fastapi)**: Production-grade web applications using FastAPI.
  - **[backend-forge](./fastapi/backend-forge)**: A modular FastAPI starter with asynchronous database support (asyncpg, SQLAlchemy), Alembic migrations, and environment-based configuration.

- **[resources](./resources)**: Reference materials and books.
  - Includes PDF guides on Deep Learning, Large Language Models, and Machine Learning.

- **[roadmap](./roadmap)**: Career paths and learning roadmaps for AI engineering.

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
