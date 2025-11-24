[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/BqipVvSh)
We're halfway through the bootcamp phase of the apprenticeship, and a couple of questions that have come has come around the other parts of the apprenticeship and how they fit together. I thought the best way to do this was in code, but I've not been the best developer....

This exercise is designed to help you:

- Debug existing non-working code
- Identify and apply simple refactorings, including separating source and test code
- Discover and apply new dependencies within a project
- Use ATDD and TDD in a project

_This project will explore themes found in duties 1,8,11, and 12_

The steps are listed in increasing order of difficulty-the more stars, the more challenging. Everyone should be able to get one star, and some might be able to get two or 3 stars. You can always return at a later time to apply new learnings!

You are allowed to ask for help (definitely ask me!), but this is one of the few times I want to see what __you__ can do, so please attempt this on your own.

### To Pass: Complete Parts 1 and 2
### For a Merit: Complete Parts 3 and 4
 

Now let's see what kind of developer I am...


## Part 1- Is That It?! :star:

I thought a good place to start was to write a program that would display on the screen all the duties in this apprenticeship. *Obviously* I wrote some tests using [pytest](https://docs.pytest.org/en/stable/) but you should run it just to make sure. You can check [here](https://skillsengland.education.gov.uk/apprenticeships/st0825-v1-1) for the full list of duties.

***Hint: If you can't run the tests, make sure everything is where you think it should be.***


## Part 2-Make it Pretty :star::star:

It looks like displaying all these duties on the command line isn't the best way. What might be cool is saving them to an HTML document so that it's easier to read. Can you do that?


## Part 3-Category Is... :star::star::star:

As I mentioned where in _Bootcamp_ which is one of the themes of the apprenticeship. But what are the others, and how are they linked to the duties?

Extend the options so that users can click a number for each of the additional themes. This should then write that theme __and__ the associated duties to a HTML file.

Always reading from the list in memory might be troublesome, so feel free to please the duties in a file and read them from there.

### Themes

- Bootcamp
    - Duties: 1,2,3,4,13
- Automate!
    - Duties: 5,7,10
- Houston, Prepare to Launch
    - Duties: 6,7,10,12
- Going Deeper
    - Duties: 11
- Assemble!
    - Duties: 8
- Call Security:
    - Duties: 9


## Part 4-As Seen On Screen :star::star::star::star:

After all this work, it still would be nice to have the results displayed on the screen. Could you find a Python library to do this? We can then give an option to the user to seen it on the screen, or download a file.

