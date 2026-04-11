# AI Engineer

This repository contains various projects, notebooks, and resources for AI and Machine Learning engineering. It covers foundational libraries, Natural Language Processing (NLP), and Generative AI.

## Project Structure

The project is organized into the following modules:

- **[python](./python)**: Foundations of Python programming.

  | Notebook | Description |
  | :--- | :--- |
  | [basics.ipynb](./python/1_python_basics.ipynb) | Print, data types, variables, and literals. |
  | [operators_loops.ipynb](./python/2_python_operators_loops.ipynb) | Operators, if-else, modules, and loops. |
  | [loops_strings.ipynb](./python/3_python_loops_strings.ipynb) | Advanced loops and string manipulation. |
  | [time_complexity.ipynb](./python/4_time_complexity.ipynb) | Efficiency, Big O, and examples. |
  | [lists.ipynb](./python/5_python_lists.ipynb) | Memory management, methods, and comprehensions. |
  | [tuples_sets_dicts.ipynb](./python/6_python_tuples_sets_dicts.ipynb) | Immutability of tuples, unique sets, and key-value dictionaries. |
  | [functions.ipynb](./python/7_python_functions.ipynb) | Creation, scope, closures, and functional programming. |
  | [oop_part1.ipynb](./python/8_python_oop_part1.ipynb) | Classes, objects, 'self', and dunder methods. |
  | [oop_part2.ipynb](./python/9_python_oop_part2.ipynb) | Encapsulation, static members, and reference variables. |
  | [oop_part3.ipynb](./python/10_python_oop_part3.ipynb) | Aggregation, inheritance types, MRO, polymorphism, and abstraction. |
  | [exception_handling.ipynb](./python/11_python_exception_handling.ipynb) | Robust error management with try-except. |
  | [decorators.ipynb](./python/12_python_decorators.ipynb) | Function wrapping and LEGB scope rules. |
  | [iterators.ipynb](./python/13_python_iterators.ipynb) | Traversal protocols and custom iteration logic. |
  | [generators.ipynb](./python/14_python_generators.ipynb) | Memory-efficient data processing with yield. |

- **[numpy](./numpy)**: Fundamental numerical computing with NumPy.

  | Notebook | Description |
  | :--- | :--- |
  | [basics.ipynb](./numpy/1_numpy_basics.ipynb) | Basics, random generation, attributes. |
  | [indexing_slicing.ipynb](./numpy/2_numpy_indexing_slicing.ipynb) | Reshaping, indexing, and slicing. |
  | [operations.ipynb](./numpy/3_numpy_operations.ipynb) | Element-wise and advanced operations. |
  | [exercises.ipynb](./numpy/4_numpy_exercises.ipynb) | Practice problems and exercises. |

- **[pandas](./pandas)**: Data manipulation and analysis using Pandas.

  | Notebook | Description |
  | :--- | :--- |
  | [basics.ipynb](./pandas/1_pandas_basics.ipynb) | Series and DataFrame basics. |
  | [selection_indexing.ipynb](./pandas/2_pandas_selection_indexing.ipynb) | Data selection, indexing, and slicing. |
  | [missing_data.ipynb](./pandas/3_pandas_missing_data.ipynb) | Handling and cleaning missing data. |
  | [combining_data.ipynb](./pandas/4_pandas_combining_data.ipynb) | Merging, Joining, and Concatenating DataFrames. |
  | [grouping_aggregating.ipynb](./pandas/5_pandas_grouping_aggregating.ipynb) | GroupBy operations and aggregations. |

- **[matplotlib](./matplotlib)**: Data visualization techniques using Matplotlib and Seaborn.

  | Notebook | Description |
  | :--- | :--- |
  | [basics.ipynb](./matplotlib/1_matplotlib_basics.ipynb) | Matplotlib basics and object-oriented interface. |
  | [seaborn_plots.ipynb](./matplotlib/2_seaborn_plots.ipynb) | Statistical visualizations with Seaborn. |
  | [plotly_cufflinks.ipynb](./matplotlib/3_plotly_cufflinks.ipynb) | Interactive charts with Plotly and Cufflinks. |
  | [ipl_capstone_project.ipynb](./matplotlib/4_ipl_capstone_project.ipynb) | Data visualization project on IPL dataset. |

