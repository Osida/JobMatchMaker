import argparse

from file_handler import load_file_content, print_file_content


def run_jobmatch_maker_cli():
    argument_parser = argparse.ArgumentParser(description='JobMatch Maker CLI')
    argument_parser.add_argument('-re', '--resume', type=str, help='Path to the resume file.')
    argument_parser.add_argument('-job', '--jobdesc', type=str, help='Path to the job description file.')
    arguments = argument_parser.parse_args()
    resume_content = load_file_content(arguments.resume)
    job_description_content = load_file_content(arguments.jobdesc)
    print_file_content(resume_content, 'Resume')
    print_file_content(job_description_content, 'Job Description')


if __name__ == '__main__':
    run_jobmatch_maker_cli()
