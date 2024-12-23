"""
Part 2: Performance Comparisons

**Released: Wednesday, October 16**

In this part, we will explore comparing the performance
of different pipelines.
First, we will set up some helper classes.
Then we will do a few comparisons
between two or more versions of a pipeline
to report which one is faster.
"""

import part1
import matplotlib.pyplot as plt
import timeit
import pandas as pd
"""
=== Questions 1-5: Throughput and Latency Helpers ===

We will design and fill out two helper classes.

The first is a helper class for throughput (Q1).
The class is created by adding a series of pipelines
(via .add_pipeline(name, size, func))
where name is a title describing the pipeline,
size is the number of elements in the input dataset for the pipeline,
and func is a function that can be run on zero arguments
which runs the pipeline (like def f()).

The second is a similar helper class for latency (Q3).

1. Throughput helper class

Fill in the add_pipeline, eval_throughput, and generate_plot functions below.
"""

# Number of times to run each pipeline in the following results.
# You may modify this if any of your tests are running particularly slow
# or fast (though it should be at least 10).
NUM_RUNS = 10
class ThroughputHelper:
    def __init__(self):
        # Initialize the object.
        # Pipelines: a list of functions, where each function
        # can be run on no arguments.
        # (like: def f(): ... )
        self.pipelines = []

        # Pipeline names
        # A list of names for each pipeline
        self.names = []

        # Pipeline input sizes
        self.sizes = []

        # Pipeline throughputs
        # This is set to None, but will be set to a list after throughputs
        # are calculated.
        self.throughputs = None

    def add_pipeline(self, name, size, func):

        self.pipelines.append(func)
        self.names.append(name)
        self.sizes.append(size)


    def compare_throughput(self):
        # Measure the throughput of all pipelines
        # and store it in a list in self.throughputs.
        # Make sure to use the NUM_RUNS variable.
        # Also, return the resulting list of throughputs,
        # in **number of items per second.**
        self.throughputs = []

        for i in range(len(self.pipelines)):  

            pipeline = self.pipelines[i]
            num_items = self.sizes[i]
            execution_time = timeit.timeit(pipeline, number=NUM_RUNS)#run the funciton "NUM_RUNS" times 
            throughput = num_items * NUM_RUNS / execution_time
            self.throughputs.append(throughput)

        


    def generate_plot(self, filename):
        # Generate a plot for throughput using matplotlib.
        # You can use any plot you like, but a bar chart probably makes
        # the most sense.
        # Make sure you include a legend.
        # Save the result in the filename provided.
        plt.figure(figsize=(17, 10))
        plt.bar(self.names, self.throughputs)
        plt.tight_layout()
        plt.xticks(fontsize = 9)
        plt.savefig(filename)
        plt.close()
"""
As your answer to this part,
return the name of the method you decided to use in
matplotlib.

(Example: "boxplot" or "scatter")
"""

def q1():
    return "barplot"
    # Return plot method (as a string) from matplotlib
"""
2. A simple test case

To make sure your monitor is working, test it on a very simple
pipeline that adds up the total of all elements in a list.

We will compare three versions of the pipeline depending on the
input size.
"""

LIST_SMALL = [10] * 100
LIST_MEDIUM = [10] * 100_000
LIST_LARGE = [10] * 100_000_000

def add_list(l):
    tot = 0
    for i in l:
        tot += i

    return tot



def q2a():
    # Create a ThroughputHelper object
    h = ThroughputHelper()
    # Add the 3 pipelines.
    # (You will need to create a pipeline for each one.)
    # Pipeline names: small, medium, large

    h.add_pipeline("small", len(LIST_SMALL), lambda:add_list(LIST_SMALL))

    h.add_pipeline("medium", len(LIST_MEDIUM), lambda:add_list(LIST_MEDIUM))

    h.add_pipeline("large", len(LIST_LARGE),lambda: add_list(LIST_LARGE))
    # Generate a plot.
    # Save the plot as 'output/q2a.png'.
    h.compare_throughput()
    h.generate_plot("output/q2a.png")
    # Finally, return the throughputs as a list.
    return h.throughputs

"""
2b.
Which pipeline has the highest throughput?
Is this what you expected?

=== ANSWER Q2b BELOW ===

The list large has the biggest throughput of 62874904.882991575


=== END OF Q2b ANSWER ===
"""

