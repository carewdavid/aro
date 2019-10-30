import argparse

def main():
    parser argparse.ArgumentParser(description="Tag based file manager")
    parser.add_argument("--search", "-s", nargs="*", help="list of tags to search", required=False)
    parser.add_argument("--add", "-a", nargs="+", help="add file(s) to database", required=False)
    parser.add_argument("--tags", "-t", nargs="+", help="add tags to file(s)", required=False)
    parser.add_argument("--db", nargs=1)
    args = parser.parse_args()

    

