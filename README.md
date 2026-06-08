# 🚀 The AI Engineer Journey: An Open-Source Learning Curriculum

Welcome to the **AI Engineer Journey** hub! This repository is designed as a structured, self-paced, open-source curriculum and sandbox for software engineers, data scientists, and AI enthusiasts aiming to master the practical discipline of **AI Engineering**.

AI Engineering is the art and science of building, deploying, and optimizing intelligence-driven applications. Unlike traditional machine learning research, AI Engineering is focused on **systems, integration, orchestration, and production-grade software architecture**. This repository covers the entire path: from foundational programming and statistics to deep learning, computer vision, agentic systems, and MLOps.

---

## 🗺️ The 5-Phase Learning Roadmap

This repository is organized into a curriculum consisting of five progressive phases. Each phase builds on the previous one, transitioning from core math and programming foundations to productionizing complex AI agents.

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    PHASE 1: Software & Mathematical Foundations                 │
│          Python OOP & Advanced Features ➔ NumPy ➔ Pandas ➔ Matplotlib ➔ Stats   │
└───────────────────────┬─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    PHASE 2: Classical Machine Learning & Pipelines              │
│       ML Math ➔ Regressions & Classification ➔ Custom Estimators ➔ Ingestion    │
└───────────────────────┬─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    PHASE 3: Deep Learning, PyTorch & Computer Vision            │
│       PyTorch Core ➔ ANNs, CNNs, RNNs ➔ OpenCV Processing ➔ YOLOv8 Detection    │
└───────────────────────┬─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    PHASE 4: Generative AI, LLMs & Stateful Agents               │
│        GPT from Scratch ➔ LangChain Orchestration ➔ LangGraph Multi-Agents       │
└───────────────────────┬─────────────────────────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    PHASE 5: Production Deployment & MLOps                       │
│    Pydantic Data Schemas ➔ Async FastAPI ➔ ZenML Orchestration ➔ Dockerization  │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 📚 Phase 1: Software & Mathematical Foundations
*Every robust AI system requires efficient, readable, and clean software architecture under the hood. AI engineers work at the intersection of heavy math and high-performance software.*

### 🛠️ Python Foundations (`python/`)
* **How it helps your journey**: Models and frameworks are written in Python. Mastering OOP, memory management, generators (for data streaming), and decorators is critical for customizing deep learning lifecycles and dataloaders.
* **Notebooks**:
  * [1_python_basics.ipynb](./python/1_python_basics.ipynb): Print, data types, variables, and literals.
  * [2_python_operators_loops.ipynb](./python/2_python_operators_loops.ipynb): Operators, if-else, modules, and loops.
  * [3_python_loops_strings.ipynb](./python/3_python_loops_strings.ipynb): Advanced loops and string manipulation.
  * [4_time_complexity.ipynb](./python/4_time_complexity.ipynb): Complexity analysis, Big O notation, and performance optimization.
  * [5_python_lists.ipynb](./python/5_python_lists.ipynb): Memory layouts, list operations, and comprehensions.
  * [6_python_tuples_sets_dicts.ipynb](./python/6_python_tuples_sets_dicts.ipynb): Immutability of tuples, unique sets, and fast dict key lookups.
  * [7_python_functions.ipynb](./python/7_python_functions.ipynb): Function scopes, closures, namespaces, and functional paradigms.
  * [8_python_oop_part1.ipynb](./python/8_python_oop_part1.ipynb): Classes, objects, `self`, constructors, and dunder methods.
  * [9_python_oop_part2.ipynb](./python/9_python_oop_part2.ipynb): Encapsulation, static members, and reference variable management.
  * [10_python_oop_part3.ipynb](./python/10_python_oop_part3.ipynb): Aggregation, inheritance structures, MRO, polymorphism, and abstract base classes.
  * [11_python_exception_handling.ipynb](./python/11_python_exception_handling.ipynb): Writing robust, fail-safe code blocks.
  * [12_python_decorators.ipynb](./python/12_python_decorators.ipynb): Wrapping functions and standardizing interfaces (LEGB scope).
  * [13_python_iterators.ipynb](./python/13_python_iterators.ipynb): Custom traversal protocols and iterable design patterns.
  * [14_python_generators.ipynb](./python/14_python_generators.ipynb): Lazy execution and memory-efficient data processing with `yield`.