"""
3. Latency helper class.

Now we will create a similar helper class for latency.

The helper should assume a pipeline that only has *one* element
in the input dataset.

It should use the NUM_RUNS variable as with throughput.
"""

class LatencyHelper:
    def __init__(self):
        # Initialize the object.
        # Pipelines: a list of functions, where each function
        # can be run on no arguments.
        # (like: def f(): ... )
        self.pipelines = []

        # Pipeline names
        # A list of names for each pipeline
        self.names = []

        # Pipeline latencies
        # This is set to None, but will be set to a list after latencies
        # are calculated.
        self.latencies = None

    def add_pipeline(self, name, func):
        self.pipelines.append(func)
        self.names.append(name)
    
    def compare_latency(self):

        self.latencies = []

        for i in range(len(self.pipelines)):
            pipeline = self.pipelines[i]
            execution_time = timeit.timeit(pipeline, number=NUM_RUNS)
            latency = execution_time / NUM_RUNS * 1000
            self.latencies.append(latency)


        # Measure the latency of all pipelines
        # and store it in a list in self.latencies.
        # Also, return the resulting list of latencies,
        # in **milliseconds.**

    def generate_plot(self, filename):
        # Generate a plot for latency using matplotlib.
        # You can use any plot you like, but a bar chart probably makes
        # the most sense.
        # Make sure you include a legend.
        # Save the result in the filename provided.
        plt.bar(self.names, self.latencies)
        plt.savefig(filename)
        plt.close()


"""
As your answer to this part,
return the number of input items that each pipeline should
process if the class is used correctly.
"""

def q3():
    return 1
    # Return the number of input items in each dataset,
    # for the latency helper to run correctly


"""
4. To make sure your monitor is working, test it on
the simple pipeline from Q2.

For latency, all three pipelines would only process
one item. Therefore instead of using
LIST_SMALL, LIST_MEDIUM, and LIST_LARGE,
for this question run the same pipeline three times
on a single list item.
"""

LIST_SINGLE_ITEM = [10] # Note: a list with only 1 item

def q4a():
    # Create a LatencyHelper object
    h = LatencyHelper()
    h.add_pipeline("1", lambda:add_list(LIST_SINGLE_ITEM))
    h.add_pipeline("2", lambda:add_list(LIST_SINGLE_ITEM))
    h.add_pipeline("3", lambda:add_list(LIST_SINGLE_ITEM))
    # Add the single pipeline three times.

    # Generate a plot.
    # Save the plot as 'output/q4a.png'.
    h.compare_latency()
    h.generate_plot("output/q4a.png")
    # Finally, return the latencies as a list.
    return h.latencies

"""
4b.
How much did the latency vary between the three copies of the pipeline?
Is this more or less than what you expected?

=== ANSWER Q1b BELOW ===


I thouhg it would run more constintly but it first run of the function took a lot longer comparered to next ones

=== END OF Q1b ANSWER ===
"""

"""
Now that we have our helpers, let's do a simple comparison.

NOTE: you may add other helper functions that you may find useful
as you go through this file.

5. Comparison on Part 1

Finally, use the helpers above to calculate the throughput and latency
of the pipeline in part 1.
"""

# You will need these:
# part1.load_input
# part1.PART_1_PIPELINE

def q5a():
    # Return the throughput of the pipeline in part 1.

    part1.load_input()
    part1.PART_1_PIPELINE()

    h = ThroughputHelper()
    h.add_pipeline("part1", 1, part1.PART_1_PIPELINE)
    h.compare_throughput()
    return h.throughputs

def q5b():
    # Return the latency of the pipeline in part 1.
    part1.load_input()
    part1.PART_1_PIPELINE()
    h = LatencyHelper()
    h.add_pipeline("part1", part1.PART_1_PIPELINE)
    h.compare_latency()
    return h.latencies


