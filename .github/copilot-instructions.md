# Fijian Data Fine-Tuning Project
Data engineering project to curate Fijian language data for AI/ML and Fine-tuning LLM for better understanding of low resource language.

**ALWAYS follow these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.**

## Current Project State
This project is in early development stage with minimal codebase. The repository currently contains only documentation. Expect the project to evolve with Python-based data engineering tools, Jupyter notebooks, and machine learning frameworks.

## Working Effectively

### Initial Setup and Dependencies
Since this is a data engineering project for language data curation, expect to work with:
- **Python 3.8+** for data processing and ML workflows
- **pip** or **conda** for package management  
- **Jupyter notebooks** for exploratory data analysis
- **Git LFS** for large dataset storage (if datasets are added)

Standard setup commands for data engineering projects:
```bash
# Check Python version (required: 3.8+)
python3 --version

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install common data engineering dependencies (when requirements.txt exists)
pip install -r requirements.txt

# Install Jupyter for notebooks (if not in requirements.txt)
# NOTE: pip install may timeout due to network limitations. If this occurs, 
# document the failure and continue with existing system packages
pip install jupyter pandas numpy scikit-learn matplotlib seaborn
```

### Building and Testing
**Current State**: No build system or tests exist yet.

When the project develops, expect these patterns:
- **Data processing scripts**: `python scripts/process_data.py` 
- **Notebook execution**: `jupyter notebook` or `jupyter lab`
- **Testing**: `pytest tests/` or `python -m pytest`
- **Linting**: `flake8 .` or `black .` for code formatting

**NEVER CANCEL long-running operations**:
- Data processing may take 30+ minutes for large datasets. Set timeout to 60+ minutes.
- Model training/fine-tuning may take hours. Set timeout to 240+ minutes.
- Large file downloads may take 15+ minutes. Set timeout to 30+ minutes.

### Running the Application
**Current State**: No runnable application exists yet.

Expected future patterns for data engineering workflows:
- **Data collection**: `python scripts/collect_fijian_data.py`
- **Data preprocessing**: `python scripts/preprocess.py`
- **Model fine-tuning**: `python scripts/finetune_model.py`
- **Evaluation**: `python scripts/evaluate.py`

## Validation and Testing

### Manual Validation Requirements
When code is added, ALWAYS validate:
1. **Data integrity**: Verify processed data maintains expected structure and content
2. **Model outputs**: Test that fine-tuned models produce reasonable Fijian language responses
3. **Pipeline execution**: Run complete data processing pipeline end-to-end
4. **Notebook execution**: Execute all notebook cells without errors

### Common Validation Commands
Run before committing any changes:
```bash
# Check data file integrity (when data files exist)
python scripts/validate_data.py

# Run all tests
pytest tests/ --timeout=1800  # 30-minute timeout for data tests

# Format code  
black .
flake8 .

# Check notebook execution
jupyter nbconvert --to notebook --execute notebooks/*.ipynb
```

## Repository Structure and Navigation

### Current Structure
```
.
├── README.md           # Project description
└── .github/
    └── copilot-instructions.md  # This file
```

### Expected Future Structure
```
fijian-data-ft/
├── README.md
├── requirements.txt    # Python dependencies
├── setup.py           # Package setup
├── data/              # Raw and processed datasets
│   ├── raw/           # Original Fijian language data
│   ├── processed/     # Cleaned and curated data
│   └── models/        # Fine-tuned model outputs
├── scripts/           # Data processing and training scripts
│   ├── collect_data.py
│   ├── preprocess.py
│   ├── finetune_model.py
│   └── evaluate.py
├── notebooks/         # Jupyter notebooks for analysis
│   ├── data_exploration.ipynb
│   ├── model_analysis.ipynb
│   └── evaluation.ipynb
├── tests/            # Unit and integration tests
├── docs/             # Additional documentation
└── .github/
    ├── workflows/    # CI/CD pipelines
    └── copilot-instructions.md
```

## Key Project Information

### Domain Focus
- **Primary Language**: Fijian (low-resource language)
- **Task Type**: Language data curation and LLM fine-tuning
- **Data Sources**: Expect text corpora, dictionaries, and language samples
- **ML Frameworks**: Likely Hugging Face Transformers, PyTorch, or TensorFlow

### Common Data Engineering Tasks
When working on this project, you'll likely encounter:
1. **Text data collection** from various Fijian language sources
2. **Data cleaning** to remove noise and standardize format
3. **Tokenization** and preprocessing for Fijian language specifics
4. **Dataset preparation** for fine-tuning workflows
5. **Model evaluation** on Fijian language understanding tasks

### Performance Expectations
- **Data loading**: Large language datasets may take 5-15 minutes to load
- **Preprocessing**: Text cleaning and tokenization may take 30-60 minutes for large corpora
- **Model fine-tuning**: NEVER CANCEL - can take 2-8 hours depending on model size and data volume
- **Evaluation**: Model evaluation may take 15-45 minutes

### Critical Reminders
- **ALWAYS** preserve original data in `data/raw/` directory
- **NEVER** commit large datasets to git (use Git LFS or external storage)
- **ALWAYS** validate Fijian text encoding (UTF-8) and character preservation
- **NEVER CANCEL** long-running ML training processes
- Set timeouts of 240+ minutes for any model training commands
- Set timeouts of 60+ minutes for data processing commands

### Troubleshooting Common Issues
- **Unicode errors**: Ensure all text files use UTF-8 encoding
- **Memory issues**: Use data chunking for large datasets
- **Model loading failures**: Verify Hugging Face model compatibility
- **Slow processing**: Consider using GPU acceleration for ML tasks

## Development Workflow
1. **Always** activate virtual environment before starting work
2. **Always** run data validation after processing steps
3. **Always** test notebook execution end-to-end
4. **Always** check for data corruption or encoding issues
5. **Never** commit without validating model outputs
6. **Never** skip linting and formatting checks

This project focuses on preserving and enhancing Fijian language understanding through careful data curation and responsible AI development.