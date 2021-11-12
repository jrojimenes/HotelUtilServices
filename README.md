# fastapi-template
After your initial project generation has completed, you can view your app on PCF by going to your PCF URL. Log in to https://login.sys.pp01.edc1.cf.ford.com/login, select the space and look for the app you deployed. The route(URL) will be will be listed in the last column next to your app name.

# First Time Setup
## Github
1. To take advantage of the project template Dev Central Station has provided, you will need Git. Git can be found [here](https://git-scm.com/downloads).
2. In your Github repo, locate the project you just created:

    a. Click the green button in the upper right corner that says "Clone or Download".
    
    b. Copy the link provided, it should look something like ```git@github.ford.com:RepoOrgName/Generated project name.git```. For help setting up your authentication to GitHub for the first time, please follow the directions found [here](https://github.ford.com/DevEnablement/pcfdev-guides/blob/master/git/GitConfiguration.md)
    
3. On your computer, open a terminal window and type ````git clone```` and the paste the link you copied above all in one line - this will clone your repo locally
4. Open your favorite IDE and navigate to the Github folder you just downloaded and open it. For help pushing your code to your Github repo or to PCF, scroll to the "Commit and push your code" section below

## Pipenv

[pipenv](pipenv.pypa.io) is a python package management tool that builds on top of `pip`. It installs packages from the same place as `pip` (pypi.org). Its main benefit over pip is that it also handles virtual environment management and dependency pinning. _real python_, an awesome website with great python tutorials, has a [pipenv tutorial](https://realpython.com/pipenv-guide/) that will probably be useful for anyone picking up pipenv for the first time.

### MacOS Pipenv setup

`brew install pipenv`

### linux Pipenv setup

1. [Install `pyenv`](https://github.com/pyenv/pyenv-installer#installation--update--uninstallation)
2. Install python 3.7 w/ pyenv: `pyenv install 3.7.7 && pyenv global 3.7.7`
3. Install pipenv: `python3.7 -m pip install pipenv`

`python3 -m pip install pipenv`

### windows pipenv setup

1. [Install python3.7](https://www.python.org/downloads/release/python-377/)
2. `py -3.7 -m pip install pipenv`

note: windows is a bit tricky, due to path issues. The python.org python installer doesn't add everything to your path that you would normally expect. For that reason, you will probably need to run `py -3.7 -m pipenv <commands...>`.

## {pipenv_cmd}

Due to differences between various operating systems, the preferred way of invoking CLI packages like pipenv will be different. Here are some ways to invoke pipenv in different OSes:

### 🍎 {pipenv_cmd}

If you used `brew` to install pipenv, you can just invoke pipenv as below:

`pipenv <args>`

### 🐧 {pipenv_cmd}

`pipenv` might be on your path, but if you installed it into one of your `pyenv` environments, you'll need to invoke it as below:

`python3.7 -m pipenv <args>`

### windows {pipenv_cmd}

If you installed pipenv into a python.org python installation, you might need to invoke it as below:

`py -3.7 -m pipenv <args>`

## Installing dependencies

To install this project's dependencies, navigate to the root folder and run

```bash
{pipenv_cmd} install --dev
```

note: `{pipenv_cmd}` [depends on your OS / pipenv installation](#-pipenv_cmd)

## Every time you open a terminal

Once you've [created your virtual environment with pipenv](#installing-dependencies), pipenv provides a helper command for "activating" your virtual environment

```bash
{pipenv_cmd} shell
```

## Adding new packages

You _can_ `pip install` after activating your pipenv environment, but then you'll need to manually edit your Pipfile if you want to track those changes. For that reason, it's better to use the `pipenv install` command again. For example, to install pandas-1., I would run

```bash
{pipenv_cmd} install "pandas>0,<2"
```

The `pipenv install` command (👆) will install the specified package / packages, and add it to your 


# Run a local version

Run the fastapi app:

```bash
pipenv run uvicorn app.main:app
```

# Run tests
Execute all tests:

```pipenv run python -m pytest```

# Commit and push your code
In order to push your code to PCF, Open the terminal in your IDE and use the Git commands. If you do not have git installed, you can find it [here](https://git-scm.com/downloads).
1. Type ```git add -p``` to review changes and accept or reject each. Alternatively, you could choose to use ```git add .``` to add all changes without review.
2. Once your changes have been reviewed, type ```git commit -m "Some message about what code you changed"```
3. Type ```git pull``` to grab the latest code from your Github repository
4. Type ```git push``` to deploy your code to PCF
5. To check the status or progress of your build, navigate to the DCS Shared pipeline by going [here](https://dcs-jenkins-quartermaster.jenkins.app.caas.ford.com/job/45%20Day%20Jenkins%20Jobs/) and locating your team folder. 
6. To check your app on PCF, log in to https://login.sys.pp01.edc1.cf.ford.com/login, select the space and look for the app you deployed. The route(URL) will be will be listed in the last column next to your app name.

# openapi (swagger) docs

You'll find swagger docs at `{api_url}/docs`

# Contact Us
Need to notify us of a bug, have issues, new feature request or simply want to brag? Join the /d/c/s Community Channels!
- [Dev/Central/Station Slack](https://app.slack.com/client/T5V3ZFCD6/C9L83E6DQ)
- [Dev/Central/Station Webex Teams](https://www.webexteams.ford.com/space?r=fz8y)
