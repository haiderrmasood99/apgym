# APSIM Next Generation Site Crawl

Source root: https://apsimnextgeneration.netlify.app
Pages captured: 69

Notes:
- Extracted from the main content container on each page.
- Relative links were resolved to absolute URLs.

## Page Index

- `/usage/met/` - Climate/Weather Data
- `/usage/commandline/` - Command Line
- `/development/git/` - GIT and GitHub
- `/usage/graphs/` - Graphs
- `/contribute/issues/` - Issue guidelines
- `/technicalinformation/` - Technical Information
- `/usage/` - Usage
- `/usage/commandline/commandlanguage/` - APSIM Command Language
- `/contribute/` - Contribute
- `/development/` - Development
- `/development/git/gitfork/` - Git Fork
- `/development/compile/` - How to compile
- `/install/` - Install
- `/contribute/pullrequests/` - Pull request guidelines
- `/development/software/` - Software
- `/usage/commandline/batch/` - Batch files
- `/development/git/git-sourcetree/` - SourceTree
- `/development/git/git-cli/` - CLI
- `/usage/commandline/commandlinetutorialwindows/` - Windows Tutorial
- `/usage/commandline/command-line-linux/` - Command Line on Linux
- `/usage/commandline/commandlanguage-old-to-new/` - APSIM Command Language (old to new)
- `/development/how-to-modify-the-web-site/` - How to modify the web site
- `/usage/commandline/playlist/` - Playlist
- `/contribute/science-contributions/` - Science contributions
- `/development/tutorial/` - Tutorial
- `/development/tutorial/buildmodeltutorial/` - Build a model tutorial
- `/development/tutorial/howpmffunctionswork/` - How PMF functions work
- `/development/software/compile-apsimng/` - Publish APSIMNG from source code
- `/_header/` - APSIM Docs
- `/user_tutorials/` - APSIM Next Gen User Tutorials
- `/usage/server/` - APSIM Server
- `/technicalinformation/versioning/` - APSIM file versions & APSIM Software versions
- `/usage/met/customdata/` - Accessing non-standard columns of data from .met file
- `/development/software/autodocumentation/` - Auto documentation
- `/categories/` - Unavailable Page
- `/usage/graphs/datetimexaxes/` - Changing datetime x axes intervals
- `/development/software/codingstyle/` - Coding Style
- `/usage/debugmanagerscript/` - Debug Manager Script
- `/usage/graphs/errorbars/` - Error Bars
- `/usage/factorials/` - Factorial Simulations
- `/usage/graphs/graphfilters/` - Graph filters
- `/install/linux/` - Linux Installation
- `/install/macos/` - MacOS Installation
- `/usage/memo/` - Memo
- `/usage/scope/` - Model Scope
- `/development/software/modeldesign/` - Model design
- `/modeldocumentation/` - Model documentation
- `/user_tutorials/module1/moduleonetutorial/` - Module 1: Fallow Simulation
- `/user_tutorials/module2/moduletwotutorial/` - Module 2: Surface Organic Matter Simulation
- `/user_tutorials/module3/modulethreetutorial/` - Module 3: The Nitrogen Cycle
- `/user_tutorials/module4/modulefourtutorial/` - Module 4: Sowing A Crop
- `/user_tutorials/module5/modulefivetutorial/` - Module 5: Long-term simulations
- `/development/software/pmfdesign/` - PMF code design
- `/usage/croptimizr/` - Parameter Optimisation
- `/usage/pathspecification/` - Path Specification
- `/usage/graphs/creating-predicted-observed-graphs/` - Predicted observed graphs
- `/usage/report/` - Report Node
- `/usage/rotationmanager/` - Rotation Manager
- `/usage/sensitivityanalysis/` - Sensitivity Analysis
- `/development/software/interfaces/` - Software interfaces
- `/tags/` - Unavailable Page
- `/usage/tests/` - Test Results
- `/` - The next generation of APSIM
- `/development/software/unittests/` - Unit tests
- `/development/software/userinterfacedesign/` - User interface design
- `/usage/met/usingexcelforweatherdata/` - Using Excel for weather data
- `/usage/met/csvweather/` - Using a .csv file for weather data
- `/usage/writemanagerscript/` - Write Manager Scripts
- `/usage/documentationtutorial/` - Writing Documentation for Models

---

## /usage/met/

Source: https://apsimnextgeneration.netlify.app/usage/met/
Title: Climate/Weather Data

# Climate/Weather Data

