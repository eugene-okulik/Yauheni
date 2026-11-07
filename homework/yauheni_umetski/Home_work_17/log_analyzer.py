import os
import argparse
import re


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Log analyzer that searches for keywords and extracts error blocks with surrounding context."
    )

    parser.add_argument('path', help="full log file path")

    parser.add_argument('--text', help="text to search in the log file")

    parser.add_argument('--first-only', action='store_true', help="stop after finding the first match")

    return parser.parse_args()


def get_files_list(path: str) -> list[str]:
    if not os.path.exists(path):
        return []

    if not os.path.isdir(path):
        return [path]

    return [entry.path for entry in os.scandir(path) if entry.is_file()]


def extract_log_blocks(file_path: str) -> dict[str, str]:
    TIME_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}")
    blocks = {}
    current_time = None

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:
            match = TIME_PATTERN.match(line)

            if match:
                current_time = match.group()
                blocks[current_time] = line
            else:
                if current_time is not None:
                    blocks[current_time] += line
    return blocks


def filter_log_blocks(blocks: dict[str, str], filter: str) -> list[str]:
    filtered_block = {k: v for k, v in blocks.items() if filter in v}

    if not filtered_block:
        return []

    result = []

    for block_text in filtered_block.values():
        words = block_text.split()

        try:
            index = next(i for i, word in enumerate(words) if filter in word)
        except StopIteration:
            index = 0

        start_index = max(0, index - 5)
        end_index = index + 6

        log_text = " ".join(words[start_index: end_index])
        result.append(log_text)
    return result


def main():
    args = parse_args()

    if not args.text:
        print("Please enter arguments")
        return

    files = get_files_list(args.path)

    if not files:
        print(f"No files in: {args.path}")
        return

    found_any = False

    for file_path in files:
        blocks = extract_log_blocks(file_path)

        matches = filter_log_blocks(blocks, args.text)

        if matches:
            print(f"File: {file_path}.")

            for match in matches:
                print(match)
                found_any = True

                if args.first_only:
                    print("First match found")
                    return

    if not found_any:
        print("No match found")


if __name__ == "__main__":
    main()