### 🔢 Numerical Computing with NumPy (`numpy/`)
* **How it helps your journey**: Neural networks operate on multi-dimensional matrices (tensors). NumPy introduces vectorization, element-wise math, and linear algebra operations without slow Python loops.
* **Notebooks**:
  * [1_numpy_basics.ipynb](./numpy/1_numpy_basics.ipynb): Array initialization, random number generation, and attributes.
  * [2_numpy_indexing_slicing.ipynb](./numpy/2_numpy_indexing_slicing.ipynb): Reshaping arrays, boolean masking, and indexing techniques.
  * [3_numpy_operations.ipynb](./numpy/3_numpy_operations.ipynb): Vectorized mathematics, matrix multiplication, and broadcasting.
  * [4_numpy_exercises.ipynb](./numpy/4_numpy_exercises.ipynb): Practical coding exercises to solidify understanding.

### 🐼 Data Wrangling & Analysis with Pandas (`pandas/`)
* **How it helps your journey**: Real-world AI engineering is 80% data cleaning. Pandas is the standard utility for processing raw database exports and user logs.
* **Notebooks**:
  * [1_pandas_basics.ipynb](./pandas/1_pandas_basics.ipynb): Understanding core Series and DataFrame structures.
  * [2_pandas_selection_indexing.ipynb](./pandas/2_pandas_selection_indexing.ipynb): Selecting rows/columns, filtering, and indexing.
  * [3_pandas_missing_data.ipynb](./pandas/3_pandas_missing_data.ipynb): Cleaning and imputing missing dataset features.
  * [4_pandas_combining_data.ipynb](./pandas/4_pandas_combining_data.ipynb): Merging, joining, and concatenating structured dataframes.
  * [5_pandas_grouping_aggregating.ipynb](./pandas/5_pandas_grouping_aggregating.ipynb): GroupBy splits, combinations, and custom aggregations.

### 📊 Statistical Visualization with Matplotlib & Seaborn (`matplotlib/`)
* **How it helps your journey**: Essential for plotting training losses, visualizing evaluation metrics (like confusion matrices), and exploring dataset feature correlations.
* **Notebooks**:
  * [1_matplotlib_basics.ipynb](./matplotlib/1_matplotlib_basics.ipynb): Subplots, figures, styles, and the object-oriented plotting interface.
  * [2_seaborn_plots.ipynb](./matplotlib/2_seaborn_plots.ipynb): Statistical distributions, violin plots, and correlation heatmaps.
  * [3_plotly_cufflinks.ipynb](./matplotlib/3_plotly_cufflinks.ipynb): Creating interactive charts for web visualization.
  * [4_ipl_capstone_project.ipynb](./matplotlib/4_ipl_capstone_project.ipynb): An end-to-end exploratory data visualization analysis.

### 📐 Applied Statistics & Testing (`statistics/`)
* **How it helps your journey**: Used to detect outliers in model inputs, analyze distribution shifts (data drift), and run hypothesis tests (e.g., A/B testing a new LLM prompt).
* **Notebooks**:
  * [chi-square.ipynb](./statistics/chi-square.ipynb): Categorical relation testing using Chi-Square.
  * [outliers.ipynb](./statistics/outliers.ipynb): Z-score and IQR-based outlier detection methods.
  * [t-test.ipynb](./statistics/t-test.ipynb): Validating statistical difference between two group means.
  * [z-test.ipynb](./statistics/z-test.ipynb): Testing proportions and means against normal distributions.

---

## 🧠 Phase 2: Classical Machine Learning & Pipelines
*Moving from data processing to building predictive models and end-to-end ML pipelines.*