"""
===== Questions 6-10: Performance Comparison 1 =====

For our first performance comparison,
let's look at the cost of getting input from a file, vs. in an existing DataFrame.

6. We will use the same population dataset
that we used in lecture 3.

Load the data using load_input() given the file name.

- Make sure that you clean the data by removing
  continents and world data!
  (World data is listed under OWID_WRL)

Then, set up a simple pipeline that computes summary statistics
for the following:

- *Year over year increase* in population, per country

    (min, median, max, mean, and standard deviation)

How you should compute this:

- For each country, we need the maximum year and the minimum year
in the data. We should divide the population difference
over this time by the length of the time period.

- Make sure you throw out the cases where there is only one year
(if any).

- We should at this point have one data point per country.

- Finally, as your answer, return a list of the:
    min, median, max, mean, and standard deviation
  of the data.

Hints:
You can use the describe() function in Pandas to get these statistics.
You should be able to do something like
df.describe().loc["min"]["colum_name"]

to get a specific value from the describe() function.

You shouldn't use any for loops.
See if you can compute this using Pandas functions only.
"""

def load_input(filename):
    data_pd = pd.read_csv(filename)
    data_pd_clean =  data_pd[(data_pd["Code"] != "OWID_WRL") & (data_pd["Code"].notna())]

    #data_pd_clean['partition_count'] = data_pd_clean.groupby(['Entity'])['Entity'].transform('count')

    #final_daa = data_pd_clean[data_pd_clean['partition_count'] > 1]
    #final_daa = final_daa.drop(columns=['partition_count'])
    return data_pd_clean

    # Return a dataframe containing the population data
    # **Clean the data here**

def population_pipeline(df):
    df =  pd.read_csv('data/population.csv')


    grouped_df = df.groupby('Entity').agg(
        Year_Min=('Year', 'min'),
        Year_Max=('Year', 'max')
    ).reset_index()

    min_years = pd.merge(grouped_df, df, left_on=['Entity', 'Year_Min'], right_on=['Entity', 'Year'])
    min_years = min_years[['Entity', 'Year_Min', 'Population (historical)']]

    max_years = pd.merge(grouped_df, df, left_on=['Entity', 'Year_Max'], right_on=['Entity', 'Year'])
    max_years = max_years[['Entity', 'Year_Max', 'Population (historical)']]


    min_max_merge = min_years.merge(max_years,on = 'Entity')

    min_max_merge['gradiant'] = (min_max_merge['Population (historical)_y'] - min_max_merge['Population (historical)_x']) / (min_max_merge['Year_Max'] - min_max_merge['Year_Min'])

    rate = min_max_merge['gradiant'] 
    return [rate.min(), rate.median(), rate.max(), rate.mean(), rate.std()]
    # Input: the dataframe from load_input()
    # Return a list of min, median, max, mean, and standard deviation

def q6():
    a = load_input("data/population.csv")
    stats = population_pipeline(a)
    # As your answer to this part,
    # call load_input() and then population_pipeline()
    # Return a list of min, median, max, mean, and standard deviation
    return stats

"""
7. Varying the input size

Next we want to set up three different datasets of different sizes.

Create three new files,
    - data/population-small.csv
      with the first 600 rows
    - data/population-medium.csv
      with the first 6000 rows
    - data/population-single-row.csv
      with only the first row
      (for calculating latency)

You can edit the csv file directly to extract the first rows
(remember to also include the header row)
and save a new file.

Make four versions of load input that load your datasets.
(The _large one should use the full population dataset.)
"""
    
pop_csv_read_in = pd.read_csv('data/population.csv')

def load_input_small():
    pop_csv_read_in.head(600).to_csv('data/population-small.csv',index = False )
    return pd.read_csv('data/population-small.csv')

def load_input_medium():
     pop_csv_read_in.head(6000).to_csv('data/population-medium.csv',index = False )
     return pd.read_csv('data/population-medium.csv')

def load_input_large():
    return pop_csv_read_in

def load_input_single_row():
     pop_csv_read_in.head(1).to_csv('data/population-single-row.csv',index = False )
     return pd.read_csv('data/population-single-row.csv')
    # This is the pipeline we will use for latency.

def q7():
    # Don't modify this part
    s = load_input_small()
    m = load_input_medium()
    l = load_input_large()
    x = load_input_single_row()
    return [len(s), len(m), len(l), len(x)]

"""
8.
Create baseline pipelines

First let's create our baseline pipelines.
Create four pipelines,
    baseline_small
    baseline_medium
    baseline_large
    baseline_latency

based on the three datasets above.
Each should call your population_pipeline from Q7.
"""

def baseline_small():
    stats = population_pipeline(load_input_small())
    

