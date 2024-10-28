"""
Part 3: Short Exercises on the Shell

**Released: Friday, October 18**

For the third and last part of this homework,
we will complete a few tasks related to shell programming
and shell commands, particularly, with relevance to how
the shell is used in data science.

Please note:
The "project proposal" portion will be postponed to part of Homework 2.

===== Questions 1-5: Setup Scripting =====

1. For this first part, let's write a setup script
that downloads a dataset from the web,
clones a GitHub repository, and runs the Python script
contained in `script.py` on the dataset in question.

For the download portion, we have written a helper
download_file(url, filename) which downloads the file
at `url` and saves it in `filename`.

You should use Python subprocess to run all of these operations.

To test out your script, and as your answer to this part,
run the following:
    setup(
        "https://github.com/DavisPL-Teaching/119-hw1",
        "https://raw.githubusercontent.com/DavisPL-Teaching/119-hw1/refs/heads/main/data/test-input.txt",
        "test-script.py"
    )

Then read the output of `output/test-output.txt`,
convert it to an integer and return it. You should get "12345".

"""

# You may need to conda install requests or pip3 install requests
import requests
import os 
import subprocess
import part2

def download_file(url, filename):
    r = requests.get(url)
    with open(filename, 'wb') as f:
        f.write(r.content)

def clone_repo(repo_url):

    os.system(f"git clone {repo_url}")

def run_script(script_path, data_path):

    os.system(f"python {script_path} {data_path}")

def setup(repo_url, data_url, script_path):
    # Download the data file
    clone_repo(repo_url)

    download_file(data_url, "data.txt")

    run_script(script_path, "data.txt")


def q1():
    # Call setup as described in the prompt

    setup(
        "https://github.com/DavisPL-Teaching/119-hw1",
        "https://raw.githubusercontent.com/DavisPL-Teaching/119-hw1/refs/heads/main/data/test-input.txt",
        "test-script.py"
    )

    # TODO
    # Read the file test-output.txt to a string
    # Convert the string to an integer

    with open("output/test-output.txt", "r") as f:
        output = f.read()

    inter =  int(output)

    # TODO
    # Return the integer value of the output
    return inter
    # TODO

"""
2.
Suppose you are on a team of 5 data scientists working on
a project; every 2 weeks you need to re-run your scripts to
fetch the latest data and produce the latest analysis.

a. When might you need to use a script like setup() above in
this scenario?

=== ANSWER Q2a BELOW ===

it make it faster to download the data and run the script. Also it does the same thing every time 
so if some one else has to do it it would be the same every time.

=== END OF Q2a ANSWER ===

Do you see an alternative to using a script like setup()?

=== ANSWER Q2b BELOW ===

make a website that does it for you but it probaly has to do somthing similar to the setup() function.

=== END OF Q2b ANSWER ===

3.
Now imagine we have to re-think our script to
work on a brand-new machine, without any software installed.
(For example, this would be the case if you need to run
your pipeline inside an Amazon cloud instance or inside a
Docker instance -- to be more specific you would need
to write something like a Dockerfile, see here:
https://docs.docker.com/reference/dockerfile/
which is basically a list of shell commands.)

Don't worry, we won't test your code for this part!
I just want to see that you are thinking about how
shell commands can be used for setup and configuration
necessary for data processing pipelines to work.

Think back to HW0. What sequence of commands did you
need to run?
Write a function setup_for_new_machine() that would
be able to run on a brand-new machine and set up
everything that you need.

Assume that you need your script to work on all of the packages
that we have used in HW1 (that is, any `import` statements
and any other software dependencies).

Assume that the new server machine is identical
in operating system and architecture to your own,
but it doesn't have any software installed.
It has Python 3.12
and conda or pip3 installed to get needed packages.

Hint: use subprocess again!

Hint: search for "import" in parts 1-3. Did you miss installing
any packages?
"""



def setup_for_new_machine():

    subprocess.run(['sudo', 'apt-get', 'update'], check=True)
    subprocess.run(['sudo', 'apt-get', 'install', '-y', 'git'], check=True)

    # Install conda packages
    subprocess.run(['conda', 'install', '-c', 'conda-forge', 'pyspark'], check=True)

    # Install pip packages
    subprocess.run(['pip', 'install', 'pandas', 'pytest', 'pyspark'], check=True)

    # Verify installations (you can add more if needed)
    subprocess.run(['python', '--version'], check=True)
    subprocess.run(['pip', '--version'], check=True)
    subprocess.run(['conda', '--version'], check=True)

def q3():
    # As your answer, return a string containing
    # the operating system name that you assumed the
    # new machine to have.
    os = 'MacOS'
    return os