### 📈 Machine Learning Models & Custom Pipelines (`machine-learning/`, `scikit-learn/`)
* **How it helps your journey**: Writing algorithms from scratch builds deep intuition about optimization and loss calculations. Using Scikit-Learn teaches the `fit`/`transform`/`predict` API structure, which is the backbone of production-ready pipelines.
* **Notebooks**:
  * **Supervised — Regression**:
    * [linear-regression-1.ipynb](./machine-learning/models/supervised/regression/notebooks/linear-regression-1.ipynb): Linear regression implementation from scratch (math derivation & NumPy).
    * [linear-regression-2.ipynb](./machine-learning/models/supervised/regression/notebooks/linear-regression-2.ipynb): Extending scratch linear regression with gradient descent.
    * [simple-linear-regression.ipynb](./machine-learning/models/supervised/regression/notebooks/simple-linear-regression.ipynb): Single variable regression model.
    * [multiple-linear-regression.ipynb](./machine-learning/models/supervised/regression/notebooks/multiple-linear-regression.ipynb): High-dimensional regression modeling.
    * [linear-regression-assumptions.ipynb](./machine-learning/models/supervised/regression/notebooks/linear-regression-assumptions.ipynb): Verifying multicollinearity, homoscedasticity, and normality.
    * [regression-metrics.ipynb](./machine-learning/models/supervised/regression/notebooks/regression-metrics.ipynb): Mathematically computing MAE, MSE, RMSE, and R² scores.
    * [batch-gradient-descent.ipynb](./machine-learning/models/supervised/regression/notebooks/batch-gradient-descent.ipynb): Batch gradient update calculations.
    * [stochastic-gradient-descent.ipynb](./machine-learning/models/supervised/regression/notebooks/stochastic-gradient-descent.ipynb): Stochastic gradient updates.
  * **Supervised — Classification**:
    * [logistic-regression.ipynb](./machine-learning/models/supervised/classification/logistic-regression.ipynb): Binary classification and probability thresholding.
    * [rf_learning_tool.ipynb](./machine-learning/models/supervised/classification/rf_learning_tool.ipynb): Random forest ensembles.
  * **Custom Scikit-Learn Components**:
    * [estimator.ipynb](./scikit-learn/estimator.ipynb): Building custom ML models adhering to the Scikit-Learn API.
    * [transformers.ipynb](./scikit-learn/transformers.ipynb): Creating stateful custom feature transformers (e.g., custom encoders).

### 🧹 Preprocessing & Feature Engineering (`machine-learning/preprocessing/`)
* **How it helps your journey**: Models expect structured, clean numerical vectors. Feature scaling, encoding, and missing value imputation prevent data leakage and ensure model convergence.
* **Notebooks**:
  * **Scaling**: [standard-scaler.ipynb](./machine-learning/preprocessing/scaling/standard-scaler.ipynb) (Z-score normalization) | [min-max-scaler.ipynb](./machine-learning/preprocessing/scaling/min-max-scaler.ipynb) (Bound normalization).
  * **Encoding**: [label-encoding.ipynb](./machine-learning/preprocessing/encoding/label-encoding.ipynb) (Ordinal mapping) | [one-hot-encoding.ipynb](./machine-learning/preprocessing/encoding/one-hot-encoding.ipynb) (Nominal arrays) | [ordinal-encoding.ipynb](./machine-learning/preprocessing/encoding/ordinal-encoding.ipynb) (Custom rank scaling).
  * **Imputation**: [simple-imputer.ipynb](./machine-learning/preprocessing/missing-values/simple-imputer.ipynb) (Mean/median replacements) | [knn-imputer.ipynb](./machine-learning/preprocessing/missing-values/knn-imputer.ipynb) (Nearest neighbor analysis).

### 📥 Data Ingestion Pipelines (`machine-learning/data-ingestion/`)
* **How it helps your journey**: Models consume data from databases, JSON interfaces, or APIs. Setting up memory-efficient chunk loaders prevents Out-Of-Memory (OOM) exceptions.
* **Notebooks**:
  * [working-with-csv.ipynb](./machine-learning/data-ingestion/working-with-csv.ipynb): Chunking, using data converters, and low-memory CSV reading.
  * [working-with-json.ipynb](./machine-learning/data-ingestion/working-with-json.ipynb): Parsing complex, nested JSON objects.
  * [working-with-rest-api.ipynb](./machine-learning/data-ingestion/working-with-rest-api.ipynb): Fetching and parsing HTTP response data in streaming batches.
  * [working-with-sql.ipynb](./machine-learning/data-ingestion/working-with-sql.ipynb): Connecting, querying, and streaming records from relational tables.

### 💼 Production ML Projects (`machine-learning/projects/`)
* **How it helps your journey**: Translating business goals into robust ML systems.
* **Projects**:
  * [ford-car-price-prediction](./machine-learning/projects/ford-car-price-prediction): End-to-end pricing model.
  * [heart-disease-prediction](./machine-learning/projects/heart-disease-prediction): Health risk classifier.
  * [insurance-coverage-prediction](./machine-learning/projects/insurance-coverage-prediction): Cost regression analysis.
  * [reddit-sentimental](./machine-learning/projects/reddit-sentimental): Text analytics and extraction.
  * [document-validation](./machine-learning/projects/document-validation): Hybrid Computer Vision pipeline (detects glare, crops faces, checks blur, and removes background).

