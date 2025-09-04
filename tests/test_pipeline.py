"""
Tests for the Fijian Data Cleaning Pipeline
"""

import pytest
import tempfile
import json
from pathlib import Path
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from fijian_data_cleaning_pipeline import FijianDataCleaner


class TestFijianDataCleaner:
    """Test class for FijianDataCleaner functionality."""
    
    def setup_method(self):
        """Set up test fixtures before each test method."""
        self.temp_dir = tempfile.mkdtemp()
        self.input_dir = Path(self.temp_dir) / 'input'
        self.output_dir = Path(self.temp_dir) / 'output'
        self.input_dir.mkdir(parents=True)
        self.output_dir.mkdir(parents=True)
        
        self.cleaner = FijianDataCleaner(str(self.input_dir), str(self.output_dir))
    
    def test_clean_text_basic(self):
        """Test basic text cleaning functionality."""
        # Test normal text
        result = self.cleaner.clean_text("Bula vinaka vei kemuni!")
        assert result == "Bula vinaka vei kemuni!"
        
        # Test text with extra whitespace
        result = self.cleaner.clean_text("  Bula   vinaka  ")
        assert result == "Bula vinaka"
        
        # Test HTML removal
        result = self.cleaner.clean_text("<p>Bula vinaka</p>")
        assert result == "Bula vinaka"
        
        # Test empty input
        result = self.cleaner.clean_text("")
        assert result == ""
        
        # Test None input
        result = self.cleaner.clean_text(None)
        assert result == ""
    
    def test_is_valid_fijian_text(self):
        """Test Fijian text validation."""
        # Valid Fijian text
        assert self.cleaner.is_valid_fijian_text("Bula vinaka") == True
        assert self.cleaner.is_valid_fijian_text("Na noda vanua") == True
        
        # Invalid text (too short)
        assert self.cleaner.is_valid_fijian_text("a") == False
        assert self.cleaner.is_valid_fijian_text("") == False
        
        # Invalid text (too many non-alphabetic characters)
        assert self.cleaner.is_valid_fijian_text("123456789!@#") == False
        
        # Single word (should be invalid - needs at least 2 words)
        assert self.cleaner.is_valid_fijian_text("bula") == False
    
    def test_process_dictionary_data(self):
        """Test dictionary data processing."""
        # Create test CSV file
        test_csv = self.input_dir / 'test_dict.csv'
        with open(test_csv, 'w', encoding='utf-8') as f:
            f.write('fijian_word,english_definition\n')
            f.write('bula,hello or life\n')
            f.write('vinaka,thank you\n')
            f.write('moce,goodbye\n')
        
        entries = self.cleaner.process_dictionary_file(test_csv)
        
        assert len(entries) == 3
        assert entries[0]['fijian_word'] == 'bula'
        assert entries[0]['english_definition'] == 'hello or life'
        assert entries[0]['source'] == 'test_dict.csv'
    
    def test_process_text_data(self):
        """Test text file processing."""
        # Create test text file
        test_txt = self.input_dir / 'test_text.txt'
        with open(test_txt, 'w', encoding='utf-8') as f:
            f.write('Bula vinaka vei kemuni. Na noda vanua e vinaka sara. Moce mada.')
        
        sentences = self.cleaner.process_text_file(test_txt)
        
        assert len(sentences) >= 2  # Should extract multiple sentences
        assert any('Bula vinaka' in sentence for sentence in sentences)
    
    def test_initialization(self):
        """Test cleaner initialization."""
        assert self.cleaner.input_dir == self.input_dir
        assert self.cleaner.output_dir == self.output_dir
        assert self.cleaner.stats['files_processed'] == 0
        assert self.cleaner.stats['lines_processed'] == 0


def test_main_function_imports():
    """Test that main functions can be imported without errors."""
    from fijian_data_cleaning_pipeline import FijianDataCleaner, main
    
    # Test that classes can be instantiated
    with tempfile.TemporaryDirectory() as temp_dir:
        cleaner = FijianDataCleaner(temp_dir, temp_dir)
        assert cleaner is not None


if __name__ == '__main__':
    pytest.main([__file__])