def baseline_medium():
    stats = population_pipeline(load_input_medium())
    

def baseline_large():
    stats = population_pipeline(load_input_large())
   
def baseline_latency():
    stats = population_pipeline(load_input_single_row())
   

def q8():
    # Don't modify this part
    _ = baseline_medium()
    return ["baseline_small", "baseline_medium", "baseline_large", "baseline_latency"]

"""
9.
Finally, let's compare whether loading an input from file is faster or slower
than getting it from an existing Pandas dataframe variable.

Create four new dataframes (constant global variables)
directly in the script.
Then use these to write 3 new pipelines:
    fromvar_small
    fromvar_medium
    fromvar_large
    fromvar_latency

As your answer to this part;
a. Generate a plot in output/q9a.png of the throughputs
    Return the list of 6 throughputs in this order:
    baseline_small, baseline_medium, baseline_large, fromvar_small, fromvar_medium, fromvar_large
b. Generate a plot in output/q9b.png of the latencies
    Return the list of 2 latencies in this order:
    baseline_latency, fromvar_latency
"""


POPULATION_SMALL = load_input_small()
POPULATION_MEDIUM = load_input_medium()
POPULATION_LARGE = load_input_large()
POPULATION_SINGLE_ROW = load_input_single_row()

def fromvar_small():
    stat = population_pipeline(POPULATION_SMALL)

def fromvar_medium():
    stat = population_pipeline(POPULATION_MEDIUM)

def fromvar_large():
    stat = population_pipeline(POPULATION_LARGE)
 
def fromvar_latency():
    stat = population_pipeline(POPULATION_SINGLE_ROW)
   

def q9a():

    h = ThroughputHelper()
    h.add_pipeline("baseline_small", len(POPULATION_SMALL), baseline_small)
    h.add_pipeline("baseline_medium", len(POPULATION_MEDIUM), baseline_medium)
    h.add_pipeline("baseline_large", len(POPULATION_LARGE), baseline_large)

    h.add_pipeline("fromvar_small", len(POPULATION_SMALL), fromvar_small)
    h.add_pipeline("fromvar_medium", len(POPULATION_MEDIUM), fromvar_medium)
    h.add_pipeline("fromvar_large", len(POPULATION_LARGE), fromvar_large)

    h.compare_throughput()
    h.generate_plot("output/q9a.png")
    return h.throughputs

    # Add all 6 pipelines for a throughput comparison
    # Generate plot in ouptut/q9a.png
    # Return list of 6 throughputs
def q9b():
    h = LatencyHelper()
    h.add_pipeline("baseline_latency", baseline_latency)
    h.add_pipeline("fromvar_latency", fromvar_latency)
    h.compare_latency()
    h.generate_plot("output/q9b.png")
    return h.latencies
    # Add 2 pipelines for a latency comparison
    # Generate plot in ouptut/q9b.png
    # Return list of 2 latencies
   

"""
10.
Comment on the plots above!
How dramatic is the difference between the two pipelines?
Which differs more, throughput or latency?
What does this experiment show?

===== ANSWER Q10 BELOW =====
In mine very dramatic. I think it becuase i used a good amount of pandas fucntin within mine 
===== END OF Q10 ANSWER =====
"""

"""
===== Questions 11-14: Performance Comparison 2 =====

Our second performance comparison will explore vectorization.

Operations in Pandas use Numpy arrays and vectorization to enable
fast operations.
In particular, they are often much faster than using for loops.

Let's explore whether this is true!

11.
First, we need to set up our pipelines for comparison as before.

We already have the baseline pipelines from Q8,
so let's just set up a comparison pipeline
which uses a for loop to calculate the same statistics.

Create a new pipeline:
- Iterate through the dataframe entries. You can assume they are sorted.
- Manually compute the minimum and maximum year for each country.
- Add all of these to a Python list. Then manually compute the summary
  statistics for the list (min, median, max, mean, and standard deviation).
"""

