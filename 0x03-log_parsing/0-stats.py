#!/usr/bin/python3
"""An interview question on log parsing"""

def parse_log_line(line):
    """
    Parses a log line and extracts the status code and file size.

    Args:
        line (str): A log line in the specified format.

    Returns:
        tuple: (status_code, file_size) if the line is valid, else
        (None, None).
    """
    try:
        _, _, _, _, _, status_code, file_size = line.split()
        return int(status_code), int(file_size)
    except ValueError:
        return None, None


def main():
    """
    Reads log lines from stdin, computes metrics, and prints statistics.

    Metrics:
    - Total file size
    - Number of lines by status code (200, 301, 400, 401, 403, 404, 405, 500)
    """
    total_file_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0,
                     500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            status_code, file_size = parse_log_line(line)
            if status_code is not None:
                total_file_size += file_size
                status_counts[status_code] += 1
                line_count += 1

                if line_count % 10 == 0:
                    print(f"File size: {total_file_size}")
                    for code in sorted(status_counts.keys()):
                        if status_counts[code] > 0:
                            print(f"{code}: {status_counts[code]}")

    except KeyboardInterrupt:
        # Print final statistics when interrupted (CTRL + C)
        print(f"File size: {total_file_size}")
        for code in sorted(status_counts.keys()):
            if status_counts[code] > 0:
                print(f"{code}: {status_counts[code]}")
        sys.exit(0)

if __name__ == "__main__":
    import sys
    main()
