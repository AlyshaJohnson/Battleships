# Battleships

Purpose:

Aim:

![Responsive Mockup](<directory to image>)

## 1. Design and Development

For the design of this <application>, the 5 pillars of User Experience Design (UXD) were used to cover the strategy, scope, structure, skeleton and surface to make sure the design is intuitive, simple and enjoyable.

### 1.1 Strategy

The target user audience…

Interviews and workshops with users and stakeholders were conducted to understand their requirements and perspectives.

Research was conducted …

### 1.2 Scope

From the research and interviews conducted with the target audience and stakeholders, user stories were created to determine the flow of the app. The focus was put on the following user stories:

![User Stories 1 - 3](<insert image location>)
![User Stories 4 - 5](<insert image location>)

### 1.3 Structure

From the user stories, content, data, features and functionality can be determined.

**For the content:**


**For the data:**


**For the features / functionality:**


### 1.4 Skeleton

When the structure of the app, information and features had been determined, a wireframe for each view could be created:

<insert view of app/website>

### 1.5 Surface

**Colour Palette**

Colour was added to certain key elements to highlight them and improve the user experience in the game.

- Instructions - 
- When a battleship was hit
- Ship count for computer and player

## 2. Features

### 2.1 Existing Features

The features deployed for this quiz are as follows:

<insert feature descriptions and images>

### 2.2 Future Features

In addition to the features deployed, some features that could be deployed in a future release are:
- <list future features>

## 3. Technologies Used

Several technologies were used to aid the project:

- [Python](https://www.python.org/)
    - Python is the core programming language used to write all of the code in this game to make it fully functional.
    - In addition, the following Python modules were used :
        - [Colored](https://pypi.org/project/colored/)
            - Used to add colours to the printed terminal messages
- [GitHub](https://github.com/)
    - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/)
    - Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [Gitpod](https://www.gitpod.io/)
    - Used as the development environment.
- [Heroku](https://dashboard.heroku.com/apps)
    - Used to deploy the game.
- [Lucid](https://lucid.app/documents#/dashboard)
    - Used to create the flowchart for the project.
- [Pep8](http://pep8online.com/)
    - Used to test my code for any issues or errors.

## 4. Testing

### 4.1 Initial Developer Testing

<introduce developer testing>

The development of this app was conducted on Google Chrome, therefore extensive testing was conducted on this browser. This was used as a benchmark against Firefox and Safari.

The elements of testing conducted on each browser are:
<insert list of testing performed and why - see example below>
- User Experience - what does the game look like; are all elements where they are expected; is the text format presently adequately?
- Functionality - do the inputs work as expected; are out of range inputs captured; ?
- Performance - how responsive is the site?
- Other - this includes spelling and grammatical errors.

The user experience is consistent on Chrome, Firefox and Safari.

Responsive design is based on the deployment 

### 4.2 Validator Testing

Using tools such as PEP8 validator and Lighthouse gives visibility of any code, scripts or elements that are causing any errors. The results for the site are as follows:

**Python**
- 

**Performance**
- Results can be seen through the official [Lighthouse](<insert link to report>) report.

As part of the performance test through Lighthouse, some changes were made:
- Accessibility (aria-label) tags were implemented on all buttons to improve the score from 82 to 100.
- The cache policy was amended to increase the length of number of seconds the browser should cache the resource.
- The image file sizes needed to be compressed so reduce the impact on performance. This was successfully done using [tinyPNG](https://tinypng.com/).

### 4.3 User Testing
This app has been tested by a small group of 10 users in which some feedback was captured in the design and some errors in functionality and spelling were corrected.

UI improvements made:
- <list any improvements to UI that were made here>

Errors / bug fixes:
- <list errors/bugs that were found, what the problem was and how they were fixed>

### 3.4 Unfixed Bugs

- <list unfixed bugs here>

## 5. Deployment

The ‘<insert website name>’ was deployed to GitHub pages. The steps to deploy are as follows:
- In the GitHub repository, navigate to the Settings tab
- From the source section drop-down menu, select the Master Branch
- Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment.

The ‘<insert app name>’ was deployed with the help of the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

The live link can be found here - <insert link>

## 6 Credits

### 6.1 Content

Logos and Fonts:
- The fonts were taken from [GoogleFonts](https://fonts.google.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

Tutorials and support:
- General guidance, information and limitations on elements, attributes, and methods from [w3schools](https://www.w3schools.com/default.asp) and [MDN Web Docs](https://developer.mozilla.org/en-US/)
- <insert list of tutorials followed>
- The many people who 'beta tested' the quiz app.

### 6.2 Media

Any photos used throughout the app are stock imagery from the following services:
- [unsplash](https://unsplash.com/)
- [FreeImages](https://www.freeimages.com/)
- [PikWizard](https://pikwizard.com/)

<insert any other media used throughout the app/site here>

### 6.3 Research

As mentioned in the design section, competitor research was conducted. These are credited below:
- <insert list of research links>

### 6.4 Special Thanks


## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.