- [Accessing non-standard columns of data from .met file](https://apsimnextgeneration.netlify.app/usage/met/customdata)
- [Using an Excel file for weather data](https://apsimnextgeneration.netlify.app/usage/met/usingexcelforweatherdata)
- [Using a .csv file for weather data](https://apsimnextgeneration.netlify.app/usage/met/csvweather)

---

## /usage/commandline/

Source: https://apsimnextgeneration.netlify.app/usage/commandline/
Title: Command Line

# Command Line

To run APSIM from the command line you need to locate the Models.exe binary file. On Windows this is located in

```
C:\Program Files\APSIM<Version-number>\bin\Models.exe
```

on LINUX it is located in

```
/usr/local/bin/Models.exe
```

## Command line usage.

To run simulation specific files from the command line: `Models.exe file.apsimx file2.apsimx`

- **–recursive** - Recursively search through subdirectories for files matching the file specification. `Models --recursive dir/*.apsimx`
- **–upgrade** - Upgrade a file to the latest version of the .apsimx file format without running the file.
- **–run-tests** - After running a file, run all tests inside the file.
- **–verbose** - Write detailed messages to stdout when a simulation starts/finishes.
- **–csv** - After running all files, export all reports to .csv files
- **–merge-db-files** - Merge multiple .db files into a single .db file. `Models.exe --merge-db-files site1.db site2.db`
- **–list-simulations** - write the names of all simulations in a .apsimx file to stdout. The files are not run.
- **–list-enabled-simulations** - write the names of all *enabled* simulations in a .apsimx file to stdout. The files are not run.
- **–list-referenced-filenames** - write the names of all files that are referenced by an .apsimx file(s) to stdout e.g. weather files, xlsx files.
- **–single-threaded** - Run all simulations sequentially on a single thread.
- **–simulation-names** - Only run simulations if their names match a regular expression. `Models.exe file1.apsimx --simulation-name *Australia*`
- **–apply** - Apply commands from a .txt file. Can be used to create new simulations and modify existing ones. [Click here for more info](https://apsimnextgeneration.netlify.app/usage/commandline/commandlanguage) `Models.exe --apply commands.txt Models.exe file1.apsimx --apply commands.txt`
- **–playlist** - Allows a group of simulations to be selectively run. Requires a playlist node to be present in the APSIM file. [Click here for more info](https://apsimnextgeneration.netlify.app/usage/commandline/playlist) `Models.exe file1.apsimx --playlist playlist1`
- **–log** - Change the log (summary file) verbosity. `Models.exe example.apsimx --log error Models.exe example.apsimx --log warning Models.exe example.apsimx --log information Models.exe example.apsimx --log diagnostic Models.exe example.apsimx --log all`
- **–in-memory-db** - Use an in memory database rather than writing simulation output to a .db file. `Models.exe example.apsimx --in-memory-db`
- **–batch** - Allows the use of a .csv file to specify values of variables than can be substituted into a command file (–apply). [Click here for more info](https://apsimnextgeneration.netlify.app/usage/commandline/batch) `Models.exe --apply command.txt --batch values.csv`
- **–file-version-number** - Write the file version number of an apsimx file to stdout. `Models.exe File1.apsimx --file-version-number`
- **–help** - Write all command line switches to stdout.
- **–version** - Write the APSIM version number to stdout.

---

## /development/git/

Source: https://apsimnextgeneration.netlify.app/development/git/
Title: GIT and GitHub

# GIT and GitHub

# Create a GitHub Account

The APSIM source code is located on GitHub so you will need to have a GitHub login if you want to contribute new features or modifications to the APSIM repository.

To create an account head to [Github](https://www.github.com/).

# Making and getting changes

- [Use Git Fork](https://apsimnextgeneration.netlify.app/development/git/gitfork)
- [Use SourceTree](https://apsimnextgeneration.netlify.app/development/git/git-sourcetree)
- [Use the command line](https://apsimnextgeneration.netlify.app/development/git/git-cli)

---

## /usage/graphs/

Source: https://apsimnextgeneration.netlify.app/usage/graphs/
Title: Graphs

# Graphs

- [Error bars](https://apsimnextgeneration.netlify.app/usage/graphs/errorbars)
- [Graph filters](https://apsimnextgeneration.netlify.app/usage/graphs/graphfilters)
- [Creating Predicted/Observed Graphs](https://apsimnextgeneration.netlify.app/usage/graphs/creating-predicted-observed-graphs)
- [Changing datetime x axes intervals](https://apsimnextgeneration.netlify.app/usage/graphs/datetimexaxes)

---

## /contribute/issues/

Source: https://apsimnextgeneration.netlify.app/contribute/issues/
Title: Issue guidelines

# Issue guidelines

### Issue best practices

- The issue title is important. It must be a sentence accurately describing the issue. It is also used as the release description when installing or upgrading APSIM. Having a good description helps the user to decide which release version to download.
- Describe issues with an emphasis on the “Why” more than “What” or “How”. The issue description should be clear enough that another person should be able to fix the problem or create the feature.
- Submit issues before you begin creating a solution. This has the advantage of avoiding unnecessary effort if the issue is found to be resolved or in the process of being resolved and allows others to suggest possible approaches and considerations that can improve the subsequent PR.
- For defects:
  - Defect issues must be reproducible. Include a simulation file with required met and input files in a zip archive.
  - Describe the steps to reproduce the defect. This includes details like where you clicked, what settings were enabled and what operating system it occurred on.
  - For graphical user interface (GUI) issues please submit a minimally reproducible example apsim file, describe the user interface model this issue affects and the steps to reproduce the error.

---

## /technicalinformation/

Source: https://apsimnextgeneration.netlify.app/technicalinformation/
Title: Technical Information

# Technical Information

- [APSIM file versions & APSIM Software versions](https://apsimnextgeneration.netlify.app/technicalinformation/versioning)

---

## /usage/

Source: https://apsimnextgeneration.netlify.app/usage/
Title: Usage

# Usage

- [Graphs](https://apsimnextgeneration.netlify.app/usage/graphs)
- [Command line](https://apsimnextgeneration.netlify.app/usage/commandline)
- [Debug manager script](https://apsimnextgeneration.netlify.app/usage/debugmanagerscript)
- [Edit .apsimx files from command line](https://apsimnextgeneration.netlify.app/usage/editfile)
- [Parameter Optimisation](https://apsimnextgeneration.netlify.app/usage/croptimizr)
- [Memo markdown cheatsheet](https://apsimnextgeneration.netlify.app/usage/memo)
- [Scope](https://apsimnextgeneration.netlify.app/usage/scope)
- [Path specification](https://apsimnextgeneration.netlify.app/usage/pathspecification)
- [Test Results](https://apsimnextgeneration.netlify.app/usage/tests)
- [Climate/Weather Data](https://apsimnextgeneration.netlify.app/usage/met)
- [Write manager scripts](https://apsimnextgeneration.netlify.app/usage/writemanagerscript)
- [Rotation Manager](https://apsimnextgeneration.netlify.app/usage/rotationmanager)
- [APSIM Server](https://apsimnextgeneration.netlify.app/usage/server)
- [Reports](https://apsimnextgeneration.netlify.app/usage/report)
- [Sensitivity Analysis](https://apsimnextgeneration.netlify.app/usage/sensitivityanalysis)

---

## /usage/commandline/commandlanguage/

Source: https://apsimnextgeneration.netlify.app/usage/commandline/commandlanguage/
Title: APSIM Command Language

# APSIM Command Language

The APSIM command language is a way for the user to change the structure of a simulation and parameterise models from the command line. The language is specified via a series of string commands, usually contained within a text file (a command file).

An example use case for the command language is: “Replace the soil, weather file, clock start/end dates in a .apsimx file and run APSIM i.e. run an APSIM simulation for a grid point”. The user can create a command file to do the replacements and have it applied from the command line. They can then call this from a batch/bash file to do this repeatedly for multiple grid points. Prior to the command language, the user would have had to write Python/R scripts to directly manipulate the JSON in the .apsimx file. The problem with this approach is that the structure of the JSON changes over time which breaks the user’s scripts.

This language replaces an older version of the language. If you have command files written using the old syntax, [see here](https://apsimnextgeneration.netlify.app/usage/commandline/commandlanguage-old-to-new) for details on how to convert the syntax.

## What commands can you perform?

- **load** - loads a .apsimx file into memory. Subsequent commands will then apply to the contents of the file. `load C:\TestSims\wheatTest.apsimx`
- **save** - saves the in-memory simulations to file. `save C:\TestSims\wheatTest.apsimx`
- **run** - run APSIM on the in-memory simulations. `run`
- **add** - add a new or existing model to another model. `add new Report to [Zone]` `add new Report to [Zone] name MyReport` `add [Report] to all [Zone]` `add [Soil1] from soils.apsimx to [Zone] name Soil`
- **delete** - delete a model
  - `delete [Zone].Soil`

- **duplicate** - duplicate a model.
  - `duplicate [Zone].Report name NewReport`

- **replace** - replace a model with another model
  - `replace all [Report] with NewReport name ReportWithNewName`
  - `replace all [Report] with NewReport from anotherfile.apsimx name ReportWithNewName`

- **property set** - Change the property of a model `[Weather].FileName=Dalby.met`
- **property set** - Change the property of a model using the value read from a file (contents of value.txt). `[Weather].FileName=<value.txt`
- **property add to array** - Add a string to a model array property or update it if it already exists. `[Janz].Command += [Phenology].CAMP.EnvData.VrnTreatTemp = 5.5`
- **property delete from array** - Remove a string from a model array property `[Janz].Command -= [Phenology].CAMP.EnvData.VrnTreatTemp`
- **comment lines** - you can comment out command lines `# Add Soil1 from the soils database file` *note 1: all file name references can either have an absolute path or no path making the file relative to the command file.* *note 2: a property set/add/remove/update is only applied to the first occurence of it in the simulation tree. For example, if there are multiple occurences of `Janz` and you are setting `[Janz].Command` then the change will only be applied to the first occurence.*

## Property formatting when setting property values

### Dates

dd/MM/yyyy will not work. yyyy-MM-dd is the recommended format.

### Numbers

Decimal place should be a period (not a comma). Comma is allowed as thousands separator but isn’t mandatory.

### Strings (text)

Quotes will be included in the value which is assigned to the property. For example, if you do this:

[Clock].Name = “This is a clock”

the name of the Clock model will be `"This is a clock"`

### Arrays

Array or list properties should be specified as comma-separated values. It is also possible to modify an element at a particular index or indices of an array or list, but the indices start at 1. If modifying multiple elements, a second index can be provided after a colon, as in the example below.

```
[Physical].BD = 1,2,3,4,5,6,7
[Physical].AirDry[1] = 8
[Physical].LL15[3:5] = 9
[Physical].BD =                # sets to an empty array.
```

## What does an example config file look like?

```
# Makes a new apsimx file and builds it up to something that will run
# Dalby.met needs to be in C:\TestSims\

load C:\TestSims\minimalSim.apsimx

# Add various models to the Simulations model. minimalSim.apsimx only has
# a Simulations model with a child DataStore model.
add new Simulation to [Simulations]
add new Summary to [Simulation]
add new Clock to [Simulation]
add new Weather to [Simulation]

# Change data in various nodes.
[Weather].FileName=Dalby.met
[Clock].Start=1900-01-01
[Clock].End=1900-01-31

# Adds a soil from soils.apsimx, removing the existing soil
delete [Zone].Soil
add [Soil1] from soils.apsimx to [Zone] name Soil

# Saves the Simulation to new file.
save C:\TestSims\Test.apsimx

# Runs the simulation.
run
```

---

## /contribute/

Source: https://apsimnextgeneration.netlify.app/contribute/
Title: Contribute

# Contribute

This outlines the APSIM review process for all contributions to GitHub.

### Step 1 Developer raises a GitHub Issue

- Describe the issue and functionality required with an emphasis on “Why” the change is required i.e. the use-case.
- Raise the issue early (well before development) to allow input from others.
- For a user interface defect, create a small video that demonstrates the problem.
- Ensure code conforms to the [Issue guidelines](https://apsimnextgeneration.netlify.app/contribute/issues)

### Step 2 Issue is reviewed by software team

The software team will:

- Review the issue for clarity
- Check to see if it is a duplicate of an existing issue.
- Optionally tag `@APSIMInitiative/reference-panel` if issue might be of interest to the Reference Panel.

### Step 3 Developer raises a GitHub Pull Request (PR)

- Ensure the PR conforms to the [PR guidelines](https://apsimnextgeneration.netlify.app/contribute/pullrequests)
- The developer must link to an issue. Use `working on #issue` or `resolves #issue`
- Ensure the PR matches the Issue
- The build/test system will run automatically and set a green/red (pass/fail) status.
- The developer may need to push changes multiple times to resolve errors.
- When development is complete, the developer adds a `Ready for Review` label.

### Step 4 High Level Review by software team

The software team will:

- Add `High Level Review` label
- Ensure the PR matches the Issue
- Suggest design improvements (e.g. missing converter)
- Ask for additional tests if necessary
- Ensure PR conforms to the [PR guidelines](https://apsimnextgeneration.netlify.app/contribute/pullrequests)

This review may take several iterations. Once the team is satisfied, a low level review can take place.

### Step 5 Low Level Review

The software team will:

- Perform a full code review
- Initiative a Co-pilot review
- Suggest [style guideline](https://apsimnextgeneration.netlify.app/contribute/#style-guidelines) fixes
- Review the tests
- Review any changes in statistics
- Check for inadvertent changes in statistics
- Check for inadvertent changes in code

**If this is a software change only**

- The software team will merge once resolved.

**Else if a minor science change that DOES NOT change model behaviour** e.g. addition to test datasets or addition of new outputs

- Tag `@APSIMInitiative/reference-panel` FYI
- The software team will merge the PR immediately.

**Else if a minor science change that DOES change model behaviour** e.g. simple changes or defect fixes to model

- Tag `@APSIMInitiative/reference-panel` FYI
- The software team will merge the PR within 3 business days.

**Else if this is a significant change to science code or data sets** e.g. a new model or significant changes to a published model.

- The software team will tag `@APSIMInitiative/reference-panel` for additional review
- Move to Step 6.

### Step 6 Reference Panel Review

The software team will:

- Add `Reference Panel Review` label to PR
- Contact the Reference Panel coordinator to put a PR review on the agenda for the next meeting
- The software team will assist the developer to ensure all code, tests, documentation, stats should be ready for review by the Reference Panel.
- Most of the meaningful interactions could happen on GitHub prior to the meeting.
- The Reference Panel will review the changes and make suggested improvements.
- Once completed, the process will return to Step 5.

Further details can be found in [Science contributions](https://apsimnextgeneration.netlify.app/contribute/science-contributions)

---

## /development/

Source: https://apsimnextgeneration.netlify.app/development/
Title: Development

# Development

For changes to be accepted by the APSIM Initiaive Reference Panel submissions must adhere to software and science guidelines.

All submissions that contain source code changes will be subject to a software peer review that ensures all software guildlines have been met.

All submissions that contain major changes to model science e.g. new models or new processes (labeled as ‘Major’ in GitHub) will undergo peer-review by at least one independent reviewer. The Reference Panel will manage this process. The science reviewer(s) will be ensure all science guildlines have been met.

Reasons need to be given by the model author should any of the guidelines not be followed.

**Submission Guidelines**

- Submissions will be via a [GitHub Pull Request](https://apsimnextgeneration.netlify.app/contribute/sourcetree/pushandpullrequest)
- Where possible, submissions should be small. For example, rather than adding a new model validation dataset and changing the parameterisation of a model, separate these into 2 submissions. This will allow the impacts of the new dataset and the changed parameterisation to be independently assessed.
- For science submissions (new models or processes), the submission pull request will have all files (.apsimx, .met, .xlsx) in a directory formatted as Tests\UnderReview\MODELNAME. The directory can contain:
  - weather files (*.met)
  - observed files (*.xlsx)
  - MODELNAME.apsimx (validation simulations)
  - MODELNAME Example.apsimx (example simulations)

- If a new model has been submitted, it will be under a *Replacements* node in the MODELNAME.apsimx and MODELNAME Example.apsimx files.

**Software Guidelines**

- [Coding style](https://apsimnextgeneration.netlify.app/development/software/codingstyle)
- [Model design](https://apsimnextgeneration.netlify.app/development/software/modeldesign)
- [User interface design](https://apsimnextgeneration.netlify.app/development/software/userinterfacedesign)
- [PMF model design](https://apsimnextgeneration.netlify.app/development/software/pmfdesign)
- [Software interfaces](https://apsimnextgeneration.netlify.app/development/software/interfaces)
- [Unit tests](https://apsimnextgeneration.netlify.app/development/software/unittests)

**Science guidelines**

- [Testing](https://apsimnextgeneration.netlify.app/development/science/testing)
- [Documentation](https://apsimnextgeneration.netlify.app/development/science/documentation)
- [Examples](https://apsimnextgeneration.netlify.app/development/science/examples)

---

## /development/git/gitfork/

Source: https://apsimnextgeneration.netlify.app/development/git/gitfork/
Title: Git Fork

# Git Fork

## Download and install Git using “Git Fork”

Download [Git Fork](https://git-fork.com/)

## Cloning the repository

The first thing to do is to clone the [APSIMInitiative/ApsimX](https://github.com/APSIMInitiative/ApsimX) repository. This can be done by using a command line terminal to navigate to the directory you want to download the source code to and run the command:

```
git clone https://github.com/APSIMInitiative/ApsimX.git
```

Alternatively, you can use Visual Studio to clone the repository from the start screen

![Clone repo in visual studio](https://apsimnextgeneration.netlify.app/images/clone_repo_visual_studio.png)

It is best practice to fork(copy) the APSIM repository and push changes to this before submitting changes to the master version of APSIM.

See [“To Create a Fork”](https://apsimnextgeneration.netlify.app/development/git/gitfork/#to-create-a-fork) section below.

## Using Git to make changes

Instructions on how to use Git to make and submit changes can be found [here](https://git-scm.com/doc)

A good practice is to always pull changes from the master APSIM repository before starting any new work. This is important to avoid any problems when it comes time to submit your changes. Doing this will ensure you have the most up to date version of the APSIM source files. ![Pulling changes from master image](https://apsimnextgeneration.netlify.app/images/pull_master_changes.png)

## Commiting changes to your local repository

If you have files that you have added or modified, you can commit them to git. This process of adding commits keeps track of your progress as you work on files in APSIM.

Commits also create a transparent history of your work that others can follow to understand what you’ve done and why. Each commit has an associated commit message, which is a description explaining why a particular change was made. Furthermore, each commit is considered a separate unit of change. This lets you roll back changes if a bug is found, or if you decide to head in a different direction.

Commit messages are important, especially since git tracks your changes and then displays them as commits once they’re pushed to the server. By writing clear commit messages, you can make it easier for other people to follow along and provide feedback.

Commits are local to your computer only until you do a push to a remote repository.

## Committing using Fork

To view the changes you’ve made that are ready to be committed:

- Select Local Changes.
- Next highlight any files in the unstaged list that you would like to commit and click ‘stage’. ![committing changes](https://apsimnextgeneration.netlify.app/images/committing_changes.png)
- The files will then move to the ‘Staged’ section. ![Staged changes](https://apsimnextgeneration.netlify.app/images/staged_changes.png)
- Next include a ‘Commit Subject’ and detailed ‘Description’ describing the changes you’ve made. This will benefit anyone reviewing your changes.
- To commit the changes click ‘confirm’. ![committing changes](https://apsimnextgeneration.netlify.app/images/confirm_commit.png)

## Committing using the command line interface

To list new/modified files use `git status`

To view the changes from the previous commit, use `git diff`

To undo changes which you don’t want to keep, use `git checkout ModifiedFile.txt`

Before you commit your changes you must first add any new or modified files to the index.

```
git add ModifiedFile.txt
```

To remove a file from the index, use the reset command:

```
git reset ModifiedFile.txt
```

To perform the commit:

```
git commit -m "Commit message"
```

For additional options/help, use `git help commit` or `man git`

## Working on Apsim

To see how to begin working on APSIM for your unique operating system see [Compile Section](https://apsimnextgeneration.netlify.app/contribute/compile/).

An option for working on APSIM is to use Visual Studio 2022. You can be download it [here](https://visualstudio.microsoft.com/vs/).

# 3. Contributing your changes

You can’t push directly to the main ApsimX repository. Instead, you need to push to your remote fork (copy) of ApsimX.

## To create a fork:

- Open a web browser, go to the [APSIM github page](https://github.com/APSIMInitiative/ApsimX) and click on the fork link in the top right hand corner of the repository on GitHub.
- Clicking this will create a copy of the APSIM repository into your GitHub account. ![fork repo](https://apsimnextgeneration.netlify.app/images/fork_repo.png)
- Once you’ve done this you need to add your GitHub ‘remote’ to your git client. We recommend Fork. You can download it [here](https://git-fork.com/)
- In the screenshot below, right click on ‘Remotes’ in the tree, click ‘Add Remote’ and fill in a name for your remote (usually your name or your github name) and the URL for the ApsimX repo. Mine looks like: ![add remote](https://apsimnextgeneration.netlify.app/images/add_remote.png)
  - Alternatively, you can add this as your remote repository by navigating to your APSIM project location on your pc and using the command in a terminal: ``` git remote add https://github.com/ric394/ApsimX.git ```
  - Note: replace “ric394” in the above command with your personal GitHub profile username.

- You can then push to your remote (rather than origin). Click push and change ‘remote’ drop down to your newly created one. Mine looks like: ![push to remote](https://apsimnextgeneration.netlify.app/images/push_to_remote.png)
  - Alternatively, you can push to your remote repository by navigating to your local APSIM project directory and use the command below in a terminal: ``` git push ric394 master ```
    - replace “ric394” with your remote repository name.
    - replace “master” with the branch name you’d like to push the changes to.

- After pushing you need to create a pull request. Right click on your ‘master’ branch and choose create pull request: ![pull request](https://apsimnextgeneration.netlify.app/images/pull_request.png)
- This will open a browser window where you need to enter a comment in the top comment box. ![Create pull request](https://apsimnextgeneration.netlify.app/images/create_pull_request.png)
  - You can reference issue numbers here. Each pull request must contain a issue number.
    - For example, if this pull request resolves an issue, type: ``` resolves #1234 ```
    - However, if this pull request involves an issue but does not resolve the issue, type: ``` working on #1234 ```

  - It is also good to add some extra comments in the top box that explain what is in the pull request e.g. New cotton validation data from site xyz.
  - Once done, click the ‘Create Pull Request’ button at the bottom of the browser window.
  - Once the PR has been created, everyone can see it automatically and a peer-review will be performed.
  - It will also automatically trigger a build and test of our test suite. If it is approved, it will be merged it into the main master branch and it will be made available to all users.

This looks complicated but once you’ve created a few pull requests you’ll get the hang of it.

---

## /development/compile/

Source: https://apsimnextgeneration.netlify.app/development/compile/
Title: How to compile

# How to compile

# Windows

APSIM can be compiled using Microsoft Visual Studio 2019 or later. A single solution file exists in the root of the repository (ApsimX.sln). All executables will be built to the bin directory. The exact output path will depend upon whether the solution is built in debug or release mode. The default (debug) will output files to `bin\Debug\net8.0\`. APSIM currently can only be built against .NET 8.

Building APSIM requires that version 8.0 of the .NET SDK is installed. This can be installed at the same time as Visual Studio. If Visual Studio is already installed, the installation can be modified by navigating to ‘Tools\Get Tools and Features…’ in the menu bar and modifying the existing installation by adding either the “.NET desktop development” or “Universal Windows Platform development” workload.

![Install the .NET Core SDK](https://apsimnextgeneration.netlify.app/images/vs-modify-workload.png)

1. Open ApsimX.sln in visual studio
2. Build solution (default ctrl + shift + b) Right-click on the solution in the solution explorer and click “Build solution”

# LINUX

Apsim may be built with the .NET SDK - currently version 8.0 is required. When building the solution, assemblies for all projects will be compiled to the bin/ directory. The exact location of a given file will depend upon how it is built - e.g. debug vs release configuration.

1. Install the .NET Core 8.0 SDK. The [dotnet-install script](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet-install-script) is a simple way to do this. Otherwise, consult [this page](https://docs.microsoft.com/en-us/dotnet/core/install/linux)
2. Install required packages
  - libsqlite3-dev
  - git (required for obtaining the source code)
  - gtk-sharp3
  - libgtksourceview-4-0
  - dotnet-sdk-8.0

3. Obtain source code ``` git clone https://github.com/APSIMInitiative/ApsimX ```
4. Build the solution ``` dotnet build ApsimX.sln # (debug mode) dotnet build -c Debug ApsimX.sln # (debug mode) dotnet build -c Release ApsimX.sln # (release mode) ```
5. Run apsim The outputs may be found under ApsimX/bin. If built in debug mode, they will be in `bin/Debug/net8.0/`. If built in release mode, they will be in `bin/Release/net8.0/`. The entrypoint program for the user interface is called `ApsimNG`. The CLI has two “main” entrypoints - `Models` and `apsim`. `Models` may be used to run .apsimx files. `apsim` accepts multiple verb arguments, but `apsim run` will function identically to an invocation of `Models`.

## Common Problems

When running apsim:

```
System.DllNotFoundException: Unable to load shared library 'sqlite3' or one of its dependencies. In order to help diagnose loading problems, consider setting the LD_DEBUG environment variable: libsqlite3: cannot open shared object file: No such file or directory
```

This error can occur on Debian (and its derivatives) when the sqlite3 package is installed. This package typically provides a file named `libsqlite3.so.0` or similar, but apsim is looking for `libsqlite3.so`. This file is provided by the `libsqlite3-dev` package, so installing this package should fix the problem. Otherwise, creating a symlink to `libsqlite3.so.0` called `libsqlite3.so` should also fix the problem.

---

When attempting to install apsim from our binary package:

```
E: Unable to locate package dotnet-runtime-8.0
```

This package is not included in the official Debian repositories. You will need to follow the instructions on [this page](https://docs.microsoft.com/en-us/dotnet/core/install/linux) to install the package from microsoft’s repositories.

# Mac OSX

APSIM can be compiled using Microsoft’s [Visual Studio Code](https://code.visualstudio.com/download). A single solution file exists in the root of the repository (ApsimX.sln). Building this solution will extract all 3rd party packages from NuGet and build everything. All executables will be built to the bin folder, but the exact output location will depend on how the solution is built (ie release vs debug). The default (debug) will cause outputs to be copied to `bin/Debug/net8.0/`.

1. Install [Visual Studio Code](https://code.visualstudio.com/download)
2. Once visual studio is installed, install the vs code c# dev kit extension.
3. Install [git](https://git-scm.com/downloads) and a git client, we recommend [Fork](https://git-fork.com/).
4. Install the .NET 8 SDK. The SDK can be found [here](https://dotnet.microsoft.com/en-us/download/dotnet/8.0) for your specific operating system.
5. Check that the SDK is installed by opening a terminal and running the command: ``` dotnet --list-sdks ```
  - You should see at least one line that says: ``` 8.X.X ```
    - `x` is any number. The version numbers of a SDK may change over time.
    - There may be other lines with differing values. This is normal.

6. Install GTK+3 and gtksourceview4 ``` brew install gtk+3 brew install gtksourceview4 ```
7. Obtain the source code ``` git clone https://github.com/APSIMInitiative/ApsimX ```
8. Build and Run

---

## /install/

Source: https://apsimnextgeneration.netlify.app/install/
Title: Install

# Install

- [MacOS Installation](https://apsimnextgeneration.netlify.app/install/macos)
- [Linux Installation](https://apsimnextgeneration.netlify.app/install/linux)

---

## /contribute/pullrequests/

Source: https://apsimnextgeneration.netlify.app/contribute/pullrequests/
Title: Pull request guidelines

# Pull request guidelines

### Pull Request (PR) Priorities

- The software team prioritise defect fixes above new features. This is in line with the software teams’ zero bug policy.
- New features are then prioritized.

### Pull request best practices

- Short-lived (1-2 weeks max) feature branches are ideal. Branches that are used to develop a new plant are an exception here.
- Aim to make smaller and more frequent PRs over larger less frequent PRs. Smaller PRs tend to be easier to review. Larger pieces of work can usually be broken into smaller feature branches which are easier to manage.
- Regularly pull in changes from the APSIMInitiative/master branch.
- Ensure a pull request is close to the tip revision i.e. ensure the most recent version of repo is pulled into the PR branch.
- A pull request must only do one thing.
- A pull request should briefly and concisely describe what the issue was, what changes have been made and the rationale.
- Changes to observed data, or the addition of new data, should be on a PR with no other changed files. This allows the software team to clearly see the effect of the changed/new data without it being confounded by other changes.
- **Science** changes require observed data to demonstrate that the change does what it intends. Additionally unit tests are to be included.
- **Graphical user interface (GUI)** changes and fixes that include a short video showing the changes working will improve review time.
- **Bug fixes** should include a unit test to reduce the likelihood of recurrence and to also verify the fix.

## Things to Avoid

- Keeping branches in development for long periods of time. Branches that have been left and need to be brought up to date with the newest changes can be difficult to update.
- Submitting pull requests that resolve multiple unrelated issues in the one pull request. Doing so increases the difficulty of review.
- Submitting pull requests that contain multiple new features. This also increases the review time.
- Leaving PRs inactive for long lengths of time (60+ days). PRs not marked with the following labels will be closed automatically to help with PR review efforts: `Ready for Reference Panel Comment, Do Not Merge, High Level Review, Low Level Review, Ready for Software Review`

---

## /development/software/

Source: https://apsimnextgeneration.netlify.app/development/software/
Title: Software

# Software

## Software Guidelines

- [Coding style](https://apsimnextgeneration.netlify.app/development/software/codingstyle)
- [Model design](https://apsimnextgeneration.netlify.app/development/software/modeldesign)
- [User interface design](https://apsimnextgeneration.netlify.app/development/software/userinterfacedesign)
- [PMF model design](https://apsimnextgeneration.netlify.app/development/software/pmfdesign)
- [Software interfaces](https://apsimnextgeneration.netlify.app/development/software/interfaces)
- [Unit tests](https://apsimnextgeneration.netlify.app/development/software/unittests)

---

## /usage/commandline/batch/

Source: https://apsimnextgeneration.netlify.app/usage/commandline/batch/
Title: Batch files

# Batch files

## Making repeated changes to many files (batching)

- For situations where you need to make the same changes to many apsim files but need specific nodes or parameters changed, the `--apply` switch can be used in conjunction with the `--batch` switch.
- An example where this would be useful is when you want to change the soil and weather for each individual APSIM file and you have 10s to 100s to 1000s of APSIM files.
- To do this you will need two specific files along with any APSIM files you want to change, these files are:
  - A config file containing ‘placeholders’ ``` load BaseCl.apsimx [Soil]=SoilLibrary.apsimx;[$soil-name] [Weather].FileName=$weather-file-name [SimulationExp].Name=$sim-name run ```
    - the placeholders are the values that will be replaced by the values in the batch file
    - a placeholder is a name that starts with a `$` symbol. An example would be `$weather-file-name`.
    - placeholders cannot contain spaces.
    - an example config file:

  - A batch file, this is a csv file with headers that match the placeholders (minus the `$` symbols) | soil-name | weather-file-name | sim-name | | --- | --- | --- | | Ahiaruhe_1a1 | 16864.met | Sim0001 | | Ahuriri_7a1 | 19479.met | Sim0002 | | Ailsa_5a1 | 19479.met | Sim0003 |
    - for each row in the batch file a run through of the config file is completed.
    - an example batch file:

- To run this we would run something like: `"C:\Program Files\APSIM<your version number>\bin\Models.exe" --apply config-file-name.txt --batch batch-file-name.csv`

---

## /development/git/git-sourcetree/

Source: https://apsimnextgeneration.netlify.app/development/git/git-sourcetree/
Title: SourceTree

# SourceTree

SourceTree is only available on Windows and OSX. If you are using Linux, version control will need to be managed [via the command line](https://apsimnextgeneration.netlify.app/contribute/cli/)

## Create GitHub account

The APSIM source code is located on GitHub so you will need to have a GitHub login if you want to contribute new features or modifications to the APSIM repository.

This document assumes that your APSIM Next Generation folder is C:\Work\ApsimX.

## Fork the repository

If you plan to modify or add to the APSIM code/datasets, you will need to fork the repository. A fork creates a copy of the repository associated with your github account.

- Click on the fork link in the top right hand corner of the [APSIM repository](https://github.com/APSIMInitiative/ApsimX) on GitHub

## Clone ApsimX to your computer

To bring the source code from GitHub to your computer, you will need to clone the repository. We recommend you use a Git GUI client. We recommend [SourceTree](http://www.sourcetreeapp.com) for this. Once you have SourceTree installed on your computer, goto *File | Clone* menu item.

Click the ‘Clone / New’ button in SourceTree and specify:

- Source Path / URL: [https://github.com/APSIMInitiative/ApsimX](https://github.com/APSIMInitiative/ApsimX)
- Destination Path: C:\Work\ApsimX <- this is the folder on your computer
- Name: ApsimX <- This is the name that this respository will be known by

Once you click ‘Clone’, all files will be downloaded to your computer into the destination path that you specified above. SourceTree will create a tab for your new cloned repository.

## Add a remote repository

You now need to create a link to your ApsimX fork that you created earlier.

- Click Repository | Repository Settings
- Click ‘Add’
- Remote name: hol353 <- Can be anything, but we recommend using the username of your GitHub account.
- URL / Path: [https://github.com/hol353/ApsimX](https://github.com/hol353/ApsimX) <- URL of your ApsimX fork
- Host Type: GitHub
- Username: hol353 <- GitHub user name

We suggest you name the remote repository the same as your GitHub user name, hence the need to enter it twice. The reason for linking to two repositories will become evident later. You ALWAYS **pull** from the ApsimX repository and **push** to your forked repository.

At this point, you have all source code. If you wish to compile the code yourself, see [here](https://apsimnextgeneration.netlify.app/contribute/compile/). If you don’t wish to compile the code, you can run any of the examples/prototypes/test sets with the released version of apsim, but it will need to be up-to-date.

After you have made some changes to the code or test sets, you will need to [commit your changes](https://apsimnextgeneration.netlify.app/contribute/sourcetree/commit/).

## Initial setup

**The first time you use SourceTree** we recommend you turn staging off.

- Click ‘Commit’
- Choose ‘No staging’ in the drop down beside the ‘Modified files…’ drop down

![SourceTreeRemotes](https://apsimnextgeneration.netlify.app/images/Development.SourceTreeNoStaging.png)

## Commit

If you have files that you have added or modified, you can commit them to git. This process of adding commits keeps track of your progress as you work on files in APSIM.

Commits also create a transparent history of your work that others can follow to understand what you’ve done and why. Each commit has an associated commit message, which is a description explaining why a particular change was made. Furthermore, each commit is considered a separate unit of change. This lets you roll back changes if a bug is found, or if you decide to head in a different direction.

Commit messages are important, especially since Git tracks your changes and then displays them as commits once they’re pushed to the server. By writing clear commit messages, you can make it easier for other people to follow along and provide feedback.

Commits are local to your computer only until you do a push to a remote repository.

![SourceTreeRemotes](https://apsimnextgeneration.netlify.app/images/Development.SourceTreeCommit.png)

In the top left corner, SourceTree shows (by default) the files that you have modified but haven’t commited yet. If you have created new files that have never been commited they won’t be shown yet. To see these files, change the drop down box from ‘Modified files” to “Untracked”. Note that the .db files produced by APSIM simulations are ignored by git and should not be committed.

- You can then right click on the untracked files and select “Add” to tell git to start tracking them.
- If you don’t want to keep them, right click and select “Remove”. **This will delete them from your folder**
- Change the drop down back to “Modified files”

Clicking on a file will show you what you have changed. If you don’t want to keep the changes you have made, right click on the file and select ‘Discard’.

Tick the files you want to commit.

Finally, at the bottom type in a commit message, make sure ‘Push changes immediately…’ is **unticked** and then click Commit. At this point, your new commit is only on your computer and noone else can see it. You can commit files as many times as you wish.

**NOTE:** Before you bring your folder up to date, you need to [commit or discard all files that you have added or modified](https://apsimnextgeneration.netlify.app/development/commit). If you don’t do this you may get errors during the pull process outlined below.

## Pull

To bring the current branch up to date you get the latest commits from the *master* branch in the *MasterRepo* repository. Click the pull button:

![SourceTreeRemotes](https://apsimnextgeneration.netlify.app/images/Development.SourceTreePull.png)

Ensure the remote is *MasterRepo* and the branch is *master*. Leave all other checkboxes alone. This will bring down the latest commits from the MasterRepo/master branch into your ‘current’ branch (the one in bold in SourceTree).

**RECOMMENDATION:** You should always bring your branch up to date at the beginning of a major piece of work. In addition, you should also do a pull regularly, at least weekly.

## Push changes to a remote

Once you’re ready to share your commits with the wider APSIM community and have them merged into the master repository, you will need to push your commits to your forked remote repository (e.g. hol353). Doing a push won’t impact on other developers and won’t cause Jenkins to run the test suite. Pushing will allow other developers to pull from your branch on your repository so it is a good way to share what you are doing with others.

![SourceTreeRemotes](https://apsimnextgeneration.netlify.app/images/Development.SourceTreeRemotes.png)

In this image there are two remote repositories, hol353 (a developers remote) and MasterRepo (the main APSIM repository). **You should never push to the MasterRepo remote**. Instead, you push to your remote repository - *hol353* in this example. Click the push button.

![SourceTreeRemotes](https://apsimnextgeneration.netlify.app/images/Development.SourceTreePush.png)

Always make sure the remote (highlighted in the above image) is your remote and not *MasterRepo*. You also need to tick the branch you want to push to your remote repository, in this case master.

## Open a Pull Request

Pull Requests initiate discussion about your commits. They say to other developers that you are wanting a peer review of your changes.

You can open a Pull Request at any point during the development process: when you have little or no code but want to share some screenshots or general ideas, when you’re stuck and need help or advice, or when you’re ready for someone to review your work. By using GitHub’s @mention system in your Pull Request message, you can ask for feedback from specific people or teams, whether they’re down the hall or ten time zones away.

### 1. Peer review

Once a Pull Request has been opened, a developer will review your changes and may have questions or comments. Perhaps the coding style doesn’t match project guidelines, the change is missing unit tests, or maybe everything looks great. Pull Requests are designed to encourage and capture this type of conversation.

You can also continue to push to your branch in light of discussion and feedback about your commits. If someone comments that you forgot to do something or if there is a bug in the code, you can fix it in your branch and push up the change. GitHub will show your new commits and any additional feedback you may receive in the unified Pull Request view.

### 2. Jenkins build and run system

Jenkins will automatically run all pull requests and flag pass/fail with GitHub. If you have finished a piece of work then you need to state somewhere in the first comment box of the pull request:

Resolves #45

or

Working on #45

This will alert the administrators of the APSIM repository that the pull request fixes issue number 45 (or you are working on it). All merges to master must have an issue describing the piece of work. T

### 3. The APSIM Performance Testing site

The APSIM Performance Testing suite will also test your pull request, calculating statistics on all predicted / observed data found and check them against the ‘accepted’ statistics. This will also be reported back to your pull request.

## Merging with the MasterRepo

If the pull request has been reviewed by a developer, the Jenkins build system passes and the APSIM Performance Testing system also passes, the administrators will then merge the pull request with the master branch of the main repository and close the issue (if you specified ‘resolves’). Once the issue is closed it should not be reopened.

After a Pull request that resolves an issue is authorised to be merged, the the automated upgrade building process will commence to create an upgrade available in the upgrade manager of the user interface. The upgrade make take a while to generate and has the following naming: [Date of merge yyyy.mm.dd].[resolved issue number] “Issue description” (e.g. 2021.08.12.6699 Predicted-observed graphs not displaying).

---

## /development/git/git-cli/

Source: https://apsimnextgeneration.netlify.app/development/git/git-cli/
Title: CLI

# CLI

This is a guide to using version control from the command line. If you are stuck at any time, a useful git cheat sheet may be found [here](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet).

## Create GitHub account

The APSIM source code is located on GitHub so you will need to have a GitHub login if you want to contribute new features or modifications to the APSIM repository.

This document assumes that your APSIM Next Generation folder is ~/ApsimX/.

## (Optional) Fork the two repositories

There are two repositories:

1. [https://github.com/APSIMInitiative/ApsimX](https://github.com/APSIMInitiative/ApsimX) - This contains the main APSIM source code of the infrastructure and all models.
2. [https://github.com/APSIMInitiative/APSIM.Shared](https://github.com/APSIMInitiative/APSIM.Shared) - This contains many utilities and classes that are shared between many projects.

Both of these will need to be ‘forked’ to your GitHub account if you plan to change files in both repositories.

- Click on the fork link in the top right hand corner of the [APSIM repository](https://github.com/APSIMInitiative/ApsimX]) on GitHub. Clicking this will create a copy of the APSIM repository in your GitHub account.

## Install git

First, you will need to install the git client (if you don’t already have it installed):

`sudo apt install git`

## Clone the two Repositories

To bring the source code from GitHub to your computer, you will need to clone the two repositories. The ApsimX and APSIM.Shared directories should be siblings. For example if you clone ApsimX to ~/ApsimX, you should clone APSIM.Shared to ~/APSIM.Shared.

```
git clone https://github.com/APSIMInitiative/ApsimX
git clone https://github.com/APSIMInitiative/APSIM.Shared
```

## Add a remote repository

If you forked either of the repositories, you will need to add your remote repository:

```
cd ApsimX
git remote add $remote_name https://github.com/$username/ApsimX
```

Replace $username with your github username and $remote_name with a name of your choosing. This will be the name you use to refer to your remote repository. You will need to perform this step for both repositories if you forked both.

## Commit

If you have files that you have added or modified, you can commit them to git. This process of adding commits keeps track of your progress as you work on files in APSIM.

Commits also create a transparent history of your work that others can follow to understand what you’ve done and why. Each commit has an associated commit message, which is a description explaining why a particular change was made. Furthermore, each commit is considered a separate unit of change. This lets you roll back changes if a bug is found, or if you decide to head in a different direction.

Commit messages are important, especially since git tracks your changes and then displays them as commits once they’re pushed to the server. By writing clear commit messages, you can make it easier for other people to follow along and provide feedback.

Commits are local to your computer only until you do a push to a remote repository.

To list new/modified files use `git status`

To view the changes from the previous commit, use `git diff`

To undo changes which you don’t want to keep, use `git checkout ModifiedFile.txt`

Before you commit your changes you must first add any new or modified files to the index.

```
git add ModifiedFile.txt
```

To remove a file from the index, use the reset command:

```
git reset ModifiedFile.txt
```

To perform the commit:

```
git commit -m "Commit message"
```

For additional options/help, use `git help commit` or `man git`

**NOTE:** Before you bring your folder up to date, you need to [commit or discard all files that you have added or modified](https://apsimnextgeneration.netlify.app/contribute/cli/commit). If you don’t do this you may get errors during the pull process outlined below.

## Pull

Pulling from a remote branch will update a local branch to reflect the latest changes made in the remote branch.

**RECOMMENDATION:** You should always bring your branch up to date at the beginning of a major piece of work. In addition, you should also do a pull regularly, at least weekly.

You will usually want to pull from the master branch in the main APSIM repository.

To list your remote repositories and their associated URLs, use `git remote -v`

Then simply run `git pull <remote> <branch>`, where <remote> and <branch> are the names of the repository and branch you wish to pull from.

## Push changes to a remote

Once you’re ready to share your commits with the wider APSIM community and have them merged into the master repository, you will need to push your commits to your forked remote repository (e.g. hol353). Doing a push won’t impact on other developers and won’t cause Jenkins to run the test suite. Pushing will allow other developers to pull from your branch on your repository so it is a good way to share what you are doing with others.

To list your remote repositories, use `git remote`. To view remote URLs as well, use `git remote -v`.

**You should never push to the main APSIM repository** (located at [https://github.com/APSIMInitiative/ApsimX/](https://github.com/APSIMInitiative/ApsimX/)).

To push your current branch to a remote repository, use `git push <remote>`, where <remote> is the name of your remote repository. If you have not pushed your current branch before, you will need to create a remote branch: `git push -u <remote> <branch_name>`.

For more details, see `git help push`.

## Open a Pull Request

Pull Requests initiate discussion about your commits. They say to other developers that you are wanting a peer review of your changes.

You can open a Pull Request at any point during the development process: when you have little or no code but want to share some screenshots or general ideas, when you’re stuck and need help or advice, or when you’re ready for someone to review your work. By using GitHub’s @mention system in your Pull Request message, you can ask for feedback from specific people or teams, whether they’re down the hall or ten time zones away.

To open a pull request, open a web browser and navigate to your remote repository (or the APSIM repository under pull requests tab) on GitHub, then click New Pull Request.

### 1. Peer review

Once a Pull Request has been opened, a developer will review your changes and may have questions or comments. Perhaps the coding style doesn’t match project guidelines, the change is missing unit tests, or maybe everything looks great. Pull Requests are designed to encourage and capture this type of conversation.

You can also continue to push to your branch in light of discussion and feedback about your commits. If someone comments that you forgot to do something or if there is a bug in the code, you can fix it in your branch and push up the change. GitHub will show your new commits and any additional feedback you may receive in the unified Pull Request view.

### 2. Jenkins build and run system

Jenkins will automatically run all pull requests and flag pass/fail with GitHub. If you have finished a piece of work then you need to state somewhere in the first comment box of the pull request:

Resolves #45

or

Working on #45

This will alert the administrators of the APSIM repository that the pull request fixes issue number 45 (or you are working on it). All merges to master must have an issue describing the piece of work.

### 3. The APSIM Performance Testing site

The APSIM Performance Testing suite will also test your pull request, calculating statistics on all predicted / observed data found and check them against the ‘accepted’ statistics. This will also be reported back to your pull request.

## Merging with the MasterRepo

If the pull request has been reviewed by a developer, the Jenkins build system passes and the APSIM Performance Testing system also passes, the administrators will then merge the pull request with the master branch of the main repository and close the issue (if you specified ‘resolves’). Once the issue is closed it should not be reopened.

After a Pull request that resolves an issue is authorised to be merged, the the automated upgrade building process will commence to create an upgrade available in the upgrade manager of the user interface. The upgrade make take a while to generate and has the following naming: [Date of merge yyyy.mm.dd].[resolved issue number] “Issue description” (e.g. 2021.08.12.6699 Predicted-observed graphs not displaying).

---

## /usage/commandline/commandlinetutorialwindows/

Source: https://apsimnextgeneration.netlify.app/usage/commandline/commandlinetutorialwindows/
Title: Windows Tutorial

# Windows Tutorial

# Example workflow for APSIMX command line

- In this example we will demonstrate building a simulation from scratch using the command line.
- We will start with building a config file that gets an absolute minimum simulation.
- From there we will build up the simulation into something that contains multiple nodes.
- Afterwards we will describe how to modify, delete and copy nodes from another APSIMX file.

## Who is this tutorial for?

- This tutorial is for anyone who is unfamiliar with running APSIM from the command line.
- This is also great for user’s wanting to make repeatable changes without using the full version of APSIM

## 1. Creating a minimal simulation

1. Find your computer’s location of models.exe
  1. The location on this computer is the default which is under: `C:\Program Files\APSIM<your version number>\bin`.

2. Copy the path of models.exe containing directory.
3. To keep everything organised and isolated from other files, let’s create a directory just for this tutorial.
  - Let’s make a directory called cli-tutorial directly under C: drive.
  - Open a terminal and type the command `cd/`.
  - Next make a fresh directory called ‘cli-tutorial’ by typing the command `mkdir cli-tutorial`

4. let’s go to this directory now so that any files we make from now on are stored here. To do this type the command `cd cli-tutorial`
5. Next, let’s create a config file which will contain our commands in a file called ‘commands.txt’. To do this type the command `type nul > commands.txt`
6. Let’s add a command to save a minimum runnable apsimx file to this config file. To do this type `notepad commands.txt`
  - add the line `save cli-tutorial.apsimx`.
  - save and close the file and return to the terminal.

7. ok, now we will run the command line version of Apsimx. Earlier we copied the path of models.exe’s directory. We can now paste this into the terminal.
  - Before pressing the enter key, type `\Models.exe --apply commands.txt`. Making sure to include a space between the models.exe file path and ‘–apply’.
    - Tip: If you have a space in your file path to the Models.exe, such as with the above example with `C:\Program Files\` you can put quotes on either end of the file path, making it ignore the space. Having a space can cause the command not to run.
    - It should look like this: `"C:\Program Files\APSIM<your version number>\bin\Models.exe" --apply commands.txt`

  - After a short pause, we can type `dir`. We should see a new file now called cli-tutorial.apsimx, along with a backup file called ‘NewSimulation.bak’, and our config file called ‘commands.txt’.
  - let’s open the file and see what is in there. You’ll see that there is a Simulations node with an empty DataStore node as a child.

8. You’ve made a minimal apsimx file. From here you can build up the simulation with any nodes that you like. See below on how to do that.

## 2. Modifying a simulation

The scenario for this tutorial is we want to run a simulation with a different soil and a different weather file.

To begin we will use our barebones file we created in the previous step. If you have not got this file, follow the instructions above in part 1 [Creating a minimal simulation](https://apsimnextgeneration.netlify.app/usage/commandline/commandlinetutorialwindows/#1-creating-a-minimal-simulation).

1. To begin, let’s make sure we are in the same directory we finished in from Part 1 in a terminal. The file path for this is: `C:\cli-tutorial`
2. Let’s open up the notepad and add some steps to a config file called `commands.txt`. To do this type `notepad commands.txt`.
3. Before we add anything, lets change the keyword `save` to `load`.
4. In order to copy nodes from a file, the file has to be present in the directory we are running the commands from. So in order to take some of the nodes from APSIM’s example files we will copy these into the directory we are currently working in. To do this, run this command: `copy "C:\Program Files\Apsim<your apsim version number>\Examples\Wheat.apsimx" C:\cli-tutorial\`.
5. Let’s copy a complete simulation from the wheat example in the apsim next gen examples. To do this let’s add a copy command to the commands.txt file. The command looks like this: `add [Simulations] Wheat.apsimx;[Simulation]`.
  - This command simply says: add the node called Simulation from the wheat.apsimx file and place within the node called Simulations in the currently loaded apsimx file.

6. Now that we have a simulation all ready to run we can start changing the nodes. Let’s start by setting up the simulation to just run one year. To make this change, open the commands.txt file and add the command: `[Clock].End=31/12/1901`. The start time is already set to the start of the year 1901.
7. Let’s run the simulation now to gather the data. To do this add another line in commands.txt. The command: `run`.
8. We will gather the data in csv format. To do this we will add another switch to our models execution command in the next step.
9. Let’s run this with the command: `"C:\Program Files\APSIM<your version number>\bin\Models.exe" --apply commands.txt --csv`
10. Next let’s change the weather and soil nodes too so we can see how that changes the outputs.
11. Before we do anything else, let’s remove the add command from the commands.txt file, it looks like this: `add [Simulations] Wheat.apsimx;[Simulation]`. This will prevent us from adding an additional Simulation node to our apsimx file.
12. In order to change the soil on this simulation, its easiest to copy one from an existing simulation or use one of the nodes already within apsim. To do this we must first have a donor APSIM file located in the same folder. Let’s copy an example file from the APSIM examples folder and put it into our working directory. Let’s copy the Chickpea example from the examples folder. On my computer this is located at `C:\Program Files\APSIM<your version number>\Examples\Chickpea.apsimx`.
  - if you’re in your cli-tutorial directory you can copy this by running the command in the terminal: `copy "C:\Program Files\APSIM<your version number>\Examples\Chickpea.apsimx" .`

13. Open the commands.txt file and add this line below the line starting with “[Clock]”: `[Soil]=Chickpea.apsimx;[Black Vertosol-Mywybilla (Bongeen No001)]`
14. To change the weather file we will need to have a weather file copied to the same directory. Let’s copy the Kingaroy file from the examples folder with the following command: `copy "C:\Program Files\APSIM<your version number>\Examples\WeatherFiles\AU_Kingaroy" .`
15. Now let’s change weather node to look for the `AU_Kingaroy.met` file. Add the command below the “[Soil]” command: `[Weather].FileName=AU_Kingaroy.met`
16. Your `commands.txt` file should look like the example below:

```
load cli-tutorial.apsimx
[Clock].Start=1900/01/01
[Clock].End=1901/12/31
[Soil]=Chickpea.apsimx;[Black Vertosol-Mywybilla (Bongeen No001)]
[Weather].FileName=AU_WaggaWagga.met
save cli-tutorial-pt2.apsimx
run
```

1. Finally, let’s run the config file with the command in the terminal: `"C:\Program Files\APSIM<your version number>\bin\Models.exe" --apply commands.txt --csv`

## Recap

After completing these tutorials we’ve learned how to:

- use the `--apply` switch to add and modify an APSIM file
- write a config file to make changes to an APSIM file
- output data as csv format using the `--csv` switch
- use existing APSIM files to build and modify another APSIM file

---

## /usage/commandline/command-line-linux/

Source: https://apsimnextgeneration.netlify.app/usage/commandline/command-line-linux/
Title: Command Line on Linux

# Command Line on Linux

# Install

There are two options, option 1 is recommended for users running APSIM on cloud infrastructure (HPC, AWS, Azure) or WSL (Windows Subsystem for Linux)

1. run APSIM using a docker container
2. install APSIM using debian file (.deb) to see how to do this click [here](https://apsimnextgeneration.netlify.app/install/linux/)

# Running APSIM on Linux using Docker container

*Note: it helps to be familiar with the linux command line basics to perform the following steps.*

1. Make sure you have the docker engine installed. Instructions on how to do this can be found [here](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
2. Pull down the apsimng docker image using: `docker pull apsiminitiative/apsimng`
3. To see an example of how to run the wheat example, follow the instructions from the [APSIM.Docker GitHub repo](https://github.com/APSIMInitiative/APSIM.Docker) otherwise continue.
4. Organise your files into a directory. I’ll use an example directory here called `test-run`
5. Place an Apsimx file in this directory called `Wheat.apsimx`
6. Change directory to the newly created test-run directory.
7. Run the simulation using this command: `docker run -i --rm -v "$PWD:/test-run" apsiminitiative/apsimng /test-run/Wheat.apsimx`
8. You can use any commands available for the APSIM command line tool such as `--apply` or `--csv` after the `apsiminitiative/apsimng` command portion in the above docker command. The above command simply ran the Wheat.apsimx file we put in the test-run directory.

---

## /usage/commandline/commandlanguage-old-to-new/

Source: https://apsimnextgeneration.netlify.app/usage/commandline/commandlanguage-old-to-new/
Title: APSIM Command Language (old to new)

# APSIM Command Language (old to new)

The APSIM command language has changed to make it more intuitive. [The new language is described here](https://apsimnextgeneration.netlify.app/usage/commandline/commandlanguage). Most of the changes are to the `add` command. The other commands remain unchanged.

Examples that show how to convert new old syntax to the new syntax.

## Old -> New

- **add** - add a new or existing model to another model. ``` add [Zone] Report -> add new Report to [Zone] add [Zone] Report MyReport -> add new Report to [Zone] name MyReport add [Zone] soils.apsimx;[Soil1] Soil -> add [Soil1] from soils.apsimx to [Zone] name Soil ```
- **duplicate** - duplicate a model.
  - `duplicate [Zone].Report NewReport` -> `duplicate [Zone].Report name NewReport`

- **comment lines** - only `#` is supported as a comment character.

---

## /development/how-to-modify-the-web-site/

Source: https://apsimnextgeneration.netlify.app/development/how-to-modify-the-web-site/
Title: How to modify the web site

# How to modify the web site

The contents of this website are generated by the hugo rendering engine ([https://gohugo.io/](https://gohugo.io/)). Hugo transforms the markdown files under the directory ApsimX/docs into a website.

To make a change to the website, modify or create new markdown files, commit the changes and create a pull request on github. When the pull request is merged, the website will be automatically updated.

Before creating a pull request however, it might be a good idea to preview the changes you’ve made to the website, to ensure they look the way you intend.

1. Download hugo from [here](https://github.com/APSIMInitiative/ApsimX/Docs/Hugo/Hugo.zip)
2. Extract and place extracted folder where you normally install your programs for instance: `C:\Program Files`
3. (Optional) add the hugo binary to PATH You will need to run hugo from a terminal. This is more convenient if the hugo binary is on PATH.
4. Open a terminal, navigate to ApsimX/docs, and run `hugo server`: ``` cd /path/to/ApsimX/docs hugo server ```
5. Open a web browser and navigate to [https://localhost:1313](https://localhost:1313)
6. Note: To have the new changes made to the live site, simply create a pull request, making sure to include a `resolves #1234` comment (you may have to create a new issue in GitHub prior to doing this). This ensures changes are updated by Netlify when the pull request is merged.

---

## /usage/commandline/playlist/

Source: https://apsimnextgeneration.netlify.app/usage/commandline/playlist/
Title: Playlist

# Playlist

## Playlist (Running specified simulations in a file)

The playlist model can be used to only run specific simulation models in a file.

To do this you can add a playlist model to the `Simulations` model and add the names of the simulations or by using an expression in the provided text field.

### Simple Playlist Usage

To run a single file use a command like:

`Models.exe my_sim_name.apsimx --playlist playlist_name`

### Playlist usage with –apply switch

The Playlist’s text property can be changed dynamically using the `--apply` switch. This allows users to selectively run specific `Simulation`’s in an apsimx file.

Here is an example config file (commands.txt) that will run just Simulation named Simulation1 in an apsimx file (example.apsimx) that has two Simulation one named Simulation and another named Simulation1:

```
load example.apsimx
add [Simulations] Playlist
[Playlist].Text="Simulation1"
save sim1_example.apsimx
load sim1_example.apsimx
run
```

You’d run this with the command:

`Models.exe --apply commands.txt --playlist playlist`

Additional details are included below on its usage:

Enter a list of names of simulations that you want to run. Case insensitive.

> A wildcard * can be used to represent any number of characters. A wildcard # can be used to represent any single character. Simulations and Experiments can also be added to this playlist by right-clicking on them in the GUI. Examples: Sim1, Sim2, Sim3 - Runs simulations with exactly these names [Sim1, Sim2, Sim3] - Also allows [ ] around the entry Sim1 - Entries can be entered over multiple lines Sim2 Sim# - Runs simulations like Sim1, SimA, Simm, but will not run Sim or Sim11 Sim* - Runs simulations that start with Sim *Sim - Runs simulations that end with Sim *Sim* - Runs simulations with Sim anywhere in the name

---

## /contribute/science-contributions/

Source: https://apsimnextgeneration.netlify.app/contribute/science-contributions/
Title: Science contributions

# Science contributions

### Documentation

- Documentation is automatically generated from the submitted validation .apsimx file.
- A science document may also be submitted by the model author (e.g. [see AgPasture science document](https://apsimnextgeneration.netlify.app/modeldocumentation/)).
- All equations shall have units on all variables.

### Examples

- Good examples are important in showing the user different ways of configuring and parameterising the model.
- A single example file must be submitted by the model author. When it makes sense to do so it should contain:
  - A short memo describing the model and example
  - A simple simulation with good manager scripts that show a typical usage of the model. The report model should show the main outputs from the model. The example should also have one or more graphs showing model outputs.
  - Additional simulations or experiments should be added that show the model in typical usage scenarios. These may include:
  - a plant model in rotation with another plant model.
  - a plant model that is intercropped with another plant model.
  - a plant model being consumed by a plant consumer. This could be stock, a pest / disease or by using the SimpleGrazing model.

### Validation tests

Model submissions will provide evidence that the model works. This is normally done via validation tests that show predicted with observed data, along with validation statistics. The validation tests need to be accompanied by [memo](https://apsimnextgeneration.netlify.app/usage/memo) text that describe the experiment and treatments. The validation .apsimx file is also converted to [HTML via auto documentation](https://apsimnextgeneration.netlify.app/contribute/science-contributions/apsimnextgeneration.netlify.app/modeldocumentation/).

### Sensibility tests

Sensibility tests will be provided to broaden the validation tests into other GxExM scenarios. This is particularly important when the validation is limited in its scope, in particular for GxExM situations that are thought to be important, but where there is no data. Sensibility tests need to be accompanied by [memo](https://apsimnextgeneration.netlify.app/usage/memo) text that describes what the sensibility plots show and why the results ‘make sense’.

### Move a model to release

Once a model has been approved by the APSIM Initiative it can be moved into the release.

1. Copy the plant model node from the Replacements node in the prototype simulation ![Copy model from replacements](https://apsimnextgeneration.netlify.app/images/Development.Contribute.MoveModelToRelease.CopyModel.png)
2. Paste this into a text editor and save as a json file into ApsimX\Models\Resources folder.
3. Add the new file into the APSIMX solution. In VisualStudio, use the Solution Explorer tab to locate Model\Resources in the Models project, right-click on Resources to open a pop-up menu, select Add>Existing Item. Navigate to the folder where the newly created json file was saved, select it and click Add. The file should now appear under Model\Resources. ![Add model json as resource](https://apsimnextgeneration.netlify.app/images/Development.Contribute.MoveModelToRelease.AddModelXmlAsResource.png)
4. Locate it and right-click, select properties and change Build Action to ‘None’.
5. Add a reference to the model as an Apsim resource. For this, open the Resources.resx file (locate under Model/Properties). Copy a node from a similar existing model and change the name and value to match the new model. Note that this is case sensitive. ![Add to resX file](https://apsimnextgeneration.netlify.app/images/Development.Contribute.MoveModelToRelease.AddToResXFile.png)
6. Add icons for the model. For this, create png images, with the same name as the model, and save in ApsimNG\Resources\LargeImages (32pixels) and ApsimNG\Resources\TreeViewImages (16 pixels). These should be added to the solution (as per step 3 and 4 above). After adding the images, locate them in Solution Explorer, right click on each, select properties and change Build Action to ‘Embedded Resource’.
7. Add an example simulation to Examples folder.
8. Copy the prototype simulation from the Prototype folder into its own folder in ApsimX\Tests\Validation. In this simulation, delete the model node in Replacements.
9. Delete the model’s simulation and folder from the Prototypes folder
10. Commit all, and create a Pull Request to have all these changes merged into the APSIM repository.

---

## /development/tutorial/

Source: https://apsimnextgeneration.netlify.app/development/tutorial/
Title: Tutorial

# Tutorial

- [Build your first model](https://apsimnextgeneration.netlify.app/development/tutorial/buildmodeltutorial)
- [How PMF functions work](https://apsimnextgeneration.netlify.app/development/tutorial/howpmffunctionswork)

---

## /development/tutorial/buildmodeltutorial/

Source: https://apsimnextgeneration.netlify.app/development/tutorial/buildmodeltutorial/
Title: Build a model tutorial

# Build a model tutorial

In this step-by-step guide we will show how to create a new model for APSIM. The model we will be building is a rainfall modifier. This will be a simple model that changes the rainfall in a simulation, after a user specified date, using a simple multiplier and addition. It will modify the rainfall before the other models in APSIM use the rainfall value. This will allow you to see the effects on the crop of reducing or increasing the rainfall.

The sections in this guide increase in complexity. To follow along with this tutorial you can build the model using the manager component in the user interface (manager scripts are just models). Alternatively, you can install the necessary tools to compile and build APSIM using these steps:

- get all source code from GitHub via [a Git client](https://apsimnextgeneration.netlify.app/contribute/sourcetree) or via [the command line](https://apsimnextgeneration.netlify.app/contribute/cli)
- install [compilers](https://apsimnextgeneration.netlify.app/contribute/compile)

# 1. Create a basic model

The simplest APSIM model looks like this:

```
using Models.Core;
using System;
namespace Models
{
    /// <summary>This is a simple rainfall modifier model.</summary>
    [Serializable]
    [ValidParent(ParentType = typeof(Simulation))]
    public class RainfallModifier : Model
    {
    }
}
```

1. All models in APSIM must derive from *Model* - `public class SimpleModel : Model`
2. To allow users, via the user interface, to add the model to another model (as a child), the model developer needs to specify the valid parent models - `[ValidParent(ParentType = typeof(Simulation))]`. This will allow users to add *RainfallModifier* to a *Simulation* model. Other common options could have been *Zone*. All models can be added to a *Folder* so there is no need to specify *Folder* as a valid parent. Multiple valid parents can be specified by duplicating the *ValidParent* attribute.
3. The `[Serializable]` attribute is needed for all models and indicates that the model instance can be converted to a string (JSON) and written to the .apsimx file.
4. This model, in its current form, can be compiled and run in APSIM, even though it doesn’t do anything yet.

# 2. Add input parameters.

Models can define user specified (via the user interface) input parameters.

```
using Models.Core;
using System;

namespace Models
{
    /// <summary>This is a simple rainfall modifier.</summary>
    [Serializable]
    [ValidParent(ParentType = typeof(Simulation))]
    [ViewName("UserInterface.Views.GridView")]
    [PresenterName("UserInterface.Presenters.PropertyPresenter")]
    public class RainfallModifier : Model
    {
        /// <summary>Start date for modifying rainfall</summary>
        [Description("Start modifying rainfall from date:")]
        public DateTime StartDate { get; set; }

        /// <summary>Rainfall muliplier</summary>
        [Description("Rainfall multiplier: ")]
        public double RainfallMultiplier { get; set; }

        /// <summary>Rainfall addition</summary>
        [Description("Rainfall addition (mm): ")]
        public double RainfallAddition { get; set; }
    }
}
```

The above code defines three parameters: StartDate, RainfallMultiplier and RainfallAddition. The model will ultimately modify (using the multipler and addition properties) the simulation’s rainfall after the user specified StartDate. For now these three properties are placeholders and aren’t being used yet.

1. The *Description* attributes define the text the user will see in the user interface.
2. The *ViewName* and *PresenterName* attributes on the *RainfallModifier* class instruct the APSIM user interface to use a grid view and a property presenter (keyword / value) when the user clicks on the *RainfallModifier* model.

# 3. Add an output property

This step will add a single output to return the unmodified rainfall variable, that is the original rainfall value before this model changed it. This will be a useful output for diagnosis purposes.

```
using Models.Core;
using System;

namespace Models
{
    /// <summary>This is a simple rainfall modifier.</summary>
    [Serializable]
    [ValidParent(ParentType = typeof(Simulation))]
    [ViewName("UserInterface.Views.GridView")]
    [PresenterName("UserInterface.Presenters.PropertyPresenter")]
    public class RainfallModifier : Model
    {
        /// <summary>Start date for modifying rainfall</summary>
        [Description("Start modifying rainfall from date:")]
        public DateTime StartDate { get; set; }

        /// <summary>Rainfall muliplier</summary>
        [Description("Rainfall multiplier: ")]
        public double RainfallMultiplier { get; set; }

        /// <summary>Rainfall addition</summary>
        [Description("Rainfall addition (mm): ")]
        public double RainfallAddition { get; set; }

        /// <summary>An output variable.</summary>
        public double OriginalRain { get; private set; }
    }
}
```

The new property is call *OriginalRain*. APSIM makes all public properties visible and accessible to other models in a simulation. For example, the user can use the *Report* model to output the value of this property by specifying the output: `[RainfallModifier].OriginalRain`

The *OriginalRain* property in this example also defines a private setter so that other models cannot modify the value of this property. Only the *RainfallModifier* model is allowed to modify *OriginalRain*. To allow other models to modify the property. The *private* designator can be removed leaving:

`public double OriginalRain { get; set; }`

# 4. Add links to other models

This model will need to access properties from the *Clock* and *Weather* models in APSIM. To allow this, links are specified to each of these models.

```
using Models.Climate;
using Models.Core;
using System;

namespace Models
{
    /// <summary>This is a simple rainfall modifier.</summary>
    [Serializable]
    [ValidParent(ParentType = typeof(Simulation))]
    [ViewName("UserInterface.Views.GridView")]
    [PresenterName("UserInterface.Presenters.PropertyPresenter")]
    public class RainfallModifier : Model
    {
        [Link]
        Clock clock = null;

        [Link]
        Weather weather = null;

        /// <summary>Start date for modifying rainfall</summary>
        [Description("Start modifying rainfall from date:")]
        public DateTime StartDate { get; set; }

        /// <summary>Rainfall muliplier</summary>
        [Description("Rainfall multiplier: ")]
        public double RainfallMultiplier { get; set; }

        /// <summary>Rainfall addition</summary>
        [Description("Rainfall addition (mm): ")]
        public double RainfallAddition { get; set; }

        /// <summary>An output variable.</summary>
        public double OriginalRain { get; private set; }
    }
}
```

The *[Link]* attribute indicates a dependency on another model. In this case the *RainfallModifier* model depends on (uses) *Clock* and *Weather*. APSIM will ensure these dependencies are met at runtime. It will find a clock and weather model and set the values of these two fields so that *RainfallModifier* can communicate with the two external models.

Note: Clock is the model in APSIM that provides the current simulation date which will be needed in the next step.

# 5. Add implementation.

The last step in creating the model is to write the implementation code that modifies rainfall after the user specified *StartDate*.

```
using Models.Climate;
using Models.Core;
using System;

namespace Models
{
    /// <summary>This is a simple rainfall modifier model.</summary>
    [Serializable]
    [ValidParent(ParentType = typeof(Simulation))]
    [ViewName("UserInterface.Views.GridView")]
    [PresenterName("UserInterface.Presenters.PropertyPresenter")]
    public class RainfallModifier : Model
    {
        [Link]
        Clock clock = null;

        [Link]
        Weather weather = null;

        /// <summary>Start date for modifying rainfall</summary>
        [Description("Start modifying rainfall from date:")]
        public DateTime StartDate { get; set; }

        /// <summary>Rainfall muliplier</summary>
        [Description("Rainfall multiplier: ")]
        public double RainfallMultiplier { get; set; }

        /// <summary>Rainfall addition</summary>
        [Description("Rainfall addition (mm): ")]
        public double RainfallAddition { get; set; }

        /// <summary>An output variable.</summary>
        public double OriginalRain { get; private set; }

        /// <summary>Handler for event invoked by weather model to allow modification of weather variables.</summary>
        [EventSubscribe("PreparingNewWeatherData")]
        private void ModifyWeatherData(object sender, EventArgs e)
        {
            OriginalRain = weather.Rain;
            if (clock.Today >= StartDate)
                weather.Rain = RainfallMultiplier * weather.Rain + RainfallAddition;
        }
    }
}
```

The above code introduces a method (function) called *ModifyWeatherData*. The *EventSubscribe* attribute indicates that the method is an event handler that will be invoked (called) whenever a *PreparingNewWeatherData* event is published. In APSIM this event is published by a weather model after it has read the days weather data and before other models access the weather data. The event is published to allow models like *RainfallModifier* the change weather data e.g. for climate change simulations.

The implementation is quite simple:

1. It stores the weather models rainfall into the *OriginalRain* property.
2. It tests the current simulation date (*clock.Today*) to see if it is greater than the user specified *StartDate*
3. If the simulation date is greater than the start date it modifies the rainfall.

It is worth noting that when multiple models respond to a published event, they will be processed in the order they appear in the Explorer tree structure. In this example, if two instances the model were provided, they both respond to the published PreparingNewWeatherData event. The first would provide the response outlined above, with the second model using this altered rainfall as its OriginalRainfall and further modifying the rainfall in weather.

---

## /development/tutorial/howpmffunctionswork/

Source: https://apsimnextgeneration.netlify.app/development/tutorial/howpmffunctionswork/
Title: How PMF functions work

# How PMF functions work

In this tutorial we will explain how Plant Modelling Framework (PMF) functions work. We will use the wheat leaf photosynthesis model as an example.

Prerequisite: It is suggested you read [how to build a model](https://apsimnextgeneration.netlify.app/development/tutorial/buildmodeltutorial) first.

# 1. The PMF leaf organ

There are multiple PMF leaf organs that different crops use. For this tutorial we will examine the organ *Leaf* in Leaf.cs. This is the organ that wheat uses. The other leaf organs work the same way with respect to photosynthesis so the information in this tutorial is relevant for other crop models in APSIM.

```
/// <summary>The photosynthesis</summary>
[Link(Type = LinkType.Child, ByName = true)]
IFunction Photosynthesis = null;
```

The leaf organ has a link to a photosynthesis model that is of type *IFunction*. *Leaf* has a single call to this *Photosynthesis* function to get the amount of dry matter fixed for the day (g/m2):

```
 DMSupply.Fixation = Photosynthesis.Value();
```

The leaf organ knows nothing of the implementation of *Photosynthesis* other than it is an *IFunction*.

# 2. IFunction

As we saw in the previous code block, the *Photosynthesis* *IFunction* has a *Value* method that returns a double. All PMF functions (models) implement *IFunction* and so must supply an implementation of this method.

```
public interface IFunction
{
    /// <summary>Gets the value of the function.</summary>
    double Value(int arrayIndex = -1);
}
```

# 3. Where is the implementation of photosynthesis?

Most crop models in APSIM use the same implementation of photosynthesis but parameterise it in different ways. The flexibility exists though for the model developer to use a different implementation.

To determine what implementation and parameterisation are used for a particular crop model:

- From the user interface, open a wheat example.
- By default the wheat model won’t show it’s structure or parameterisation. To show more detail, right click on the wheat model and select ‘Show model structure’.

![Wheat model structure](https://apsimnextgeneration.netlify.app/images/Wheat.ModelStructure.png)

The image above shows *Photosynthesis* selected (under wheat) and the tooltip showing *RUEModel*. This tells us the c# class being used is *RUEModel*. The image also shows us that there are 7 child models of *RUEModel*, *RUE*, *FT*, *FN*, *FW*, *FVPD*, *FCO2* and *RandInt*.

The user interface wheat visualisation comes from the wheat.json file in the resources, which is another way of determining what functions (models) wheat photosynthesis is using.

# 4. *RUEModel*

The source code of the *RUEModel* looks like this:

```
    public class RUEModel : Model, IFunction
    {
        /// <summary>The RUE function</summary>
        [Link(Type = LinkType.Child, ByName = true)]
        IFunction RUE = null;

        /// <summary>The FCO2 function</summary>
        [Link(Type = LinkType.Child, ByName = true)]
        IFunction FCO2 = null;

        /// <summary>The FN function</summary>
        [Link(Type = LinkType.Child, ByName = true)]
        IFunction FN = null;

        /// <summary>The FT function</summary>
        [Link(Type = LinkType.Child, ByName = true)]
        public IFunction FT = null;

        /// <summary>The FW function</summary>
        [Link(Type = LinkType.Child, ByName = true)]
        IFunction FW = null;

        /// <summary>The FVPD function</summary>
        [Link(Type = LinkType.Child, ByName = true)]
        public IFunction FVPD = null;

        /// <summary>The radiation interception function.</summary>
        [Link(Type = LinkType.Child, ByName = true)]
        public IFunction RadnInt = null;

        /// <summary>Total plant "actual" radiation use efficiency.</summary>
        [Units("gDM/MJ")]
        public double RueAct
        {
            get
            {
                double RueReductionFactor = Math.Min(FT.Value(), Math.Min(FN.Value(), FVPD.Value()))
                * FW.Value() * FCO2.Value();
                return RUE.Value() * RueReductionFactor;
            }
        }

        /// <summary>Daily growth increment of total plant biomass</summary>
        /// <returns>g dry matter/m2 soil/day</returns>
        public double Value(int arrayIndex = -1)
        {
            double radiationInterception = RadnInt.Value(arrayIndex);
            if (Double.IsNaN(radiationInterception))
                throw new Exception("NaN Radiation interception value supplied to RUE model");
            if (radiationInterception < -0.000000000001)
                throw new Exception("Negative Radiation interception value supplied to RUE model");
            return radiationInterception * RueAct;
        }
    }
```

- The *RUEModel* model implements *IFunction*.
- There are links to the seven functions that we noted where under photosynthesis in the user interface.
- There is a public property (output) called *RueAct*.
  - Returns actual RUE by multiplying the smallest child function (FT, FN, FVPD) by FW and FCO2 and then RUE.

- The *Value* method provides the photosynthesis implementation.
  - It calls the *Value* method of the *RadnInt* function to get the amount of radiation interception.
  - It throws an exception if the *radiationInterception* is NaN or negative.
  - It returns radiationInterception * RueAct.

- The level of indirection caused by having child functions for each of several multipliers offers great flexibility to the model developer in defining photosynthesis. It lets the model developer, from the user interface, change the individual multipliers from constants to a more complex linear interpolation or any other function type. For example: *FT* is a *WeightedTemperatureFunction* and *FN* is a *LinearInterpolationFunction*:

![Wheat FN](https://apsimnextgeneration.netlify.app/images/Wheat.Photosynthesis.FN.png)

The above image shows the visualisation of the *FN* linear interpolation. To determine what the X variable is you need to click on *XValue* in the simulation tree:

![Wheat FN](https://apsimnextgeneration.netlify.app/images/Wheat.Photosynthesis.FN2.png)

The image above shows the model developer has specified *[Leaf].Fn* which means the FN linear interpolation will call the *Fn*property in *Leaf* to get the x value for the linear interpolation. The *Fn* property in leaf looks like this:

```
        [Units("0-1")]
        public double Fn
        {
            get
            {
                double f;
                double functionalNConc = (CohortParameters.CriticalNConc.Value()
                             - CohortParameters.MinimumNConc.Value() * CohortParameters.StructuralFraction.Value())
                             * (1 / (1 - CohortParameters.StructuralFraction.Value()));
                if (functionalNConc <= 0)
                    f = 1;
                else
                    f = Math.Max(0.0, Math.Min(Live.MetabolicNConc / functionalNConc, 1.0));

                return f;
            }
        }
```

The implementation of *Fn* then calls other functions: *CriticalNConc*, *MinimumNConc* and *StructuralFraction* which are all defined under *Leaf*.

# 5. Conclusion

This level of indirection (where one function calls another function which calls somewhere else) makes it very difficult to follow the logic of how photosynthesis works. The advantage though is that it is very flexible for the model developer to create models visually using the user interface. To help understand the PMF structure, it is recommended that you run the APSIM user interface showing the model structure beside the source code.

---

## /development/software/compile-apsimng/

Source: https://apsimnextgeneration.netlify.app/development/software/compile-apsimng/
Title: Publish APSIMNG from source code

# Publish APSIMNG from source code

## Prerequisite

- git
- Visual Studio 2022

## Checkout the latest source codes from APSIMInitiative

```
git clone  --depth 1  https://github.com/APSIMInitiative/ApsimX.git
```

## Publish solution for batch mode

Run following commands under the ApsimX directory

Publish for windows

```
dotnet publish -c Release -f net8.0 -r win-x64   --self-contained ApsimX.sln
```

Publish for Ubuntu

```
dotnet publish -c Release -f net8.0 -r ubuntu.20.04-x64 --self-contained ApsimX.sln
```

Publish for SLES (e.g. CSIRO cluster):

```
dotnet publish -c Release -f net8.0 -r sles.15-x64 --self-contained ApsimX.sln
```

All runtime identify for other operating system can be found from [github](https://github.com/dotnet/runtime/blob/main/src/libraries/Microsoft.NETCore.Platforms/src/runtime.json)

Copy the contents `bin/Release/net8.0/<runtime-identify>/publish/` to your operating system.

## .NET runtime

Apsim NG has been updated to run using .NET 8.0. This can be downloaded [from dotnet](https://dotnet.microsoft.com/en-us/download/dotnet/8.0).

## Further steps

Sqlite has been included as a nuget package in the ApsimNG project and is no longer installed seperately. However if you are using an older version of the source code this may be required.

On Windows, check whether `sqlite3.dll` is under `bin\Release\net8.0\win-x64\publish` folder. If not, copy from `bin\Release\net8.0\win-x64\` to `publish` folder.

On Linux, sqlite3 should be installed into system with following command

for Ubuntu

```
sudo apt install sqlite3
```

for CSIRO cluster

```
module load sqlite/3.35.5
```

Asp .netcoreapp3 requires `openssl 1.0`.

`openssl 3.0` is installed in the Ubuntu 22.04 by default and should be removed and reinstalled with `openssl 1.0`.

---

## /_header/

Source: https://apsimnextgeneration.netlify.app/_header/
Title: APSIM Docs

# APSIM Docs

![APSIM](https://apsimnextgeneration.netlify.app/images/ApsimLogo.png)

---

## /user_tutorials/

Source: https://apsimnextgeneration.netlify.app/user_tutorials/
Title: APSIM Next Gen User Tutorials

# APSIM Next Gen User Tutorials

Below you will find tutorials to get you up to speed on using APSIM Next Gen. These tutorials are based off the existing APSIM Classic (7.10) tutorials that have been updated to the new APSIM Next Gen workflow.

- [Module 1: Fallow Simulation](https://apsimnextgeneration.netlify.app/user_tutorials/module1/moduleonetutorial)
- [Module 2: Soil Organic Matter](https://apsimnextgeneration.netlify.app/user_tutorials/module2/moduletwotutorial)
- [Module 3: The Nitrogen Cycle](https://apsimnextgeneration.netlify.app/user_tutorials/module3/moduleThreeTutorial)
- [Module 4: Sowing A Crop](https://apsimnextgeneration.netlify.app/user_tutorials/module4/moduleFourTutorial)
- [Module 5: Long-term Simulations](https://apsimnextgeneration.netlify.app/user_tutorials/module5/moduleFiveTutorial)

---

## /usage/server/

Source: https://apsimnextgeneration.netlify.app/usage/server/
Title: APSIM Server

# APSIM Server

## Overview

An APSIM Server holds an .apsimx file open in memory and runs it on demand, potentially with modified parameter values. Communication with the server occurs via sockets, which results in far less overhead than repeatedly invoking Models.exe. There is currently no windows implementation of a client capable of communicating with the server.

Two protocols are implemented in the apsim source tree, and others exist in the wild. The first protocol (“V1”) implements a command and data exchange capability over native and managed sockets. A second (“zmqserver”) implements both a one-shot protocol to run simulations from beginning to end, and an interactive protocol that can exchange data (encoded via the [msgpack library](https://msgpack.org/)) and receive commands during the course of a simulation.

## V1 Behaviour

When the server starts, it will read the .apsimx file, prepare the file to be run, and will then wait for client connections. If a client application is already running, the server will establish a connection with this client. Once a connection is established with a client, the server will wait for instructions from the client. Currently two commands are implemented:

- RUN (run the .apsimx file, possibly with modified parameters)
- READ (read results from the most recent run)

The recommended way to send these commands to the server is to use a client API. A sample C API is provided [here](https://github.com/APSIMInitiative/APSIM.Client).

## Zmqserver Behaviour

Likewise the server will initially prepare a simulation to run, and then wait for a client connection. In the oneshot mode, the commands (run, get) are similar to the V1 server. In interactive mode, the server will pass the simulation the address of a controlling port that a manager component within the simulation will connect to. The protocol (get/set/do/resume) for this connection is implemented within the manager component. Samples of clients in R and Python are in the [Test Directory](https://apsimnextgeneration.netlify.app/Tests/Simulation/ZMQ-Sync/).

## Notes on running/invoking the server

The server is not included in an APSIM binary installation, and must be built from source. There are two ways to invoke the server (these should be run from the ApsimX directory):

`dotnet run -p APSIM.Server -- <arguments>`

`dotnet <path/to/apsim-server.dll> <arguments>`

`dotnet run -p ApsimZMQServer -- <arguments>`

`dotnet <path/to/ApsimZMQServer.dll> <arguments>`

When using the [first option](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-run), the `--` is necessary - it separates the arguments passed to the `dotnet` command from the arguments passed to the server.

When using the [second syntax](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet), it’s important to use the correct path to the apsim-server.dll file, as this path can be variable depending on how it was built. Typically, it will be located at `ApsimX/bin/Debug/net8.0/apsim-server.dll`, but this will be different if the server was built in release mode (path will contain Release instead of Debug), and will be different again if the project was published.

## Command Line Arguments

When the server is started, several command-line arguments may be passed. These may be viewed by running the server with the `-h` or `--help` command-line arguments. The only mandatory argument is the `--file <file.apsimx>` argument, where should be the path to an .apsimx file on disk. This is the file which will be read when the server starts, and run whenever the server receives a RUN command.

The `--comunication-mode` flag tells the server which communications protocol to use for communication to a client application. Normally this should be set to `Native`, which will allow for communications with a native application (e.g. a C program). If the client program is written in C# using C# named pipes, this option may be set to `Managed`, and will allow for much simpler comms code.

The `--keep-alive` argument tells the server to continue running when a client disconnects. If this argument is not passed, then the server will exit immediately after a client disconnects.

---

## /technicalinformation/versioning/

Source: https://apsimnextgeneration.netlify.app/technicalinformation/versioning/
Title: APSIM file versions & APSIM Software versions

# APSIM file versions & APSIM Software versions

There are two different versions used in APSIM Next Gen with different meanings and uses. They are:

1. The build number or the APSIM program version (as seen in upgrade). This tracks every time the APSIM Next Generation codebase changes and is packaged for all users (GitHub pull requests with hash resolved) and is used to identify when any fix was made or a new feature added (Git commit history). You report this version in publications for repeatability and transparency as you can ensure the simulation will always give the same results when run with this same version and your simulation file provided with supplementary data, and
2. the three digit version number stored in the apsimx file. This version identifies the “simulation file format version” and tracks changes from (1) that require changes to apsimx simulation settings file (.apsimx json file) for some users, such as where a class or property was renamed, or a new simulation tree structure (model nesting) is implemented. For each increment in this version the developers have added code to automatically update your simulation file to implement the required changes and this will happen automatically when you open a simulation file with an older version number.

Most of the program updates (1) will not require any simulation file changes and so the three-digit version number changes much slower and is usually associated with larger model changes.

APSIM will not allow you to open a simulation with a later simulation file version as this implies the simulation file may have functionality included that is not available in your current version of APSIM.

When you get this error the solutions are:

1. upgrade your APSIM software if you have an installed version.
2. pull the latest changes from APSIM GitHub repo to ensure your development version is up to date.
3. create a copy of your simulation file (apsimx) and edit in a text editor to reduce the version in your apsimx file by:
  - Try to open this file in apsim, and repeat by reducing the version until the error message is not displayed and the simulation opens, or you get an error message about a bad json file in which case you must do (1) or (2) above or know how to address the issue. This assumes the changes required and applied to the apsimx file with the higher version were in parts of the model not used in your simulation and can be ignored.

---

## /usage/met/customdata/

Source: https://apsimnextgeneration.netlify.app/usage/met/customdata/
Title: Accessing non-standard columns of data from .met file

# Accessing non-standard columns of data from .met file

It is possible to access custom data stored in a .met file from a manager script.

Met file:

```
[weather.met.weather]
latitude = -27  (DECIMAL DEGREES)
longitude = 150  (DECIMAL DEGREES)
tav =  19.09 (oC)
amp =  14.63 (oC)
year  day radn  maxt   mint  rain  pan    vp      code    my_column_name
 ()   () (MJ/m^2) (oC) (oC)  (mm)  (mm)   (hPa)     ()                ()
1900   1   24.0  29.4  18.6   0.0   8.2  20.3 300070                   6
1900   2   25.0  31.6  17.2   0.0   8.2  16.5 300070                   7
1900   3   25.0  31.9  16.6   0.0   8.2  14.8 300070                   2
1900   4   24.0  33.8  16.8   0.0   8.2  17.5 300070                   3
1900   5   24.0  33.3  19.3   0.0   8.4  18.3 300070                   4
```

Manager script:

```
using System;
using Models.Core;
using Models.Climate;

namespace Models
{
    [Serializable]
    public class Script : Model
    {
        [Link] private Weather weather;

        public double MyColumn
        {
            get
            {
                return weather.GetValue("my_column_name");
            }
        }
    }
}
```

Then the MyColumn variable can be reported (e.g. as `Manager.Script.MyColumn`).

![Screenshot of report data](https://apsimnextgeneration.netlify.app/images/CustomMetDataReport.png)

---

## /development/software/autodocumentation/

Source: https://apsimnextgeneration.netlify.app/development/software/autodocumentation/
Title: Auto documentation

# Auto documentation

The APSIM infrastructure has the ability to create a PDF file by examining the validation .apsimx file and the source code. The .apsimx file needs to have the same name as the .apsimx file (e.g. Maize.apsimx for the Maize model). To generate the document, the user can right click on the top level node (Simulations) in the user interface and select ‘Create documentation’.

## Model design to support auto documentation

To enable auto-documentation, every model must have a ‘Document’ method with this signature:

```
/// <summary>Writes documentation for this function by adding to the list of documentation tags.</summary>
/// <param name="tags">The list of tags to add to.</param>
/// <param name="headingLevel">The level (e.g. H2) of the headings.</param>
/// <param name="indent">The level of indentation 1, 2, 3 etc.</param>
public void Document(List<AutoDocumentation.ITag> tags, int headingLevel, int indent);
```

If a model is derived from ‘Model’, it can rely on the base class to provide a default implementation of a documentation method. in a lot of cases, this default implementation will be good enough to provide basic documentation. It writes a heading to the PDF, the text inside the <summary> tags for the class and then proceeds to call ‘Document’ in all children.

To provide specialised functionality, a model can have it’s own Document method. For example, LinearInterpolation.cs has this method:

```
/// <summary>Writes documentation for this function by adding to the list of documentation tags.</summary>
/// <param name="tags">The list of tags to add to.</param>
/// <param name="headingLevel">The level (e.g. H2) of the headings.</param>
/// <param name="indent">The level of indentation 1, 2, 3 etc.</param>
public override void Document(List<AutoDocumentation.ITag> tags, int headingLevel, int indent)
{
    // add a heading.
    tags.Add(new AutoDocumentation.Heading(Name, headingLevel));

    // write memos.
    foreach (IModel memo in Apsim.Children(this, typeof(Memo)))
        memo.Document(tags, -1, indent);

    // add graph and table.
    if (XYPairs != null)
    {
        IVariable xProperty = Apsim.GetVariableObject(this, XProperty);
        string xName = XProperty;
        if (xProperty != null && xProperty.Units != string.Empty)
            xName += " (" + xProperty.Units + ")";

        tags.Add(new AutoDocumentation.Paragraph("<i>" + Name + "</i> is calculated as a function of <i>" + xName + "</i>", indent));

        tags.Add(new AutoDocumentation.GraphAndTable(XYPairs, string.Empty, xName, Name, indent));
    }
}
```

This method adds a heading, writes any child memos and then adds a bit of text in italics (using HTML) and finally adds a graph and a table.

The first argument to the method is a list of ‘tags’ that can be added to. These tags are used to create the PDF. The AutoDocumentation class has various tags that can be created (Heading, Paragraph, GraphAndTable). It also has some static helper methods to get the units and description of a declaration and the description of a class:

```
/// <summary>Gets the units from a declaraion.</summary>
/// <param name="model">The model containing the declaration field.</param>
/// <param name="fieldName">The declaration field name.</param>
/// <returns>The units (no brackets) or any empty string.</returns>
public static string GetUnits(IModel model, string fieldName);

/// <summary>Gets the description from a declaraion.</summary>
/// <param name="model">The model containing the declaration field.</param>
/// <param name="fieldName">The declaration field name.</param>
/// <returns>The description or any empty string.</returns>
public static string GetDescription(IModel model, string fieldName);

/// <summary>Writes the description of a class to the tags.</summary>
/// <param name="model">The model to get documentation for.</param>
/// <param name="tags">The tags to add to.</param>
/// <param name="indent">The indentation level.</param>
public static void GetClassDescription(object model, List<ITag> tags, int indent);
```

## Examining the .apsimx file

The auto documentation code will also walk through all nodes in the .apsimx file, writing any ‘Memo’ and ‘Graph’ models that it finds. For graphs, the menu option ‘Include in auto-documentation?’ (right click on graph) needs to be checked. This allows the model developer to optionally include graphs in the PDF and exclude others.

---

## /categories/

Source: https://apsimnextgeneration.netlify.app/categories/
Title: Unavailable Page

# Unavailable Page

Fetch failed with HTTP 404 for https://apsimnextgeneration.netlify.app/categories/

---

## /usage/graphs/datetimexaxes/

Source: https://apsimnextgeneration.netlify.app/usage/graphs/datetimexaxes/
Title: Changing datetime x axes intervals

# Changing datetime x axes intervals

To do this:

1. Click the title to display the axes controls.
2. Enter a number into the interval text box to change the date intervals.

The interval number equals number of days. The higher the number the less specific the datetime format.

- Numbers less than 30 the intervals will be in datetime format dd/MM/yyyy
- Numbers more than 30 but less than 1825 (roughly 5 years in days) the intervals will be in datetime format MM-yyyy.
- Numbers more 1825 show intervals in datetime format yyyy.

**Note:** When no interval is given, vaxes specifics are automatically determined.

---

## /development/software/codingstyle/

Source: https://apsimnextgeneration.netlify.app/development/software/codingstyle/
Title: Coding Style

# Coding Style

To ensure ease of maintenance and development, it is important that a consistent design is used when implementing models in APSIM Next Generation. To achieve this, APSIM follows many of the [Microsoft C Sharp code conventions](https://learn.microsoft.com/en-us/dotnet/csharp/fundamentals/coding-style/coding-conventions) and [C Sharp coding style](https://github.com/dotnet/runtime/blob/main/docs/coding-guidelines/coding-style.md) with some variations for code that has been ported from others languages such as Fortran. If you intend on contributing code we recommend following these guides and conventions.

# Naming variables

All source code should be written using the Microsoft naming conventions.

In particular please note these guidelines:

Capitalize the first letter of each word in the identifier. Do not use underscores to differentiate words, or for that matter, anywhere in identifiers. There are two appropriate ways to capitalize identifiers, depending on the use of the identifier:

- PascalCasing
- camelCasing

The PascalCasing convention, used for all identifiers except parameter names, capitalizes the first character of each word (including acronyms over two letters in length), as shown in the following examples:

```
PropertyDescriptor
HtmlTag
```

A special case is made for two-letter acronyms in which both letters are capitalized, as shown in the following identifier:

```
IOStream
```

The camelCasing convention, used only for argument names to methods and private field names, capitalizes the first character of each word except the first word, as shown in the following examples. As the example also shows, two-letter acronyms that begin a camel-cased identifier are both lowercase.

```
propertyDescriptor
ioStream
htmlTag
```

Example:

```
public class ModelA : Model
{
    private double aVariable;            // camelCase naming convention for private field
    public double BVariable {  get; }    // PascalCase naming convention for properties

    public void AMethod(double argument)   // camelCase the argument.
    {
        // Do something
    }
}
```

We also use the Visual Studio default brace indention and tab settings (4 spaces). Line endings should be CR/LF (Windows standard).

Instance variables should be named differently to the type/object names. e.g.

```
Soil Soil;    // BAD
Soil soil;    // BAD - variable name only differs by case

Soil soilModel;    // BETTER
```

# Region Usage

The use of #region is not recommended.

# Inheritance

Try and avoid inheritance. For a software engineering view on this see: [https://codingdelight.com/2014/01/16/favor-composition-over-inheritance-part-1/](https://codingdelight.com/2014/01/16/favor-composition-over-inheritance-part-1/). There is general consensus that inheriting from an interface is GOOD but inheriting from a base class is BAD. There are always exceptions of course. In our case, I’ve been migrating away from having a BaseOrgan and instead put code that is common across organs in a ‘library’ or ‘model’ somewhere and simply call methods in that library. An example of this is in the way GenericOrgan relies on a [Link] BiomassRemovalModel to remove biomass from the organ. A simpler way would be to create a class called say PMFLibrary and put in static methods e.g. ‘RemoveBiomass’ …

# Code Formatting

Use [Allman-style](https://en.wikipedia.org/wiki/Indentation_style#Allman_style) braces, where curly braces start on a new line. A single line statement block should go without braces but must still be indented on its own line. e.g.

```
if (x)
{
	foo();
	bar();
}
else
	baz();
```

# Order of declarations in a C# class

## 1. Links

Links should be first in a class declaration. They specify the dependencies to other models in the simulation. They should be private c# fields and be preceded with Link attributes. ##Optional links should be avoided##. They obscure from the developer what the defaults are when a model is missing. Better to be explicit e.g. define a non optional function called Photosynthesis in GenericOrgan. If an organ doesn’t photosynthesise then the developer has to think about it and add a constant function called Photosynthesis and set a value of 0. The auto-documentation will then show that an organ doesn’t photosynthesise which is nice.

```
	/// <summary>The parent plant</summary>
	[Link]
	private Plant parentPlant = null;

	/// <summary>The surface organic matter model</summary>
	[Link]
	private ISurfaceOrganicMatter surfaceOrganicMatter = null;
```

For links to functions that must be child functions use:

```
	/// <summary>The senescence rate function</summary>
    [ChildLinkByName]
    [Units("/d")]
    private IFunction senescenceRate = null;

    /// <summary>The detachment rate function</summary>
    [ChildLinkByName]
    [Units("/d")]
    private IFunction detachmentRateFunction = null;
```

This will avoid the situation where the same named function exists in different places.

## 2. Private and protected fields

Private and protected fields and enums are next:

```
	/// <summary>The dry matter supply</summary>
	private BiomassSupplyType dryMatterSupply = new BiomassSupplyType();

	/// <summary>The nitrogen supply</summary>
	private BiomassSupplyType nitrogenSupply = new BiomassSupplyType();
```

## 3. The constructor

The constructor (if any) comes next:

```
	/// <summary>Constructor</summary>
	public GenericOrgan()
	{
		Live = new Biomass();
		Dead = new Biomass();
	}
```

## 4. Public events and enums

If a class needs to define public events (that other models can subscribe to) or enums then they come after the constructor.

```
	/// <summary>Occurs when a plant is about to be sown.</summary>
	public event EventHandler Sowing;
```

## 5. Public properties

Public properties (outputs) are next and **should have a trivial implementation**.

```
	/// <summary>The live biomass</summary>
	[XmlIgnore]
	public Biomass Live { get; private set; }

	/// <summary>The dead biomass</summary>
	[XmlIgnore]
	public Biomass Dead { get; private set; }

	/// <summary>Gets the DM demand for this computation round.</summary>
	[XmlIgnore]
	public BiomassPoolType DMDemand { get { return dryMatterDemand; } }
```

## 6. Public methods

Public methods come next. These will be callable from other models including manager scripts.

```
	/// <summary>Calculate and return the dry matter supply (g/m2)</summary>
	public virtual BiomassSupplyType CalculateDryMatterSupply()
	{
	}
```

## 7. Private and protected methods

Private and protected methods come last. This includes all APSIM event handlers (which should always be private or protected)

```
	/// <summary>Called when crop is ending</summary>
	/// <param name="sender">The sender.</param>
	/// <param name="data">The <see cref="EventArgs"/> instance containing the event data.</param>
	[EventSubscribe("PlantSowing")]
	private void OnPlantSowing(object sender, SowPlant2Type data)
	{
	}
```

---

## /usage/debugmanagerscript/

Source: https://apsimnextgeneration.netlify.app/usage/debugmanagerscript/
Title: Debug Manager Script

# Debug Manager Script

To debug a manager script you need to insert

```
using System.Diagnostics;
```

at the top of your manager script. Then to trigger a breakpoint, insert

```
Debugger.Break();
```

into a method or property to have the debugger stop. Apsim Next Generation needs to be run from Visual Studio and be in debug mode.When a simulation is run from APSIM Next Generation, Visual Studio will stop on the above line and you will be able to inspect values of variables and step into/over lines of code.

---

## /usage/graphs/errorbars/

Source: https://apsimnextgeneration.netlify.app/usage/graphs/errorbars/
Title: Error Bars

# Error Bars

Error bars will automatically be added to a graph if an error column exists corresponding to the x or y data series. The error column must have the same name as the x or y series, with a suffix of “Error” (without the quotes). For example, if the y axis is displaying the Yield column, the error data must be in a column called YieldError. If using a PredictedObserved component, any error columns in the predicted or observed data will be automatically added to the PredictedObserved table.

## Simple Example

#### Report configuration

![Report](https://apsimnextgeneration.netlify.app/images/Usage.Graphs.ErrorBars.SimpleExample.Report.png)

### Resultant graph

![Simple Example - grpah](https://apsimnextgeneration.netlify.app/images/Usage.Graphs.ErrorBars.SimpleExample.Graph.png)

## PredictedObserved Example

In this example, there is an error column in the observed data which will appear automatically on the graph. See [here](https://apsimnextgeneration.netlify.app/usage/Graphs/creating-predicted-observed-graphs) for full details on merging and graphing predicted/observed data.

#### Observed data

(Note that missing error values are fine.)

![Observed Data](https://apsimnextgeneration.netlify.app/images/Usage.Graphs.ErrorBars.ObservedData.png)

#### Report configuration

![Report](https://apsimnextgeneration.netlify.app/images/Usage.Graphs.ErrorBars.Report.png)

#### Resultant graph

![Resultant Graph](https://apsimnextgeneration.netlify.app/images/Usage.Graphs.ErrorBars.Graph.png)

---

## /usage/factorials/

Source: https://apsimnextgeneration.netlify.app/usage/factorials/
Title: Factorial Simulations

# Factorial Simulations

An factorial allows a single simulation to be run multiple times with different parameters or inputs. At its most simple, a factorial consists of an experiment node with two children - a simulation, and a factors node. The simulation (sometimes called the base simulation) defines the default behaviour of the experiment. The factors node should contain multiple factor children, where each factor defines one or more treatments (levels) of the experiment.

![A basic experiment configuration](https://apsimnextgeneration.netlify.app/images/Usage.Factorial.BasicExperiment.png)

When run, the experiment will generate one simulation for each factor level. The factors and factor levels are defined by the factor configurations under the Factors node. There are different types of factors, and they can be combined as needed. The different types of factors are described below, and examples of each type of factor are given in the factorial example file (Factorial.apsimx) which is included with APSIM installations.

## Factor

The factor node allows a single model or property to be modified. The factor’s behaviour is defined by the factor specification, which is a piece of text. The factor specification can be one of:

- A property set with multiple values, separated by commas e.g.

`[SowingRule].Script.SowingDate = 2000-11-01, 2000-12-03`

This will result in one treatment being generated for each property value.

- A property set with a range e.g.

`[FertiliserRule].Script.ApplicationAmount = 0 to 200 step 20`

This will result in one treatment being generated for each property value.

- A path to a model that will be replaced with one or more children of this factor that have a matching type e.g.

![A model replacement example](https://apsimnextgeneration.netlify.app/images/Usage.Factorial.ModelReplacement.png)

- Can be empty if the factor has one or more composite factor children. In this case, one treatment will be generated for each composite factor child.

## Composite Factor

The composite factor allows multiple models or properties to be changed in a single treatment. The composite factor user interface is a freeform (multiline) text input. Each line should contain a single factor specification string, which can be any valid factor specification (described above). If changing a property, only one value is allowed per line (ie no comma separated values).

![An example of composite factors](https://apsimnextgeneration.netlify.app/images/Usage.Factorial.CompositeFactor.png)

## Permutations

The permutations node should have multiple factor children, and it will generate one factor level (treatment) for each permutation of its child factors’ values.

![Permutation Example](https://apsimnextgeneration.netlify.app/images/Usage.Factorial.Permutation.png)

---

## /usage/graphs/graphfilters/

Source: https://apsimnextgeneration.netlify.app/usage/graphs/graphfilters/
Title: Graph filters

# Graph filters

The filter box in the graph configuration is very flexible - see examples below. All column names need to be in square brackets and must be in the table specified by ‘Data Source’. The column names that are available to be used in the filter are shown in the X or Y drop down lists.

## Examples

**if [Clock].Today has been output then these filters will work:**

```
[Clock.Today]>='1996-01-01'
[Clock.Today]>='1996-01-01' AND [Clock.Today] <= '2000-12-31'
```

**if [Clock].Today.Year has been output then these filters will work:**

```
[Clock.Today.Year] = 1995
[Clock.Today.Year] <> 1995
[Clock.Today.Year] >= 1995
[Clock.Today.Year] > 1995 AND [Clock.Today.Year] < 2000
[Clock.Today.Year] = 1995 OR [Clock.Today.Year] = 1996
[Clock.Today.Year] IN (1995, 1997, 1999)
[Clock.Today.Year] NOT IN (1995, 1997, 1999)
```

**Other examples**

```
[Wheat.SowingData.Cultivar] = 'Hartog'
[SimulationName] LIKE 'ExperimentFactorOneSlurp_Minus'
[SimulationName] LIKE 'ExperimentFactorOneSlurp_%'
```

---

## /install/linux/

Source: https://apsimnextgeneration.netlify.app/install/linux/
Title: Linux Installation

# Linux Installation

##### Last updated: 20/06/2024 - Please alert us at our [github page](https://github.com/APSIMInitiative/ApsimX/issues) if these instructions become outdated or incorrect

## Download debian binary

1. Download the debian file from the [APSIM website](https://www.apsim.info/download-apsim/).

## Installing

1. Find the download in your Downloads directory, and double click to install. If it does not install, you can run the command `sudo apt install ./apsim-<version-number>.deb` remembering to replace the version number with the one from your download.

## Running

1. You’ll then find APSIM installed under the directory: `/usr/local/bin`.

## Install using docker

- To do this see the instructions [here](https://apsimnextgeneration.netlify.app/usage/commandline/command-line-linux)

---

## /install/macos/

Source: https://apsimnextgeneration.netlify.app/install/macos/
Title: MacOS Installation

# MacOS Installation

##### Last Updated 4/4/2024 - Please alert us at our [github page](https://github.com/APSIMInitiative/ApsimX/issues) if these instructions become outdated or incorrect

Be aware that these instructions will require administrator privileges to be completed.

Apsim requires four libraries to be installed to run on MacOS:

1. [.NET version 8.0](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)
2. [Homebrew](https://brew.sh/)
3. [Gtk+3](https://docs.gtk.org/gtk3/macos.html) (Using Homebrew)
4. [GtkSourceView4](https://github.com/GNOME/gtksourceview) (Using Homebrew)

## Installing .NET

Apsim requires the **x64 verion of the .NET 8.0 SDK library**.

Do **NOT** install the Arm64 version. The x64 version will work on an Arm M1/M2/M3 system, and is the library that Apsim is looking to run with.

![.NET Version](https://apsimnextgeneration.netlify.app/images/netversion.png)

Download the SDK MacOS x64 library and run the installer it gives you. Please only use the installer. Afterwards, open up a terminal and run:

```
dotnet --list-sdks
```

It should respond with the version of .NET that you have installed. If it does not, you may need to link .NET manually with this terminal command:

```
sudo ln -s /usr/local/share/dotnet/x64/dotnet /usr/local/bin/
```

If after doing the above step you are still unable to execute dotnet commands, modify your `/etc/paths` file to include the path `/usr/local/share/dotnet/x64/` as a separate line underneath the existing lines in the file. Doing this may require super user permissions.

Once you have done this save the file and retry the `dotnet --list-sdks` command in a new terminal.

Once you can get the dotnet versions showing in the terminal, dotnet should be correctly installed:

```
user@system ~ % dotnet --list-sdks
8.0.407 [/usr/local/share/dotnet/sdk]
```

## Installing Homebrew

Use the console to install Homebrew if you don’t have it installed aready.

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Afterwards, check the version with:

```
brew --version
```

If brew cannot be found, you may need to link it manually with:

```
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

Once you can get the brew version showing, it is correctly installed:

```
user@system ~ % brew --version
Homebrew 3.2.6
Homebrew/homebrew-core (git revision a97c2a6737; last commit 2021-08-09)
Homebrew/homebrew-cask (git revision 8e931b20db; last commit 2021-08-09)
```

## Installing Gtk3 and GtkSourceView

With Homebrew installed, you then need to install gtk and the gtk source view libraries. These are installed with:

GTK3:

```
brew install gtk+3
```

GTK SourceView 4:

```
brew install gtksourceview4
```

## Installing Apsim

1. To install Apsim on MacOS, download a copy from the [apsim website](https://www.apsim.info/download-apsim/).
2. Click ‘Click here to download or upgrade APSIM’ which will take you to a registration website.
3. Next, enter your email address
4. On the next screen, in the ‘Download Link’ column, select ‘MacOS’. This will download an apsim dmg file.
5. Open the dmg and drag the app to your Applications folder
6. Run the Apsim file you just created in Aplications
7. **A prompt will say that “APSIM cannot be opened because it is from an unidentified developer”. Close this Window.**
8. Run the application again and it will now have an Open option, click that.

## Common issues

**Unable to open APSIM after install.** This usually means that a library is missing from your system that Apsim requires. Check that you have installed the correct version of .NET and that you have both GTK3 and GTKSourceView4 installed.

**Running Apsim from the terminal** If Apsim is not opening from the Applications folder, open a terminal and type the following with the version number you installed:

```
open ../../Applications/APSIM2024.4.7437.0.app
```

If Apsim does not open, this will give an error message that could help you work out what is causing it to fail. If you report an issue with running Apsim on MacOS, please provide these error messages to help us solve your problem.

**SQLite Permissions Error** There are a number of reasons why the database may have permission problems.

1. If your apsim file is within a Dropbox/OneDrive/Cloud Storage folder, that will cause problems when accessing the database due to the cloud storage trying to sync the file while it’s being changed.
2. It has been reported that running apsim from the terminal can fix this error if it’s not related to cloud storage.

---

## /usage/memo/

Source: https://apsimnextgeneration.netlify.app/usage/memo/
Title: Memo

# Memo

The *Memo* control uses ***MarkDown*** as its formatting language. The control contains two panes: the lower one allows you to edit your text using Markdown, and the upper displays the resulting formatted text.

The tables immediately below give a brief description of the Markdown syntax. This is followed by a more detailed description, largely taken from the [website of John Gruber](https://daringfireball.net/projects/markdown/syntax), the developer of Markdown.

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.Memo1.png)

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.Memo2.png)

---

## *Markdown* Syntax

Markdown paragraphs are simply one or more lines of consecutive text, separated by one or more blank lines. They should not be indented with spaces or tabs. Most formatting operations can be easily accomplished using the features described below. If that is not sufficient, HTML tags may be used within Markdown, but there is generally little need to do so. This document is itself written in Markdown, with no additional tags.

### Headers

Markdown headers are created by placing 1-6 hash characters at the start of the line, corresponding to header levels 1-6. For example:

```
# This is an H1

## This is an H2

###### This is an H6
```

These will appear as:

# This is an H1

## This is an H2

###### This is an H6

### Emphasis

Markdown treats asterisks (`*`) and underscores (`_`) as indicators of emphasis. Text wrapped with one `*` or `_` will be wrapped with an HTML `<em>` tag; double `*`’s or `_`’s will be wrapped with an HTML `<strong>` tag. E.g., this input:

`*single asterisks*` will appear as *single asterisks*

`_single underscores_` will appear as *single underscores*

`**double asterisks**` will appear as **double asterisks**

`__double underscores__` will appear as **double underscores**

`***triple_asterisks***` will appear as ***triple_asterisks***

You can use whichever style you prefer; the lone restriction is that the same character must be used to open and close an emphasis span.

Emphasis can be used in the middle of a word:

`x*y*z` will appear as x*y*z.

But if you surround an `*` or `_` with spaces, it’ll be treated as a literal asterisk or underscore.

To produce a literal asterisk or underscore at a position where it would otherwise be used as an emphasis delimiter, you can backslash escape it:

`\*this text is surrounded by literal asterisks\*` produces *this text is surrounded by literal asterisks*

### Lists

Markdown supports ordered (numbered) and unordered (bulleted) lists.

Unordered lists use asterisks, pluses, and hyphens – interchangably – as list markers:

```
*   Red
*   Green
*   Blue
```

is equivalent to:

```
+   Red
+   Green
+   Blue
```

and:

```
-   Red
-   Green
-   Blue
```

With any of these, the results will appear as:

- Red
- Green
- Blue

Ordered lists use numbers followed by periods:

```
1.  Bird
2.  McHale
3.  Parish
```

It’s important to note that the actual numbers you use to mark the list have no effect on the output Markdown produces. If you instead wrote the list in Markdown like this:

```
1.  Bird
1.  McHale
1.  Parish
```

or even:

```
3. Bird
1. McHale
8. Parish
```

All of these will produce:

1. Bird
2. McHale
3. Parish

The point is, if you want to, you can use ordinal numbers in your ordered Markdown lists, so that the numbers in your source match the numbers in your published document. But if you want to be lazy, you don’t have to. If you do use lazy list numbering, however, you should still start the list with the number 1. At some point in the future, Markdown may support starting ordered lists at an arbitrary number.

List markers typically start at the left margin, but may be indented by up to three spaces. List markers must be followed by one or more spaces or a tab. List items may consist of multiple paragraphs. Each subsequent paragraph in a list item must be indented by either 4 spaces or one tab:

```
1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, consectetuer adipiscing elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.
```

will produce:

1. This is a list item with two paragraphs. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus. Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
2. Suspendisse id sem consectetuer libero luctus adipiscing.

It’s worth noting that it’s possible to trigger an ordered list by accident, by writing something like this:

```
1986. What a great season.
```

In other words, a *number-period-space* sequence at the beginning of a line. To avoid this, you can backslash-escape the period:

```
1986\. What a great season.
```

### Code Blocks

Pre-formatted code blocks are used for writing about programming or markup source code. Rather than forming normal paragraphs, the lines of a code block are interpreted literally. To produce a code block in Markdown, simply indent every line of the block by at least 4 spaces or 1 tab. For example, given this input:

```
This is a normal paragraph:

    This is a code block.
    public string LabelText
    {
        get { return label1.Text; }
        set { label1.Text = value; }
    }
```

Markdown will generate:

This is a normal paragraph:

```
This is a code block.
public string LabelText
{
    get { return label1.Text; }
    set { label1.Text = value; }
}
```

One level of indentation – 4 spaces or 1 tab – is removed from each line of the code block.

A code block continues until it reaches a line that is not indented (or the end of the article).

Regular Markdown syntax is not processed within code blocks. E.g., asterisks are just literal asterisks within a code block. This means it’s also easy to use Markdown to write about Markdown’s own syntax.

If indenting every line by four spaces or a tab is inconvenient, an alternative is to use “fenced” code blocks. Use three tildes (~~~) on the lines before and after the code block.

```
~~~
public string LabelText
{
    get { return label1.Text; }
    set { label1.Text = value; }
}
~~~
```

produces

```
public string LabelText
{
    get { return label1.Text; }
    set { label1.Text = value; }
}
```

### Block quotes

Markdown uses email-style `>` characters for blockquoting. If you’re familiar with quoting passages of text in an email message, then you know how to create a blockquote in Markdown. It looks best if you hard wrap the text and put a `>` before every line:

```
> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
>
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.
```

to produce

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus. Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse id sem consectetuer libero luctus adipiscing.

Markdown allows you to be lazy and only put the `>` before the first line of a hard-wrapped paragraph:

```
> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.
```

Blockquotes can be nested (i.e. a blockquote-in-a-blockquote) by adding additional levels of `>`:

```
> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.
```

will produce

> This is the first level of quoting. This is nested blockquote. Back to the first level.

### Horizontal rules

You can produce a horizontal rule by placing three or more hyphens, asterisks, or underscores on a line by themselves. If you wish, you may use spaces between the hyphens or asterisks. Each of the following lines

```
* * *

***

*****

- - -

---------------------------------------
```

will generate:

---

### Tables

To add a table, use three or more hyphens (—) to create each column’s header, and use pipes (|) to separate each column. You can optionally add pipes on either end of the table.

```
| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |
```

The rendered output looks like this:

| Syntax | Description |
| --- | --- |
| Header | Title |
| Paragraph | Text |

Cell widths can vary, as shown below. The rendered output will look the same.

```
| Syntax | Description |
| --- | ----------- |
| Header | Title |
| Paragraph | Text |
```

You can align text in the columns to the left, right, or center by adding a colon (:) to the left, right, or on both side of the hyphens within the header row.

```
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And more      |
```

The rendered output looks like this:

| Syntax | Description | Test Text |
| --- | --- | --- |
| Header | Title | Here’s this |
| Paragraph | Text | And more |

You can format the text within tables. For example, you can add links, code (words or phrases in tick marks (`) only, not code blocks), and emphasis. You can’t add headings, blockquotes, lists, horizontal rules, images, or HTML tags.

### Links

Markdown supports two style of links: *inline* and *reference*.

In both styles, the link text is delimited by [square brackets].

To create an inline link, use a set of regular parentheses immediately after the link text’s closing square bracket. Inside the parentheses, put the URL where you want the link to point, along with an *optional* title for the link, surrounded in quotes. For example:

```
This is [an example](http://example.com/ "Title") inline link.

[This link](http://example.net/) has no title attribute.
```

Will produce:

This is [an example](http://example.com/) inline link.

[This link](http://example.net/) has no title attribute.

If you’re referring to a local resource on the same server, you can use relative paths:

```
See my [About](/about/) page for details.
```

Reference-style links use a second set of square brackets, inside which you place a label of your choosing to identify the link:

```
This is [an example][id] reference-style link.
```

You can optionally use a space to separate the sets of brackets:

```
This is [an example] [id] reference-style link.
```

Then, anywhere in the document, you define your link label like this, on a line by itself:

```
[id]: http://example.com/  "Optional Title Here"
```

That is:

- Square brackets containing the link identifier (optionally indented from the left margin using up to three spaces);
- followed by a colon;
- followed by one or more spaces (or tabs);
- followed by the URL for the link;
- optionally followed by a title attribute for the link, enclosed in double or single quotes, or enclosed in parentheses.

The following three link definitions are equivalent:

```
[foo]: http://example.com/  "Optional Title Here"
[foo]: http://example.com/  'Optional Title Here'
[foo]: http://example.com/  (Optional Title Here)
```

You can put the title attribute on the next line and use extra spaces or tabs for padding, which tends to look better with longer URLs:

```
[id]: http://example.com/longish/path/to/resource/here
    "Optional Title Here"
```

Link definitions are only used for creating links during Markdown processing, and are stripped from your document in the HTML output.

Link definition names may consist of letters, numbers, spaces, and punctuation – but they are *not* case sensitive. E.g. these two links:

```
[link text][a]
[link text][A]
```

are equivalent.

The *implicit link name* shortcut allows you to omit the name of the link, in which case the link text itself is used as the name. Just use an empty set of square brackets – e.g., to link the word “Google” to the google.com web site, you could simply write:

```
[Google][]
```

And then define the link:

```
[Google]: http://google.com/
```

Because link names may contain spaces, this shortcut even works for multiple words in the link text:

```
Visit [Daring Fireball][] for more information.
```

And then define the link:

```
[Daring Fireball]: http://daringfireball.net/
```

Link definitions can be placed anywhere in your Markdown document. I tend to put them immediately after each paragraph in which they’re used, but if you want, you can put them all at the end of your document, sort of like footnotes.

Here’s an example of reference links in action:

```
I get 10 times more traffic from [Google][1] than from
[Yahoo][2] or [MSN][3].

  [1]: http://google.com/        "Google"
  [2]: http://search.yahoo.com/  "Yahoo Search"
  [3]: http://search.msn.com/    "MSN Search"
```

Using the implicit link name shortcut, you could instead write:

```
I get 10 times more traffic from [Google][] than from
[Yahoo][] or [MSN][].

  [google]: http://google.com/        "Google"
  [yahoo]:  http://search.yahoo.com/  "Yahoo Search"
  [msn]:    http://search.msn.com/    "MSN Search"
```

Both of the above examples will produce the following output:

I get 10 times more traffic from [Google](http://google.com/) than from [Yahoo](http://search.yahoo.com/) or [MSN](http://search.msn.com/).

For comparison, here is the same paragraph written using Markdown’s inline link style:

```
I get 10 times more traffic from [Google](http://google.com/ "Google")
than from [Yahoo](http://search.yahoo.com/ "Yahoo Search") or
[MSN](http://search.msn.com/ "MSN Search").
```

The point of reference-style links is not that they’re easier to write. The point is that with reference-style links, your document source is vastly more readable. Compare the above examples: using reference-style links, the paragraph itself is only 81 characters long; with inline-style links, it’s 176 characters; and as raw HTML, it’s 234 characters. In the raw HTML, there’s more markup than there is text.

With Markdown’s reference-style links, a source document much more closely resembles the final output, as rendered in a browser. By allowing you to move the markup-related metadata out of the paragraph, you can add links without interrupting the narrative flow of your prose.

### Images

Admittedly, it’s fairly difficult to devise a “natural” syntax for placing images into a plain text document format. Markdown uses an image syntax that is intended to resemble the syntax for links, allowing for two styles: *inline* and *reference*.

Inline image syntax looks like this:

`![Alt text](/path/to/img.jpg)`

`![Alt text](/path/to/img.jpg "Optional title")`

That is:

- An exclamation mark: `!`;
- followed by a set of square brackets, containing the `alt` attribute text for the image;
- followed by a set of parentheses, containing the URL or path to the image, and an optional `title` attribute enclosed in double or single quotes.

Reference-style image syntax looks like this:

`![Alt text][id]`

Where “id” is the name of a defined image reference. Image references are defined using syntax identical to link references.

`[id]: url/to/image "Optional title attribute"`

As of this writing, Markdown has no syntax for specifying the dimensions of an image; if this is important to you, you can simply use regular HTML `<img>` tags.

#### Where do I put my Memo images?

Place these under the `ApsimNG/Resources` directory.

The markdown view searches in this location (among other locations) for images. The URL is simply the relative path from this location so if you put it directly under the ApsimNG/Resources directory it will be the name of the file including its extension, if its in a sub folder, then it will be `subfolder/<image-name>` where image name is the name of the file including the file extension e.g. `![Picture of wheat crop](wheat-images/wheat.png)`

### Superscript

Text enclosed between caret (^) characters will be rendered as superscript.

`super^script^`

### Subscript

Text enclosed between tilde (~) characters will be rendered as subscript.

`sub~script~`

---

## /usage/scope/

Source: https://apsimnextgeneration.netlify.app/usage/scope/
Title: Model Scope

# Model Scope

When trying to find models that are in scope (either by links or the ‘get’ method), the APSIM framework will look for matches hierarchically in the simulation. The find algorithm will return all children (recursively), all siblings and then all parent siblings recursively for a given reference model.

In the image below, the models highlighted in yellow are in scope of *Potato*

![Scope](https://apsimnextgeneration.netlify.app/images/Development.Scope.png)

---

## /development/software/modeldesign/

Source: https://apsimnextgeneration.netlify.app/development/software/modeldesign/
Title: Model design

# Model design

All models are written as normal .NET classes but must be derived from Model

## Properties initialised at startup

Models must be binary and JSON serializable. Serialization is the process where models (objects) are created at startup and their properties / fields are given values from the serialization file (.apsimx). Normally this doesn’t require any extra work by the model developer so long as the data types used are serializable (most .NET types are). For JSON serialzation to work, fields and properties that are to be given values at startup need to be public. APSIM, though, assumes that only public properties are serialized. Public fields are considered poor programming practice. There should be no public fields in any model. There are two ways to declare properties:

```
// Option 1 - auto-generated property
public DateTime StartDate { get; set; }

// Option 2 - manual property
private DateTime _StartDate = new DateTime(1940, 12, 31);
public DateTime StartDate
{
    get
    {
        return _StartDate;
    }
    set
    {
        _StartDate = value;
    }
}
```

The setter for a property must not have side affects. In other words, the setter must not invoke behaviour that affects the state of other properties. Remember, the setter will be invoked for each property during deserialisation at startup.

## Communicating with other models - Links

If models need to communicate with other models, they may do so by declaring a public or private field with a [Link] attribute. APSIM will provide a valid reference for the field at simulation start time by finding another model that is in scope and has the same type as the field declaration. Once found, models can then call properties and methods of the referenced model as normal. e.g

```
[Link] private Clock clock = null;
[EventSubscribe("StartOfDay")]
private void OnStartOfDay(object sender, EventArgs e)
{
    if (Clock.Today == SowDate)
        // do something
}
```

In order to decouple models from other models, it may be necessary to create interfaces (e.g. IClock) that specify what the public interface for the type of model. This would then allow a different model to be swapped in. This would be particularly important for models where we have different implementations e.g. SoilWater.

Even though there is the ability to have optional links, they should be avoided. It is better to be explicit and say the there is always a dependency on another model. Optional links lead to users not knowing when they need to satisfy a model dependency or not.

There are also other types of links that are useful.

```
[Link(Type = LinkType.Child, ByName = true)]
private IFunction mortalityRate = null; // Link will be resolved by a child model with a name of 'mortalityRate'
```

```
[Link(Type = LinkType.Child)]
public GenericTissue[] Tissue; // All child models of type 'GenericTissue' will be stored in the 'Tissue' array
```

```
[Link(Type=LinkType.Ancestor)]    // Link will be resolved by looking for a parent model of type 'PastureSpecies'
private PastureSpecies species = null;
```

```
[Link(Type = LinkType.Path, Path = "[Phenology].DltTT")]
protected IFunction DltTT = null;   // Link will be resolved by the model on path '[Phenology].DltTT'
```

## Published events and subscribing to events

APSIM uses the .NET event mechanism to signal when things happen during a simulation. Models can create their own events using the normal .NET event syntax:

```c#
public event EventHandler MyNewEvent;
 ...
if (MyNewEvent != null)
    MyNewEvent.Invoke(this, new EventArgs());
```

In this code snippet, an event is declared called ‘MyNewEvent’ (first line). Elsewhere, the event is published (invoked).

Models can subscribe to these events by putting an EventSubscribe attribute immediately before a private event handler method. The code example at the top of this page shows an event handler (OnStartOfDay) and an example of how to subscribe to the “StartOfDay” event. The event handlers will automatically be connected to the event publishers. There is no need to disconnect events. The APSIM infrastructure will take care of this.

Models in APSIM (particularly the CLOCK model) produce many events that may be useful for models. For a complete list see the sequence diagram of a running simulation. One event in particular is OnSimulationCommencing. This provides a model with an opportunity to perform setup functions. By the time this method is called by the infrastructure, APSIM will have satisfied all link references so a model is free to call properties on the linked models. Be aware though that the linked models may not have had their OnSimulationCommencing method called yet and so may not be in a consistent state.

Another useful event is called OnSimulationCompleted which will be invoked immediately after the simulation has completed running. This provides an opportunity for a model to perform cleanup.

## A hierarchy of models

In all APSIM simulations, models are run under a parent model and ultimately a parent ‘Zone’ (a core model that looks after a collection of models (used to be called a Paddock). This zone model is itself contained within a ‘Simulation’, which in turn is parented by a ‘Simulations’ model. Interfaces for these are provided in the reference documentation. If a model needs to communicate with its Zone or Simulation, it may do so via the normal link mechanism.

## Methods provided by the Model base class.

As stated above, all models must be derived from Model. This base class provides a number of methods for interacting with other models at runtime and discovering and altering the simulation structure.

```
/// <summary>
/// Get or set the name of the model
/// </summary>
public string Name { get; set; }

/// <summary>
/// Get or set the parent of the model.
/// </summary>
public Model Parent { get; set; }

/// <summary>
/// Get or sets a list of child models.
/// </summary>
public List<Model> Children { get; set; }
```

All models have a name, a parent model (except the Simulation model which has a null Parent) and child models.

## Errors

To flag a fatal error and immediately terminate a simulation, a model may simply throw an ‘ApsimXException’. The framework guarantees that the OnSimulationCompleted method will still be called in all models after the exception has been raised.

## Writing summary (log) information

To write summary information to the summary file, link to a model implementing the

```
ISummary interface:
[Link] private ISummary Summary = null;
ISummary has two methods for writing information:
/// <summary>
/// Write a message to the summary
/// </summary>
void WriteMessage(string FullPath, string Message);
/// <summary>
/// Write a warning message to the summary
/// </summary>
void WriteWarning(string FullPath, string Message);
```

WriteMessage will simply write a message, attaching the current simulation date (Clock.Today) to the message. WriteWarning can be used to write a warning (e.g. out of bounds) message to the summary.

## Simulation API

While the preference is for models to use the [Link] mechanism above for communicating with other models, sometimes it is necessary to dynamically work with models in a simulation in a more flexible way. For example, the REPORT model needs to get the values of variables from models where the interface to a model isn’t known. To enable this type of interaction, a static API exists that contains methods that may be called by a model during a simulation. The API class is called ‘Apsim’ and it contains many useful methods:

```
// Get the value of the SW variable from a soil model.
double[] sw = Apsim.Get(this, "[Soil].Water);

// Find a crop model that is in scope.
ICrop crop = Apsim.Find(this,, typeof(ICrop)) as ICrop;

// Loop through all crop models that are in scope.
foreach (ICrop crop in Apsim.FindAll(this, typeof(ICrop)))
{ }

// Find the parent simulation
Simulation simulation = Apsim.Parent(this, typeof(Simulation)) as Simulation;
```

## Attributes

```
[Bounds(Lower = 0.0, Upper = 10.0)]  // Specifies lower and upper bound of 'a_interception'
public double a_interception { get; set; }
```
```c#
[Description("Frequency of grazing")]   // Specifies the text displayed to the user in the GUI for a model
public string SimpleGrazingFrequencyString { get; set; }
```

```
[ViewName("UserInterface.Views.GridView")]  // Use this view and presenter when user clicks on model.
[PresenterName("UserInterface.Presenters.PropertyPresenter")]
public class PastureSpecies : ModelCollectionFromResource, IPlant, ICanopy, IUptake, IPlantDamage
```

```
[Separator("Grazing parameters")] // Show a separator description to user
```

```
[Summary]  // Write 'Thickness' to summary file
public double[] Thickness { get; set; }
```

```
[Tooltip("Name of the predicted table in the datastore")] // Show tool tip to user
public string PredictedTableName { get; set; }
```

```
[Units("kg/ha")] // Specify units that are shown on graphs.
public double Wt { get; set; }
```

```
[ValidParent(ParentType=typeof(Simulation))] // Specify models that 'weather' can be dropped in.
[ValidParent(ParentType = typeof(Zone))]
public class Weather : Model, IWeather, IReferenceExternalFiles
```

## Display attributes

```
[Display]  // Show this property to user.
public bool CalcStdDev { get; set; } = true;
```

```
[Display(Type = DisplayType.DirectoryName)] // Allows the user to click on a button to choose a directory name
public string OutputPath { get; set; }
```

```
[Display(EnabledCallback = "IsSpecifyYearsEnabled")]
public double[] Years { get; set; } // Will call c# property 'IsSpecifyYearsEnabled' to enable/disable option.

public bool IsSpecifyYearsEnabled { get { return TypeOfSampling == RandomiserTypeEnum.SpecifyYears; } }
```

```
[Display(Values = "GetValues")] // Show a drop down to user. Call 'GetValues' method to get dropdown values.
public string ColumnName { get; set; }

public string[] GetVales() { return new string[] {"A", "B" };
```
```c#
[Display(Type = DisplayType.Model, ModelType = typeof(IPlantDamage))]
public IPlantDamage HostPlant { get; set; } // Show a drop down to user with matching model names.
```

```
[Display(Type = DisplayType.TableName)] // Show a drop down to user containing table names from datastore
public string PredictedTableName { get; set; }
```

```
[Display(Type = DisplayType.FieldName)] // Show a drop down to user with field names from a table.
public string FieldNameUsedForMatch { get; set; }
```

```
[Display(Format = "N2")] // Show 2 decimals to user.
public double[] LL15 { get; set; }
```

```
[Display(Type = DisplayType.ResidueName)] // Show a drop down containing surface residue types.
public string InitialResidueType { get; set; }
```

---

## /modeldocumentation/

Source: https://apsimnextgeneration.netlify.app/modeldocumentation/
Title: Model documentation

# Model documentation

[Model documentation and tutorials](https://docs.apsim.info/)

---

## /user_tutorials/module1/moduleonetutorial/

Source: https://apsimnextgeneration.netlify.app/user_tutorials/module1/moduleonetutorial/
Title: Module 1: Fallow Simulation

# Module 1: Fallow Simulation

Created 22/02/2023 - Last updated 05/03/2023

*IMPORTANT NOTE: It is highly recommended that you upgrade your APSIM Next Gen version to at least version 2023.2.7164.0 or later.*

We will create a simulation that examines the water balance over time in a fallow field in two locations with different soil types.

1. In the top menu bar, click on “Open an example”. ![Open example menu bar option](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step1.png) Because all simulations generally share the same base components, we do not recommend starting from scratch. The best method is to choose the simulation closest to the one you want to build then modify it. For the purpose of this exercise we will use the Continuous Wheat simulation. Click ‘Wheat.apsimx’ then click Open.
2. Select “Wheat.apsimx”. ![Open wheat.apsim](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step2.png)
3. Click Save as. ![Save as](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step3.png)
4. Create a new folder called ‘Apsim Training’ to save all of your work in. ![Create new folder](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step4.png) ![Simulation loaded](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step5.png)
  - Remember this location, as you will save all training modules to this location. Save the file as “Module1”. You will now see the new simulation loaded.

5. The Apsim UI consists of four panels; the main toolbar at the top, a simulation tree on the left that lists all the components in the loaded file, a module properties pane on the right and a bar at the bottom that displays messages.

## Building a simulation

1. First we will make sure we’re using the right weather data. Click the “Weather” component in the simulation tree. You should be able to see weather data for Dalby loaded. Click browse and select “AU_Goondiwindi.met” to change it to Goondiwindi weather. ![Weather view](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step6.png) ![Weather view file select](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step7.png)
2. Next we’ll set the start and end dates for the simulation. In the clock component, set the start date to 1/1/1989 and the end date to 31/12/1989. ![Changing clock settings](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step8.png)
3. We are going to utilise a pre made toolbox to make it easier to access some soil data. In APSIM Next Gen, you can access this by: ![Getting to the training toolbox](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step9.png)
  - Clicking ‘Home’
  - Then clicking “Training toolbox” from the menu bar.

  - Inside the training toolbox double-click “Soils”.
  - Right-click the “Heavy Clay”, click copy. ![Getting to the training toolbox](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step10.png)
  - Next Click “Module 1”. This is located above the menu bar. This will take you back to your Module 1 simulation view.
  - Next, right-click “Field” and click “paste” from the menu that appears. ![Adding heavy clay to field](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step11.png)

4. Delete the old soil by clicking it and pressing delete. You can reorder components by right clicking and choosing Move Up/Down (Keyboard shortcut: Hold ctrl + up or down keys). ![Reordering plus removing old soil](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step12.png)
5. We need to set the starting water and nitrogen conditions for the soil. Expand the new soil node “Heavy Clay” and click “Water”. Make sure “Filled from top” is checked and set “Percent full” to 10%. ![Setting starting water settings](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step13.png)
6. Click the “NO3” component and set the starting NO3 to 50 kg/ha and starting NH4 to 3 kg/ha. We’ll spread it evenly through the entire soil profile. First, we need to tell Apsim that we want to work in units of kg/ha, not ppm.
  - To change the units, right-click the “initial values” cell and select “kg/ha”
  - Change NO3 and NH4 to kg/ha then enter the values below. ![Setting starting NO3](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step14.png) ![Setting starting NH4](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step15.png)

1. We want the nitrogen spread evenly through the entire soil profile. To find out how deep the profile is, click the Water node under Soil. The table should show layers ranging from 0-150 to 1500-1800mm. As the depths are not set correctly we will modify NO3 and NH4’s depth values to 0-1800.

![Checking depths](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step16.png)

1. In the SurfaceOrganicMatter node, check that the ‘Type of initial residue pool’ is wheat and change the ‘Mass of initial surface residue (kg/ha)’ to 1000 kg/ha. This means we start the simulation with 1000kg/ha of wheat stubble on the surface. This will decay over time putting nutrients back in the soil. It will also reduce surface evaporation.
  - To do this click in the cell to the right of “Mass of initial surface residue (kg/ha)”.
  - Then change the value from 500 to 1000.

  1. Delete the Fertiliser, Wheat, and three Manager nodes: Sow using a variable rule, Fertilise at sowing and Harvest, as we do not need them for a fallow simulation. It should now look like this:
    - To do this right click each manager node
    - Then click delete.
    - These nodes have this icon: ![Image](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step14pt2.png)

![New simulation structure](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step17.png)

1. Rename the simulation. To do this: ![New simulation structure](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step18.png)
  - Right-click the Simulation node under Simulations.
  - Click ‘rename’.
  - Type in ‘Clay Fallow’ and press enter.

2. Results for the simulation are found in the ‘DataStore’ node. The data that is reported into the datastore is configured in the “Report” node, found under the “Field” node. Click the “Report” node and delete all the Variables under the “Reporting variables” section. To do this: ![Deleting reporting variables](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step19.png)
  - Highlight all the text.
  - Right-click the highlighted text and click “delete”.

3. Next we will enter the variables we want reported. These are: ``` [Clock].Today [Weather].Rain sum([Soil].SoilWater.ESW) [Soil].SoilWater.Es [Soil].SoilWater.Runoff [Soil].SoilWater.Drainage sum([Soil].NO3.kgha) sum([Soil].Nutrient.MineralisedN [SurfaceOrganicMatter].Wt [SurfaceOrganicMatter].Cover ``` Where Reporting frequency displays the variable : ``` [Wheat].Harvesting ``` Replace with the variable by typing: ``` [Clock].EndOfDay ``` Your report view should now look like this: ![Reporting variables](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step20.png) You can choose a regular interval such as every day or once a month/year, etc, or you specify an event. For instance you might want to output on sowing, harvesting or fertilising. You can have multiple events in a report but this will result in duplicated writes if a day meets both criteria. For this simulation we want to output daily so we’ve used: ``` [Clock].EndOfDay. ```
  1. We’ve finished building the simulation.
    - Click `run` button in the menu bar. The bottom panel will display a message like `Simulation complete [.09 sec]`.
    - Once the run is complete, click the ‘DataStore’ component to view the results.
    - This information can be exported as a spreadsheet by:
      - right-clicking “DataStore” node ![DataStore](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step21.png)
      - click “Export to EXCEL”
        - This will be saved as “Module1.xlsx” in the same folder you saved your “Module1.apsimx” file.

      - or “export output to text files”.
        - This will be saved as “Module1.Report.csv” in the same folder you saved your “Module1.apsimx” file.

## Creating a graph

Apsim has the ability to do basic visualisation and analysis right in the user interface. Let’s use the inbuilt APSIM graphs to display the output file in a graph.

We will create a graph of Date vs ESW and Rain(Right Hand Axis).

1. First lets delete the existing graph called: “Wheat Yield Time Series” by right-clicking the node and clicking “delete”. ![Delete graph](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step22.png)
2. Next lets create a new graph for this simulation.
  - Right-click “Clay Fallow”
  - Click “add model” ![add model](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step23.png)
  - Double-click “graph” this will add it to the list of nodes. ![add graph](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step24.png)

3. To add data to our graphs we will add “series” to our graph. To do this:
  - Right-click “graph”
  - Click “Add model…”
  - Double-click “Series” ![add series](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step25.png)

4. Click “Series”. Rename it to ESW.Now we will change the specifics for this series.
  - In the `Data Source` drop down menu, select `Report`.
  - In the `X` drop down menu, select `Clock.Today`.
  - In the `Y` drop down menu, select `sum(Soil.SoilWater.ESW)`.
  - In the `Type` drop down menu, select `Scatter`.
  - In the `Line Type` drop down menu, select `Solid`.
  - In the `Marker type` drop down menu, select `None`.
  - In the `Colour` drop down menu, select orange.
  - Your ESW series variables should now look like this: ![ESW series variables](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step26.png)

5. Let’s add another series to the “Graph” node. Rename it “Rain”.
  - In the `Data Source` drop down menu, select `Report`.
  - In the `X` drop down menu, select `Clock.Today`.
  - In the `Y` drop down menu, select `Weather.Rain`.
    - Also, tick the “on right?” checkbox. This will add it to the right side of the graph.

  - In the `Type` drop down menu, select `Scatter`.
  - In the `Line Type` drop down menu, select `Solid`.
  - In the `Marker type` drop down menu, select `None`.
  - In the `Colour` drop down menu, select blue.
  - Your Rain series variables should now look like this: ![Rain graph variables](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step27.png)

6. If we click on the “Graph” node now it will display all the data like so ![Graphed data](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step28.png)
7. Try to create a graph of Date vs Runoff and Rain (right hand axis). - Change the line type to “Dot”. - Tip: you can copy a graph by dragging it to the node where you want it to appear. - Try copying your graph to the “Simulation” node and then edit the new one. - It should look like this: ![Runoff graph](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step29.png)

## Comparing Simulations

Quite often you will want to examine differences between multiple simulations. Let’s examine the effect of runoff on the water balance of two different soil types. To do this, we’ll copy our simulation to create a new one exactly the same.

1. Drag the “Clay Fallow” node up to the top simulations node. Now drop it on the node to create a copy. ![Copy Clay Fallow node](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step30.png)
2. Rename this new simulation “Sand Fallow”. ![Rename Simulation](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step31.png)
3. In Report for the Sand Fallow Simulation, remove the report variable named `[Weather].Rain`. This avoids making the rain line return to the start of the graph.
4. Drag the Sand soil from the Training toolbox onto the “Field” node under the new Sand Fallow simulation. Then delete the Heavy Clay soil. ![Copy sand soil type](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step32.png)
5. Since we have a new soil we need to set initial water and nitrogen again.
  - Click “Water” node and change variable “percent full” to 10% and check “filled from top?” ![Change water variables](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step33.png)
  - Click “NO3” node and change “0-2000” Depth value to: “0-1300”.
  - Change “ppm” to “kg/ha” by right-clicking “ppm” and clicking “kg/ha”.
  - Change the “initial value” to 50 and press enter.
  - Next, click “NH4” node and change the “ppm” value to “kg/ha” like we did above with “NO3” node.
  - Change Depth to “0-1300” and “initial value” to “3”.
  - Your nodes variables should look like below:| NO3 | NH4 | | --- | --- |

## Graph both Simulations

1. Next, run APSIM.
2. Let’s graph both the simulations together. To do this:
  - Right-click “Simulations” node at the very top of the left panel.
  - Click “Add model…”
  - Double-click “Graph” ![Whole simulation graph](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step36.png)

3. Let’s rename it “Runoff”.
4. Let’s add a series to this graph by right-clicking the “Graph”, clicking “Add model…”, and double-clicking “Series”.
5. Rename the series “runoff” and change the variables to match the image below. ![runoff series variables](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step37.png)
6. Add another “series” to the “Runoff” graph and rename it “rain”.
7. Change the variables to match the image below> ![rain series variables](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step38.png)
8. Now we have a graph showing the runoff of both soils. ![Final graph](https://apsimnextgeneration.netlify.app/images/ModuleOneImages/step39.png)

*Congratulations on completing your first module!*

*Note: If you found any incorrect/outdated information in this tutorial, please let us know on GitHub by [submitting an issue.](https://www.github.com/APSIMInitiative/ApsimX/issues/new/choose/)*

---

## /user_tutorials/module2/moduletwotutorial/

Source: https://apsimnextgeneration.netlify.app/user_tutorials/module2/moduletwotutorial/
Title: Module 2: Surface Organic Matter Simulation

# Module 2: Surface Organic Matter Simulation

Created 23/02/2023 - Last updated 05/03/2023

*IMPORTANT NOTE: It is highly recommended that you upgrade your APSIM Next Gen version to at least version 2023.2.7164.0 or later.*

## The Effect of Residue Cover on Soil Water Storage during Fallow

### Tracking the Decline of Cover as Residues Decompose.

APSIM simulates the influence of crop residues on the efficiency with which water is captured and retained during fallows. Residue cover declines as residues decompose. Residue decomposition is simulated in APSIM in response to weather, as well as the chemical composition of the residues. By doing this simulation you will reinforce skills learned in previous exercises and learn to do some basic editing of default values to “customise” your simulations.

This module assumes you have completed the previous module: “Module One: Fallow Simulation”. It will introduce you to the Surface Organic Matter module and demonstrate how surface residue decomposes over time.

1. For this module we will use the simulation we created in Exercise 1 (Module1) as a base. There is also a completed example in the training toolbox if you would prefer to use that. Open the file Module1.apsim.
2. Save the file as Module2.apsim in your `Apsim Training` folder. Remember to use `Save As` not `Save` or you will overwrite the old file.
3. Delete the `Sand Fallow` simulation. We’ll use `Clay Fallow` as the starting point. Also delete the graph.
4. Make a copy of `Clay Fallow` by dragging it to the simulations node in the tree and rename this new simulation to `Clay Residue`.
  - Your node tree should look like this: ![Node tree](https://apsimnextgeneration.netlify.app/images/moduleTwoImages/step1.png)

5. Expand the new simulation then expand the paddock node. Click the SurfaceOrganicMatter module and change the initial surface residue to 3000 kg/ha. ![residue variable](https://apsimnextgeneration.netlify.app/images/moduleTwoImages/step2.png)
6. Run both of the simulations, either by clicking on the `simulations` node at the top and then clicking Run, or selecting them individually and running them.
7. Create a graph of Date vs surface organic matter cover (SurfaceOrganicMatter.Cover) and Weather.Rain (right hand axis) for the `Clay Residue` simulation.
  - To do this:
    - right-click `Clay Residue` node.
    - change graph name to `Organic Matter Cover`
    - right-click `Organic Matter Cover` node,
      - double-click `Add model...`,
      - double-click `Series`

    - click `Series` node
      - change `X` to `Clock.Today`
      - change `Y` to `SurfaceOrganicMatter.Cover`
      - select `Report` as data source
      - change the `type` to `Scatter`
      - change `line type` to `Solid`
      - change `marker type` to `None`
      - change `colour` to yellow
      - rename this `Series` node as `SOM`.

    - Your node tree should look like this: ![SOM node](https://apsimnextgeneration.netlify.app/images/moduleTwoImages/step3.png)

8. Create another series for rain under the `Graph` node.
  - To do this:
    - right-click `Organic Matter Cover` node
      - double-click `Add model...`
      - double-click `Series`
      - rename this series to `Rain`

    - click `Rain` node
      - select `Report` for `Data Source`
      - change `X` to `Clock.Today`
      - change `Y` to `Weather.Rain`
        - check `on right?` checkbox

      - change `Type` to `Scatter`
      - change `Line type` to `Solid`
      - change `Marker type` to `None`
      - change `Colour` to blue.

    - Your node tree should look like this: ![Rain node](https://apsimnextgeneration.netlify.app/images/moduleTwoImages/step4.png)

## The effect of cover decline on runoff and evaporation

We will compare the effect that ground cover has on runoff.

1. Graph both simulations, with Date vs runoff (cumulative) and Rain (right axis).
  - To do this:
    - right-click the `Simulations` node
    - click `add model...`
    - double-click `Graph`

2. Rename the graph to Runoff.
3. Let’s build the graph
  - To do this:
    - right-click `Runoff` graph
    - click `Add model...`
    - double-click `Series`
    - rename series to `Cumulative Runoff`
    - Set your series variables to below: ![Runoff graph image](https://apsimnextgeneration.netlify.app/images/moduleTwoImages/step5.png)
    - NOTE: If you only get one graph it means that one simulation has not been run yet.

4. Let’s add another Series for `Rain`
  - To do this:
    - right-click `Runoff`
    - click `Add model`
    - double-click `Series`
    - rename this series to `Rain`
    - set the series variables to below: ![rain series variables](https://apsimnextgeneration.netlify.app/images/moduleTwoImages/step6.png)

## The effect of residue type on speed of decomposition

The APSIM residue model will decompose residues at differing rates according to the C:N ratio of the material. To demonstrate this we will reproduce the previous simulation but apply legume residues in the place of the wheat residues.

1. Create another copy of the `Clay Residue` simulation. Rename it to `Clay Chickpea Residue`. Remove the graph component.
  - Remove the [Weather].Rain Report Variable from the Report node in the ‘Clay Chickpea Residue’ simulation.

2. Change the SurfaceOrganicMatter residue parameters to 3000 kg/ha of chickpea residue.
  - Also change the initial residue pool to ‘chickpea’.

3. Change the C:N ratio to 25. ![Surface organic matter chickpea](https://apsimnextgeneration.netlify.app/images/moduleTwoImages/step7.png)
4. Run the simulation.
5. Create a graph with all three residue simulations with residue as a function of time. Call the graph `Cover`.
  - To do this:
    - right-click the `simulations` node
    - click `Add model...`
    - double-click `Graph`
    - rename `Graph` to `Cover`
    - right-click `Cover` graph
    - click `Add model...`
    - double-click `Series`

6. Change the variables to match the image below: ![Series variables for cover graph](https://apsimnextgeneration.netlify.app/images/moduleTwoImages/step8.png)
7. If you’d like the lengend to appear on the right of the graph like the image:
  - Click one of the legend items
  - a menu will appear at the bottom of the graph and you can change the drop down menu’s value to top right or any other position to your liking. ![Change legend location](https://apsimnextgeneration.netlify.app/images/moduleTwoImages/step9.png)

*Congratulations on completing module two!*

*Note: If you found any incorrect/outdated information in this tutorial, please let us know on GitHub by [submitting an issue.](https://www.github.com/APSIMInitiative/Apsimx/issues/new/choose/)*

---

## /user_tutorials/module3/modulethreetutorial/

Source: https://apsimnextgeneration.netlify.app/user_tutorials/module3/modulethreetutorial/
Title: Module 3: The Nitrogen Cycle

# Module 3: The Nitrogen Cycle

Created 01/03/2023 - Last updated 23/05/2024

*IMPORTANT NOTE: It is highly recommended that you upgrade your APSIM Next Gen version to at least version 2023.2.7164.0 or later.*

## The Nitrogen Cycle

In this exercise you will observe the cycle of fertiliser nitrogen in a fallow situation; urea to ammonium, ammonium to nitrate and the loss of soil nitrate via denitrification. This simulation will introduce editing a simple Manager rule and demonstrate more advanced features of graphing simulation results.

1. Start a new simulation based on the `Wheat` example.
2. Rename this simulation to Nitrogen Cycle.
3. Save this file as `Module3`.
4. The simulation will use a different weather file. To do this:
  - click the `weather` node
  - click the `browse` button
  - double-click `AU_Dalby` (C:\Program Files\APSIM[Version]\Examples\WeatherFiles) ![Change weather image](https://apsimnextgeneration.netlify.app/images/moduleThreeImages/img1.png)

5. In the `Clock` node, change the starting date to `1/1/1989` and the end date to `31/12/1989` ![Clock variables](https://apsimnextgeneration.netlify.app/images/moduleThreeImages/img2.png)
6. Add the `Heavy Clay` soil from the `Training toolbox`
7. Delete `Soil` node
8. Set `Percent full` to 50 in the `Heavy Clay's` `Water` node. ![change water % full](https://apsimnextgeneration.netlify.app/images/moduleThreeImages/img3.png)
9. Set starting nitrogen to 19kg/ha NO3 and 0 NH4, evenly distributed. Don’t forget to change units to kg/ha (right-click the column header `ppm`). Make the depth equal to the entire soil profile (check Water node for the profile depth). ![NO3 amount](https://apsimnextgeneration.netlify.app/images/moduleThreeImages/img4.png) ![NH4 amount](https://apsimnextgeneration.netlify.app/images/moduleThreeImages/img5.png)
10. Delete all manager scripts (all have a farmer icon: SowingFertiliser, Harvest, SowingRule1)
11. Copy a `Fertilise on fixed dates` management node to the field node. You can locate this by going to:
  - Home
  - Management toolbox
  - Fertilise folder
  - You can either drag this to your `Field` node or copy and paste it to the `Field` node. ![Fertilise on fixed date node](https://apsimnextgeneration.netlify.app/images/moduleThreeImages/img6.png)

12. Change `Type of fertiliser to apply?` to `UreaN`
13. Change fertilisation date to `10-Jan`
14. Change `Amount of fertiliser to be applied (kg/ha)` to `100`
15. In the `Report` node let set up the output variables: ``` [Clock].Today [Weather].Rain [Soil].SoilWater.Drainage sum([Soil].SoilWater.ESW) sum([Soil].NO3.kgha) as NO3Total sum([Soil].NH4.kgha) as NH4Total sum([Soil].Nutrient.DenitrifiedN) as Denitrification ```
16. In the `Report events` section remove existing event variables. Then add: ``` [Clock].EndOfDay ```
17. Run the simulation
18. Delete the current graph named `Wheat Yield Time Series`
19. Add another `Graph` node to the `Nitrogen Cycle` simulation node
20. Rename `Graph` to `Nitrogen`
21. Add a `Series` to `Nitrogen` graph
22. Rename `Series` to `NO3 total`
  - Variables for this `Series` ![NO3 total series variables](https://apsimnextgeneration.netlify.app/images/moduleThreeImages/img7.png)

23. Add another `Series` node to `Nitrogen`
24. Rename this `Series` to `NH4 total`
  - Variables for this `Series` ![NH4 total series variables](https://apsimnextgeneration.netlify.app/images/moduleThreeImages/img8.png)

25. Create a new graph with a series each for `rain`, `sum([Soil].SoilWater.ESW)`, `NO3Total`, `Denitrification`.
  - each series should have `[Clock].Today` as the `X` axis variable.

26. From this chart you can see that significant nitrogen is lost via denitrification when large amounts of nitrate are available in saturated soil conditions. ![Denitrification graph](https://apsimnextgeneration.netlify.app/images/moduleThreeImages/img9.png)

*Congratulations on finishing the 3rd module!*

*Note: If you found any incorrect/outdated information in this tutorial, please let us know on GitHub by [submitting an issue.](https://www.github.com/APSIMInitiative/Apsimx/issues/new/choose/)*

---

## /user_tutorials/module4/modulefourtutorial/

Source: https://apsimnextgeneration.netlify.app/user_tutorials/module4/modulefourtutorial/
Title: Module 4: Sowing A Crop

# Module 4: Sowing A Crop

Created 23/02/2023 - Last updated 05/03/2023

*IMPORTANT NOTE: It is highly recommended that you upgrade your APSIM Next Gen version to at least version 2023.2.7164.0 or later.*

## Sowing A Crop

In this exercise you will observe the growth of a crop over a single season. You will learn a bit more about how to use APSIM to do a ‘what-if’ experiment with fertiliser rates. These skills can not only be used to experiment with sowing fertiliser rates but also variables such as:

- Time of planting.
- Rate of sowing.
- Crop comparisons and different starting soil moisture conditions.

1. Start a new simulation using the `Wheat.apsimx` example. ![Open example simulation](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img1.png)
  - you can find this in the `open an example` menu item

2. Rename the simulation as `Wheat`.
3. Save this simulation as `Module4`. ![Save the simulation](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img2.png)
4. Make sure that `AU_Dalby.met` is the selected met file under the weather node.
5. Set the start and end dates of the simulation as `1/01/1989 - 31/12/1989` under the `Clock` node. ![Set dates](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img3.png)
6. Set the starting water to 25% full - filled from top. This is under `Soil` then `Water`. ![Set starting water](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img4.png)
7. Set the `initial values` column of both `NO3` and `NH4` to `kg/ha`. ![NO3](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img5.png) ![NH4](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img6.png)
8. Now let’s make some changes to the `Fertilise at sowing` management node.
9. Change the `Fertilise at sowing` parameter `Amount of fertiliser to be applied (kg/ha)` to `0`: ![SowingFertiliser to 0](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img7.png)
10. Let’s run the simulation and then inspect the `Graph` graph.
11. Make sure the x and y axes are set to `Clock.Today` and `Yield` respectively.
12. Rename the graph to `Wheat Yield Time Series` and its’ `Series` to `Wheat Yield`. ![Graph](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img8.png)
13. We can see with 0 sowing fertiliser we achieved a yield of almost 900 kg/ha.
14. Next we will create an experiment where we alter the sowing fertiliser amount for this year. We will see how this affects the yield.

## Creating an experiment

1. First add a `Experiment` node to the `Simulations` node at the top of the simulations tree. ![Add an experiment](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img9.png)
2. The `Experiment` node will be added to the bottom of the tree, hold `ctrl` key and press `up arrow` several times until it is directly below the `Simulations` node.
3. Add a `Factors` node to this experiment. ![Add a Factors node](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img10.png)
4. Add a `Factor` node to the `Factors` node. ![Add a Factor node](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img12.png)
5. To be able to change factors in our experiment, we will have to add our `Wheat` simulation to the experiment as a child node.
6. Drag and drop the `Wheat` simulation node onto the `Experiment` node. ![Add wheat to experiment](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img13.png)
7. Delete the `Wheat` simulation that is not a child of the experiment node. ![Delete wheat](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img14.png)
8. Next, we will create several versions of our experiment with varying sowing fertiliser amounts.
9. To do this, add this line to the `Factor` node: `[Fertilise at sowing].Script.Amount = 0 to 60 step 30` ![Create experiment variations](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img15.png)
10. If we click back on the `Experiment` node, you can see 3 differing amounts of sowing fertiliser. ![See variations](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img16.png)
11. To see the results lets drag a copy of the `Wheat Yield Time Series` graph onto the `Experiment` node. Change the variables to reflect the image below: ![Setup graph](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img17.png)
12. Run the simulation. You’ll see that the sowing fertiliser amounts increase the yield of the wheat crop by varying degrees. ![Final graph](https://apsimnextgeneration.netlify.app/images/moduleFourImages/img18.png)

*Congratulations on completing the 4th module*

*Note: If you found any incorrect/outdated information in this tutorial, please let us know on GitHub by [submitting an issue.](https://www.github.com/APSIMInitiative/ApsimX/issues/new/choose/)*

---

## /user_tutorials/module5/modulefivetutorial/

Source: https://apsimnextgeneration.netlify.app/user_tutorials/module5/modulefivetutorial/
Title: Module 5: Long-term simulations

# Module 5: Long-term simulations

Created 07/03/2023 - Last updated 05/03/2023

*IMPORTANT NOTE: It is highly recommended that you upgrade your APSIM Next Gen version to at least version 2023.2.7164.0 or later.*

## Long-term Simulations

### Chickpea sowing rates - 40 year runs

In this exercise you will use sowing rules to plant Chickpea crops and observe yield probabilities for a 40 year period given a half full soil moisture profile at sowing. We will compare two sowing rate strategies for these conditions with the goal of maximising yield. The weather will be different each year but the soil starting conditions will be the same.

By default, in long term simulations (i.e. longer than one year), the end of one years’ simulation becomes the starting point of the next year. This is useful if you are interested in seeing the degradation or improvement of the soil over a long time period. But what if you wanted to work out what the best strategy would be for the current year using weather scenarios from the past 40 years? To do this we could create 40 different simulations all with the same starting conditions but a different weather file (which would be a lot of work), or we could run the same simulation over 40 years and just reset the starting conditions each year (much simpler).

We can then try different management strategies to see which one would have worked best under the past 10 years weather scenarios.

1. Start a new simulations using `Wheat` example.
2. Rename the `simulation` as `Chickpea` and save the simulation as `Module5`.
3. Change the `Clock` nodes’ start and end date values to: `1/01/1940` and `31/12/1980`
4. Copy the `Heavy clay` soil from the `Training toolbox` and delete the exisiting `Soil` node.
5. Set the starting `Water` to `50%` full - filled from top.
6. Set NO3 `Depth` to `0-1800` and `initial value` to `20kg/ha` (right-click heading to change units).
7. Set NH4 `Depth` to `0-1800` and `initial value` to `0kg/ha`.
8. Change the `SurfaceOrganicMatter` node’s type to sorghum (don’t forget to rename the pool name to `sorghum` as well), initial surface residue: `550 kg/ha`, Carbon:Nitrogen ratio of `76`, leave the Fraction of residue standing as is.
9. Right-click `Field` and add a `Chickpea` plant node. All plants are found under the `PMF` folder.
10. Delete `Wheat`.
11. In `Sow using a variable` change the values to match the following: ![Sow using a variable's values](https://apsimnextgeneration.netlify.app/images/moduleFiveImages/img1.png)
12. Run the simulation.
13. You should get an error that at it’s end says: `.Chickpea.Field.Report can not find the component: [Wheat]`. This means we need to update the report variables and report events in `Report`. Let’s change any that have `[Wheat]` to `[Chickpea]`.
  - Remove `[Chickpea].Grain.Protein`.
  - Change the report variable `[Wheat].Phenology.Zadok.Stage` to `[Chickpea].Phenology.Zadok`.
  - Also, remember to change the report event down the bottom `[Wheat].Harvesting`.

14. Run the simulation again.
15. You should get an error with the message: Cannot find a soil crop parameterisation called ChickpeaSoil
  - This is caused by using a soil that is missing a `SoilCrop` node (located under `Physical`) with the same name as the plant node you are using. For now, create a copy of `WheatSoil` under `Physical` and rename it `ChickpeaSoil` to fix this exception.

16. Before we run again, let’s update our `Harvest` management node to look for the correct crop, now that `Wheat` has been removed and `Chickpea` has ben added.
17. Your simulation should now run successfully and you should have data in your `DataStore` node. ![Datastore node](https://apsimnextgeneration.netlify.app/images/moduleFiveImages/img2.png)
18. Add a management script called `Reset on date` to the `Chickpea` simulation (found in `Management Toolbox` under `Other`) ![reset on date location](https://apsimnextgeneration.netlify.app/images/moduleFiveImages/img3.png)
19. Leave all parameters as yes and change the `date to reset on` to `1-may`.
  - **note:** make sure this management script sits above all other management scripts in the tree as they are ran in the order they are arranged from top to bottom.

20. Remove the `Fertilise at sowing` manager node.
21. Rename the `Chickpea` simulation as `Chickpea 10 plants`.
22. Copy `Chickpea 10 plants` and rename it `Chickpea 15 plants`.
23. Change the `Plant population(/m2)` to `15` in the `Sowing using a variable` management script.
24. Right-click the `DataStore` and click `Empty the datastore`. This makes sure that we have the most up to date data once we run, then run the simulations.
25. Create a graph under `Simulations`. Rename it `Total chickpea yield time series` with a series that plots `[Clock].Today` and `Yield`.
26. Now you have a graph showing yield when comparing differing plant density over 40 years.
  - If you’ve copied the graph settings from the image below and you can’t see both simulations data displayed. Make sure `Chickpea 15 plants` sits above `Chickpea 10 plants` in the tree. ![Final total yield graph](https://apsimnextgeneration.netlify.app/images/moduleFiveImages/img4.png)

*Note: If you found any incorrect/outdated information in this tutorial. Please let us know on GitHub by [submitting an issue.](https://www.github.com/APSIMInitiative/ApsimX/issues/new/choose/)*

---

## /development/software/pmfdesign/

Source: https://apsimnextgeneration.netlify.app/development/software/pmfdesign/
Title: PMF code design

# PMF code design

In addition to the

- Root models must allow for multi-point root systems. This is provided when [IUptake](https://github.com/APSIMInitiative/ApsimX/blob/master/Models/Interfaces/IUptake.cs) is implemented and the standard *Root* class is used. If an alternate *Root* model is used, it needs to allow for multi-point root systems.
- Plant models must provide CO2 impacts. If the user changes CO2 in the weather component the plant model should respond.
- Plant models must use the transpiration value provided by MicroClimate. Without this, intercropping will not be possible.

---

## /usage/croptimizr/

Source: https://apsimnextgeneration.netlify.app/usage/croptimizr/
Title: Parameter Optimisation

# Parameter Optimisation

APSIM provides access to several parameter optimisation algorithms from within the user interface. These function as a wrapper around the [CroptimizR](https://sticsrpacks.github.io/CroptimizR/) R package. For detailed questions regarding the optimiser or the R code it may be worth consulting the package’s [documentation](https://sticsrpacks.github.io/CroptimizR/) or [bug tracker](https://github.com/SticsRPacks/CroptimizR/issues).

APSIM will by default run a CroptimizR simulation by using docker. This behaviour can be disabled by starting apsim with the environment variable `APSIM_NO_DOCKER=1`.

---

## Requirements

### Option 1: Docker (default)

- [Docker](https://docs.docker.com/engine/install/) must be installed
- If running windows, docker must be [configured](https://docs.docker.com/desktop/windows/#switch-between-windows-and-linux-containers) to run Linux containers

### Option 2: Running R natively (not recommended)

- R version >= 4.0.0 must be installed. Binary installations are available for [windows](https://cran.r-project.org/bin/windows/base/), [macOS](https://cran.r-project.org/bin/macosx/), and [linux](https://cran.r-project.org/bin/linux/)
- [Rtools40](https://cran.r-project.org/bin/windows/Rtools/) (only required on windows)

Once these requirements are in place, it is recommended to test the installation by running the example CroptimizRExample.apsimx file shipped with APSIM. This file should take 2-3 minutes to run on a modern laptop.

---

## Configuration

### Input file configuration

If using the docker runner (this is the default), all input files (ie .met, .xlsx, …) must be stored in the same directory as the .apsimx file. If the .apsimx file was generated by a script, care must be taken to ensure that the file paths are relative (not absolute).

### Simulations Configuration

The simulations which are to be run by the optimiser must be children or descendants of the CroptimizR node. No other simulations in the file will be run by the optimiser.

### Predicted/Observed data

Predicted and observed data can exist in separate tables in the database, and if so, the optimiser will automatically attempt to merge the data on the date or Clock.Today column. This is easier to set up initially, but for more complicated scenarios (e.g. matching data on flowering or harvesting dates), it may be better to allow APSIM to merge the data by using a PredictedObserved table. When using this approach, the predicted and observed table names in the CroptimizR should be set to “PredictedObserved” (or whatever the PredictedObserved table is called - ie HarvestObsPred). When using a predicted/observed table, the variable names in the “Variables to optimise” section should be prefixed with “Predicted.”. For example, “Predicted.Wheat.Leaf.LAI” (without the quotes).

### Other Parameters

##### Random seed

The random seed to be used by the optimiser. If left blank, the results of the optimisation will vary slightly between runs. If specified, it should be an integer and will cause the results returned by the optimiser to be identical if run multiple times.

##### Optimisation algorithm

Currently only simplex and bayesian algorithms are supported. For details on these algorithms, see [this page](https://sticsrpacks.github.io/CroptimizR/articles/Available_parameter_estimation_algorithms.html) in the CroptimizR documentation.

##### Critical Function

Several critical functions are offered by CroptimizR. For details, see [this page](https://sticsrpacks.github.io/CroptimizR/reference/ls_criteria.html).

##### Number of repetitions

The optimisation will be run multiple times, each time starting with different initial values for the estimated parameters. This parameter controls the number of repetitions.

##### Tolerance Criterion

Tolerance criterion between two iterations. Iterations will cease if the parameter values are changing by less than this amount.

##### Max number of iterations

The maximum number of iterations within a single repetition.

---

## Example Configurations

*Predicted and observed data in separate tables* ![example file](https://apsimnextgeneration.netlify.app/images/Usage.CroptimizR.ExampleFile.png)

*Predicted/Observed table* ![example file](https://apsimnextgeneration.netlify.app/images/Usage.CroptimizR.ExampleFile.POTable.png)

---

## Outputs

If the optimisation fails for some reason, any errors will be written to the status panel in the user interface, so it should be immediately obvious if something didn’t work. Otherwise, a successful optimisation run will result in several outputs being generated:

##### External files

Two files will be generated in the same directory as the .apsimx file. These are optim_results.Rdata and EstimatedVSinit.pdf. The filenames will be prefixed with the name of the CroptimizR as specified in the user interface - so when using default settings, they will be called CroptimizR-optim_results.Rdata and CroptimizR-EstimatedVSinit.pdf. The .pdf file contains several graphs generated by the R code. The .Rdata file contains all of the relevant outputs of the optimisation run and can be opened and perused in R. They are also automatically imported into the database associated with the .apsimx file, so they can be graphed or viewed from inside APSIM.

##### Summary file

If the .apsimx file contains a top-level summary node (as in the examples above), then all console output generated by the optimisation will be written to the summary file (accessible by selecting CroptimizR from the simulation name dropdown). This will contain some basic info about the run - it’s useful for checking that the run was successful but not much more.

##### Datastore

As mentioned earlier, the detailed outputs of the optimisation are imported into the datastore, and can be viewed by clicking on the datastore and choosing CroptimizR from the simulation name dropdown. This data shows one row per repetition of the optimisation, and can be graphed inside APSIM.

*Starting vs optimal value in each iteration* ![Sample Graphs](https://apsimnextgeneration.netlify.app/images/Usage.CroptimizR.Graphs.png)

---

## /usage/pathspecification/

Source: https://apsimnextgeneration.netlify.app/usage/pathspecification/
Title: Path Specification

# Path Specification

Paths are used throughout APSIM e.g. in REPORT. Paths are structured similarly to directory paths in Windows and Unix, using a ‘.’ character instead of slashes.

## Relative paths

Relative paths are not used much in APSIM. They are relative to the model that is using the path e.g.

If the soil model does a get for *Water* the a child model of that name will be returned.

## Absolute paths

Absolute paths have a leading ‘.’ e.g.

*.Simulations.Test.Clock* - absolute path - refers to the clock model in the ‘Test’ simulation.

## Scoped paths:

Scoped paths have a leading model type in square brackets. A model of the specified name, in scope, is located before applying the rest of the path.

*[Soil].Water* - scoped path - refers to the Water model that is a child of a model that has the name ‘Soil’ that is in scope

---

## /usage/graphs/creating-predicted-observed-graphs/

Source: https://apsimnextgeneration.netlify.app/usage/graphs/creating-predicted-observed-graphs/
Title: Predicted observed graphs

# Predicted observed graphs

All models included in the APSIM release need to have validation tests built using the user interface. Graphs with observed data need to be created in a .apsimx file.

## Observed data

Observed data needs to be in a spreadsheet (only .xlsx files are supported).

![Observed](https://apsimnextgeneration.netlify.app/images/Development.ModelValidation.Observed.png)

Observed spreadsheets must have a ‘SimulationName’ column with values that exactly matches the name of the simulations in the simulation tree. The column names also need to exactly match the column names in APSIM.

Multiple sheets can exist in the spreadsheet file. To connect the APSIM User Interface to the spreadsheet, an *Excel* component should be dropped onto the *DataStore* component, renamed to *Observed* and configured.

![ObservedInGUI](https://apsimnextgeneration.netlify.app/images/Development.ModelValidation.ObservedInGUI.png)

Multiple sheets can be specified by separating them with commas.

When you next run the simulation, the observed data will be added to the DataStore and be available for graphing.

## Predicted / Observed matching

To have APSIM match predicted and observed data, you can add a ‘PredictedObserved’ component onto your ‘DataStore’.

![PredictedObserved](https://apsimnextgeneration.netlify.app/images/Development.ModelValidation.PredictedObserved.png)

You then specify the name of your predicted and observed tables and the column name you want to match rows on. In the example above, the user interface will iterate through all rows in your observed and predicted tables and look at the value in the ‘Maize.Phenology.CurrentStageName’ column. Where one row in the observed table matches (has the same ‘Maize.Phenology.CurrentStageName’ value) one row in the predicted table, that row will be added to the new ‘PredictedObserved’ table.

This table then makes it easy to create predicted vs observed graphs.

![PredictedObservedGraph](https://apsimnextgeneration.netlify.app/images/Development.ModelValidation.PredictedObservedGraph.png)

## Testing

Everytime a change is made to APSIM and a pull request is made, Jenkins automatically runs all simulations and ensures that the model validations are still valid. It does this by looking for *Tests* components under *PredictedObserved* components. These *Tests* components calculate a range of statistics and store the ‘accepted’ values of these statistics. When Jenkins runs the simulations, it recalculates the statistics and checks to see if they are different (within 10% tolerance) of the ‘accepted’ statistics. Once a model is validated, a *Tests* component should be added to the .apsimx file under the *PredictedObserved* component.

![PredictedObservedGraph](https://apsimnextgeneration.netlify.app/images/Development.ModelValidation.Tests.png)

If you need to update the ‘accepted’ values, because for example you have modified the science in the model, you can right click on the *Tests* component and click *Accept Tests*. There after the current statistics will be the new accepted ones.

The statistics are:

| Test Name | Description |
| --- | --- |
| n | The number of PO pairs for the given variable. |
| Slope | The slope of the straight line linear regression. A perfect fit would have a value of 1. |
| Intercept | The intercept of the straight line linear regression. A perfect fit would have a value of 0. |
| SEslope | Standard error in the slope. |
| SEintercept | Standard error in the intercept. |
| R2 | R2 value. Between 0 and 1 where 1 is a perfect fit and 0 is basically random noise. |
| RMSE | Root Mean Squared Error. 0 is a perfect fit. Values less than half the standard deviation of the observed data are acceptable. |
| NSE | Nash-Sutcliffe Efficiency. Indicates how well the PO data fits the 1:1 line. Ranges from -∞ to 1 with 1 being the optimal value while values between 0 and 1 are generally viewed as acceptable. Values < 0 indicate unacceptable model performance. |
| ME | Mean Error between predicted and observed values. 0 is a perfect fit. |
| MAE | Mean Absolute Error. 0 is a perfect fit. Values less than half the standard deviation of the observed data are acceptable. |
| RSR | RMSE-observations Standard Deviation Ratio. The ratio of RMSE to standard deviation. 0 is a perfect fit. |

---

## /usage/report/

Source: https://apsimnextgeneration.netlify.app/usage/report/
Title: Report Node

# Report Node

## How to create a basic report

> Here we will describe the features of the report node and some additional information on how to use it. Understand the anatomy of the report node. Find relevant report variables. Add report variables to a report. Find report events that will record the variables when that occurs. Add events to report. How to set an alias/nickname for a report variable.

### Report variables and Report events

- Report variables are the data you want to record.
  - Examples are plant leaf area index, grain weight, grain size, yield and many others.

- Report events are when report variables are recorded.
  - This can be a time of day, week, month, year or when harvesting as well as many other events.

### The Report node

#### Report Variables window

- Top left window is the reports variables window.
  - These are the variables that are reported on when the simulation is run.
  - A typical variable starts with a simulation node name enclosed in square brackets followed by child node names or node properties separated by periods.
    - An example is `[Wheat].LAI`.

  - When you begin typing the window to the left’s content will change if there are matching reporting variables.

#### Common report variables window

- Top right window is the common report variables window.
  - These initially display any variables relevant to the entire simulation.
  - When you begin typing on any line, this window’s contents will filter common variables (if any exist) based on simulation node names typed and text that may appear match the description of common reporting variables.

#### Report events window

- The bottom left window is the report events window.
  - Code is written here that determines when the report variables are reported.
  - When you begin typing, the common report events content will change, showing relevant events if any exist.

#### Common report events window

- The bottom right window is the common report events window.
  - Initially all relevant events for the simulation show up here.
  - When you begin typing in the report events window, the contents of this window will change to show events that match either the description of a common report event or a node within your Apsimx file.

### Finding relevant report variables

- The most efficient way to find variables is to simply start typing a nodes name. Doing this will filter out common variables on the right.
- If you cannot find it in the common report variables list you may have to type something more specific to find what you are looking for.
- If you know the property you want to report on’s node. You can use the ‘intellisense’ pop-up window to help find a relevant property.
  - To bring up the intellisense window, type a node’s name encased in square brackets followed by a period.

### Adding variables to a report

- To add variables you can do this in 3 different ways:
  1. Double-clicking a variable from the list on the right.
  2. Dragging a variable from the common report variables list to the report variables window.
  3. Typing the code directly into the reporting variables window.

### Giving a report variable a nickname/alias

To do this simply add the phrase: ‘as alias’ at the end of a line to give a variable a specific column name in your report. This is a good idea for variables that are long and complex.

### Notes about report

If you try to run a report with a variable or event that is not valid you will see an error message appear in the message box at the bottom of the ApsimX window.

### Adding an event or variable to the common report variable/event list.

Anyone can submit a new common report variable or event to the lists for anyone to use. Mulitple events and variables can be added at one time.

There are two ways to do this:

1. Use the ‘submit new event/variable’ button in the common report events window.
  - This will take you to the ApsimX github page where you can submit a new ‘issue’ where you can add the information required to add a new variable or event.

2. Navigate directly to [https://github.com/APSIMInitiative/ApsimX/issues/new?assignees=&labels=New+common+report+event%2Fvariable&projects=&template=new-common-report-event-variable.yml](https://github.com/APSIMInitiative/ApsimX/issues/new?assignees=&labels=New+common+report+event%2Fvariable&projects=&template=new-common-report-event-variable.yml) and add your details there.

Once this is submitted the event or variable will be reviewed. If accepted it will be added to the list for anyone to use.

## Using report row filters

To filter the row data in your report node, you can use row filters.

To do so you type the name of the column header along with a conditional statement in the “Row Filter” field.

- Some examples:

```
"Clock.Today" = "1900-11-10"
```

- The Clock time must be a complete date of the format “YYYY-MM-DD”. However, you can include a wildcard character (*) in place of any number in the Clock time.
- You can use any greater than or less than combination too. Examples:

```
"Clock.Today" > "1900-01-01"
```

```
"Wheat.AboveGround.Wt" > 900
```

- You can have multiple filters. An Example:

```
[Clock.Today] > "1905-**-**" and [Wheat.AboveGround.Wt] > 1000
```

## Using report column filters

To filter the column data in you report node, you can use a column filter.

To do so you type the name of the column header. Some examples are:

```
Clock.Today
```

```
Wheat.AboveGround.Wt.
```

### Multiple columns

It’s possible to have all fields that contain a common keyword to be displayed.

If your report variables have many child properties you can use the name of the parent to filter all columns that contain the parent’s name.

An example:

```
Wheat
```

![report variables](https://apsimnextgeneration.netlify.app/images/report-vars.png) *Report variables in the simulation:*

![column filter results](https://apsimnextgeneration.netlify.app/images/report-column-filter-result.png) *Results of using a common keyword*

Note: Only one column filter can be used at one time.

---

## /usage/rotationmanager/

Source: https://apsimnextgeneration.netlify.app/usage/rotationmanager/
Title: Rotation Manager

# Rotation Manager

# Rotation Manager

The rotation manager visualizes and helps to implement the logic in a crop rotation. By itself, the rotation manager understands very little of the components with which it is interacting. Instead, it relies on other components (usually manager scripts) for their specific knowledge. An example crop rotation is provided in the RotationManager.apsimx example file.

## States

The general idea is that the rotation will progress through states, usually in a repeating cycle. The sequencer’s daily operation is simple:

- Can I do anything?
- If so, do it

The rules/conditions for moving from one state to another are defined in the “Rules” textbox which appears in the lower panel after clicking on an arc.

The actions to be performed are specified in the “Actions” textbox which appears in the lower panel after clicking on an arc.

In the following example, the rotation manager starts in the “initial” state and asks the MaizeManager (a manager script) each day if it is ready to sow a crop. If the manager is ready to sow, then the rotation manager will tell MaizeManager to sow a crop. Note that `CanSow` is a property in the manager script, and as such there are not parentheses required. However `SowCrop()` is a method (function) in the manager script, so parentheses are required for the invocation. Arguments can be passed if required by the method, but they must be primitive types (string, int, double, bool, etc).

![State transition](https://apsimnextgeneration.netlify.app/images/RotationManager.Transition.png) ![State transition script](https://apsimnextgeneration.netlify.app/images/RotationManager.Transition.Script.png)

States/nodes can be added by right-clicking an empty area of the rotation manager and clicking “Add Node”. Arcs can be added by selecting (clicking on) a node and then right clicking on another node and selecting “Add node from x to y”.

## State Transition Algorithm

Each rule/condition must be a boolean or numeric value, and an arc can have multiple rules (one per line). A weight is calculated for the arc as the product of all rules defined on the arc (boolean values are treated as true = 1, false = 0). If the weight is greater than 0, then transition along the arc is possible. If multiple arcs are connected to a state, then the rotation will transition along the arc with the highest weight.

When transitioning to a new stage, each action in the “Actions” textbox (one per line) will be executed. If the action contains parentheses, it is assumed to be a method. If no parentheses exist, the action is assumed to be an event name, and the event will be published.

Additionally, three extra events are published during a state transition, in this order:

- `TransitionFromX`
- `Transition`
- `TransitionToY`

Where `x` is the previous state and `y` is the next state.

---

## /usage/sensitivityanalysis/

Source: https://apsimnextgeneration.netlify.app/usage/sensitivityanalysis/
Title: Sensitivity Analysis

# Sensitivity Analysis

## What is sensitivity analysis and why is it useful?

Sensitivity analysis of crop models allows us to see a models response to changing various inputs.

There exist several examples demonstrating how sensitivity analysis can be performed. These examples can be found within the `Examples/Sensitivity` folder of your APSIM installation.

## Setup and Testing Instructions

1. If you haven’t already you can download APSIM from [the APSIM registration site](https://registration.apsim.info)
2. Download R install from: [https://cran.r-project.org/bin/windows/base/release.htm](https://cran.r-project.org/bin/windows/base/release.htm) and install with all default settings. Note: if you have Docker Desktop, you can ignore this step.
3. Open APSIM
4. Open the `Sensitivity_MorrisMethod.apsimx` example simulation from Example folder included in your apsim installation.
5. The simulation takes a minute or so depending on your system resources. This means you will not be able to interact with the APSIM window for that time span.

---

## /development/software/interfaces/

Source: https://apsimnextgeneration.netlify.app/development/software/interfaces/
Title: Software interfaces

# Software interfaces

A model needs to be loosely coupled to other models to allow it to be replaced by an alternate implementation. To enable this, it is important that models implement the required interfaces.

| Model type | Description |
| --- | --- |
| Plant | To allow users to call methods for Sow, Harvest, EndCrop implement IPlant |
|  | To allow MicroClimate to calculate and arbitrate canopy light interception implement ICanopy |
|  | To allow SoilArbitrator to calculate and arbitrate water and nutrient uptake implement IUptake |
|  | To allow plant consumers (pest / diseases / stock) to damage a plant implement IPlantDamage and IOrganDamage |
| Soil water | To allow models to get water variables implement ISoilWater |
| Nutrient | To allow models to get nutrient variables implement ISolute and INutrient |
| Surface organic matter | To allow models (e.g. Plant, Stock, SimpleGrazing) to transfer biomass to the surface residue pools and to get surface residue variables implement ISurfaceOrganicMatter |
|  | To allow plant consumers (pest / diseases / stock) to damage surface residues implement IPlantDamage and IOrganDamage |
| Weather | To allow models to get weather data implement IWeather |
| Soil temperature models | To allow models to get soil temperature variables implement ISoilTemperature |

The converse of the above table also holds true. For example, a canopy arbitration model must **look for and use** models that implement [ICanopy](https://github.com/APSIMInitiative/ApsimX/blob/master/Models/Interfaces/ICanopy.cs).

---

## /tags/

Source: https://apsimnextgeneration.netlify.app/tags/
Title: Unavailable Page

# Unavailable Page

Fetch failed with HTTP 404 for https://apsimnextgeneration.netlify.app/tags/

---

## /usage/tests/

Source: https://apsimnextgeneration.netlify.app/usage/tests/
Title: Test Results

# Test Results

To test your data, you can add something like this to a manager script:

```
using System;
using Models.Core;
namespace Models
{
    [Serializable]
    public class Script : Model, ITest
    {
        public void Run()
        {
            bool testHasFailed = true;
            if (testHasFailed)
                throw new Exception("oh dear");
        }
    }
}
```

Things to note:

- Any failures should be handled by throwing an exception.
- Whenever Apsim finishes running simulations, it will run all `IModel`s which implement the `ITest` interface. Therefore, the script must inherit from `Model`
- `ITest` is defined in the `Models.Core` namespace
- By default, Apsim will not run these tests when run from the command line, unless the `--run-tests` command line switch is provided. If you don’t know what the command line is, this will not affect you.
- [Jenkins](http://www.apsim.info:8080/jenkins) will run these tests whenever a pull request is run. Therefore, all files under the Examples, Prototypes, and Tests directories are guaranteed to be tested.

---

## /

Source: https://apsimnextgeneration.netlify.app/
Title: The next generation of APSIM

navigation

# The next generation of APSIM

Since 1991, the Agricultural Production Systems sIMulator (APSIM) has grown from a farming systems framework used by a small number of people, into a large collection of models used by many thousands of modellers internationally. The software consists of many hundreds of thousands of lines of code in 6 different programming languages. The models are connected to each other using a ‘common modelling protocol’. This infrastructure has successfully integrated a diverse range of models but isn’t capable of meeting new computing challenges. For these reasons, the APSIM Initiative has begun developing a next generation of APSIM (dubbed APSIM Next Gen.) that is written from scratch and designed to run on Windows, Linux and OSX.

The new framework incorporates the best of the APSIM 7.x framework. C# was chosen as the programming language and together with MONO and GTK#, the models and user interface run on Windows, LINUX and OSX. The Plant Modelling Framework (PMF), a generic collection of plant building blocks, was ported from the existing APSIM to bring a rapid development pathway for plant models. The user interface look and feel has been retained, but completely rewritten to support new application domains and the PMF. The ability to describe experiments has been added which can also be used for rapidly building factorials of simulations. The ability to write C# and VB.NET scripts to control farm and paddock management has been retained. Finally, all simulation outputs are written to an SQLite database to make it easier and quicker to query, filter and graph outputs.

The software engineering process has also been significantly improved. We have adopted GitHub to host the repository and have built a workflow around it involving feature branches, pull requests for peer-review of code and science reviews for major tasks. We have improved the testing regime and are building validation data sets for all models. These datasets are used to automatically revalidate each model every time there is a change and regression statistics are compared with previously accepted values. This improves the likelihood of detecting unexpected changes to model performance when a developer commits new changes.

We have also enhanced the way we document all models by auto-generating all documentation from the validation tests and from using reflection to examine comments in the source code. The result is a nicely formatted PDF that describes a model and presents its validation, with regression statistics, graphically.

---

## /development/software/unittests/

Source: https://apsimnextgeneration.netlify.app/development/software/unittests/
Title: Unit tests

# Unit tests

In theory, all methods in all classes should have unit tests that test they work correctly. In practice, user interface and infrastructure code is better tested than model science code.

APSIM uses NUnit for all unit tests. This is integrated into Visual Studio via NuGet. The UnitTests project in the APSIM solution contains all tests. The folder structure in this project mimics the folder structure in the models and ApsimNG projects.

An example of a good test is in FertiliserTests.cs:

```
        /// <summary>Ensure the the apply method works with non zero depth.</summary>
        [Test]
        public void Fertiliser_EnsureApplyWorks()
        {
            // Create a tree with a root node for our models.
            var simulation = new Simulation()
            {
                Children = new List<IModel>()
                {
                    new Clock()
                    {
                        StartDate = new DateTime(2015, 1, 1),
                        EndDate = new DateTime(2015, 1, 1)
                    },
                    new MockSummary(),
                    new MockSoil()
                    {
                        Thickness = new double[] { 100, 100, 100 },
                        NO3 = new double[] { 1, 2, 3 },
                        Children = new List<IModel>()
                        {
                            new MockSoilSolute("NO3"),
                            new MockSoilSolute("NH4"),
                            new MockSoilSolute("Urea")
                        }
                    },
                    new Fertiliser() { Name = "Fertilise" },
                    new Operations()
                    {
                        Operation = new List<Operation>()
                        {
                            new Operation()
                            {
                                Date = "1-jan",
                                Action = "[Fertilise].Apply(Amount: 100, Type:Fertiliser.Types.NO3N, Depth:300)"
                            }
                        }
                    }
                }
            };

            simulation.Run();

            var soil = simulation.Children[2] as MockSoil;
            Assert.AreEqual(new double[] { 1, 2, 103 }, soil.NO3);
            Assert.AreEqual("100 kg/ha of NO3N added at depth 300 layer 3", MockSummary.messages[0]);
        }
```

This test creates a simulation using code, runs it and then uses *Assert* to determine the outputs are as expected. The preference is to create the simulation using code (rather than reading from a resource) as the test is self contained with no need to consult other files. A lot of tests need to create complex simulations and so using a resource file is necessary.

The above test also highlights the use of mocks, classes that mimic a real model but have much simplified, controllable behaviour. The example uses *MockSoilSolute* which mimics a solute model. This allows this fertiliser test to be isolated from the other models in the simulation. It is better to test just the function in question and not the rest of the APSIM as well. Mocks allow you to do that.

---

## /development/software/userinterfacedesign/

Source: https://apsimnextgeneration.netlify.app/development/software/userinterfacedesign/
Title: User interface design

# User interface design

# Design characteristics

- The ‘Command pattern’ is used for all user interface actions (e.g. select a node, edit the clock start date, change the format of a graph). A history of commands will be stored for each .apsimx file loaded. This will allow undo/redo as each command will have the ability to undo itself. This also allows a script of commands to be sent to the user interface via the command line, allowing some automated user testing of the user interface.
- The user interface shall run on Windows, LINUX, OSX.
- GTK# (rather than Windows.Forms) is used to provide cross-platform compatibility.
- A ‘Model-View-Presenter’ pattern shall be used to disconnect views (forms) from the models.

# Commands

The requirement for Undo/Redo has led to the adoption of the ‘command’ pattern in the user interface. This pattern dictates that all changes to all ‘Model’ classes must be done via a command. Commands are also used by the user interface when the user interacts with tree nodes. Each command has two methods, one for performing the command, another for undoing the command. The interface (ICommand.cs) looks like this:

```
namespace UserInterface.Commands
{
    public interface ICommand
    {
        object Do();
        object Undo();
    }
}
```

If the command alters the state of a model during a ‘Do’ or ‘Undo’, it should return the altered model to the caller (CommandHistory). The CommandHistory will then invoke a ‘ModelChanged’ event that the views can subscribe to and update their screens. As an example of a concrete command, the ‘ChangePropertyCommand’ is given below. This command is used to change a property value in a model. Before doing this though, it will retrieve the original value so that it can reapply this value during an Undo operation.

```
namespace UserInterface.Commands
{
    class ChangePropertyCommand : ICommand
    {
        private object Obj;
        private string Name;
        private object Value;
        private object OriginalValue;

        public ChangePropertyCommand(object Obj, string PropertyName, object PropertyValue)
        {
            this.Obj = Obj;
            this.Name = PropertyName;
            this.Value = PropertyValue;
        }

        public object Do()
        {
            // Get original value of property so that we can restore it in Undo if needed.
            OriginalValue = Utility.Reflection.GetValueOfFieldOrProperty(Name, Obj);

            // Set the new property value.
            if (Utility.Reflection.SetValueOfFieldOrProperty(Name, Obj, Value))
                return Obj;
            return null;
        }

        public object Undo()
        {
            if (Utility.Reflection.SetValueOfFieldOrProperty(Name, Obj, OriginalValue))
                return Obj;
            return null;
        }
    }
}
```

# Model View Presenter

A ‘Model’ in this context is self explanatory. It is the class that holds the problem domain data (deserialised from the json files) that is editable by the user and executes during a simulation run. Some examples include SoilWater, Clock and Graph.

A ‘View’ is a form that allows user interaction. It doesn’t have any functionality beyond the display of information and receiving user input. It does not have any functionality that determines what data gets put on the screen. i.e. it doesn’t talk to the model. A ‘view’ does not have a reference to a model or presenter. It is essentially a very passive (humble) form that is told what to do by the presenter. It does not contain any logic that describes what to do when the user interacts with it. In short, the idea is to keep it as simple as possible.

A ‘Presenter’ is a class that tells the view what to display, asking the model for that data. It acts as a go-between between a view and a model. It is also responsible for determining what to do when the user does something. A Presenter should not have code that assumes a particular display technology i.e. no using System.Windows.Forms or System.Web.Forms.

In theory, the user interface should be able to be recoded from a windows app to a web app by just recoding the ‘views’ and keeping everything else the same. It should also be noted that a view could have multiple presenters in different situations. For example, a ‘GridView’ (form with a grid on it) may have 1 presenter that populates the grid with property type info (like what the user sees when they click on a manager component). It might have another presenter that displays soil profile information. A third presenter might display the contents of an APSIM output file.

For more info on the Model/View/Presenter pattern visit here: [http://codebetter.com/jeremymiller/2007/07/26/the-build-your-own-cab-series-table-of-contents](http://codebetter.com/jeremymiller/2007/07/26/the-build-your-own-cab-series-table-of-contents)

# ExplorerView / ExplorerPresenter

The central concept in the user interface is the ‘ExplorerView’, a form with a simulation tree on the left and a right hand panel where model views are displayed. The associated ‘ExplorerPresenter’ is responsible for populating the controls on the view and for responding to input from the user. When the user selects a model in the simulation tree, an event handler is called in the presenter, which will in turn look for two reflection tags in the model.

```
[ViewName("UserInterface.Views.GridView")]
[PresenterName("UserInterface.Presenters.PropertyPresenter")]
```

The ViewName tag tells the presenter the full name (including the namespace) of the ‘view’ class to display on the screen. Each view class needs a corresponding presenter class and the PresenterName specifies this. With these two class names, the ExplorerPresenter can create instances of these and tell the ExplorerView to display the view in the right hand panel.

The presenter also maintains a ‘CommandHistory’ containing all executed commands and this is passed to each presenter that it creates so that they can create commands as required. This is done via the ‘Attach’ method in IPresenter.

```
namespace UserInterface.Presenters
{
    public interface IPresenter
    {
        void Attach(IModel Model, object View, CommandHistory CommandHistory);
    }
}
```

#Example Model / View / Presenter

The Axis model is a simple data container for storing properties associated with an axis on a graph. The data deserialised from the json looks like this:

```
	{
	  "$type": "Models.Axis, Models",
	  "Type": 3,
	  "Title": "Y axis title",
	}
```

The axis model source looks like this:

```
namespace Model.Components.Graph
{
    public class Axis
    {
        public enum AxisType { Left, Top, Right, Bottom };

        /// <summary>
        /// The 'type' of axis - left, top, right or bottom.
        /// </summary>
        public AxisType Type { get; set; }

        /// <summary>
        /// The title of the axis.
        /// </summary>
        public string Title { get; set; }
    }
}
```

This model has 2 properties, type and title.

The Axis view is very simple with a single text box that displays the axis title. The AxisPresenter that connects the model to the view looks like this:

```
using Model.Components.Graph;
using UserInterface.Views;

namespace UserInterface.Presenters
{
    /// <summary>
    /// This presenter connects an instance of a Model.Graph.Axis with a
    /// UserInterface.Views.AxisView
    /// </summary>
    class AxisPresenter : IPresenter
    {
        private Axis Axis;
        private IAxisView View;
        private CommandHistory CommandHistory;

        /// <summary>
        /// Attach the specified Model and View.
        /// </summary>
        public void Attach(object model, object view, CommandHistory commandHistory)
        {
            Axis = model as Axis;
            View = view as AxisView;
            CommandHistory = commandHistory;

            // Trap change event from the model.
            CommandHistory.ModelChanged += OnModelChanged;

            // Trap events from the view.
            View.OnTitleChanged += OnTitleChanged;

            // Tell the view to populate the axis.
            View.Populate(Axis.Title);
        }

        /// <summary>
        /// The 'Model' has changed so we need to update the 'View'.
        /// </summary>
        private void OnModelChanged(object Model)
        {
            if (Model == Axis)
                View.Populate(Axis.Title);
        }

        /// <summary>
        /// The user has changed the title field on the form. Need to tell the model this via
        /// executing a command.
        /// </summary>
        void OnTitleChanged(string NewText)
        {
            CommandHistory.Add(new Commands.ChangePropertyCommand(Axis, "Title", NewText));
        }
    }
}
```

In the Attach method, the Axis presenter traps the model’s OnChanged event (caused by an Undo) and the views OnTitleChanged event (caused by the user). It also tells the view to populate the text box with the value of the title property from the model. When the title changes in the model (OnChanged), the presenter tells the view the new title. When the view changes the title (in OnTitleChanged), the presenter tells the model the new title via a command so that this can be undone at a later time.

All views should have an interface (IAxisView) to decouple the view from the presenter that calls into it. This allows a presenter to use different implementations of a view.

---

## /usage/met/usingexcelforweatherdata/

Source: https://apsimnextgeneration.netlify.app/usage/met/usingexcelforweatherdata/
Title: Using Excel for weather data

# Using Excel for weather data

It is possible to store met data in an excel ‘.xlsx’ file. The format of the worksheet is represented below

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.ExcelWeather1.png)

Each excel file can contain multiple worksheets, and they don’t all need to contain met data. This allows for weather data to be combined with other relevant data, into the one file.

## Converting met data to the excel format:

- Copy and Paste the met data into excel. If your file doesn’t look like (ie, it is automatically split into columns), this then you may need to close excel and start again.

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.ExcelWeather2.png)

- Click on the cell that contains the ‘year’ (A8), hold down the Shift, Control and the Down Arrow to highlight all of the weather data.
- Click ‘DATA’ on the ribbon menu (at top), and select ‘Text to Columns’. Select ‘Delimited’, click Next, change delimiters to be ‘Space’, check that the Data preview looks correct, and then click Finish. The data should now look like the following.

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.ExcelWeather3.png)

- Measurements should be displayed after the heading which they apply to. The following shows how the data titles and measurements should look after they have been converted.

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.ExcelWeather4.png)

- Highlight from A1 to A6, click ‘Text to Clolumns’. Select ‘Delimited’, click Next, change delimiters to be ‘Other’, and type an equal (‘=’) in the space provided, and click Finish:

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.ExcelWeather5.png)

- Edit the ‘latitude’ and ‘longitude’ rows (3 and 4) so that the ‘(DECIMAL DEGREES)’ is moved to be after the title, and the values are on their own in column 2:

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.ExcelWeather6.png)

- Edit the ‘tav’ and ‘amp’ rows so that the measurement is displayed with the title (name), and that the commenting, including the exclamation (!) is in column 3. Column 2 should only contain the values.
- Note that tav and amp are optional - if not specified, APSIM will calculate them internally.

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.ExcelWeather7.png)

The worksheet should now be complete.

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.ExcelWeather8.png)

Note: when using the excel file in APSIM, the sheet name must be specified:

![Usage](https://apsimnextgeneration.netlify.app/images/Usage.ExcelWeather9.png)

---

## /usage/met/csvweather/

Source: https://apsimnextgeneration.netlify.app/usage/met/csvweather/
Title: Using a .csv file for weather data

# Using a .csv file for weather data

It is possible to use weather data stored in a csv file. When doing so, it is necessary to provide an extra plaintext file containing some constants. This document describes the format of the two files. For an example of an .apsimx file which uses a .csv file for its weather data, see the CsvWeather.apsimx example file which is provided with all apsim installations.

**Note that the constants file *must* contain a latitude.**

## Format of the .csv file

The .csv file must be [RFC 4180](https://tools.ietf.org/html/rfc4180)-compliant. The first row of the .csv file must contain the column names, and there is currently no support for specifying units. Expected units are:

- °C for temperatures
- MJ/m2 for radiation
- mm for rain
- hPa for pressure

An example .csv weather file might look like:

```
year,day,radn,maxt,mint,rain,pan,vp,code
1900,1,24.0,29.4,18.6,0.0,8.2,20.3,300070
1900,2,25.0,31.6,17.2,0.0,8.2,16.5,300070
1900,3,25.0,31.9,16.6,0.0,8.2,14.8,300070
```

## Format of the constants file

The constants file can be any plain text file with zero or more lines of the form:

constant_name = value

Units may optionally be specified in parentheses after the value. Any text after an exclamation mark (!) character are treated as a comment.

For example:

```
location = dalby
latitude = -27.18  (DECIMAL DEGREES)
longitude = 151.26  (DECIMAL DEGREES)
tav =  19.09 (oC) ! annual average ambient temperature
amp =  14.63 (oC) ! annual amplitude in mean monthly temperature
```

The only mandatory constant is latitude, however it can often be useful to provide others such as long-term averages for tav and amp.

---

## /usage/writemanagerscript/

Source: https://apsimnextgeneration.netlify.app/usage/writemanagerscript/
Title: Write Manager Scripts

# Write Manager Scripts

Writing manager scripts is for advanced users. **It is always much easier modifying an existing script that starting one from scratch.**. C# is a case sensitive language. Upper and lower case matters.

For this tutorial, we will be using the ‘Fertilise on fixed dates (advanced version)’ manager script in the management toolbox. There are a number of input parameters for this manager script:

![Properties](https://apsimnextgeneration.netlify.app/images/Usage.ManagerScript.Parameters.png)

The parameters for this script show a range of types (checkboxes, drop down, string array etc)

**Structure of a manager script.**

![Structure](https://apsimnextgeneration.netlify.app/images/Usage.ManagerScript.ScriptStructure.png)

**namespaces**

A namespace is a collection of classes. In the screenshot above, the *Models* namespace contains one class called *Script*. All c# classes must live in a namespace. APSIM manager scripts must be in a *Models* namespace.

**used namespaces**

C# manager scripts will need to reference other namespaces to be able to use classes in those namespaces. For example, the *Models.Core* namespace contains many APSIM definitions like *Link*, *Clock*, *Weather*. It is best to copy lists of namespaces from other scripts.

**class**

A class is collection of fields, properties, event handlers and methods. Classes encapsulate all the manager script functionality i.e. sowing on fixed dates in this example. Classes in manager scripts should always be ‘public’ i.e. callable from other models in APSIM. They should also derive from Model i.e. have a *: Model* at the end of the class line.

**links**

A link defines a dependancy on another model in APSIM. If your manager script needs the value of a variable from another model then you will need to add a link to that model. An example is getting the current simulation date from the clock model. Another example would be getting the maximum temperature from the weather model. The format for links is:

![Link](https://apsimnextgeneration.netlify.app/images/Usage.ManagerScript.ScriptStructure.Link.png)

*Model type* is the class name of the model. *Variable name* is the name of the variable that clock will be known as in the manager script. For PMF models, the *Model type* will be *Plant* while the *Variable name* could be *wheat*. For AgPasture, the *Model type* will be *PastureSpecies* and the *Variable name* could be *AGPRyegrass*. If there is a model in the simulation tree, then a manager script can link to it. If you hover the mouse over the model in the simulation tree, the tool tip will show the *Model type*. The name of the model in the simulation tree will be the *Variable name*.

**fields**

Quite often a manager script will need to define fields (variables) that are private to the class i.e. cannot be accessed by another model in the simulation. The format for private fields is:

![Link](https://apsimnextgeneration.netlify.app/images/Usage.ManagerScript.ScriptStructure.Field.png)

*Data type* is the type of variable e.g.

- int: an integer variable with no decimal places,
- double: a variable with decimal places,
- string: a variable that can contain characters,
- DateTime: a variable that can contain a date and/or time,

```
These data types can also be arrays i.e. by appending
[]
 to the end of the type e.g.
double[]
 for an array of double.
Variable name
 is the name that the variable will be known as in the manager script.
```

**properties**

Properties are often used as placeholders for mapping of values from the user-input *parameters* tab and for publically available outputs that can be reported from a script.

![Link](https://apsimnextgeneration.netlify.app/images/Usage.ManagerScript.ScriptStructure.Property.png)

- They are formatted the same as for field but with *{get; set;}* appended to them. The same data types are supported.
- If they are to be used for user-input parameters then they need to have a *[Description]* attribute, the text of which appears in the *Parameters* tab.
- They can optionally have a *[Separator]* attribute to define a visual separator on the *Parameters* tab.
- If the *DataType* is an enum then a drop down list will be shown to the user. For example defining `enum DropDownMembers { A, B, C, D }` and then using this DataType in the property will cause the user interface to show a drop down list of A, B, C, D.
- They can optionally have a *[Display]* attribute that instructs the user interface to show format the user-input cell in different ways. Examples of using this attribute:
  - [Display(Type=DisplayType.TableName)]: The user interface will show a drop down list of tables in the datastore.
  - [Display(Type=DisplayType.FieldName)]: Ther user interface will show a drop down list of fields (columns) in the table specified by a table property in the same script.
  - [Display(Type=DisplayType.FileName)]: The user interface will show a browse button to let user select a file.
  - [Display(Type=DisplayType.CultivarName,Plant=“Wheat”)]: The user interface will show a drop down list of cultivars for the specified plant model.
  - [Display(Type=DisplayType.ResidueName)]: The user interface will show a drop down list of residue types from the surface organic matter modle.
  - [Display(Type=DisplayType.Model)]: The user interface will show a drop down list of all models in scope.
  - [Display(Type=DisplayType.Model,ModelType=typeof(Plant))]: The user interface will show a drop down list of all plant model in scope.

**methods**

Methods (functions) are where lines of code are put to perform calculations.

![Link](https://apsimnextgeneration.netlify.app/images/Usage.ManagerScript.ScriptStructure.Method.png)

Methods can return the value of a single variable. The data type of the return variable is specified by *Return type* in the image above. It can be void, meaning the method returns nothing, or the method can return a variable of one of the data types listed for fields above. Arguments of the method are varaibles that are passed into the method to be used by the method. They are comma separated `DataType VariableName` format similar to fields. Most methods in manager scripts are private i.e. are not callable from other models in APSIM. They can be declared public if necssary.

If a method has a *[EventSubscribe]* attribute, like the image above, then APSIM (usually the clock model) will call this method when the event specified is invoked. In the example above, when the clock model publises a *StartOfSimulation* event at the beginning of each simulation run, this method will be called. This is a good place for performing script initialisation. Clock also publishes *DoManagement* at the beginning of each day (before other models do their daily calculations) and *DoManagementCalculations* at the end of each day (after all other models have completed there calculations). Many manager scripts subscribe to these events.

---

## /usage/documentationtutorial/

Source: https://apsimnextgeneration.netlify.app/usage/documentationtutorial/
Title: Writing Documentation for Models

# Writing Documentation for Models

Created 21/10/2024 - Last updated 21/10/2024

## APSIM Documentation System

As of October 2024, the APSIM Documentation system has been rebuilt into a centralised library called APSIM.Documentation, that removes all the C# documentation code of models from the Document() function that used to exist in each model’s class.

The code for generating documentation is wrapped up within the `AutoDocumentation` class, which is now the main access point for any generation of docs. The entrypoint for the class is the static AutoDocumentation.Document(`IModel`) function that takes an APSIM model and produces all the required documentation for it. To run documentation over an entire apsimx file, the root `Simulations` model is passed to this function.

### Documenting a C# Class

```
By default all C# classes that are a type of
IModel
 are documented using a
DocGeneric
 class that outputs the name of the model, any summary or remarks in the C# class, and the contents of any
Memo
 children that the class has. For classes that have specific documentation requirements that need more than that, a
Doc[ModelName]
 class is created and linked to be used instead. For example, to document
Leaf
, a class called
DocLeaf
 is used instead of the
DocGeneric
 class. All the custom documentation classes are a subclass of
DocGeneric
 and most will first document title, summary, remarks and memos before adding additional information in order to maintain consistency across the documentation.
```

Model Classes are not linked to Documentation Class by name, instead a dictionary called documentMap within `AutoDocumentation` is used which tells the program which models use which documentation classes. Models not listed in the dictionary will use the `DocGeneric` class. Model documentation classes are all stored within APSIM.Documentation/Models/Types, and always in the format `Doc[ModelName]`.

AutoDocumention works by generating a tags structure, where elements are converted into approiate tags, then placed within sections for structuring the document. Only sections can hold other tags, as they are used to define headings and sub headings in the documents.

#### Tags:

- Section: Displays a title and holds child tags
- Paragraph: Displays text
- Table: Holds a DataTable which is shown as a table
- Image: Displays an Image
- Graph: Displays a Graph
- GraphPage: Displays multiple graphs on a page

To develop a new class documentation, the easist way is to copy an existing an documentation class and rename it, link it to the model class and then edit the Document() function to display the information required. Most documentation will begin with a called to make a summary and remarks section, which can be filled out using summary and remarks tags at the top of the C# class file.

```
    Section section = GetSummaryAndRemarksSection(model);
```

After entering all the content that you require in the documentation, the function then needs to return the tag structure. Sections will be numbered based on the structure of the tags, with sibling sections incrementing the current number, and child sections adding a subpoint to the heading number.

Formatting from memos is also read into the section structure, so if there are unintended section breaks and numbering, check if the content is coming from memos that have been written.

A simple documentation class looks like this example:

**DocMyModelClass.cs** ( Stored under APSIM.Documentation/Models/Types/ )

```
using System.Collections.Generic;
using APSIM.Shared.Documentation;
using Models.Core;

namespace APSIM.Documentation.Models.Types
{

    /// <summary>
    /// Documentation class for MyModelClass
    /// </summary>
    public class DocMyModelClass : DocGeneric
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="DocMyModelClass" /> class.
        /// </summary>
        public DocMyModelClass(IModel model) : base(model) { }

        /// <summary>
        /// Document the model.
        /// </summary>
        public override List<ITag> Document(int none = 0)
        {
            Section section = GetSummaryAndRemarksSection(model);

            Section customSection = new Section("My Custom Section");
            customSection.Add(new Paragraph("A Paragraph of Text"));
            customSection.Add(new Paragraph("A 2nd Paragraph of Text"));

            return new List<ITag>() {section, customSection};
        }
    }
}
```

Then add a link to the documentation class in AutoDocumentation.cs:

**AutoDocumentation.cs** ( Approximately Lines 49-57 )

```
/// <summary>Returns a dictionary to match model classes to document class.</summary>
private static Dictionary<Type, Type> DefineFunctions()
{
    Dictionary<Type, Type> documentMap = new()
    {
        {typeof(MyModelClass), typeof(DocMyModelClass)},
        {typeof(Plant), typeof(DocPlant)},
        {typeof(PastureSpecies), typeof(DocPlant)},
        {typeof(Sugarcane), typeof(DocPlant)},
```

### Documenting a Plant Model

Plant models are kept in .json resource files under Models/Resources/ and provide the structure of models used within APSIM. The custom DocPlant documentation class will investigate and pull out information about a plant when documentation is generated for a Plant and the json resource has been loaded, such as when selecting to create documentation from the context menu in the GUI, or when creating a validation documentation from a apsimx file in the Tests/Validation folder.

As long as your plant model is of type `Plant`, it will use the DocPlant documentation class with the following details. If you instead have a model like `Sugarcane`, it will have to be manually linked to DocPlant in the AutoDocumentation dictionary and tested that it has all the correct components to display.

**Plant Documentation Sections** 1. Memos: All content from memos at the top of the resource file. 2. Plant Model Components: A table list of all the components that make up the plant and the types they have. 3. Composite Biomass: A table list of the all the composite biomass models that the plant has. 4. Cultivars: A table list of all the available cultivars and any alternative names (alias) that they have. 5. Child Components: Generated Documentation for each of the Child Components (excluding composite biomass models). 6. Biblography: List of references used in the document.

When making a new plant model, it is important to generate the documentation for your plant and make sure the information that it produces is correct and that sections are not missing. You should not need to make changes to the DocPlant class for a new plant model, and it is up to the author to include memos in their model to decribe how it was developed and can be used.

### Documenting a Validation Set

In the current build system, model documentation is generated for this website when testing a new build. To make this, a list of preselected apsimx files under Tests/Validation/ are used to generate the required documents. This is achieved by documenting the root Simulations node for that file, which has a special case in DocSimulations for apsimx files within that directory.

For those files, any memos attached to the Simulations node are shown, then the documentation of the plant model that matches the file’s name, followed by information about the experiments and simulation that it contains. It will also render out any graphs under folders that have been set to appear in documentation, showing the results of those validation comparisions.

Currently there is no way to use the commandline to generate documentation of a single apsimx file, this functionality is wrapped up in the APSIM.Documentation program.

### Documenting a Tutorial

In the current build system, tutorials are generated for this website when testing a new build. To make this, a list of preselected apsimx files under Examples/Tutorials/ are used to generate the required documents. This is achieved by documenting the root Simulations node for that file, which has a special case in DocSimulations for tutorial files.

Tutorial content is written in memos within an apsimx file, so when generating a document, DocSimulations has a special case for tutorials so that it only pulls out the Memos, Simulations, folders and graphs, with the main aim to only include sections that help the user follow the tutorial instructions.

To create a new tutorial, first build an apsim file with a memo attached to Simulations, and save in within the Examples/Tutorial folder. Fill out the memo with all the details that you need for the tutorial, including text, pictures, headings etc, written in markdown. Lastly to have the tutorial get generated for display on the website, edit it in as a row into APSIM.Documentation/Progam.cs, using one of the existing tutorials as a reference.

*Note: If you found any incorrect/outdated information in this tutorial. Please let us know on GitHub by [submitting an issue.](https://www.github.com/APSIMInitiative/ApsimX/issues/new/choose/)*
