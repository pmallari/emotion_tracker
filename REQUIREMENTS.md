# Requirements

## What are we making

This project is a visual emotion tracker. Our goal is to be able to track specific actions by the users like keeping eye contact for example. The application is easy to use and provides detailed information on the actions of the users. The user can interact with the data collected by the web application to know what actions they are committing the most during conversation. The data provided should be displayed intuitively without being overwhelming for the user to digest. Overall, the idea of the application can be summed up in one sentence: Giving users a platform that can give them an assessment of their interactions in certain dialogues like that of an interview.

## What does an MVP look like

The user should be able to go onto the site and see a video feed of themselves. The application will begin to track the users actions once the feed starts. The user will see a feed of their emotions, in real time, displayed on a Pentagon Graph. As the emotions change, so do the positions of the points on the Pentagon Graph. Emotions displayed are TBD. The user would also see statistics of their top conditions from their session. For example, the user was "unsure" for x amount of time during the 20-minute session they just completed, which accounts for x percentage of the session.

## Technical issues needed to be discussed

* Are the users allowed to save information/data from previous sessions for reference on their progress? Where is this data saved and how do the users access it?

> For now, no. We can generate a report instead for individual sessions to start off with. Eye contact maintained for x amount of minutes for example. Report would be exported onto a PDF.

* What will the tech stack consist of?

> See Issue [#10](https://github.com/pmallari/emotion_tracker/issues/10)

* How long are the sessions?

> For now, we are making the session time default to 30 minutes each. However, the user will be allowed to end the session at anytime.

* What are the emotions being recorded?

1. Neutral
2. Calm
3. Happy
4. Sad
5. Angry
6. Fearful
7. Disgust
8. Surprise

* Where is the site being hosted?

This will be discussed later in the development process.

## To do

* Implement and train a better emotion recognition model
* Find a better face tracking module to track faces that are not facing the camera
* Create mockups of the web application