---

## 👁️ Phase 3: Deep Learning, PyTorch & Computer Vision
*Transitioning to neural network architectures, custom GPU training loops, and computer vision models.*

### 🔥 PyTorch Core Hub (`pytorch/`)
* **How it helps your journey**: PyTorch is the industry-standard deep learning library. Mastering PyTorch tensor operations, manual backpropagation, custom dataset classes, and training pipelines is essential for writing custom LLM fine-tuning scripts.
* **Notebooks & Projects**:
  * [1_tensors-in-pytorch.ipynb](./pytorch/1_tensors-in-pytorch.ipynb): Creating, manipulating, and computing on GPU with PyTorch tensors.
  * [2_autograd-in-pytorch.ipynb](./pytorch/2_autograd-in-pytorch.ipynb): Visualizing and calculating computation graphs and gradients automatically.
  * [3_pytorch-training-pipeline.ipynb](./pytorch/3_pytorch-training-pipeline.ipynb): Building an optimized custom model training loop.
  * [4_pytorch-nn-module.ipynb](./pytorch/4_pytorch-nn-module.ipynb): Subclassing `nn.Module` to build modular neural network layers.
  * [5_dataset-and-dataloader.ipynb](./pytorch/5_dataset-and-dataloader.ipynb): Building data pipelines with custom classes, batching, and multithreading.
  * [cnn-fashion-mnist-pytorch-gpu.ipynb](./pytorch/cnn-fashion-mnist-pytorch-gpu.ipynb): Harnessing GPU acceleration to train a classification CNN.
  * **PyTorch Projects**:
    * [image_classification](./pytorch/projects/image_classification/image_classification.ipynb): Custom network to classify visual objects.
    * [pytorch_chatbot](./pytorch/projects/pytorch_chatbot/main.py): A custom feed-forward network to parse intent and reply to user inputs.

### 🧠 Neural Architectures (`deep-learning/`, `nlp/`)
* **How it helps your journey**: Core neural network building blocks. Includes convolutional structures (padding, pooling, strides) and sequential architectures (RNNs) for natural language.
* **Notebooks & NLP Tasks**:
  * **CNN Internals**: [keras-padding.ipynb](./deep-learning/cnn/keras-padding.ipynb) (Valid vs Same Padding) | [keras-pooling.ipynb](./deep-learning/cnn/keras-pooling.ipynb) (Max vs Avg Pooling) | [keras-strides.ipynb](./deep-learning/cnn/keras-strides.ipynb) (Downsampling spatial grids).
  * **RNN Internals**: [rnn_architecture.ipynb](./deep-learning/rnn/rnn_architecture.ipynb) (Understanding feedback connections, time steps, and text inputs).
  * **Projects**:
    * [credit-card-customer-churn-prediction.ipynb](./deep-learning/ann/projects/credit-card-customer-churn-prediction/credit-card-customer-churn-prediction.ipynb): Dense Artificial Neural Network (ANN) classifier.
    * [cat-vs-dog.ipynb](./deep-learning/cnn/projects/cat-vs-dog/cat-vs-dog.ipynb): Binary vision classification.
    * [object-classification.ipynb](./deep-learning/cnn/projects/object-classification/object-classification.ipynb): Multi-class vision classification.
  * **Natural Language Processing (`nlp/`)**:
    * [nlp_text_preprocessing.ipynb](./nlp/text-preprocessing/nlp_text_preprocessing.ipynb): Lowercasing, stop-words, regex matching, and tokenization.
    * [nlp_identify_pos_and_names_entities.ipynb](./nlp/identify-pos-and-names-entities/nlp_identify_pos_and_names_entities.ipynb): Extracting Part-of-Speech tags and Named Entities (NER) from unstructured text.
    * [nlp_sentiment_analysis.ipynb](./nlp/sentiment-analysis/nlp_sentiment_analysis.ipynb): Text classification and sentiment evaluation.

