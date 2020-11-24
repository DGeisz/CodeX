# CodeX

The master repository for my research endeavors.  This repo contains write-ups 
for the experiments I run, the metrics I create, and the tools I build for said endeavors.  If you 
aren't me, and you actually care about learning what I'm up to, then you're welcome for keeping 
such a juicy, disgustingly well-organized log of my experiments.

### Structure (as of 11/20/2020)
There is a directory in this top directory for each topic I'm researching.  In each topic 
directory, there will be a readme with a brief overview of the topic, and a table of 
contents for the experiments, metrics, and tools I create that pertain to that topic.

Each experiment, metric, or tool (heretofore referred to as "EMT") will have its own 
directory.  The naming convention for these directories is as follows.  Each EMT 
name starts with a date, then a type, and finally a brief title of the EMT, all 
lowercase and separated by underscores.

Thus, 11_9_2020_metric_mnist_competitive_classification refers to a metric I created on 
11/9/2020 that has something to do with competitive classification on the MNIST dataset.

The table of contents readmes will include hyperlinks to each directory for ease of use.

### EMT Directory structure
Inside each EMT directory, there will be a readme with a basic description of the 
EMT.  There will also be a Jupyter Notebook that contains a write-up for that EMT.  The fields
of the write-up differ whether the EMT is an experiment, metric, or tool.  The fields of the 
different write-ups are as follows.

#### Experiment Write-up Fields
* **Code**: Includes the repo, branch (optional), and commit (optional) for the code used to run
the experiment.  If the branch and commit are omitted, you can assume the branch is the main/master branch, and 
the commit is the leading commit of that branch.  **Note:** If I simply write all the code in a jupyter
notebook, then I'll move the **Code** section above the analysis dialog and write the main code body
there. 

* **Intro**: 
    * Date: The date this experiment was started.
    * What: Describes the details of the structure of the experiment.
    * Why: Describes why I'm running this experiment. References experiments that led
    to this experiment, and any other sources.  
    * Hopes: What I hope will occur during this experiment.  This is essentially the positive
    side of the hypothesis of the experiment. 
    * Limitations: What I foresee to be the limitations of the current experiment.  So where it
    might go wrong, and what is inherently limiting about the setup.  Basically the negative side of the 
    experiment's hypothesis.
    
* **Technicals**: This is more in depth description of the inner working of the current experiment than simply
the "what" section above.  This section should include any theory or algorithms that are of utmost 
importance to the experiment.  
    
* **Analysis Dialogue**: This is basically a conversational form of analysis.  This is where I'll
include data, graphs, and other forms of analysis.  I'll describe what experiment parameters I'm choosing or running
and why I'm doing so, and then include the results of that trial.  As a note about experiments, I consider 
all trials that do not require a change to the structure of the code used during the experiment to be
part of the same experiment.  The only changes allowed to the code in a given experiment are
for bug fixes and to change experiment parameters (basically code constants).  I want to keep the
analysis dialogue as conversational and fluid as possible to make the flow of the experiment as 
clear as possible for myself in the future, or for anyone reading the CodeX.  

* **Conclusions**: Closing remarks for the experiment.  I'll address the hopes and limitations I
wrote in the intro, and talk about what happened during the experiment and why.

* **Next Steps**: In this section, I'll look at what I learned from this experiment, and talk
about what further experiments I wish to run based on the results of this experiment.

* **Data**: This is a jupyter notebook, so in this section I'll load and clean up data that I'll
use in the analysis dialogue. As a note about data, I should never overwrite any data files that 
contain data I reference in the analysis dialogue.  I want my jupyter notebooks sufficiently pragmatic 
such that I can go back and do analysis on previous data.

* **Images**: This is the section where I'll load any images I use throughout the write-up.

For experiments, there will also be a "data" directory, and an "img" directory in the EMT directory
where I'll store data and images used in the write-up.  The "img" directory is optional and isn't included
if there aren't any images referenced in the write-up.

#### Metric Write-up Fields

* **Code**: Same as for experiment write-ups.
* **Purpose**: Describes the purpose of the metric, and what it's trying to show. 
* **Methodology**: The technical details of how the metric works and how it's calculated.

In the future, it'd be pretty neat to also have an automatic listing of experiments that use
this metric, and a "leaderboard" for experimental structures based on this metric.  For the
time being, I'll leave that as an exercise for the reader 😄.

#### Tool Write-up Fields

* **Code**: Same as for experiment write-ups.
* **Purpose**: Describes what the tool is used to do.
* **Docs**: Either gives a description of how to use the tool, or links to external documentation
for the tool.

## Edits:
Here's a record of any changes I make to the structure of the CodeX.  Hopefully changes shouldn't
be major, but obviously any EMT I create before the edit doesn't necessarily adhere to the current
structure.  If you're really committed (that's a pre-pun, just you wait) to finding out the structure 
for old EMTs, then feel free to yote on over to a past git commit (that's the pun 😂) to see the structure I
was using in past CodeX eras.

* Edit 11/24/2020 - Added specification for when I run experiment code directly in the notebook. Commit: 6f189d0d20685 
* Edit 11/20/2020 - Added **Technicals** section to experiment write-ups. Commit: ec252a41962a00a
