from logger_config import setup_logger
from searcher import search_content, search_filename

def main():
    print("===File Search Tool===")
    setup_logger()

    mode = input("Search mode: input 'C' for content or input 'N' for filename\n").strip().lower()
    if mode not in ('n', 'c'):
        print("Invalid mode. Choose 'content(C)' or 'filename(N)'.")
        return
    
    root = input("Search directory: ")
    keyword = input("Keyword: ")

    if mode == 'c':
        results = search_content(root, keyword)
        print("\n=== Content Search Results ===")
        if not results:
            print("No matches found.")
        else:
            for path, line_no, text in results:
                print(f"{path}:{line_no}    {text}")
    if mode == 'n':
        print("\n=== Filename Search Results ===")
        results = search_filename(root, keyword)
        if not results:
            print("No matches found.")
        else:
            for path in results:
                print(path)

if __name__ == "__main__":
    main()
