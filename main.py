import argparse

from file_handler import load_file_content


def run_jobmatch_maker_cli():
    argument_parser = argparse.ArgumentParser(description='JobMatch Maker CLI')
    argument_parser.add_argument('-re', '--resume', type=str, help='Path to the resume file.')
    argument_parser.add_argument('-job', '--jobdesc', type=str, help='Path to the job description file.')
    arguments = argument_parser.parse_args()
    resume_content = load_file_content(arguments.resume)
    job_description_content = load_file_content(arguments.jobdesc)
    print(f'Resume file content:\n{resume_content}')
    print(f'Job description file content:\n{job_description_content}')

if __name__ == '__main__':
    run_jobmatch_maker_cli()