- **[statistics](./statistics)**: Statistical hypothesis testing and outlier detection.

  | Notebook | Description |
  | :--- | :--- |
  | [central-tendency.ipynb](./statistics/central-tendency.ipynb) | Mean, median, and mode implementation. |
  | [chi-square.ipynb](./statistics/chi-square.ipynb) | Chi-Square test implementation. |
  | [outliers.ipynb](./statistics/outliers.ipynb) | Outlier detection techniques. |
  | [t-test.ipynb](./statistics/t-test.ipynb) | T-Test implementation. |
  | [z-test.ipynb](./statistics/z-test.ipynb) | Z-Test implementation. |

- **[machine-learning](./machine-learning)**: Practical machine learning modules covering supervised, unsupervised, reinforcement learning, preprocessing, and end-to-end projects.

  **Supervised — Regression**

  | Notebook | Description |
  | :--- | :--- |
  | [simple-linear-regression.ipynb](./machine-learning/models/supervised/regression/simple-linear-regression.ipynb) | Simple Linear Regression from scratch. |
  | [multiple-linear-regression.ipynb](./machine-learning/models/supervised/regression/) | Multiple Linear Regression. |
  | [ridge-regression.ipynb](./machine-learning/models/supervised/regression/ridge-regression.ipynb) | L2 regularization with Ridge Regression. |
  | [lasso-regression.ipynb](./machine-learning/models/supervised/regression/lasso-regression.ipynb) | L1 regularization with Lasso Regression. |
  | [elastic-net.ipynb](./machine-learning/models/supervised/regression/elastic-net.ipynb) | Combined L1+L2 regularization. |
  | [svr.ipynb](./machine-learning/models/supervised/regression/svr.ipynb) | Support Vector Regression. |

  **Supervised — Classification**

  | Notebook | Description |
  | :--- | :--- |
  | [logistic-regression.ipynb](./machine-learning/models/supervised/classification/logistic-regression.ipynb) | Logistic Regression classifier. |
  | [decision-tree.ipynb](./machine-learning/models/supervised/classification/decision-tree.ipynb) | Decision Tree classifier. |
  | [knn.ipynb](./machine-learning/models/supervised/classification/knn.ipynb) | K-Nearest Neighbors classifier. |
  | [naive-bayes.ipynb](./machine-learning/models/supervised/classification/naive-bayes.ipynb) | Naive Bayes classifier. |
  | [random-forest.ipynb](./machine-learning/models/supervised/classification/random-forest.ipynb) | Random Forest classifier. |
  | [svm.ipynb](./machine-learning/models/supervised/classification/svm.ipynb) | Support Vector Machine classifier. |
  | [mlp-classifier.ipynb](./machine-learning/models/supervised/classification/mlp-classifier.ipynb) | Multi-layer Perceptron classifier. |

  **Unsupervised**

  | Notebook | Description |
  | :--- | :--- |
  | [kmeans.ipynb](./machine-learning/models/unsupervised/clustering/kmeans.ipynb) | K-Means clustering. |
  | [dbscan.ipynb](./machine-learning/models/unsupervised/clustering/dbscan.ipynb) | Density-based spatial clustering. |
  | [gmm.ipynb](./machine-learning/models/unsupervised/clustering/gmm.ipynb) | Gaussian Mixture Model clustering. |
  | [hierarchical.ipynb](./machine-learning/models/unsupervised/clustering/hierarchical.ipynb) | Hierarchical/agglomerative clustering. |
  | [pca.ipynb](./machine-learning/models/unsupervised/dimensionality-reduction/pca.ipynb) | Principal Component Analysis. |
  | [tsne.ipynb](./machine-learning/models/unsupervised/dimensionality-reduction/tsne.ipynb) | t-SNE dimensionality reduction. |
  | [umap.ipynb](./machine-learning/models/unsupervised/dimensionality-reduction/umap.ipynb) | UMAP dimensionality reduction. |
  | [isolation-forest.ipynb](./machine-learning/models/unsupervised/anomaly-detection/isolation-forest.ipynb) | Isolation Forest anomaly detection. |
  | [one-class-svm.ipynb](./machine-learning/models/unsupervised/anomaly-detection/one-class-svm.ipynb) | One-Class SVM anomaly detection. |

  **Semi-Supervised**

  | Notebook | Description |
  | :--- | :--- |
  | [self-training.ipynb](./machine-learning/models/semi-supervised/self-training.ipynb) | Self-training with labeled + unlabeled data. |
  | [label-propagation.ipynb](./machine-learning/models/semi-supervised/label-propagation.ipynb) | Graph-based label propagation. |
  | [label-spreading.ipynb](./machine-learning/models/semi-supervised/label-spreading.ipynb) | Regularized label spreading algorithm. |

  **Ensemble Methods**

  | Notebook | Description |
  | :--- | :--- |
  | [bagging.ipynb](./machine-learning/models/ensemble/bagging.ipynb) | Bagging ensemble method. |
  | [boosting](./machine-learning/models/ensemble/boosting/) | Boosting ensemble methods (AdaBoost, Gradient Boosting, XGBoost). |
  | [stacking.ipynb](./machine-learning/models/ensemble/stacking.ipynb) | Stacking ensemble method. |
  | [voting.ipynb](./machine-learning/models/ensemble/voting.ipynb) | Voting ensemble method. |

  **Deep Learning Models**

  | Notebook | Description |
  | :--- | :--- |
  | [ann.ipynb](./machine-learning/models/deep-learning/ann.ipynb) | Artificial Neural Network. |
  | [cnn.ipynb](./machine-learning/models/deep-learning/cnn.ipynb) | Convolutional Neural Network. |
  | [rnn.ipynb](./machine-learning/models/deep-learning/rnn.ipynb) | Recurrent Neural Network. |
  | [lstm.ipynb](./machine-learning/models/deep-learning/lstm.ipynb) | Long Short-Term Memory network. |
  | [gru.ipynb](./machine-learning/models/deep-learning/gru.ipynb) | Gated Recurrent Unit. |
  | [transformers.ipynb](./machine-learning/models/deep-learning/transformers.ipynb) | Transformer architecture. |

  **Reinforcement Learning**

  | Notebook | Description |
  | :--- | :--- |
  | [q-learning.ipynb](./machine-learning/models/reinforcement-learning/q-learning.ipynb) | Q-Learning algorithm. |
  | [sarsa.ipynb](./machine-learning/models/reinforcement-learning/sarsa.ipynb) | SARSA on-policy TD control. |
  | [dqn.ipynb](./machine-learning/models/reinforcement-learning/dqn.ipynb) | Deep Q-Network. |
  | [policy-gradient.ipynb](./machine-learning/models/reinforcement-learning/policy-gradient.ipynb) | Policy Gradient methods. |
  | [actor-critic.ipynb](./machine-learning/models/reinforcement-learning/actor-critic.ipynb) | Actor-Critic architecture. |

  **Preprocessing**

  | Module | Notebook | Description |
  | :--- | :--- | :--- |
  | **Scaling** | [standard-scaler.ipynb](./machine-learning/preprocessing/scaling/standard-scaler.ipynb) | Standardization using `StandardScaler`. |
  |             | [min-max-scaler.ipynb](./machine-learning/preprocessing/scaling/min-max-scaler.ipynb) | Normalization using `MinMaxScaler`. |
  |             | [robust-scaler.ipynb](./machine-learning/preprocessing/scaling/robust-scaler.ipynb) | Outlier-robust scaling using `RobustScaler`. |
  | **Encoding** | [label-encoding.ipynb](./machine-learning/preprocessing/encoding/label-encoding.ipynb) | Label Encoding for ordinal categories. |
  |              | [one-hot-encoding.ipynb](./machine-learning/preprocessing/encoding/one-hot-encoding.ipynb) | One-Hot Encoding for nominal categories. |
  |              | [ordinal-encoding.ipynb](./machine-learning/preprocessing/encoding/ordinal-encoding.ipynb) | Ordinal Encoding with custom order. |
  |              | [target-encoding.ipynb](./machine-learning/preprocessing/encoding/target-encoding.ipynb) | Target/Mean Encoding. |
  | **Missing Values** | [simple-imputer.ipynb](./machine-learning/preprocessing/missing-values/simple-imputer.ipynb) | Imputation with mean/median/mode. |
  |                    | [knn-imputer.ipynb](./machine-learning/preprocessing/missing-values/knn-imputer.ipynb) | KNN-based imputation. |
  | **Transformation** | [log-transform.ipynb](./machine-learning/preprocessing/transformation/log-transform.ipynb) | Log transformation for skewed data. |
  |                    | [power-transform.ipynb](./machine-learning/preprocessing/transformation/power-transform.ipynb) | Box-Cox and Yeo-Johnson transforms. |
  |                    | [binning.ipynb](./machine-learning/preprocessing/transformation/binning.ipynb) | Discretization and binning. |
  | **Feature Creation** | [date-features.ipynb](./machine-learning/preprocessing/feature-creation/date-features.ipynb) | Extracting date/time features. |
  |                      | [interaction-features.ipynb](./machine-learning/preprocessing/feature-creation/interaction-features.ipynb) | Creating interaction features. |
  |                      | [domain-features.ipynb](./machine-learning/preprocessing/feature-creation/domain-features.ipynb) | Domain-specific feature engineering. |
  | **Feature Selection** | [correlation.ipynb](./machine-learning/preprocessing/feature-selection/correlation.ipynb) | Correlation-based feature selection. |
  |                       | [chi-square.ipynb](./machine-learning/preprocessing/feature-selection/chi-square.ipynb) | Chi-Square statistical feature selection. |
  |                       | [feature-importance.ipynb](./machine-learning/preprocessing/feature-selection/feature-importance.ipynb) | Tree-based feature importance. |
  |                       | [rfe.ipynb](./machine-learning/preprocessing/feature-selection/rfe.ipynb) | Recursive Feature Elimination. |
  | **Pipelines** | [sklearn-pipeline.ipynb](./machine-learning/preprocessing/pipelines/sklearn-pipeline.ipynb) | Building scikit-learn Pipelines. |
  |               | [end-to-end-preprocessing.ipynb](./machine-learning/preprocessing/pipelines/end-to-end-preprocessing.ipynb) | Full preprocessing pipeline. |

  **Data Ingestion & Vision**

  | Notebook | Description |
  | :--- | :--- |
  | [rest-api.ipynb](./machine-learning/data-ingestion/rest-api.ipynb) | Fetching data from REST APIs for ML pipelines. |
  | [graphql.ipynb](./machine-learning/data-ingestion/graphql.ipynb) | Fetching data from GraphQL APIs for ML pipelines. |
  | [cnn.ipynb](./machine-learning/vision/cnn.ipynb) | CNN-based image classification workflow. |

  **Projects**

  | Project | Description |
  | :--- | :--- |
  | [ford-car-price-prediction](./machine-learning/projects/ford-car-price-prediction) | Predicting car prices based on features. |
  | [heart-disease-prediction](./machine-learning/projects/heart-disease-prediction) | Classification of heart disease risk. |
  | [insurance-coverage-prediction](./machine-learning/projects/insurance-coverage-prediction) | Predicting insurance coverage costs. |
  | [document-validation](./machine-learning/projects/document-validation) | Computer-vision pipeline for portrait photo validation (glare detection, face crop, blur check, background removal). |


