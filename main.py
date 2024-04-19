import argparse

# Main application file

from file_handler import read_file, save_to_file, get_next_version_number
from text_analysis import analyze_text_with_nltk, analyze_text_with_spacy
from api_interaction import call_api
from user_interaction import get_user_role_choice, get_user_input
from error_handling import handle_file_error, handle_api_error, handle_user_input_error


def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="JobMatch Maker CLI")

    # Add arguments
    parser.add_argument("-re", "--resume", type=str, help="Path to the resume file.")
    parser.add_argument("-job", "--jobdesc", type=str, help="Path to the job description file.")

    # Parse the arguments
    args = parser.parse_args()

    # TODO: Add functionality here
    # Read the content of the resume & Job description files
    resume_content = read_file(args.resume)
    job_desc_content = read_file(args.jobdesc)

    print(f"Resume file content:\n{resume_content}")
    print(f"Job description file content:\n{job_desc_content}")


if __name__ == "__main__":
    main()