"""
4. This question is open ended :)
It won't be graded for correctness.

What percentage of the time do you think real data scientists
working in larger-scale projects in industry have to write
scripts like setup() and setup_for_new_machine()
in their day-to-day jobs?

=== ANSWER Q4 BELOW ===

Like 10 percent of there time. I think that software dev woulddo this instead.

=== END OF Q4 ANSWER ===

5. Extra credit

Copy your setup_for_new_machine() function from Q3
(remove the other code in this file)
to a new script and run it on a friend's machine who
is not in this class. Did it work? What problems did you run into?

Only answer this if you actually did the above.
Paste the output you got when running the script on the
new machine:

=== ANSWER Q5 BELOW ===

=== END OF Q5 ANSWER ===

===== Questions 6-9: A comparison of shell vs. Python =====

The shell can also be used to process data.

This series of questions will be in the same style as part 2.
Let's import the part2 module:
"""

import part2
import pandas as pd

"""
Write two versions of a script that takes in the population.csv
file and produces as output the number of rows in the file.
The first version should use shell commands and the second
should use Pandas.

For technical reasons, you will need to use
os.popen instead of subprocess.run for the shell version.
Example:
    os.popen("echo hello").read()

Runs the command `echo hello` and returns the output as a string.

Hints:
    1. Given a file, you can print it out using
        cat filename

    2. Given a shell command, you can use the `tail` command
        to skip the first line of the output. Like this:

    (shell command that spits output) | tail -n +2

    Note: if you are curious why +2 is required here instead
        of +1, that is an odd quirk of the tail command.
        See here: https://stackoverflow.com/a/604871/2038713

    3. Given a shell command, you can use the `wc` command
        to count the number of lines in the output

   (shell command that spits output) | wc -l
"""

def pipeline_shell():

    file_path = "data/population.csv"

    a = os.popen(f'wc -l < {file_path}').read().strip()

    return int(a)
    # Return resulting integer

def pipeline_pandas():

    file_path = "data/population.csv"

    a = pd.read_csv(file_path)
    return int(a.shape[0])

    # Return resulting integer

def q6():
    # As your answer to this part, check that both
    # integers are the same and return one of them.
    # 
    oss = pipeline_shell()
    pdd = pipeline_pandas()

    if oss == pdd:
        return oss
    else:
        return f"Not the same {oss} and {pdd}"

"""
Let's do a performance comparison between the two methods.

This time, no need to generate a plot.
Just use your ThroughputHelper and LatencyHelper classes
from part 2 to get answers for both pipelines.

7. Throughput
"""

def q7():
    # Return a tuple of two floats
    # throughput for shell, throughput for pandas
    # (in rows per second)

    a = part2.ThroughputHelper()

    a.add_pipeline("OSS", 59177,pipeline_shell)
    a.add_pipeline("Pandas",59177,pipeline_pandas)

    a.compare_throughput()

    return a.throughputs

"""
8. Latency
"""

def q8():
    # Return a tuple of two floats
    # latency for shell, latency for pandas
    # (in milliseconds)
    # TODO

    a = part2.LatencyHelper()
    a.add_pipeline("OSS",pipeline_shell)
    a.add_pipeline("Pandas",pipeline_pandas)

    a.compare_latency()

    return a.latencies


"""
9. Which method is faster?
Comment on anything else you notice below.

=== ANSWER Q9 BELOW ===

oss,pandas 
[9_024_168 6_402_635.621811059]

[7.225233300414402, 9.542654099641368]
The Shell is faster than pandas by 2.3 milliseconds in latency and 2_621_532 rows per second in throughput.
=== END OF Q9 ANSWER ===
"""

"""
===== Wrapping things up =====

**Don't modify this part.**

To wrap things up, we have collected
your answers and saved them to a file below.
This will be run when you run the code.
"""

ANSWER_FILE = "output/part3-answers.txt"
UNFINISHED = 0

def log_answer(name, func, *args):
    try:
        answer = func(*args)
        print(f"{name} answer: {answer}")
        with open(ANSWER_FILE, 'a') as f:
            f.write(f'{name},{answer}\n')
            print(f"Answer saved to {ANSWER_FILE}")
    except NotImplementedError:
        print(f"Warning: {name} not implemented.")
        with open(ANSWER_FILE, 'a') as f:
            f.write(f'{name},Not Implemented\n')
        global UNFINISHED
        UNFINISHED += 1

def PART_3_PIPELINE():
    open(ANSWER_FILE, 'w').close()

    # Q1-5
    log_answer("q1", q1)
    # 2a: commentary
    # 2b: commentary
    log_answer("q3", q3)
    # 4: commentary
    # 5: extra credit
    log_answer("q6", q6)
    log_answer("q7", q7)
    log_answer("q8", q8)
    # 9: commentary

    # Answer: return the number of questions that are not implemented
    if UNFINISHED > 0:
        print("Warning: there are unfinished questions.")

    return UNFINISHED

"""
=== END OF PART 3 ===

Main function
"""

if __name__ == '__main__':
    log_answer("PART 3", PART_3_PIPELINE)