- **[deep-learning](./deep-learning)**: Deep learning modules covering Convolutional Neural Networks and related techniques.

  | Module | Notebook | Description |
  | :--- | :--- | :--- |
  | **CNN** | [keras-padding.ipynb](./deep-learning/cnn/keras-padding.ipynb) | Exploring `valid` vs `same` padding in Conv2D layers on MNIST. |
  |         | [keras-pooling.ipynb](./deep-learning/cnn/keras-pooling.ipynb) | Pooling strategies (Max, Average) for spatial downsampling. |
  |         | [keras-strides.ipynb](./deep-learning/cnn/keras-strides.ipynb) | Effect of strides on feature map dimensions. |
  | **ANN Projects** | [credit-card-customer-churn-prediction.ipynb](./deep-learning/ann/projects/credit-card-customer-churn-prediction/credit-card-customer-churn-prediction.ipynb) | Customer churn prediction using ANN. |
  | **CNN Projects** | [cat-vs-dog.ipynb](./deep-learning/cnn/projects/cat-vs-dog/cat-vs-dog.ipynb) | Binary image classification using CNN. |
  |                  | [object-detection.ipynb](./deep-learning/cnn/projects/object-detection-yolo/object-detection.ipynb) | Object detection using YOLO. |

- **[scikit-learn](./scikit-learn)**: Scikit-learn estimator and transformer patterns.

  | Notebook | Description |
  | :--- | :--- |
  | [estimator.ipynb](./scikit-learn/estimator.ipynb) | Building and using scikit-learn estimators. |
  | [transformers.ipynb](./scikit-learn/transformers.ipynb) | Building and using scikit-learn transformers. |