### 🖼️ Computer Vision & Real-time Processing (`opencv/`, `yolo/`)
* **How it helps your journey**: Integrating real-world visual feeds into AI applications. Covers image transformation matrices, filtering, gesture tracking, and real-time edge object detection.
* **Notebooks**:
  * **OpenCV Basics**:
    * [basics.ipynb](./opencv/1_opencv_basics.ipynb): Image input/output operations, format grids, and color channels.
    * [transformations.ipynb](./opencv/2_opencv_transformations.ipynb): Resizing, cropping, translation, and rotation math.
    * [processing.ipynb](./opencv/3_opencv_processing.ipynb): Blurring kernels, Sobel/Canny edge detection, and threshold masks.
    * [drawing.ipynb](./opencv/4_opencv_drawing.ipynb): Render layers (bounding boxes, overlays, text annotations).
    * [video.ipynb](./opencv/5_opencv_video.ipynb): Capturing and writing video frames in high performance.
    * [gesture_control.ipynb](./opencv/6_gesture_control.ipynb): Using MediaPipe to track skeletons and trigger keyboard/mouse scripts.
    * [motion_detector.ipynb](./opencv/7_motion_detector.ipynb): Background subtraction and pixel change delta calculations.
  * **YOLO (You Only Look Once)**:
    * [detection.ipynb](./yolo/detection.ipynb): Deploying YOLOv8 pre-trained models to detect classes.
    * [segmentation.ipynb](./yolo/segmentation.ipynb): Real-time semantic instance boundary outlining.

---

## 🤖 Phase 4: Generative AI, LLMs & Stateful Agents
*The cutting edge of AI Engineering: building neural transformers, orchestrating chains, and deploying autonomous agent systems.*

### 🛠️ Building GPT from Scratch (`build-gpt/`)
* **How it helps your journey**: The absolute best way to demystify LLMs is to build one. This module implements a GPT architecture from scratch based on Andrej Karpathy's `nanoGPT` design, teaching self-attention, masking, tokenization, and multi-head scaling.
* **Notebooks**:
  * [gpt-dev.ipynb](./build-gpt/gpt-dev.ipynb): Developing, training, and sampling from a custom character-level Generative Transformer.

### ⛓️ LangChain LLM Orchestration (`lang-chain/`)
* **How it helps your journey**: Core framework for constructing LLM applications. Learn retrieval architectures, vector embedding caches, custom tools, and the LangChain Expression Language (LCEL).
* **Modules & Projects**:
  * **Core Modules**:
    * [chat_models](./lang-chain/chat_models): Standardizing API integration (OpenAI, HuggingFace, local Ollama).
    * [embedding_models](./lang-chain/embedding_models): Mapping text to mathematical vector embeddings.
    * [document_loader](./lang-chain/document_loader): Parsers for PDFs, plain text, and online web pages.
    * [retrievers](./lang-chain/retrievers): Smart search (Arxiv integrations, MMR, and Multi-query expansions).
    * [text_splitter](./lang-chain/text_splitter): Managing document chunking boundaries to respect tokens.
    * [tools](./lang-chain/tools): Exposing backend scripts/APIs as executable tools to an LLM.
    * [runnable](./lang-chain/runnable): Designing declaratively chained pipelines using LCEL.
    * [vector_store](./lang-chain/vector_store): Storing and retrieving vector indices.
  * **Projects**:
    * [cine-sage](./lang-chain/projects/cine-sage): Structured movie metadata extractor utilizing OpenAI schema extraction.
    * [chatbot](./lang-chain/projects/chatbot): FastAPI chatbot integrating a vector store index and streaming responses.
    * [session-based-chatbot](./lang-chain/projects/session-based-chatbot): Chatbot managing multiple user sessions and memory caches.

