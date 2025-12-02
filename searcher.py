import os
import logging

def search_content(root_path, keyword):
    results = []

    # 检查目录是否存在
    if not os.path.exists(root_path):
        logging.error(f"Directory not found: {root_path}")
        raise FileNotFoundError("Search directory does not exist.")
    
    # 遍历目录
    for dirpath, _, files in os.walk(root_path):
        for filename in files:
            file_path = os.path.join(dirpath, filename)

            try:
                # 尝试按 UTF-8 读取文件
                with open(file_path, 'r', encoding='utf-8') as f:
                    for idx, line in enumerate(f, 1):
                        if keyword in line:
                            # 保存结果
                            results.append((file_path, idx, line.strip()))
                            logging.info(f"Match found in {file_path}:{idx}")

            except Exception as e:
                # 捕获无法读取的文件（权限、编码错误等）
                logging.warning(f"Cannot read {file_path}: {e}")

    return results

def search_filename(root_path, keyword):
    results = []

    # 检查目录是否存在
    if not os.path.exists(root_path):
        logging.error(f"Directory not found: {root_path}")
        raise FileNotFoundError("Search directory does not exist.")

    for dirpath, _, files in os.walk(root_path):
        for filename in files:
            if keyword in filename:
                file_path = os.path.join(dirpath, filename)
                results.append(file_path)
                logging.info(f"Matched filename: {file_path}")

    return results