# flask-sheets-starter-2023

This is an example full stack web application built in Python with the Flask framework. This application implements Google Login and interfaces with a Google Sheets datastore.


## Setup

### Prerequisites

To run this app, you'll need to have Anaconda, Python, and Pip installed (specifically Python version 3.10+).

### Installation

Make a copy of the repository from GitHub, as necessary. Clone your copy of the repo onto your local computer, for example onto your Desktop.

Navigate to the local repository from the command line, for example if on the Desktop:

```sh
cd ~/Desktop/hoya-store
```

> NOTE: it is important to navigate to the root directory before running many of the commands below.


Create new virtual environment (first time only):

```sh
conda create -n hoya-store python=3.10
```

Activate the virtual environment (first time, or whenever you return to the project):

```sh
conda activate hoya-store
```

> NOTE: it is important to activate the virual environment before running any of the commands below.

Install package dependencies (first time only):

```sh
pip install -r requirements.txt
```

### Services

Follow these guides to setup the various cloud services required by this application:

  + [Google Cloud](/setup/GOOGLE_CLOUD.md):
    + [Google Login](/setup/GOOGLE_LOGIN.md)
    + [Google APIs](/setup/GOOGLE_APIS.md)
    + [Google Sheets Datastore](/setup/GOOGLE_SHEETS.md)

## Configuration

Create a new file called ".env" in the root directory of this local repository, and place inside contents like the following:

```sh
# this is the ".env" file...

# for flask:
FLASK_APP="web_app"

# for google analytics (optional):
# GA_TRACKER_ID="G-____________"

# for google login:
GOOGLE_CLIENT_ID="___________"
GOOGLE_CLIENT_SECRET="___________"

# for google sheets:
GOOGLE_SHEETS_DOCUMENT_ID="___________"
```

> NOTE: when you push your repository to GitHub, the ".env" file does not show up - this is desired behavior, as designated by the ".gitignore" file, to prevent our secret credentials stored in the ".env" file from being uploaded or exposed on GitHub.

# Contact Form

> In order to configure contact form used in the 'About' Section, please refer to the following tutorial: https://github.com/prof-rossetti/internet-technologies/blob/main/notes/formspree.md  

## Usage

Run the web application (then view in the browser at localhost:5000):

```sh
#fetch data from the google sheets
python -m web_app.services.sheets 
flask run
```

## [Deploying](/setup/RENDER.md)