def for_loop_pipeline(df):
   
    country = df['Entity'].tolist()
    code = df['Code'].tolist()
    year = df['Year'].tolist()
    population = df['Population (historical)'].tolist()

    country_fil = []
    code_fil = []
    year_fil = []
    pop_fil = []
    rate = []

    for i in range(len(country)):# filter 
        if code[i] != 'OWID_WRL' and code[i] is not None:
            country_fil.append(country[i])  
            code_fil.append(code[i])        
            year_fil.append(year[i])        
            pop_fil.append(population[i])   


    for i in set(country_fil):
        country_min = float('inf')
        country_max = float('-inf')
        min_pop = 0
        max_pop = 0


        for j in range(len(country_fil)):
            if country_fil[j] == i:
                if year_fil[j] < country_min:
                    country_min = year_fil[j]
                    min_pop = pop_fil[j]
                if year_fil[j] > country_max:
                    country_max = year_fil[j]
                    max_pop = pop_fil[j]


        if country_max != country_min or df.shape[0] == 1: #for the latency part 

            if country_max == country_min:
                grade = 0
                rate.append(grade)
            else:

                grade = (max_pop - min_pop) / (country_max - country_min)
                rate.append(grade)

    # summary parts 

    rate.sort()
    min = float('inf')
    for i in rate:
        if i < min:
            min = i
    max =0
    for i in rate:
        if i > max:
            max = i

    mean = sum(rate) /len(rate)

    median = rate[int(len(rate) / 2)]

    std = 0
    for i in rate:
        std += (i - mean) ** 2
    std = (std / len(rate)) ** 0.5

    return [round(min,4),round(median,4), round(max,4), round(mean,4), round(std,4)]
        
    # Input: the dataframe from load_input()
    # Return a list of min, median, max, mean, and standard deviation


def q11():

    # As your answer to this part, call load_input() and then
    # for_loop_pipeline() to return the 5 numbers.
    # (these should match the numbers you got in Q6.)
    a = load_input("data/population.csv")
    stats = for_loop_pipeline(a)
    return stats

"""
12.
Now, let's create our pipelines for comparison.

As before, write 4 pipelines based on the datasets from Q7.
"""

def for_loop_small():
    stats = for_loop_pipeline(load_input_small())

def for_loop_medium():
    stats = for_loop_pipeline(load_input_medium())
    

def for_loop_large():
    stats = for_loop_pipeline(load_input_large())

def for_loop_latency():
    stats = for_loop_pipeline(load_input_single_row())

def q12():
    # Don't modify this part
    _ = for_loop_medium()
    return ["for_loop_small", "for_loop_medium", "for_loop_large", "for_loop_latency"]

"""
13.
Finally, let's compare our two pipelines,
as we did in Q9.

a. Generate a plot in output/q13a.png of the throughputs
    Return the list of 6 throughputs in this order:
    baseline_small, baseline_medium, baseline_large, for_loop_small, for_loop_medium, for_loop_large

b. Generate a plot in output/q13b.png of the latencies
    Return the list of 2 latencies in this order:
    baseline_latency, for_loop_latency
"""

def q13a():
    # Add all 6 pipelines for a throughput comparison
    # Generate plot in ouptut/q13a.png
    # Return list of 6 throughputs
    b = ThroughputHelper()
    b.add_pipeline("baseline_small", len(POPULATION_SMALL), baseline_small)
    b.add_pipeline("baseline_medium", len(POPULATION_MEDIUM), baseline_medium)
    b.add_pipeline("baseline_large", len(POPULATION_LARGE), baseline_large)

    b.add_pipeline("for_loop_small", len(POPULATION_SMALL), for_loop_small)
    b.add_pipeline("for_loop_medium", len(POPULATION_MEDIUM), for_loop_medium)
    b.add_pipeline("for_loop_large", len(POPULATION_LARGE), for_loop_large)

    b.compare_throughput()
    b.generate_plot("output/q13a.png")
    return b.throughputs


def q13b():
    # Add 2 pipelines for a latency comparison
    # Generate plot in ouptut/q13b.png
    # Return list of 2 latencies
    a = LatencyHelper()
    a.add_pipeline("baseline_latency", baseline_latency)
    a.add_pipeline("for_loop_latency", for_loop_latency)
    a.compare_latency()
    a.generate_plot("output/q13b.png")
    return a.latencies

