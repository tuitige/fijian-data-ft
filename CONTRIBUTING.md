# Contributing to Fijian Data Fine-Tuning Project

Thank you for your interest in contributing to the Fijian Data Fine-Tuning project! This project aims to curate and prepare Fijian language data for AI/ML applications and fine-tuning large language models.

## Getting Started

1. **Fork the repository** and clone your fork locally
2. **Set up your development environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Copy environment variables**: `cp .env.example .env` and fill in your values
4. **Create a new branch** for your feature: `git checkout -b feature/your-feature-name`

## Types of Contributions

### Data Contributions
- **Fijian text corpora**: Books, articles, news, social media posts
- **Bilingual data**: Fijian-English parallel texts for translation tasks
- **Linguistic resources**: Dictionaries, grammar guides, language rules
- **Audio data**: Speech recordings with Fijian transcriptions

### Code Contributions
- **Data processing scripts**: Cleaning, normalization, tokenization
- **Data validation tools**: Quality checks, format validation
- **Training pipelines**: Fine-tuning scripts for various models
- **Evaluation metrics**: Tools to assess model performance on Fijian

### Documentation
- **Setup guides**: Installation and configuration instructions
- **Data format specifications**: Standards for data contribution
- **Usage examples**: Notebooks demonstrating data processing workflows
- **Research papers**: Documentation of findings and methodologies

## Data Contribution Guidelines

### Data Quality Standards
- **Authenticity**: Ensure data represents genuine Fijian language usage
- **Clean text**: Remove HTML tags, fix encoding issues, normalize punctuation
- **Proper attribution**: Include source information and respect copyright
- **Balanced representation**: Include diverse dialects, domains, and registers

### Data Format Requirements
- **Text files**: UTF-8 encoding, one sentence per line
- **Metadata**: Include source, date, dialect, domain information
- **Bilingual data**: Aligned sentence pairs in separate files
- **File naming**: Use descriptive names with format: `fijian_[source]_[year]_[type].txt`

### Sensitive Data Guidelines
- **No personal information**: Redact names, addresses, phone numbers
- **Cultural sensitivity**: Respect traditional knowledge and sacred content
- **Privacy compliance**: Follow data protection regulations
- **Community consent**: Ensure permission for use of community-generated content

## Code Contribution Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use type hints where appropriate
- Write docstrings for all functions and classes
- Add comments for complex logic

### Testing
- Write tests for new functionality
- Ensure existing tests pass: `pytest tests/`
- Maintain test coverage above 80%

### Documentation
- Update README.md if adding new features
- Document configuration options
- Include usage examples for new scripts

## Development Workflow

1. **Create an issue** describing the contribution you want to make
2. **Get feedback** from maintainers before starting major work
3. **Make your changes** in small, focused commits
4. **Test thoroughly** including edge cases
5. **Submit a pull request** with clear description
6. **Respond to feedback** and make requested changes

## Data Processing Pipeline

### Input Data
```
data/raw/
├── dictionaries/
├── texts/
├── audio/
└── metadata/
```

### Processing Steps
1. **Validation**: Check format, encoding, completeness
2. **Cleaning**: Remove noise, normalize text, fix errors
3. **Tokenization**: Split into sentences, words, subwords
4. **Quality filtering**: Remove low-quality or inappropriate content
5. **Format conversion**: Convert to training-ready formats

### Output Data
```
data/processed/
├── training_data.jsonl
├── validation_data.jsonl
├── test_data.jsonl
└── metadata.json
```

## Secrets and Configuration Management

### Environment Variables
- Store sensitive information in `.env` file (never commit this)
- Use `.env.example` as a template
- Document all required environment variables

### API Keys and Credentials
- **GitHub Secrets**: For CI/CD workflows
- **AWS Parameter Store**: For production deployments
- **Local development**: Use `.env` file with python-dotenv

## Issue Reporting

When reporting issues, please include:
- **Clear description** of the problem
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Environment information** (OS, Python version, etc.)
- **Relevant logs or error messages**

## Community Guidelines

- **Be respectful** and inclusive in all interactions
- **Respect cultural context** of the Fijian language and community
- **Collaborate openly** and share knowledge
- **Give credit** where credit is due
- **Ask questions** if you're unsure about anything

## Getting Help

- **Create an issue** for bugs or feature requests
- **Start a discussion** for general questions
- **Review existing issues** to see if your question was already answered
- **Check the documentation** in the `docs/` directory

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes for significant contributions
- Academic papers resulting from this work (with permission)

Thank you for helping advance Fijian language technology! 🇫🇯