# eLitmus-project

Puzzle Design:
Title: Lost Treasure Hunt

Objective: Find the lost treasure by solving a series of clues that assess your soft skills.

Features:

Anyone with an email address can create an ID and password to participate in the game.
The puzzle must contain minimum 5 clues, minimum 2 dead-ends, and minimum 1 solution.
All the progress/user data (e.g., time taken by each user for every step, solution accuracy, etc.) depending on your puzzle requirements, should be stored for every user.
On refreshing from either the browser or website, the puzzle should start from the same step or give the user an option to restart.
A dashboard for the admin where the progress of all the users can be tracked and analyzed.
Clues:

Clue 1 - Welcome to Lost Treasure Hunt: Upon logging in, the user is presented with a welcome message and a clue. The clue is a riddle that leads them to a location on the website where the next clue is hidden.

Clue 2 - Eye for Detail: The second clue requires the user to pay attention to details on the website. The user needs to locate a hidden link that leads them to the next clue.

Clue 3 - Perseverance: The third clue requires perseverance. The user needs to solve a puzzle that is difficult but solvable. If the user fails to solve the puzzle after multiple attempts, they are directed to a dead-end.

Clue 4 - Curiosity: The fourth clue requires the user to be curious. The user needs to click on a link that takes them outside the website. The link leads to a YouTube video with a hidden message that provides the clue to the next location on the website.

Clue 5 - Final Clue: The final clue requires the user to use all their soft skills to locate the treasure. It's a challenging puzzle that can only be solved if the user has successfully solved all the previous clues. Once the user has solved this puzzle, they are directed to the treasure.

Dead Ends:

There are two dead-ends in the puzzle. One is in Clue 3, where the user fails to solve the puzzle after multiple attempts. The other is in Clue 6, where the user fails to solve the final puzzle.

Implementation:
We will use Python and Flask to build the Lost Treasure Hunt application. We will use a database to store user information, including their progress and data. The database will be connected to the Flask application using SQLAlchemy.

We will use Flask's session object to store user data and progress temporarily. We will use Flask's Jinja2 template engine to render HTML templates dynamically.

We will use Bootstrap to make the website responsive and mobile-friendly.

Conclusion:
This is the design and implementation plan for the Lost Treasure Hunt puzzle that assesses the soft skills of users. It includes multiple clues and dead-ends to test users' soft skills, and their progress will be tracked and stored in a database. The dashboard for the admin will provide real-time progress tracking and analysis for each user. The final puzzle will be a challenging one, and only those who successfully solve all the previous clues will be able to find the treasure.
