#!/usr/bin/env python3
"""
Fijian Data Cleaning Pipeline

This script provides functionality for ingesting and cleaning Fijian language
dictionary data and other text sources for fine-tuning language models.

Usage:
    python fijian_data_cleaning_pipeline.py --input data/raw/ --output data/processed/
    python fijian_data_cleaning_pipeline.py --help

Author: Fijian Data Fine-Tuning Project
License: MIT
"""

import argparse
import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import pandas as pd
from datasets import Dataset


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('fijian_pipeline.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class FijianDataCleaner:
    """Main class for cleaning and processing Fijian language data."""
    
    def __init__(self, input_dir: str, output_dir: str):
        """
        Initialize the Fijian data cleaner.
        
        Args:
            input_dir: Directory containing raw data files
            output_dir: Directory to save processed data
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Statistics tracking
        self.stats = {
            'files_processed': 0,
            'lines_processed': 0,
            'lines_cleaned': 0,
            'lines_removed': 0
        }
    
    def clean_text(self, text: str) -> str:
        """
        Clean and normalize Fijian text.
        
        Args:
            text: Raw text string
            
        Returns:
            Cleaned text string
        """
        if not text or not isinstance(text, str):
            return ""
        
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', text)
        
        # Normalize whitespace
        text = re.sub(r'\s+', ' ', text)
        
        # Remove extra punctuation
        text = re.sub(r'[^\w\s\-\'\.,;:!?()]', '', text)
        
        # Normalize Fijian characters (if needed)
        # Add specific Fijian character normalization here
        
        # Strip leading/trailing whitespace
        text = text.strip()
        
        return text
    
    def is_valid_fijian_text(self, text: str) -> bool:
        """
        Validate if text appears to be valid Fijian language content.
        
        Args:
            text: Text string to validate
            
        Returns:
            True if text appears valid, False otherwise
        """
        if not text or len(text.strip()) < 3:
            return False
        
        # Check for minimum length
        if len(text.split()) < 2:
            return False
        
        # Check for non-alphabetic ratio (should be mostly text)
        alpha_chars = sum(c.isalpha() for c in text)
        if alpha_chars / len(text) < 0.6:
            return False
        
        # Add Fijian-specific validation rules here
        # Common Fijian words, character patterns, etc.
        
        return True
    
    def process_dictionary_file(self, file_path: Path) -> List[Dict[str, str]]:
        """
        Process a dictionary file and extract word definitions.
        
        Args:
            file_path: Path to dictionary file
            
        Returns:
            List of dictionaries with word and definition pairs
        """
        entries = []
        
        try:
            if file_path.suffix.lower() == '.csv':
                df = pd.read_csv(file_path)
                for _, row in df.iterrows():
                    # Assuming columns: 'fijian_word', 'english_definition'
                    # Adjust column names based on actual data structure
                    if 'fijian_word' in df.columns and 'english_definition' in df.columns:
                        word = self.clean_text(str(row['fijian_word']))
                        definition = self.clean_text(str(row['english_definition']))
                        
                        if self.is_valid_fijian_text(word) and definition:
                            entries.append({
                                'fijian_word': word,
                                'english_definition': definition,
                                'source': file_path.name
                            })
            
            elif file_path.suffix.lower() == '.txt':
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        line = line.strip()
                        if not line:
                            continue
                        
                        # Try to parse word/definition pairs
                        # Adjust parsing logic based on actual file format
                        if ' - ' in line:
                            parts = line.split(' - ', 1)
                            if len(parts) == 2:
                                word = self.clean_text(parts[0])
                                definition = self.clean_text(parts[1])
                                
                                if self.is_valid_fijian_text(word) and definition:
                                    entries.append({
                                        'fijian_word': word,
                                        'english_definition': definition,
                                        'source': f"{file_path.name}:L{line_num}"
                                    })
        
        except Exception as e:
            logger.error(f"Error processing {file_path}: {str(e)}")
        
        return entries
    
    def process_text_file(self, file_path: Path) -> List[str]:
        """
        Process a general text file and extract clean sentences.
        
        Args:
            file_path: Path to text file
            
        Returns:
            List of cleaned sentences
        """
        sentences = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Split into sentences (basic approach)
            raw_sentences = re.split(r'[.!?]+', content)
            
            for sentence in raw_sentences:
                cleaned = self.clean_text(sentence)
                if self.is_valid_fijian_text(cleaned):
                    sentences.append(cleaned)
        
        except Exception as e:
            logger.error(f"Error processing {file_path}: {str(e)}")
        
        return sentences
    
    def process_all_files(self):
        """Process all files in the input directory."""
        dictionary_entries = []
        text_sentences = []
        
        # Process all files recursively
        for file_path in self.input_dir.rglob('*'):
            if file_path.is_file():
                logger.info(f"Processing {file_path}")
                
                if 'dict' in file_path.name.lower() or 'dictionary' in file_path.name.lower():
                    entries = self.process_dictionary_file(file_path)
                    dictionary_entries.extend(entries)
                    logger.info(f"Extracted {len(entries)} dictionary entries from {file_path.name}")
                
                elif file_path.suffix.lower() in ['.txt', '.csv']:
                    sentences = self.process_text_file(file_path)
                    text_sentences.extend(sentences)
                    logger.info(f"Extracted {len(sentences)} sentences from {file_path.name}")
                
                self.stats['files_processed'] += 1
        
        # Save processed data
        self.save_processed_data(dictionary_entries, text_sentences)
    
    def save_processed_data(self, dictionary_entries: List[Dict], text_sentences: List[str]):
        """
        Save processed data to output files.
        
        Args:
            dictionary_entries: List of dictionary entry dictionaries
            text_sentences: List of text sentences
        """
        # Save dictionary data
        if dictionary_entries:
            dict_file = self.output_dir / 'fijian_dictionary.jsonl'
            with open(dict_file, 'w', encoding='utf-8') as f:
                for entry in dictionary_entries:
                    f.write(json.dumps(entry, ensure_ascii=False) + '\n')
            logger.info(f"Saved {len(dictionary_entries)} dictionary entries to {dict_file}")
        
        # Save text data
        if text_sentences:
            text_file = self.output_dir / 'fijian_text.jsonl'
            with open(text_file, 'w', encoding='utf-8') as f:
                for sentence in text_sentences:
                    f.write(json.dumps({'text': sentence}, ensure_ascii=False) + '\n')
            logger.info(f"Saved {len(text_sentences)} sentences to {text_file}")
        
        # Save combined training data
        self.create_training_data(dictionary_entries, text_sentences)
        
        # Save statistics
        stats_file = self.output_dir / 'processing_stats.json'
        with open(stats_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=2)
        logger.info(f"Processing statistics saved to {stats_file}")
    
    def create_training_data(self, dictionary_entries: List[Dict], text_sentences: List[str]):
        """
        Create training data in various formats for different fine-tuning approaches.
        
        Args:
            dictionary_entries: Dictionary entries
            text_sentences: Text sentences
        """
        training_data = []
        
        # Convert dictionary entries to training format
        for entry in dictionary_entries:
            # Format for translation/definition tasks
            training_data.append({
                'instruction': f"Define the Fijian word: {entry['fijian_word']}",
                'input': entry['fijian_word'],
                'output': entry['english_definition'],
                'task_type': 'definition'
            })
        
        # Add text for language modeling
        for sentence in text_sentences:
            training_data.append({
                'instruction': "Complete the following Fijian text:",
                'input': sentence[:len(sentence)//2],  # First half as input
                'output': sentence[len(sentence)//2:],  # Second half as output
                'task_type': 'completion'
            })
        
        # Save training data
        if training_data:
            train_file = self.output_dir / 'fijian_training_data.jsonl'
            with open(train_file, 'w', encoding='utf-8') as f:
                for item in training_data:
                    f.write(json.dumps(item, ensure_ascii=False) + '\n')
            logger.info(f"Saved {len(training_data)} training examples to {train_file}")


def main():
    """Main function to run the pipeline."""
    parser = argparse.ArgumentParser(description='Fijian Data Cleaning Pipeline')
    parser.add_argument('--input', '-i', required=True, 
                       help='Input directory containing raw data files')
    parser.add_argument('--output', '-o', required=True,
                       help='Output directory for processed data')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose logging')
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize and run the cleaner
    cleaner = FijianDataCleaner(args.input, args.output)
    
    logger.info("Starting Fijian data cleaning pipeline")
    logger.info(f"Input directory: {args.input}")
    logger.info(f"Output directory: {args.output}")
    
    try:
        cleaner.process_all_files()
        logger.info("Pipeline completed successfully")
        logger.info(f"Statistics: {cleaner.stats}")
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
        sys.exit(1)


if __name__ == '__main__':
    main()