- **[nlp](./nlp)**: Comprehensive NLP modules covering text processing and analysis.

  | Module | Notebook | Description |
  | :--- | :--- | :--- |
  | **Text Preprocessing** | [nlp_text_preprocessing.ipynb](./nlp/text-preprocessing/nlp_text_preprocessing.ipynb) | Lowercasing, stop words, regex, and tokenization. |
  |                        | [practice.ipynb](./nlp/text-preprocessing/practice.ipynb) | Practice exercises for text preprocessing. |
  | **POS & NER** | [nlp_identify_pos_and_names_entities.ipynb](./nlp/identify-pos-and-names-entities/nlp_identify_pos_and_names_entities.ipynb) | Parts-of-speech tagging and Named Entity Recognition. |
  | **Sentiment Analysis** | [nlp_sentiment_analysis.ipynb](./nlp/sentiment-analysis/nlp_sentiment_analysis.ipynb) | Analyzing text sentiment and emotions. |

- **[opencv](./opencv)**: Computer vision and image processing with OpenCV.

  | Notebook | Description |
  | :--- | :--- |
  | [basics.ipynb](./opencv/1_opencv_basics.ipynb) | Installation and basic image I/O. |
  | [transformations.ipynb](./opencv/2_opencv_transformations.ipynb) | Resizing, cropping, rotation, and flipping. |
  | [processing.ipynb](./opencv/3_opencv_processing.ipynb) | Blurring, edge detection, and thresholding. |
  | [drawing.ipynb](./opencv/4_opencv_drawing.ipynb) | Drawing shapes (lines, rectangles, circles) and text. |
  | [video.ipynb](./opencv/5_opencv_video.ipynb) | Video capture and processing basics. |
  | [gesture_control.ipynb](./opencv/6_gesture_control.ipynb) | Hand gesture control using MediaPipe. |
  | [motion_detector.ipynb](./opencv/7_motion_detector.ipynb) | Real-time motion detection implementation. |

  *Resources: [input_img](./opencv/input_img), [output_img](./opencv/output_img), [output_video](./opencv/output_video).*

