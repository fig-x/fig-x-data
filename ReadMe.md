# Data file for fig-x.github.io

Jul 6, 2024 by Fumeng Yang

This repository contains the datasets used to render [fig-x.github.io](https://github.com/fig-x/fig-x.github.io/tree/main). I decided to separate data from the code to lower the bar for updating, though later it may be approved a bad idea. I anticipate that everyone should know how to update the website, but maybe we still need a web master to do this for checking and consistency. 

Basically, you just need to look at json and add a similar entry in the json and upload images to the respective folders. You can pull this repo in your computer or just add information on Github. I would expect the webmaster to have this repo locally.

## research.json

This renders [https://fig-x.github.io/reseach](https://fig-x.github.io/reseach). It contains an array of area. And each area entry looks like

```json
   {
        "area": "Trust in Computational Models",
        "core": " ",
        "description": "We study ... ",
        "paper": [
            "2020-ml-trust",
            "2024-dice"
        ]
    },

```

The first line is used to render the headers and so on. Except for the paper list, I don't think we need to update these often. The paper list contains an id, specified in `publication.json`. The thumbnails on this page are read from `publication.json` too. The max number is 7 now. If there are more than 4 images, definitely **take a look at the page**, including **the mobile view**. If there are more than **7 papers** in an area, you need to **add an entry** in `index.css` (imagecard) and test it.

If we need to add an area, besides adding an entry, we need to add a line in the `research.js` (`fig-x.github.io`) to add an icon.

## people and people.json

These two files specify the information of lab members and store their headshots. 

```json
   {
        "name": "Fumeng Yang",
        "website": "https://www.fmyang.com/",
        "headshot": "https://raw.githubusercontent.com/fig-x/fig-x-data/main/people/Fumeng-Yang.JPG",
        "position": "Assistant Professor",
        "quote": "It's just me and The Seaweeds for now. Contact me if you are interested in working with me!",
        "catergory": "current",
        "year": 2024,
        "month": 6,
        "nickname": "themachine"
    },
```

To add a person, just copy-add a similar entry, and also upload a headshort to `people/`. 
- If you don't have a field, you could leave it as `null` or `""`.   

- The **position** should be something like Ph.D. student. 
  
- The **quote** field ideally should be your research focus. 
  
- The **category** could be current, current-non-human, or alumni. If we need new category, we need to add to `People.js`. 