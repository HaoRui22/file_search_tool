import argparse
from logger_config import setup_logger
from searcher import search_content, search_filename

from colorama import init, Fore, Style

# 启用 colorama
init(autoreset=True)

def print_with_paging(lines, page_size=20):
    '''分页显示 long output'''
    count= 0
    for line in lines:
        print(line)
        count += 1

        if count >= page_size:
            user = input(Fore.YELLOW + "---按 Enter 查看更多， 输入 q 退出---")
            if user.lower() == 'q':
                return
            count = 0

def main():
    setup_logger()

    parser = argparse.ArgumentParser(description='File Search Tool')
    parser.add_argument("-m", "--mode", choices=["content", "name"], required=True,
                        help="Search mode: content or name")
    parser.add_argument("-d", "--directory", required=True,
                        help="Directory to search")
    parser.add_argument("-k", "--keyword", required=True,
                        help="Keyword to search")
    
    args = parser.parse_args()

    # 执行搜索
    if args.mode == "content":
        results = search_content(args.directory, args.keyword)

        # 自动计算对齐宽度
        if results:
            max_len = max(len(f"{path}:{line_no}") for path, line_no, _ in results)
        else:
            max_len = 30

        print(Fore.CYAN + "\n=== Content Search Results ===")
        if not results:

            print(Fore.RED + "No matches found.")
            return
        
        output_lines = []

        for path, line_no, text in results:
            left = f"{path}:{line_no}".ljust(max_len)
            # 高亮关键字
            highlighted = text.replace(args.keyword,
                                       Fore.RED + args.keyword + Style.RESET_ALL)
            output_lines.append(f"{Fore.GREEN}{left}{Style.RESET_ALL}    {highlighted}")
            print_with_paging(output_lines)

    if args.mode == "name":
        results = search_filename(args.directory, args.keyword)

        print(Fore.CYAN + "\n=== Filename Search Results ===")

        if not results:
            print(Fore.RED + "No matches found.")
            return
        
        output_lines = [f"{Fore.GREEN}{path}{Style.RESET_ALL}" for path in results]
        print_with_paging(output_lines)

if __name__ == "__main__":
    main()
