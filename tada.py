"""Run doubling experiments and 'Tada!' you get the time complexity"""

import subprocess

import perf


UTF8 = "utf-8"
CONFIGURATION = ".configuration.txt"


def run_command(command):
    """Run a command and return the output and error code"""
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    return output, error


def save_configuration(configurationfile, size):
    """Save the current size for the doubling experiment to a file"""
    with open(configurationfile, "w") as fp:
        fp.write(str(size))


def display_output(timingoutput):
    """Display the timing output as long as it is not empty"""
    if timingoutput != "":
        print(timingoutput)


def read_benchmark_results(resultsfile):
    """Read the results from a JSON file and return a benchmark"""


if __name__ == "__main__":
    # setup parameters of a simple doubling experiment
    size = 100
    factor = 2
    size_stop = 200
    save_configuration(CONFIGURATION, size)
    # perform the small doubling experiment
    while size <= size_stop:
        # run the benchmark by using it through python
        print("Start running experiment for size " + str(size) + " →\n")
        current_output, current_error = run_command("python3 perf_mcopies_ofc.py")
        # display the standard output and error
        display_output(current_output.decode(UTF8))
        display_output(current_error.decode(UTF8))
        print("→ Done running experiment for size " + str(size) + "\n")
        # go to the next size for the doubling experiment
        size = size * 2
        # write the next doubling experiment size to the file
        save_configuration(CONFIGURATION, size)