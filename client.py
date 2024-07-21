import argparse
import json


from application import (
    add_text_to_collection, 
    get_answer, 
    verify_pdf_path, 
    clear_coll
  )

from messaging import post_message_to_slack

def main():
    parser = argparse.ArgumentParser(description="PDF Processing CLI Tool")
    parser.add_argument("-f", "--file", help="Path to the input PDF file")
    parser.add_argument("-v", "--value",default=1000, type=int, help="Optional integer value for no. words in a single chunk")
    parser.add_argument("-q", "--question",nargs="+", help="Ask question(s)")
    parser.add_argument("-c", "--clear", type = bool, help = "Clear existing collection data")
    parser.add_argument('-n', "--number", type = int, default=1, help = "Optional Number of results to be fetched from collection")

    args = parser.parse_args()
    
    if args.file is not None:
        verify_pdf_path(args.file)
        confirmation = add_text_to_collection(file = args.file, word = args.value)
        print(confirmation)

    if args.question is not None:
        if args.number:
            n = args.number
        else:
            n = 1
        outputlist = list()
        for i in args.question:
            answer = get_answer(i, n = n)
            outputlist.append({"question": i, "answer": answer})
        json_data = json.dumps(outputlist)
        response = post_message_to_slack(json_data)
        print(response)
    if args.clear:
        clear_coll()
        return "Current collection cleared successfully"


if __name__ == "__main__":
    main()