- **[lang-chain](./lang-chain)**: A comprehensive collection of Generative AI modules and projects.

  | Category | Module / Project | Description |
  | :--- | :--- | :--- |
  | **Core** | [chat_models](./lang-chain/chat_models) | Various LLM chat implementations (OpenAI, HuggingFace, Local). |
  |          | [embedding_models](./lang-chain/embedding_models) | Vector embedding generation and management. |
  |          | [document_loader](./lang-chain/document_loader) | Loaders for PDF, Text, and Web content. |
  |          | [retrievers](./lang-chain/retrievers) | Advanced retrieval techniques (Arxiv, MMR, Multi-query). |
  |          | [text_splitter](./lang-chain/text_splitter) | Document chunking strategies. |
  |          | [tools](./lang-chain/tools) | Custom tool definitions for agentic workflows. |
  |          | [runnable](./lang-chain/runnable) | LangChain Expression Language (LCEL) and runnable components. |
  |          | [vector_store](./lang-chain/vector_store) | Vector database integration. |
  | **Projects** | [cine-sage](./lang-chain/projects/cine-sage) | Structured movie metadata extraction. |
  |              | [chatbot](./lang-chain/projects/chatbot) | FastAPI-based chatbot with vector database and streaming API. |
  |              | [session-based-chatbot](./lang-chain/projects/session-based-chatbot) | Session-aware chatbot with memory management. |