### 🕸️ LangGraph Multi-Agent Workflows (`lang-graph/`)
* **How it helps your journey**: While linear chains are great, production LLM systems require loops, conditional logic, human approvals, and collaborative agent structures. LangGraph models workflows as stateful, cyclic graphs.
* **Notebooks**:
  * **Workflows**:
    * [1_state_graph_basics.ipynb](./lang-graph/workflows/1_state_graph_basics.ipynb): Nodes, edges, and state transition fundamentals.
    * [2_llm_node_integration.ipynb](./lang-graph/workflows/2_llm_node_integration.ipynb): Modifying graph states using LLM node updates.
    * [3_prompt_chaining.ipynb](./lang-graph/workflows/3_prompt_chaining.ipynb): Sequencing LLM nodes for multi-step reasoning.
    * [4_parallel_nodes.ipynb](./lang-graph/workflows/4_parallel_nodes.ipynb): Distributing operations in parallel nodes.
    * [5_structured_output.ipynb](./lang-graph/workflows/5_structured_output.ipynb): Enforcing Pydantic schemas on LangGraph node exits.
    * [6_conditional_edges.ipynb](./lang-graph/workflows/6_conditional_edges.ipynb): Dynamic routing decisions based on output parsing.
    * [7_review_reply_workflow.ipynb](./lang-graph/workflows/7_review_reply_workflow.ipynb): Multi-stage customer review generation workflow.
  * **Stateful Chatbots**:
    * [1_basic_chatbot.ipynb](./lang-graph/chatbot/1_basic_chatbot.ipynb): Basic chat graph loop.
    * [2_chatbot_persistence.ipynb](./lang-graph/chatbot/2_chatbot_persistence.ipynb): Graph memory checkpoints.
    * [3_chatbot_stream.ipynb](./lang-graph/chatbot/3_chatbot_stream.ipynb): Streaming state updates node-by-node.
    * [4_chatbot_tools.ipynb](./lang-graph/chatbot/4_chatbot_tools.ipynb): Exposing client-side tools to the graph.
    * [5_chatbot_mcp.ipynb](./lang-graph/chatbot/5_chatbot_mcp.ipynb): Connecting to Model Context Protocol (MCP) servers.
    * [6_chatbot_sqlite.ipynb](./lang-graph/chatbot/6_chatbot_sqlite.ipynb): Saving graph histories in an external SQL database.
    * [7_chatbot_observibility.ipynb](./lang-graph/chatbot/7_chatbot_observibility.ipynb): Tracing node performance and prompt tokens.
    * [8_chatbot_rag.ipynb](./lang-graph/chatbot/8_chatbot_rag.ipynb): Graph-based Retrieval-Augmented Generation (RAG).
    * [9_chatbot_hitl.ipynb](./lang-graph/chatbot/9_chatbot_hitl.ipynb): Implementing human verification and manual override states (Human-In-The-Loop).
    * [10_chatbot_stm_trimming.ipynb](./lang-graph/chatbot/10_chatbot_stm_trimming.ipynb): Trimming old messages to preserve token context windows.
    * [11_chatbot_stm_deletion.ipynb](./lang-graph/chatbot/11_chatbot_stm_deletion.ipynb): Deleting obsolete context states.
    * [12_chatbot_stm_summary.ipynb](./lang-graph/chatbot/12_chatbot_stm_summary.ipynb): Summarizing historical context dynamically.

---

## ⚙️ Phase 5: Production Deployment & MLOps
*Transforming prototypes into production-grade systems: scaling, validation, serving, and automation.*

### 🛡️ Pydantic Data Validation (`pydantic/`)
* **How it helps your journey**: Production APIs cannot trust raw JSON payloads. Pydantic validates input schemas, forces type hints, handles custom validations, and ensures consistent outputs from structured LLM calls.
* **Notebooks**:
  * [basics.ipynb](./pydantic/basics.ipynb): Model definitions, Field configurations, and type requirements.
  * [field_validators.ipynb](./pydantic/field_validators.ipynb): Creating custom input filters (e.g., matching character sets).
  * [model_validators.ipynb](./pydantic/model_validators.ipynb): Validating multiple fields at once (e.g., comparing field combinations).
  * [computed_fields.ipynb](./pydantic/computed_fields.ipynb): Dynamically generating derived properties.
  * [nested_models.ipynb](./pydantic/nested_models.ipynb): Building complex database schemas.
  * [serialization.ipynb](./pydantic/serialization.ipynb): Exporting validated structures into JSONs.

### 🌐 FastAPI Production Applications (`fastapi/`)
* **How it helps your journey**: FastAPI is the go-to web framework for ML models and LLMs due to its asynchronous runtime, fast performance, and built-in OpenAPI integration.
* **Architecture (`fastapi/`)**:
  * [app/main.py](./fastapi/app/main.py): Async server start, middleware registration, and routes.
  * [app/core/](./fastapi/app/core): Environment settings and async SQLAlchemy engine configuration.
  * [app/models/](./fastapi/app/models): Database schema models mapping directly to relational databases.
  * [app/schemas/](./fastapi/app/schemas): Request and response models.
  * [app/crud/](./fastapi/app/crud): Encapsulated database queries.
  * [app/api/](./fastapi/app/api): Clean modular routes.
  * [alembic/](./fastapi/alembic): Generating and executing SQL schema migration files.

