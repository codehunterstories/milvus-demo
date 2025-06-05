import os
import sys
import unittest
import importlib

class TestMilvusVDefaults(unittest.TestCase):
    def setUp(self):
        # Save and clear environment variables
        self.saved = {k: os.environ.pop(k, None) for k in ['MILVUS_IP', 'MILVUS_PORT', 'MILVUS_DATASET_PATH']}
        if 'question_answer.common.milvus_v' in sys.modules:
            del sys.modules['question_answer.common.milvus_v']
        self.milvus_v = importlib.import_module('question_answer.common.milvus_v')

    def tearDown(self):
        # Restore environment variables
        for k, v in self.saved.items():
            if v is not None:
                os.environ[k] = v
        if 'question_answer.common.milvus_v' in sys.modules:
            del sys.modules['question_answer.common.milvus_v']
        importlib.import_module('question_answer.common.milvus_v')

    def test_get_ip_default(self):
        self.assertEqual(self.milvus_v.get_ip(), '127.0.0.1')

    def test_get_port_default(self):
        self.assertEqual(self.milvus_v.get_port(), '19530')

    def test_get_q_a_path_default(self):
        self.assertEqual(self.milvus_v.get_q_a_path(), './dataset/question_answer.csv')

if __name__ == '__main__':
    unittest.main()