- **[lang-graph](./lang-graph)**: Interactive agentic workflows and chatbots using LangGraph.

  **Workflows**

  | Notebook | Description |
  | :--- | :--- |
  | [state_graph_basics.ipynb](./lang-graph/workflows/1_state_graph_basics.ipynb) | StateGraph fundamentals and node/edge setup. |
  | [llm_node_integration.ipynb](./lang-graph/workflows/2_llm_node_integration.ipynb) | Integrating LLM nodes into a graph workflow. |
  | [prompt_chaining.ipynb](./lang-graph/workflows/3_prompt_chaining.ipynb) | Advanced prompt chaining techniques for complex tasks. |
  | [parallel_nodes.ipynb](./lang-graph/workflows/4_parallel_nodes.ipynb) | Running multiple nodes in parallel within a graph. |
  | [structured_output.ipynb](./lang-graph/workflows/5_structured_output.ipynb) | Extracting structured outputs from LLM nodes. |
  | [conditional_edges.ipynb](./lang-graph/workflows/6_conditional_edges.ipynb) | Dynamic routing using conditional edges. |
  | [review_reply_workflow.ipynb](./lang-graph/workflows/7_review_reply_workflow.ipynb) | Automated customer review response generation. |

  **Chatbot**

  | Notebook | Description |
  | :--- | :--- |
  | [basic_chatbot.ipynb](./lang-graph/chatbot/1_basic_chatbot.ipynb) | Basic chatbot implementation using LangGraph. |
  | [chatbot_persistence.ipynb](./lang-graph/chatbot/2_chatbot_persistence.ipynb) | Chatbot with memory persistence across turns. |
  | [chatbot_stream.ipynb](./lang-graph/chatbot/3_chatbot_stream.ipynb) | Streaming responses in a LangGraph chatbot. |
  | [chatbot_tools.ipynb](./lang-graph/chatbot/4_chatbot_tools.ipynb) | Tool-augmented chatbot with agentic capabilities. |
  | [chatbot_mcp.ipynb](./lang-graph/chatbot/5_chatbot_mcp.ipynb) | Chatbot using Model Context Protocol (MCP). |
  | [chatbot_sqlite.ipynb](./lang-graph/chatbot/6_chatbot_sqlite.ipynb) | Chatbot with SQLite-based persistent memory. |
  | [chatbot_observability.ipynb](./lang-graph/chatbot/7_chatbot_observibility.ipynb) | Observability and tracing in LangGraph chatbots. |
  | [chatbot_rag.ipynb](./lang-graph/chatbot/8_chatbot_rag.ipynb) | Retrieval-Augmented Generation (RAG) chatbot. |
  | [chatbot_hitl.ipynb](./lang-graph/chatbot/9_chatbot_hitl.ipynb) | Human-in-the-loop (HITL) chatbot with approval steps. |


- **[yolo](./yolo)**: Object detection and instance segmentation using YOLO models.

  | Notebook | Description |
  | :--- | :--- |
  | [detection.ipynb](./yolo/detection.ipynb) | Object detection using YOLOv8. |
  | [segmentation.ipynb](./yolo/segmentation.ipynb) | Instance segmentation using YOLOv8. |