### 🐳 MLOps & Pipeline Orchestration (`mlops/`)
* **How it helps your journey**: Moving models from notebooks to automated systems. Covers orchestrating data dependencies and containerizing applications.
* **Modules & Projects**:
  * [zen_pipeline.ipynb](./mlops/zenml/zen_pipeline.ipynb): Orchestrating end-to-end training and deployment tasks using ZenML.
  * [dogs-vs-cats](./mlops/projects/dogs-vs-cats): Packaging a Keras CNN model into a Docker container and serving it via a Streamlit web interface.

---

## 📚 The AI Engineer's Bookshelf (`resources/`)
Supplement your notebook sandbox with a curated collection of industry-leading ebooks stored in `resources/eBooks/`.

| Book | Focus Area | Key Takeaway |
| :--- | :--- | :--- |
| **[AI Engineering](./resources/eBooks/AI%20Engineering.pdf)** by Chip Huyen | AI Systems | Building and deploying real-time AI applications at scale. |
| **[Designing ML Systems](./resources/eBooks/Designing%20Machine%20Learning%20Systems.pdf)** by Chip Huyen | Architecture | Data flow design, model updates, drift detection, and monitoring. |
| **[Deep Learning](./resources/eBooks/Deep%20Learning%20by%20Ian%20Goodfellow%2C%20Yoshua%20Bengio%2C%20Aaron%20Courville.pdf)** | Math & Foundations | The theoretical foundation for deep neural networks. |
| **[Hands-On Machine Learning](./resources/eBooks/Hands-On%20Machine%20Learning%20with%20Scikit-Learn%2C%20Keras%2C%20and%20TensorFlow.pdf)** | ML Implementations | Pratical machine learning modeling from classical to deep networks. |
| **[Hands-On Large Language Models](./resources/eBooks/Hands-On%20Large%20Language%20Models.pdf)** | Modern GenAI | Fine-tuning, prompt engineering, and building apps using transformers. |
| **[LLM Engineers Handbook](./resources/eBooks/LLM%20Engineers%20Handbook.pdf)** | Advanced LLMOps | Production patterns for RAG, optimization, and deploying LLMs. |
| **[Generative Deep Learning](./resources/eBooks/Generative-Deep-Learning.pdf)** | Generative AI | Implementing VAEs, GANs, Diffusion models, and GPTs. |
| **[NLP with Transformers](./resources/eBooks/NLP%20with%20Transformer%20models.pdf)** | Transformer Models | Deep-dive on BERT, GPT, and custom tokenizers. |
| **[Mathematics for Machine Learning](./resources/eBooks/Mathematics%20for%20Machine%20Learning.pdf)** | Math Foundations | Linear algebra, calculus, probability, and optimization math. |

---

## 🚀 Sandbox Setup & Installation

Follow these instructions to set up your local development environment:

### Prerequisites
- Python 3.10+
- CUDA-compatible GPU (optional, for accelerated deep learning notebooks)

### 1. Clone & Set Up Environment
```bash
# Clone the repository
git clone https://github.com/ksbisht941/ai-engineer.git
cd ai-engineer

# Create a python virtual environment
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

### 2. Install Core Dependencies
```bash
pip install --upgrade pip
pip install ipykernel numpy pandas matplotlib seaborn scikit-learn
```
For deep learning, PyTorch, and OpenCV dependencies, refer to specific installation commands inside their respective notebooks or use:
```bash
pip install torch torchvision torchaudio opencv-python ultralytics pydantic fastapi langchain langgraph zenml
```

### 3. Open in VS Code & Run Notebooks
1. Open this repository directory in VS Code.
2. Open any `.ipynb` file.
3. Click on **Select Kernel** in the top right corner.
4. Select the `.venv` environment from your list.

---

## 🤝 Contributing
This hub is open-source! We welcome contributions that add:
- New notebooks exploring cutting-edge AI architectures.
- Clean implementations of classical ML algorithms from scratch.
- Detailed agentic workflows or production templates.
- Typo corrections or code optimization PRs.

To contribute, fork the repository, make your changes in a feature branch, and submit a Pull Request. Let's build the ultimate AI Engineering roadmap together!
