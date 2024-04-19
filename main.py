import argparse


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


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