- **[fastapi](./fastapi)**: Production-grade FastAPI application with async database, migrations, and layered architecture.

  | Module | Description |
  | :--- | :--- |
  | [app/main.py](./fastapi/app/main.py) | Application entry point. |
  | [app/core/](./fastapi/app/core) | Env-based config (`pydantic-settings`) and async SQLAlchemy engine/session. |
  | [app/models/](./fastapi/app/models) | SQLAlchemy database models. |
  | [app/schemas/](./fastapi/app/schemas) | Pydantic validation schemas. |
  | [app/crud/](./fastapi/app/crud) | Async CRUD operations. |
  | [app/api/](./fastapi/app/api) | API router and endpoints. |
  | [alembic/](./fastapi/alembic) | Database migration scripts. |

- **[pydantic](./pydantic)**: Data validation and settings management using Pydantic v2.

  | Notebook | Description |
  | :--- | :--- |
  | [basics.ipynb](./pydantic/basics.ipynb) | BaseModel, Field, Annotated, type constraints, and Optional fields. |
  | [field_validators.ipynb](./pydantic/field_validators.ipynb) | Field-level validation with `@field_validator` (name transformation, age range). |
  | [model_validators.ipynb](./pydantic/model_validators.ipynb) | Cross-field validation with `@model_validator` and nested models. |
  | [computed_fields.ipynb](./pydantic/computed_fields.ipynb) | Derived fields using `@computed_field` and `@property` (BMI calculation). |
  | [nested_models.ipynb](./pydantic/nested_models.ipynb) | Composing nested Pydantic models (ContactDetails, AddressDetails). |
  | [serialization.ipynb](./pydantic/serialization.ipynb) | Serialization with `model_dump()` and `model_dump_json()` (include, exclude, exclude_unset). |

- **[mlops](./mlops)**: MLOps workflows and pipeline orchestration.

  | Notebook | Description |
  | :--- | :--- |
  | [zen_pipeline.ipynb](./mlops/zenml/zen_pipeline.ipynb) | End-to-end ML pipeline orchestration using ZenML. |

- **[resources](./resources)**: Reference materials and eBooks.

  | Resource | Description |
  | :--- | :--- |
  | [AI Engineering](./resources/eBooks/AI%20Engineering.pdf) | AI Engineering by Chip Huyen. |
  | [Deep Learning](./resources/eBooks/Deep%20Learning%20by%20Ian%20Goodfellow%2C%20Yoshua%20Bengio%2C%20Aaron%20Courville.pdf) | Deep Learning by Goodfellow, Bengio & Courville. |
  | [Hands-On ML (Scikit-Learn, Keras, TF)](./resources/eBooks/Hands-On%20Machine%20Learning%20with%20Scikit-Learn%2C%20Keras%2C%20and%20TensorFlow.pdf) | Hands-On Machine Learning by Aurélien Géron. |
  | [Hands-On LLMs](./resources/eBooks/Hands-On%20Large%20Language%20Models.pdf) | Hands-On Large Language Models. |
  | [LLM Engineers Handbook](./resources/eBooks/LLM%20Engineers%20Handbook.pdf) | LLM Engineers Handbook. |
  | [Designing ML Systems](./resources/eBooks/Designing%20Machine%20Learning%20Systems.pdf) | Designing Machine Learning Systems by Chip Huyen. |
  | [Generative Deep Learning](./resources/eBooks/Generative-Deep-Learning.pdf) | Generative Deep Learning by David Foster. |
  | [NLP with Transformers](./resources/eBooks/NLP%20with%20Transformer%20models.pdf) | Natural Language Processing with Transformers. |
  | [Mathematics for ML](./resources/eBooks/Mathematics%20for%20Machine%20Learning.pdf) | Mathematics for Machine Learning. |
  | [And more...](./resources/eBooks) | 25 eBooks covering ML, DL, MLOps, and Generative AI. |

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
  - `google-generativeai` / `langchain` / `langgraph` (for Gen-AI)
