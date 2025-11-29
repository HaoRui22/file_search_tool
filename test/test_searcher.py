import unittest
from searcher import search_keyword

class TestSearcher(unittest.TestCase):

    def test_directory_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            search_keyword('no_such_dir', 'hello')

    def test_found_keyword(self):
        # 你可创建一个临时文件进行测试
        pass

if __name__ == '__main__':
    unittest.main()
