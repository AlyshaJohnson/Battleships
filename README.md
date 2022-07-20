# Battleships

This is the README.md file for command-line-interface application of a single player game of battleships, played against the computer.

![Responsive Mockup](/assets/images/Device-mockup.jpeg)

A link to the deployed project can be found [here](https://alyshajohnson-battleships.herokuapp.com/).

## 1. Design and Development

For the design of this application, the 5 pillars of User Experience Design (UXD) were used to cover the strategy, scope, structure, skeleton and surface to make sure the design is intuitive, simple and enjoyable.

### 1.1 Strategy

The brief that was given by the stakeholder is as follows:

*External user’s goal:*

- The application user wants to play a logic game

*Site owner's goal:*

- The Battleships game is played on grids on which each player's fleet of battleships are marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
- The application provides a working battleships game for a single user to play against the computer.

Research was conducted into the wants of a variety of target audiences and other versions of battleship games, from physical board games to online games. All this was used to determine the minimum requirements for features, logic and user experience. 

### 1.2 Scope

From the research and interviews conducted with the target audience and stakeholders, user stories were created to determine the flow of the app. The focus was put on the following user stories:

![User Stories 1 - 3](/assets/images/user_stories_1_2_3.jpeg)
![User Stories 4 - 5](/assets/images/user_stories_4_5.jpeg)

These user stories start to determine the logic required throughout the game. Although these have changed slightly due to time, the premise of the logic and flow still holds true.

### 1.3 Structure

From the user stories, content, logic and libraries can be determined.

**For the content:**

- Generate computer ship placement
- Input player ship placement
    - refresh board if unhappy
- Generate player and computer boards
    - placement rules for ships
- Hit / miss ship
    - if coordinates = 'X' -> hit
    - if coordinates = '0' -> miss
- Generate computer guess
    - logic of guess after 'hit'
- End game
    - if user_ships = 0 or if computer_ships = 0
- Results
    - if user_ships > computer
        user = winner
    - play again?

The content determined here was produced whilst in the design phase of the project. Due to time constraints, it was planned to randomly generate the player's board for them with an input to allow them to refresh the board if desired, and the logic of the computer's guess.

**For the libraries:**

For the above content to be produced it was determined the library `random` would be required to generate computer ship placement and computer guess with the use of the function `randint()`.

### 1.4 Skeleton and Surface

As this application is a back-end code, run through a web-based portal, little can be done to change the webpage without some front-end code to match. However, the user still needs to enjoy the game. The features that are included in the code, are instructional, informative and clear.

The features included are:
1. Welcome page
2. Rules and legend
3. Visible player guess and ship boards including:
    - ship counter to show how many computer ships are left
    - ship counter to show how many player ships are left
    - guess counter to show how many guesses have been played
4. Refresh board input
5. Coordinates input
6. Restart game

User testing of the code will be implemented to gain feedback and insight into how the user responds to the game, and determine if there are any changes that will need to be implemented to make it more useful, readable and enjoyable.

![](/assets/images/start_screen.jpeg)

## 2. Features

### 2.1 Existing Features

The features deployed for this game are as follows:

<insert feature descriptions and images>

### 2.2 Future Features

In addition to the features deployed, some features that could be deployed in a future release are:
- Player to input their own ship placement through use of coordinates. This can be done in a similar manner to the input for the coordinate guess.
- Greater logic when the computer 'picks' the coordinates. For example, if a hit is successful then coordinates up, down, left and right are returned before returning to a random selection.
- Coin toss to determine which user fires a missile first - this could be done by using the randint(0, 1), where 0 is heads and 1 is tails, against a user input or heads or tails to go first.

## 3. Technologies Used

Several technologies were used to aid the project:

- [Python](https://www.python.org/)
    - Python is the core programming language used to write all of the code in this game to make it fully functional.
- [GitHub](https://github.com/)
    - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/)
    - Used for version control by utilising the Gitpod terminal to commit to Git and Push to GitHub.
- [Gitpod](https://www.gitpod.io/)
    - Used as the development environment.
- [Heroku](https://dashboard.heroku.com/apps)
    - Used to deploy the game.
- [PythonTutor](https://pythontutor.com/)
    - Used to visualise the flow of code as it is executed
- [Pep8](http://pep8online.com/)
    - Used to test my code for any issues or errors.

## 4. Testing

### 4.1 Initial Developer Testing

As the project was developed and coded, developer testing was conducted to reduce the impact of bugs and errors in the code. This testing consisted of general debugging of written code based off gitpod IDE recommendations; running through input validator testing scenarios to check for input errors; and testing on different browsers.

**General Debugging**

Throughout the development, errors occurred when writing code due to the existance of white space, function name recommendations, etc. which were generated by gitpod IDE. While most of these were simple fixes and amended quickly, there are a total of 7 amber problems that have been left in the code for the following reasons:
- 'Invalid assignment to self in method' needs to occur in order to create a list
- 2 'Used variable 'value'' which needs to be included as looping through a dictionary which require key, value pairs
- 4 'Using the global statement' which is required to call and alter global variables

A major bug that was managed and caught whilst in development was the generation of the ship boards for both player and computer would produce an overwrite of one ship over another, causing there to be one less ship to hit. This caused a subsequent bugs as the game would be unfair as the ship_count for either player or computer would never be 0. This is especially concerning if both players had only 8 ships placed instead of 9 the game could not end.

The solution for this was to add a while loop in the place_ships function to count all the ships placed on the board, if this did not equal 9, then the board was refreshed until this condition becam true.

**Input Validator Testing**

The input validator testing scenarios conducted to ensure input errors were captured and mitigated correctly:
1. player_board_reset input out of range (e.g. 7, Nah)
2. capitalisation for player_board_reset input does not return error (e.g. Y, y)
3. row/column input out of range (e.g. A9, Z1 and A10)
4. duplicate entry for row/column input
5. capitalisation of row/column input does not return error (e.g. a1, A1)
6. row/column input already used
7. new_game input out of range (e.g. 7, Nah)
8. capitalisation for new_game input does not return error (e.g. Y, y)

Scenarios 2, 5 and 8 returned no errors.

Scenarios 1, 3, 6 and 7 returned bugs due to the use of an if loop to iterate through the expected conditions. These bugs were fixed by replacing the if loop with a while loop.

Scenario 4 counted the duplicate input as a coordinate and continued with the code. This was not desired, so an additional while loop was added to ask for input if the coordinates in the board aren't a space.

**Browser Tesing**

The development of this app was conducted on Google Chrome, therefore extensive testing was conducted on this browser. This was used as a benchmark against Firefox and Safari.

The elements of testing conducted on each browser are:
- User Experience - what does the game look like; are all elements where they are expected; is the text format presently adequately?
- Functionality - do the inputs work as expected; are out of range inputs captured; ?
- Performance - how responsive is the site?

The user experience is consistent on Chrome, Firefox. However, on Safari the app loads but a user cannot type into their input. Heroku recommend using Chrome as the browser of choice for running the application. See support documentation [here](https://devcenter.heroku.com/articles/heroku-ci-browser-and-user-acceptance-testing-uat/).

### 4.2 Validator Testing

Using the tool [Pep8](http://pep8online.com/checkresult) validator gives visibility of any code, scripts or elements that are causing any errors. The results for the site are as follows:

![](/assets/images/pep8_validation.jpeg)

### 4.3 User Testing
This app has been tested by a small group of 5 users in which some feedback was captured in the design and some errors in functionality and spelling were corrected.

UI improvement suggestions:
- write instructions and welcome for someone who has never played game before
- input descriptions need to be clear to what user is inputting (e.g. name, coordinates, Y/N, etc.)
- printing computer_guess_coords as numbers instead of [letter, number]

Errors / bug fixes:
- some coordinates not printing onto player_guess_board
- "coordinates already submitted" printed to terminal between boards

The improvements and fixes that were made were adjustments to the input description and writing more descriptive instructions. Additionally, the bug relating to some coordinates not printing onto the player_guess_board was due to the reference symbols in the if loop not being correct and therefore no 'X' appearing in the board.

### 4.4 Unfixed Bugs

From all the testing completed, there are only two known bugs that have not been fixed. These are:
- printing computer_guess_coords as numbers instead of [letter, number]
- "coordinates already submitted" printed to terminal between boards

## 5. Deployment

The master branch of this repository has been used for the deployed version of this application.

### 5.1 Using Github & Gitpod

To deploy this command-line interface application, the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template) was used, as this enables the application to be properly viewed on Heroku using a mock terminal. 

- Click the `Use This Template` button.
- Add a repository name and brief description.
- Click the `Create Repository from Template` to create your repository.
- To create a Gitpod workspace you then need to click `Gitpod`, this can take a few minutes.
- When you want to work on the project it is best to open the workspace from Gitpod (rather than Github) as this will open your previous workspace rather than creating a new one. You should pin the workspace so that it isn't deleted.
-  Committing your work should be done often and should have clear/explanatory messages, use the following commands to make your commits:
    - `git add .`: adds all modified files to a staging area
    - `git commit -m "A message explaining your commit"`: commits all changes to a local repository.
    - `git push`: pushes all your committed changes to your Github repository.

*Forking the GitHub Repository*

To make changes to a repository without affecting it, a copy can be be made by 'Forking' it. This ensures the original repository remains unchanged.

1. Find the relevant GitHub repository
2. In the top right corner of the page, click the Fork button (under account)
3. The repository has now been 'Forked' and a copy has been made

*Cloning the GitHub Repository*

Cloning a repository will allow a local version of the repository to be downloaded and worked on. Cloning is also be a great way to backup work.

1. Find the relevant GitHub repository
2. Press the arrow on the Code button
3. Copy the link that is shown in the drop-down
4. Now open Gitpod & select the directory location where the clone is to be created
5. In the terminal type 'git clone' & then paste the link copied in GitHub
6. Press enter and a local clone will be created.

### 5.2 Creating an Application with Heroku

Following the below steps using the Code Institute tutorial:

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install project dependencies `pip3 freeze --local > requirements.txt`. Please note this file should be added to a .gitignore file to prevent the file from being committed. Int he instance of this project, no requirements were created as there were no project dependencies.

1. Go to [Heroku.com](https://dashboard.heroku.com/apps) and log in; create an account if needed.
2. Click the `New` dropdown and select `Create New App`.
3. Enter a name for the new project - all Heroku apps need to have a unique name.
4. Select the region.

*Heroku Settings*
Environment Variables need to be set up - this is a key step to ensuring the application is deployed properly.
- In the Settings tab, click on `Reveal Config Vars` and set the following variables:
    - If using credentials they will need to be added as a variable, the key is the name 'CREDS' and the value is the contents of the creds JSON
    - Add key: `PORT` & value `8000`
- Buildpacks are also required for proper deployment, simply click `Add buildpack` and search for the ones required.
    - For this project, `Python` and `Node.js` were needed, in this order.

*Heroku Deployment*
In the Deploy tab:
1. Connect the Heroku account to the Github Repository following these steps:
    1. Click on the `Deploy` tab and choose `Github-Connect to Github`.
    2. Enter the GitHub repository name and click on `Search`.
    3. Choose the correct repository for the application and click on `Connect`.
2. A choice is given to deploy the project manually or automatically, automatic deployment will generate a new application every time a change is pushed to Github, whereas manual deployment requires the `Deploy Branch` button to be pushed whenever a change is made.
3. Once the deployment method has been chosen, the application will be built and can be opened using the `Open App` button at the top of the page.

![](/assets/images/heroku_deployed_image.jpeg)

## 6. Credits

All code was written by the developer, but help and guidance was required to generate ideas, troubleshoot and test. The following credits who helped and guided this project.

### 6.1 Content

Tutorials and support:
- General guidance, information and limitations on variable, functions, and methods from [w3schools](https://www.w3schools.com/default.asp), [RealPython](https://realpython.com/) and [StackOverflow](https://stackoverflow.com/)
- Logical flow of game, [Pythondex](https://pythondex.com/python-battleship-game) was used as inspiration.
- Logical flow of game and step by step guidance of creating game, KnowledgeMaverns on [youtube](https://www.youtube.com/watch?v=tF1WRCrd_HQ) was used.
- Use of Object Oriented Programming in game was inspired by user: cloud2236863496 on [CodeCademy](https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605).
- The many people who 'beta tested' the app.

### 6.2 Research

As mentioned in the design section, competitor research was conducted. These are credited below:
- [battleshiponline](https://www.battleshiponline.org)
- [battleship-game](http://en.battleship-game.org)

### 6.3 Special Thanks
A special thanks to Harry Dhillon for providing guidance and suggested improvements on this project.