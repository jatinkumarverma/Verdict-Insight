# Verdict Insight

Verdict Insight is an analytical platform designed to process and analyze **Indian Supreme Court judgments** focusing on key legal principles, precedents, and case outcomes using **advanced Natural Language Processing (NLP)** techniques and **Reinforcement Learning (RL)**. By leveraging a custom reward function, the model generates legally accurate, concise, and contextually relevant summaries, offering a valuable tool for legal professionals. This tool supports legal professionals, researchers, and policymakers with actionable insights from legal texts.

## **Table of Contents**

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Usage](#usage)
- [Results](#results)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Indian Supreme Court delivers numerous judgments that shape the country's legal landscape. However, systematic analysis to uncover underlying patterns and trends is lacking. Verdict Insight aims to fill this gap by providing a comprehensive analytical tool to process and analyze these judgments. This project also introduces a **Reinforcement Learning-based** approach to generate high-quality summaries of legal texts that focus on critical legal elements such as principles, precedents, and outcomes.

The model utilizes a **transformer-based architecture** fine-tuned using RL to optimize for legal-specific requirements. The primary contributions of this project include:

- Custom reward functions that focus on legal elements.
- An RL training pipeline designed for abstractive summarization.
- Evaluation using standard summarization metrics and legal-specific criteria.

## **Project Structure**

```
.
├── data/                       # Directory containing dataset (Indian Supreme Court judgments in PDF)
├── src/                        # Main source code directory
│   ├── preprocess.py           # Script for PDF preprocessing and text extraction
│   ├── train_rl.py             # Script for model training using RL
│   ├── reward_functions.py     # Custom reward functions for RL training
│   ├── evaluation.py           # Evaluation metrics and scripts (ROUGE, BLEU, legal-specific metrics)
│   ├── model.py                # Model architecture and loading functions
├── README.md                   # Project documentation (this file)
└── requirements.txt            # List of dependencies and Python libraries
```

## **Installation**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/jatinkumarverma/verdict-insight.git
   cd verdict-insight
   ```

2. Set up a virtual environment and install the required dependencies:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. You will need **Google Colab** or a local machine with **GPU support** (optional) to train the model efficiently. Make sure to install the necessary libraries for GPU usage if you're using local GPU resources.

## **Dataset**

The dataset consists of 300 PDF files of Indian Supreme Court judgments. These files need to be preprocessed to extract the raw text.

- Preprocessing is done using the `preprocess.py` script, which extracts the text from PDFs and formats it for model training.
- The dataset should be stored in the `data/` directory, with each case judgment as a separate file.

## **Model Training**

### **Reinforcement Learning Training Process**

To train the model using reinforcement learning:

1. Preprocess the dataset:

   ```bash
   python src/preprocess.py --input_dir data/ --output_file processed_data.json
   ```

2. Run the RL training script:

   ```bash
   python src/train_rl.py --dataset processed_data.json --epochs 3 --lr 1e-5
   ```

   - The training script fine-tunes a **BART** or **T5** model on the dataset using reinforcement learning, optimizing the model for legal principles, precedents, and outcome clarity.
   - You can adjust hyperparameters like the number of **epochs** and the **learning rate**.

### **Reward Function**

The custom reward function is defined in the `reward_functions.py` script. It assigns positive rewards based on:

- **Principle extraction accuracy**
- **Precedent citation accuracy**
- **Outcome clarity**

These components help guide the model to focus on legal elements during training.

## **Usage**

Once the model is trained, you can use it to generate summaries for new legal judgments. Run the `inference.py` script to summarize a judgment:

```bash
python src/inference.py --model_path models/rl_legal_summarizer.pt --input_text "input_judgment.txt"
```

This will generate a summary based on the trained model.

## **Results**

Our RL-based summarization model was evaluated using both standard summarization metrics (**ROUGE**, **BLEU**) and legal-specific evaluation metrics:

- **ROUGE-1**: 42.5
- **ROUGE-L**: 40.1
- **BLEU**: 20.9
- **Principle Extraction Accuracy**: 85.9%
- **Precedent Citation Accuracy**: 80.7%
- **Outcome Clarity**: 82.5%

The model showed significant improvements over traditional models like **BART** and **T5**, particularly in its ability to generate legally meaningful summaries.

## **Future Work**

- **Multi-Document Summarization**: Extend the model to handle multiple related legal documents.
- **Domain Adaptation**: Adapt the RL model for summarizing other types of legal texts, such as contracts or statutes.
- **Explainability**: Improve the model’s interpretability to better understand how it generates summaries.

## **Contributing**

We welcome contributions to improve the project. Please open an issue or submit a pull request with suggestions or improvements.

### **Contributing Guidelines:**

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## **License**

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

By implementing Verdict Insight, we aim to foster greater transparency in the legal system and provide valuable tools for legal analysis and research.

---

Feel free to reach out if you have any questions or need further assistance!