"""
14.
Comment on the results you got!

14a. Which pipelines is faster in terms of throughput?

===== ANSWER Q14a BELOW =====

Baseline large is that fastest temrms of throughput

===== END OF Q14a ANSWER =====

14b. Which pipeline is faster in terms of latency?

===== ANSWER Q14b BELOW =====

for loop as a the lower latency.

===== END OF Q14b ANSWER =====

14c. Do you notice any other interesting observations?
What does this experiment show?

===== ANSWER Q14c BELOW =====

It was interesting that the for loop was faster in terms of latency but slower in terms of throughput.But k

===== END OF Q14c ANSWER =====
"""

"""
===== Questions 15-17: Reflection Questions =====
15.

Take a look at all your pipelines above.
Which factor that we tested (file vs. variable, vectorized vs. for loop)
had the biggest impact on performance?

===== ANSWER Q15 BELOW =====

Having a large amount of data seems to have the biggest impact on performance on thoughput looking at 
graphs 13a we can see the large basline had the highest throuput compared to any of the other one but 
the outher baslines data sizes where actually slower compared to the forloop.

Also in graph 9a we can see the var and basline had a major diffrecne compared to any of the other 
sizes of data when the data was large.


===== END OF Q15 ANSWER =====

16.
Based on all of your plots, form a hypothesis as to how throughput
varies with the size of the input dataset.

(Any hypothesis is OK as long as it is supported by your data!
This is an open ended question.)

===== ANSWER Q16 BELOW =====

The bigger the set is the higher throuput it has. As seen in graphs 9a and 13a

===== END OF Q16 ANSWER =====

17.
Based on all of your plots, form a hypothesis as to how
throughput is related to latency.

(Any hypothesis is OK as long as it is supported by your data!
This is an open ended question.)

===== ANSWER Q17 BELOW =====

Latecny is not an import factor if the data set is big enorugh. As we can see in graph 13a the basline pandas pipline was slower
througput compaed to the small and meduim sets but the througput was fastster for the bigger data set.

===== END OF Q17 ANSWER =====
"""

"""
===== Extra Credit =====

This part is optional.

Use your pipeline to compare something else!

Here are some ideas for what to try:
- the cost of random sampling vs. the cost of getting rows from the
  DataFrame manually
- the cost of cloning a DataFrame
- the cost of sorting a DataFrame prior to doing a computation
- the cost of using different encodings (like one-hot encoding)
  and encodings for null values
- the cost of querying via Pandas methods vs querying via SQL
  For this part: you would want to use something like
  pandasql that can run SQL queries on Pandas data frames. See:
  https://stackoverflow.com/a/45866311/2038713

As your answer to this part,
as before, return
a. the list of 6 throughputs
and
b. the list of 2 latencies.

and generate plots for each of these in the following files:
    output/extra_credit_a.png
    output/extra_credit_b.png
"""

# Extra credit (optional)

def extra_credit_a():
    raise NotImplementedError

def extra_credit_b():
    raise NotImplementedError

"""
===== Wrapping things up =====

**Don't modify this part.**

To wrap things up, we have collected
your answers and saved them to a file below.
This will be run when you run the code.
"""

ANSWER_FILE = "output/part2-answers.txt"
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

def PART_2_PIPELINE():
    open(ANSWER_FILE, 'w').close()

    # Q1-5
    log_answer("q1", q1)
    log_answer("q2a", q2a)
    # 2b: commentary
    log_answer("q3", q3)
    log_answer("q4a", q4a)
    # 4b: commentary
    log_answer("q5a", q5a)
    log_answer("q5b", q5b)

    # Q6-10
    log_answer("q6", q6)
    log_answer("q7", q7)
    log_answer("q8", q8)
    log_answer("q9a", q9a)
    log_answer("q9b", q9b)
    # 10: commentary

    # Q11-14
    log_answer("q11", q11)
    log_answer("q12", q12)
    log_answer("q13a", q13a)
    log_answer("q13b", q13b)
    # 14: commentary

    # 15-17: reflection
    # 15: commentary
    # 16: commentary
    # 17: commentary

    # Extra credit
    log_answer("extra credit (a)", extra_credit_a)
    log_answer("extra credit (b)", extra_credit_b)

    # Answer: return the number of questions that are not implemented
    if UNFINISHED > 0:
        print("Warning: there are unfinished questions.")

    return UNFINISHED

"""
=== END OF PART 2 ===

Main function
"""

if __name__ == '__main__':
    log_answer("PART 2", PART_2_PIPELINE)
