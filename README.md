# subtitle-remover
A light piece of code to remove hard-coded subtitle from movie/pictures.

## Motivation
Many people (including me and many of my friends) learn a language by watching movies and shows in that language. Sometimes, we start to read the subtitles instead of listening without even noticing it (especially when the movie is amazing)!

Removing the subtitles could allow us to focus on learning the language without distraction. If your movie has both subtitles in your language and in the language you wish to learn, you can choose to remove the subtitle in your language.

## How it works
Hard-coded subtitle is removed by masking the area where the subtitle exists. 

Provide the tool with 3 things:
1. The path to your movie/image
2. The path to where you want to save the processed movie/image
3. The rectangular region that encaptures the subtitle

Enjoy!

In the future, I would like to implement this as a web application and make it more user-friendly by allowing a GUI for selecting the region to mask, like [Aiseesoft](https://www.aiseesoft.com/resource/subtitle-remover.html) but without having to download an app for this task.