# Stanford Code in Place Final Project

## Simba Friends Twitter Bot

![](simba.png)

Simba; Photo Credit: Chris Piech

[Simba Friends Bot](https://twitter.com/SimbaFriendsBot) was inspired by Simba, the adorable Stanford Code in Place dog. Using [Python](https://www.python.org/) programming language and [Requests](https://requests.readthedocs.io/en/master/), [Pillow](https://pillow.readthedocs.io/en/stable/), and [Twython](https://twython.readthedocs.io/en/latest/) libraries, I created a [program](photo.py) that downloads a random pet photo from the Unsplash curated "[Personable Pets](https://unsplash.com/collections/2489501/personable-pets)" collection, modifies it with a randomly chosen image filter algorithm, and tweets the photo on the [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) Twitter account. 

### GitHub Actions Proof of Concept

Initially, I got the bot working locally. But my stretch goal was to figure out how to run the bot solely via [GitHub Actions](https://github.com/features/actions). I wasn't sure if this was even possible, because a photo would need to be downloaded, modified, saved, and tweeted via a GitHub Actions `$GITHUB_WORKSPACE` for all of this to work. Amazingly, I was able to create a successful proof of concept!

Table of Contents
-----------------

* [Set Up](#set-up)
  * [Create a Twitter Developer Account](#create-a-twitter-developer-account)
  * [GitHub Actions Set Up](#github-actions-setup-up)
  * [Local Set Up](#local-set-up)
* [Image Filter Algorithms](#image-filter-algorithms)
* [How the Program Works](#how-the-program-works)
  * [Program Steps Summary](#program-steps-summary)
* [Milestones](#milestones)
  * [Milestone 1- Download the Image](#milestone-1--download-the-image)
  * [Milestone 2- Modify the Image](#milestone-2--modify-the-image)
  * [Milestone 3- Tweet the Image](#milestone-3--tweet-the-image)
  * [Milestone 4- Run the Bot via GitHub Actions (Proof of Concept)](#milestone-4--run-the-bot-via-github-actions-proof-of-concept)
  * [Milestone 5- Publish and Publicize](#milestone-5--publish-and-publicize)
  * [Milestone 6- Submit](#milestone-6--submit)
* [Possible Enhancements](#possible-enhancements)

## Set Up

After using the bot both locally and via GitHub Actions, I personally prefer using it via GitHub Actions. GitHub Actions is more stable than ever and it's a luxury to avoid the messiness of setting up and managing a local environment.

### Create a Twitter Developer Account

Following the instructions of the Twitter Developer docs, I created the [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) Twitter account, including verifying a phone number. Using that account, I created a Twitter Developer account under the "Hobbyist" category, choosing "Making a bot" as my task.

In my "Simba and Friends Bot" app, I clicked on the "Keys and tokens" tab. Here I obtained the "secrets" that would need to be passed into `Twython` as environmental variables in order to programatically [authenticate](https://twython.readthedocs.io/en/latest/usage/starting_out.html#authentication) into Twitter and tweet.

* API key a.k.a `APP_KEY`
* API secret key a.k.a. `APP_SECRET`
* Access token a.k.a `OAUTH_TOKEN`
* Access token secret a.k.a `OAUTH_TOKEN_SECRET`

### GitHub Actions Set Up

There are two steps to setting [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) up in a GitHub repo. 

#### Store Secrets

The secrets can be stored int he repo settings as [encrypted secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets), to be accessed by the program via GitHub Actions variables. Click on the "Settings" tab, then "Secrets". Click on "New secret", entering the environmental variable name and value, then "Add secret". Do this four times, once for each secret. 

#### Set Up the Event

An [event](https://help.github.com/en/actions/reference/events-that-trigger-workflows) needs to happen to trigger the GitHub Action workflow to run the program. The Simba Friends Bot GitHub Action workflow is set up to trigger after a "[push](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#onpushpull_requestbranchestags)" to the GitHub branch, or based on a [cron schedule](https://help.github.com/en/actions/reference/workflow-syntax-for-github-actions#onschedule) that causes the GitHub Action to be run at certain times of day. Whichever one is not being used can be commented out.

### Local Setup

For local setup, I cloned the repository, changed directory into it, and created a virtual environment. I then used the terminal to `export` the environmental variables, so they could be accessed by the program. 

```bash
$ export APP_KEY="<app-key>"
$ export APP_SECRET="<app-secret>"
$ export OAUTH_TOKEN="<oauth-token>"
$ export OAUTH_TOKEN_SECRET="<oauth-token-secret>"
```

I ran the program via the terminal and used the error info to debug. Once the program was working properly, had I not used GitHub Actions, I would have created a local cron job to run the program on a schedule. 

## Image Filter Algorithms

* Black and white
* No change

## How This Program Works

### Program Steps Summary

* Download a random image from an Unsplash curated "Personable Pets" collection
* Randomly choose an image filter algorithm from a list
* Call that image filter algorithm function to apply the filter to the image
* Tweet the modified image to a Simba Friends Bot Twitter account, using the Twitter API and Twython
* Delete the image

## Milestones

In our assignment instructions, it was suggested that we use milestones. These were my project milestones.

### Milestone 1- Download the Image

* At this time, the "Personable Pets" collection contains 278 images
* An individual image in the collection can be identified using the collection ID and file number
* Use `randrange()` function to choose a random `file_number` between 1 and 278, inclusive
* Create a string using the collection URL and ID and insert the `file_number` at the end
* Use the Requests library to download the image (optionally, use a `photos/` directory)
* Open the image using the Pillow library and show the image locally before transformation

### Milestone 2- Modify the Image

* Unfortunately, Twython, Pillow, and SimpleImage were not compatible, so I used Pillow directly
* My SimpleImage algorithms are commented out at the bottom of this file
* Pass list of image filter algorithms into `random.choice()` to randomly choose an algorithm
* The chosen image filter algorithm function will be called, passing in the `new_image` and `file_path`
* After the algorithm is applied, `save_image()` function will be called to save and return the modified image
* Optionally, uncomment `modified_image.show()` to show the image locally after transformation

### Milestone 3- Tweet the Image

* Open the modified image
* Using Twython, upload and tweet the modified image, optionally with a `status` message
* Call the `remove_file()` function to delete the image
* Check your terminal and the associated Twitter account to verify tweet posted! 

### Milestone 4- Run the Bot via GitHub Actions (Proof of Concept)

* Create a GitHub Action that can cache the downloaded photo so the bot can be run from GitHub

### Milestone 5- Publish

* Add PyPI packaging configurations to the GitHub repo where the code is hosted
* Create a GitHub Action that can auto-publish the package when a release is tagged on GitHub
* Tag the release and verify published to PyPI

### Milestone 6- Publicize

* Create a README.md with instructions for how to use the code
* Create a blog post for fun, explaining how to set up this bot
* Share my project with friends, family, and colleagues :)

### Milestone 7- Submit Assignment

* Make assignment video and submit assignment :)
* Sit back, drink some tea, and enjoy some cute pet photos at [Simba Friends Bot](https://twitter.com/SimbaFriendsBot) Twitter account.

## Possible Enhancements

* Add a photographer credit (not required by Unsplash) as the status update
