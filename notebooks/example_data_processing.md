# Fijian Data Fine-Tuning: Example Notebook

This notebook demonstrates how to use the Fijian data processing pipeline and prepare data for fine-tuning language models.

## Setup

First, let's import the necessary libraries and set up our environment:

```python
import sys
sys.path.append('../src')

from fijian_data_cleaning_pipeline import FijianDataCleaner
import pandas as pd
import json
from pathlib import Path

# Set up paths
raw_data_path = '../data/raw'
processed_data_path = '../data/processed'
```

## Data Processing

### Initialize the cleaner
```python
cleaner = FijianDataCleaner(raw_data_path, processed_data_path)
```

### Process sample data
```python
# Create some sample data for demonstration
sample_dict_data = [
    {'fijian_word': 'bula', 'english_definition': 'hello, life, good health'},
    {'fijian_word': 'vinaka', 'english_definition': 'thank you, good'},
    {'fijian_word': 'moce', 'english_definition': 'goodbye, sleep'}
]

# Save as CSV for processing
sample_df = pd.DataFrame(sample_dict_data)
sample_df.to_csv('../data/raw/sample_dictionary.csv', index=False)
```

### Run the pipeline
```python
cleaner.process_all_files()
print(f"Processing complete. Statistics: {cleaner.stats}")
```

## Data Analysis

### Load processed data
```python
# Load dictionary data
dict_file = Path(processed_data_path) / 'fijian_dictionary.jsonl'
if dict_file.exists():
    with open(dict_file, 'r') as f:
        dict_data = [json.loads(line) for line in f]
    print(f"Loaded {len(dict_data)} dictionary entries")

# Load training data
train_file = Path(processed_data_path) / 'fijian_training_data.jsonl'
if train_file.exists():
    with open(train_file, 'r') as f:
        train_data = [json.loads(line) for line in f]
    print(f"Loaded {len(train_data)} training examples")
```

### Analyze data quality
```python
if 'dict_data' in locals():
    # Word length distribution
    word_lengths = [len(entry['fijian_word'].split()) for entry in dict_data]
    print(f"Average word length: {sum(word_lengths)/len(word_lengths):.2f} tokens")
    
    # Definition length distribution  
    def_lengths = [len(entry['english_definition'].split()) for entry in dict_data]
    print(f"Average definition length: {sum(def_lengths)/len(def_lengths):.2f} tokens")
```

## Next Steps

1. **Collect more data**: Add additional dictionary and text sources
2. **Quality validation**: Implement more sophisticated validation rules
3. **Model training**: Use the processed data to fine-tune language models
4. **Evaluation**: Develop metrics to assess model performance on Fijian

This is a starting template - expand it based on your specific data and use cases!