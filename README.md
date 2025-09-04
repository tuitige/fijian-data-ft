# Fijian Data Fine-Tuning Project 🇫🇯

A comprehensive data engineering project to curate, process, and prepare Fijian language data for AI/ML applications and fine-tuning large language models to better understand and support this low-resource language.

## 🎯 Project Overview

The Fijian language is spoken by approximately 350,000-450,000 people, primarily in Fiji. As a low-resource language, it lacks sufficient digital representation in AI and machine learning models. This project aims to:

- **Aggregate** Fijian language data from multiple sources
- **Clean and standardize** text data for training purposes  
- **Create** high-quality datasets for various NLP tasks
- **Enable** fine-tuning of language models for Fijian
- **Preserve** and promote the digital presence of Fijian language

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment tool (venv, conda, etc.)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/tuitige/fijian-data-ft.git
   cd fijian-data-ft
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

5. **Run the data cleaning pipeline**
   ```bash
   python src/fijian_data_cleaning_pipeline.py --input data/raw --output data/processed
   ```

## 📁 Project Structure

```
fijian-data-ft/
├── src/                           # Source code and scripts
│   ├── fijian_data_cleaning_pipeline.py  # Main data processing pipeline
│   └── __init__.py
├── data/                          # Data storage (gitignored)
│   ├── raw/                      # Raw, unprocessed data
│   ├── interim/                  # Intermediate processing steps
│   └── processed/                # Final, clean datasets
├── configs/                       # Configuration files
├── docs/                         # Additional documentation
├── tests/                        # Test files
├── notebooks/                    # Jupyter notebooks for exploration
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variables template
├── .gitignore                   # Git ignore rules
├── LICENSE                      # MIT License
├── CONTRIBUTING.md              # Contribution guidelines
└── README.md                    # This file
```

## 🔧 Data Processing Pipeline

### Input Data Sources

The pipeline can process various types of Fijian language data:

- **Dictionary data**: Word-definition pairs in CSV/TXT format
- **Text corpora**: Books, articles, social media posts
- **Bilingual data**: Fijian-English parallel texts
- **Audio transcriptions**: Speech-to-text data

### Data Formats

#### Dictionary Format (CSV)
```csv
fijian_word,english_definition,part_of_speech,example
bula,hello/life,noun/interjection,"Bula vinaka" (good health)
moce,goodbye,interjection,"Moce mada" (goodbye for now)
```

#### Text Format (TXT)
```
One sentence per line format.
Na noda vanua e dau yacovi kina na veikau vinaka duadua.
Fijian sentences should be clean and properly formatted.
```

#### Training Output (JSONL)
```json
{"instruction": "Define the Fijian word: bula", "input": "bula", "output": "hello, life, or a general greeting expressing good health", "task_type": "definition"}
{"instruction": "Complete the following Fijian text:", "input": "Na noda vanua", "output": "e dau yacovi kina na veikau vinaka duadua", "task_type": "completion"}
```

### Usage Examples

#### Basic Pipeline Run
```bash
# Process all files in data/raw/
python src/fijian_data_cleaning_pipeline.py -i data/raw -o data/processed

# With verbose logging
python src/fijian_data_cleaning_pipeline.py -i data/raw -o data/processed --verbose
```

#### Custom Processing
```python
from src.fijian_data_cleaning_pipeline import FijianDataCleaner

# Initialize cleaner
cleaner = FijianDataCleaner('data/raw', 'data/processed')

# Process specific file types
dictionary_entries = cleaner.process_dictionary_file('path/to/dictionary.csv')
text_sentences = cleaner.process_text_file('path/to/text.txt')
```

## 🔐 Secrets Management

This project supports multiple approaches for managing sensitive information:

### 1. Environment Variables (.env file)
```bash
# Copy the template and fill in your values
cp .env.example .env
# Edit .env (never commit this file!)
```

### 2. GitHub Secrets (for CI/CD)
- Go to repository Settings → Secrets and variables → Actions
- Add secrets like `OPENAI_API_KEY`, `HUGGINGFACE_TOKEN`, etc.

### 3. AWS Secrets Manager (for production)
```python
import boto3
from botocore.exceptions import ClientError

def get_secret(secret_name, region_name="us-west-2"):
    session = boto3.session.Session()
    client = session.client(service_name='secretsmanager', region_name=region_name)
    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        return get_secret_value_response['SecretString']
    except ClientError as e:
        raise e
```

### 4. External Secret Management
Consider using services like:
- **HashiCorp Vault**: For enterprise secret management
- **Azure Key Vault**: If using Azure cloud services
- **Google Secret Manager**: If using Google Cloud Platform

## 📊 Data Quality Guidelines

### Text Quality Standards
- ✅ **Authentic Fijian**: Native speaker content preferred
- ✅ **Clean encoding**: UTF-8 with proper character handling
- ✅ **Balanced representation**: Multiple dialects and domains
- ✅ **Proper attribution**: Source information included
- ❌ **No personal data**: Remove names, addresses, phone numbers
- ❌ **No sacred content**: Respect traditional/ceremonial texts

### Validation Checks
- Minimum sentence length (3+ words)
- Character encoding validation
- Language detection confidence
- Duplicate content removal
- Format consistency

## 🤝 Contributing

We welcome contributions from the community! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### Quick Contribution Steps
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Types of Contributions Needed
- **Data**: Fijian text corpus, dictionaries, audio transcriptions
- **Code**: Data processing improvements, new features
- **Documentation**: Setup guides, examples, tutorials
- **Testing**: Unit tests, integration tests, data validation

## 🧪 Testing

Run the test suite to ensure everything works correctly:

```bash
# Install test dependencies (included in requirements.txt)
pip install pytest pytest-cov

# Run all tests
pytest tests/

# Run with coverage report
pytest tests/ --cov=src --cov-report=html
```

## 📚 Documentation

Additional documentation can be found in the `docs/` directory:

- [Data Sources Guide](docs/data-sources.md)
- [Model Training Tutorial](docs/model-training.md)
- [API Reference](docs/api-reference.md)
- [Troubleshooting](docs/troubleshooting.md)

## 📈 Roadmap

### Phase 1: Foundation (Current)
- [x] Project structure setup
- [x] Basic data cleaning pipeline
- [x] Documentation and contribution guidelines
- [ ] Initial data collection
- [ ] Quality validation framework

### Phase 2: Expansion
- [ ] Web scraping tools for Fijian websites
- [ ] Audio processing pipeline
- [ ] Bilingual alignment tools
- [ ] Advanced text normalization

### Phase 3: Model Training
- [ ] Fine-tuning scripts for popular models
- [ ] Evaluation benchmarks
- [ ] Model deployment tools
- [ ] Community feedback integration

## 🏆 Acknowledgments

- The Fijian community for preserving and sharing their language
- Contributors and maintainers of this project
- Open source libraries that make this work possible
- Academic researchers studying Pacific languages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Projects

- [Universal Dependencies for Fijian](https://universaldependencies.org/)
- [Pacific Languages Text Corpus](https://github.com/pacific-languages)
- [Low-Resource Language Processing](https://github.com/low-resource-languages)

## 📞 Contact

- **Project Maintainer**: [tuitige](https://github.com/tuitige)
- **Issues**: Please use [GitHub Issues](https://github.com/tuitige/fijian-data-ft/issues)
- **Discussions**: Join our [GitHub Discussions](https://github.com/tuitige/fijian-data-ft/discussions)

---

**Bula vinaka!** Thank you for supporting the preservation and advancement of the Fijian language in the digital age. 🌺
