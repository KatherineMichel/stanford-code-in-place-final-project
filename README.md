# Stanford Code in Place Final Project

## Simba Friends Twitter Bot

![](simba.png)

Simba; Photo Credit: Chris Piech

[Simba Friends Bot](https://twitter.com/SimbaFriendsBot) was inspired by Simba, the adorable Stanford Code in Place dog. Using [Python](https://www.python.org/) programming language and [Requests](https://requests.readthedocs.io/en/master/), [Pillow](https://pillow.readthedocs.io/en/stable/), and [Twython](https://twython.readthedocs.io/en/latest/) libraries, I created a [program](photo.py) that downloads a random pet photo from the Unsplash curated "[Personable Pets](https://unsplash.com/collections/2489501/personable-pets)" collection, modifies it with a randomly chosen image filter algorithm, and tweets the image on the [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) Twitter account. 

### GitHub Actions Proof of Concept

Initially, I got the bot working locally. But my stretch goal was to figure out how to run the bot solely via [GitHub Actions](https://github.com/features/actions). I wasn't sure if this was even possible, because a photo would need to be downloaded, modified, saved, and tweeted via a GitHub Actions `$GITHUB_WORKSPACE` for all of this to work. Amazingly, I was able to create a successful proof of concept!

Table of Contents
-----------------

* [Image Filter Algorithm Examples](#image-filter-algorithm-examples)
* [My Favorite Example So Far](#my-favorite-example-so-far)
* [How The Program and GitHub Actions Workflow Work](#how-the-program-and-github-actions-workflow-work)
* [Local Environment Versus GitHub Actions Environment](#local-environment-versus-github-actions-environment)
  * [I Prefer GitHub Actions](#i-prefer-github-actions)
* [Project Set Up](#project-set-up)
  * [Create a Twitter Developer Account](#create-a-twitter-developer-account)
  * [GitHub Actions Set Up](#github-actions-set-up)
  * [Local Set Up](#local-set-up)
* [Milestones](#milestones)
  * [Milestone 1- Download the Image](#milestone-1--download-the-image)
  * [Milestone 2- Modify the Image](#milestone-2--modify-the-image)
  * [Milestone 3- Tweet the Image](#milestone-3--tweet-the-image)
  * [Milestone 4- Run the Bot via GitHub Actions (Proof of Concept)](#milestone-4--run-the-bot-via-github-actions-proof-of-concept)
  * [Milestone 5- Publicize](#milestone-5--publicize)
  * [Milestone 6- Submit Assignment](#milestone-6--submit-assignment)
* [Video Agenda](#video-agenda)
* [Possible Enhancements](#possible-enhancements)

## Image Filter Algorithm Examples

This Jalitha Hewage [photo](https://unsplash.com/photos/_NL4b8hfOww) is used for this demo. 

### No Change

![](demo-photos/jalitha-hewage-_NL4b8hfOww-unsplash.jpg)

### Black and White

![](demo-photos/black-and-white.jpg)

### Sepia

![](demo-photos/sepia.jpg)

### Gaussian Blur

`radius` set to 2

![](demo-photos/gaussian-blur-2.jpg)

`radius` set to 4

![](demo-photos/gaussian-blur-4.jpg)

### Unsharp Mask

`radius` set to 6

![](demo-photos/unsharp-mask-6.jpg)

### Kernel

![](demo-photos/kernel.jpg)

### Negative

![](demo-photos/negative.jpg)

:top: <sub>[**Back to Top**](#table-of-contents)</sub>

## My Favorite Example So Far

As I've been watching the [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) Twitter account tweet images, one photo in particular has been my absolute favorite so far. While most of the other photos modified by the `negative_algorithm()` have been downright creepy, the negative version of this Karina Vorozheeva [photo](https://unsplash.com/photos/rW-I87aPY5Y) is breathtaking. It's one of the most beautiful images I've ever seen. 

Original photo

![](demo-photos/karina-vorozheeva-rW-I87aPY5Y-unsplash.jpg)

Negative version that was tweeted

![](demo-photos/favorite-negative.jpg)

Black and white version that was tweeted

![](demo-photos/favorite-black-and-white.jpg)

:top: <sub>[**Back to Top**](#table-of-contents)</sub>

## How the Program and GitHub Actions Workflow Work

To better understand how the program works, read the comments in the [program](photo.py) or read the [Milestones](#milestones) section. To better understand how the GitHub Actions "Process Photo" workflow works, read the comments in the [workflow](.github/workflows/process-photo.yml) file.

:top: <sub>[**Back to Top**](#table-of-contents)</sub>

## Local Environment Versus GitHub Actions Environment

Regardless of whether the program is run locally or via GitHub Actions, a development environment needs to exist that has all of the software installed that is needed to run the program.

Something I learned from working through this project is that a GitHub Actions development environment can replicate a local development environment. 

In both my local development environment and GitHub Actions development environment, [Python 3.8](https://www.python.org/downloads/release/python-380/) is used by default, [pip](https://pypi.org/project/pip/) is installed, and the [Requests](https://requests.readthedocs.io/en/master/), [Pillow](https://pillow.readthedocs.io/en/stable/), and [Twython](https://twython.readthedocs.io/en/latest/) libraries are installed as dependencies used by the project. The repo master branch is accessed, the environment variables are available, and the program is run by calling  `python photo.py`.

The Python and third-party libraries required to run the program are imported, the environment variables are passed into Twython, and Python 3.8 interprets the `photo.py` file.

### I Prefer GitHub Actions

After running the program both locally and via GitHub Actions, I prefer using GitHub Actions. Although a major GitHub Actions outage occurred while I was working on this project, GitHub Actions is improving over time. It feels like a luxury to avoid setting up and managing a longterm project in a local environment.
    
:top: <sub>[**Back to Top**](#table-of-contents)</sub>
    
## Project Set Up

There are a couple important set up steps to make this project work:

* Create a Twitter Developer account, create an app in the account, and obtain the app "secrets" needed to use the Twitter API to programatically [authenticate](https://twython.readthedocs.io/en/latest/usage/starting_out.html#authentication) into Twitter and tweet from the account
* Designate an event or cron schedule as a trigger for the program to be run

### Create a Twitter Developer Account

Following the instructions of the [Twitter Developer](https://developer.twitter.com/) docs, I created the [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) Twitter account, including verifying a phone number. Using that account, I created a Twitter Developer account under the "Hobbyist" category, choosing "Making a bot" as my task.

In my "Simba and Friends Bot" app, I clicked on the "Keys and tokens" tab. Here I obtained the secrets that would need to be passed into `Twython` as environment variables.

* API key a.k.a `APP_KEY`
* API secret key a.k.a. `APP_SECRET`
* Access token a.k.a `OAUTH_TOKEN`
* Access token secret a.k.a `OAUTH_TOKEN_SECRET`

### GitHub Actions Set Up

There are two steps to setting [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) up in a GitHub repo:

#### Store Secrets

The secrets can be stored in the repo settings as [encrypted secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) and made available to the program by variables in the GitHub Actions workflow file. Click on the "Settings" tab, then "Secrets". Click on "New secret", entering the environment variable name and value, then "Add secret". Do this four times, once for each secret. 

#### Set Up the Event

An [event](https://help.github.com/en/actions/reference/events-that-trigger-workflows) needs to happen to trigger the GitHub Action workflow to run the program. The Simba Friends Bot GitHub Action workflow is set up to trigger after a "[push](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestbranchestags)" to the GitHub branch, or based on a [cron schedule](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#onschedule) that causes the GitHub Action to be run at certain times of day. Whichever one is not being used can be commented out.

```yaml
on:
  push:
    branches: [ master ]

on:
  schedule:
    # This line can be altered to change the schedule; in this example, the cron job will run every 10 minutes
    - cron: '*/10 * * * *'
```

### Local Set Up

For local setup, I cloned the repository, changed directory into it, and created a virtual environment. I then used the terminal to `export` the environment variables, so they could be accessed by the program. 

```bash
$ export APP_KEY="<app-key>"
$ export APP_SECRET="<app-secret>"
$ export OAUTH_TOKEN="<oauth-token>"
$ export OAUTH_TOKEN_SECRET="<oauth-token-secret>"
```

I ran the program via the terminal and used the error info to debug. Once the program was working properly, I pushed the code back to GitHub and used GitHub Actions. Had GitHub Actions not worked, I would have created a local [cron job](https://en.wikipedia.org/wiki/Cron) to run the program on a schedule. 

:top: <sub>[**Back to Top**](#table-of-contents)</sub>

## Milestones

In our assignment instructions, it was suggested that we use milestones. These were my project milestones:

### Milestone 1- Download the Image

* At this time, the "Personable Pets" collection contains 278 images
* An individual image in the collection can be identified using the collection ID and file number
* Use `randrange()` function to choose a random `file_number` between 1 and 278, inclusive
* Create a string using the collection URL and ID and insert the `file_number` at the end
* Use the Requests library to download the image (optionally, use a `photos/` directory)
* Open the image using the Pillow library and show the image locally before transformation

### Milestone 2- Modify the Image

* Unfortunately, Twython, Pillow, and SimpleImage were not compatible, so I used Pillow directly
* Pass a list of image filter algorithms into `random.choice()` to randomly choose an algorithm
* The chosen image filter algorithm function will be called, passing in the `new_image` and `file_path`
* After the algorithm is applied, `save_image()` function will be called to save and return the modified image
* Optionally, uncomment `modified_image.show()` to show the image locally after transformation

### Milestone 3- Tweet the Image

* Open the modified image
* Using Twython, upload and tweet the modified image, optionally with a `status` message
* Call the `remove_file()` function to delete the image
* Check your terminal and the associated Twitter account to verify tweet posted! 

### Milestone 4- Run the Bot via GitHub Actions (Proof of Concept)

* Create a GitHub Action that can run the program solely via GitHub

### Milestone 5- Publicize

* Create a README.md with instructions for how to use the code
* Create a blog post for fun, explaining how to set up this bot
* Share my project with friends, family, and colleagues :)

### Milestone 6- Submit Assignment

* Make assignment video and submit assignment :)
* Sit back, drink some tea, and enjoy some cute pet photos at [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) Twitter account.

:top: <sub>[**Back to Top**](#table-of-contents)</sub>

## Video Agenda

* Introduction (what project is about)
* Show image filter algorithm examples and favorite example so far
* Explain how `photo.py` file works
* Explain how GitHub Action workflow file works (preferred method)
* Show local development example in comparison
* Show Actions tab build info
* Show Twitter account

:top: <sub>[**Back to Top**](#table-of-contents)</sub>

## Possible Enhancements

* Add PyPI packaging configurations to the GitHub repo where the code is hosted
* Create a GitHub Action that can auto-publish the package when a release is tagged on GitHub; tag the release and verify published to PyPI
* Create the option to publish to the PyPI test instance first
* Add a proper Change Log
* Add a photographer credit (not required by Unsplash) as the status update
* Add additional image filter algorithms (ex. blue or red filter)
* Create an `if` `else` statement to check if a photo exists before downloading (in case of an error that caused a photo to be downloaded, but not deleted; this might be irrelevant for GitHub Actions, if the workspace is destroyed after it runs

:top: <sub>[**Back to Top**](#table-of-contents)</sub>
