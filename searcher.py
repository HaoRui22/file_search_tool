import os
import logging

def search_keyword(root_path, keyword):
    results = []

    if not os.path.exists(root_path):
        logging.error(f"Directory not found: {root_path}")
        raise FileNotFoundError("Search directory does not exist.")

    for dirpath, _, files in os.walk(root_path):
        for filename in files:
            file_path = os.path.join(dirpath, filename)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    for idx, line in enumerate(f, 1):
                        if keyword in line:
                            results.append((file_path, idx, line.strip()))
                            logging.info(f"Match found in {file_path}:{idx}")

            except Exception as e:
                logging.warning(f"Cannot read {file_path}: {e}")

    return results
