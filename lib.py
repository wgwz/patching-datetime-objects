from datetime import datetime
import unittest
from unittest.mock import patch

def get():
    return datetime.utcnow()

class TestLib(unittest.TestCase):
    
    @patch('__main__.datetime.utcnow')
    def test_get_function(self, mock_utcnow):
        mock_utcnow.return_value = 'pAtChEd'
        assert get() == 'pAtChEd' 

if __name__ == '__main__':
    unittest.main()
