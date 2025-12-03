# 需要测试的四类情况：
# 1.目录不存在
# 2.内容搜索能找到内容
# 3.文件名搜索能找到文件
# 4. 搜索无结果

import unittest
import os
import tempfile
from searcher import search_content, search_filename

class TestSearcher(unittest.TestCase):

    def test_directory_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            search_content("no_such_dir", "hello")

    def test_search_content_found(self):
        # 创建临时目录
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "example.txt")

            # 写入测试内容
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("这是一个测试内容\nHello world\nHello Python\n")

            result = search_content(tmpdir, "测试")
            self.assertEqual(len(result), 1)
            self.assertIn("example.txt", result[0][0])
    
    def test_search_content_not_found(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "example.txt")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write("没有关键字\n")

            result = search_content(tmpdir, "不存在的关键字")
            self.assertEqual(result, [])

    def test_search_filename_found(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "测试文件.txt")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write("dummy")

            result = search_filename(tmpdir, "测试")
            self.assertEqual(len(result), 1)
            self.assertIn("测试文件.txt", result[0])

    def test_search_filename_not_found(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_path = os.path.join(tmpdir, "example.txt")

            with open(file_path, "w", encoding="utf-8") as f:
                f.write("hello")

            result = search_filename(tmpdir, "不存在")
            self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
