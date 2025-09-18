# Data files for fig-x.github.io 

Jul 6, 2024 by Fumeng Yang

This repository contains the datasets used to render [fig-x.github.io](https://github.com/fig-x/fig-x.github.io/tree/main). I decided to separate data from the code to lower the bar for updating, though later, we may want to merge them. I anticipate that everyone should know how to update the website, but we may still need a webmaster to do this for checking and consistency. 

Basically, you just need to (1) look at the json and (2) add a similar entry in the json and  (3) upload images to the respective folders. You can pull this repo onto your computer, directly add information on GitHub, or use a pull request (preferred so the webmaster can check it). 

I would expect the webmaster to have this repo locally and check the outcome.  
> To add **publication**, I feel you don't need to ask me/Fumeng for permission.    
To add **people**, maybe just notify me beforehand.    
To add **artifact**, you may want to discuss it with me briefly unless it's obvious, like a package or a library.      
To add a new **research** area, hmmm, you definitely want to ask me.   But to add a paper to an existing area, you probably don't need to ask me.   
After you edit them locally or on Github, commit and push, wait for 1-2 minutes, and then definitely check [fig-x.github.io](https://github.com/fig-x/fig-x.github.io/tree/main) to see if anything breaks. If there is a bug and we don't have a coding person, report it to Fumeng. (If the problem is misspecified json, you should fix your json...)   
A headshot must have an aspect ratio of 1:1, and a paper thumbnail must have an aspect ratio of 16:9. Check for any large files! 


## people and people.json

These render [https://fig-x.github.io/people](https://fig-x.github.io/people).  These two files specify the information of lab members and store their headshots. 

The first object (this must be the first object!! so **don't move this**!) specify meta information: **category** and the displayed name. 

```json
{
    "current": "Current members",
    "current-non-human": "Non-human friends",
    "alumni": "Alumni"
}
```

The others are people entries.

```json
{
    "name": "Fumeng Yang",
    "website": "https://www.fmyang.com/",
    "headshot": "https://raw.githubusercontent.com/fig-x/fig-x-data/main/people/Fumeng-Yang.JPG",
    "position": "Assistant Professor",
    "quote": "It's just me and The Seaweeds for now. Contact me if you are interested in working with me!",
    "category": "current",
    "year": 2024,
    "month": 6,
    "nickname": "themachine",
    "sorting": "prof"
}
```

To add a person, copy-add a similar entry to the json and upload a headshort to `people/`. The aspect ratio should be 1:1. Make sure the resolution is not too small or too large. 

- If you don't have a field, you could leave it as `null` or `""`.   

- The **position** should be something like Ph.D. student. 
  
- The **quote** field ideally should be your research focus. 
  
- The **category** could be current, current-non-human, or alumni. If we need a new category, we need to add it to `People.js`. 

- **Year** and **month** are the time when joining the lab, but it is loosely defined. This will be used to sort people by their seniority. 
  
- **nickname** could be null or "". This will be used as an id.

- **sorting** could be `prof`, `phd`, `master`, or `undergrad`. This variable is used in sorting the order. If we have someone other than these, we need to change the `People.js` ([fig-x.github.io](https://github.com/fig-x/fig-x.github.io/tree/main)). It doesn't matter if it is `pet`.


## research.json

This renders [https://fig-x.github.io/reseach](https://fig-x.github.io/reseach). It contains an array of areas. And each area entry looks like

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

The first line is used to render the headers and so on. Except for the paper list, I don't think we need to update these often. The paper list contains an id, specified in `publication.json`. The thumbnails on this page are read from `publication.json` too. The max number is 7 now. If there are more than 4 images, definitely **take a look at the page**, including **the mobile view**. If there are more than **7 papers** in an area, you need to **add an entry** in `index.css` (imagecard) in [fig-x.github.io](https://github.com/fig-x/fig-x.github.io/tree/main) and test it.

If we need to add an area, besides adding an entry, we need to add a line in the `research.js` ([fig-x.github.io](https://github.com/fig-x/fig-x.github.io/tree/main)) to add an icon.



## publication and publication.json

These render [https://fig-x.github.io/publication](https://fig-x.github.io/publication).  
These two files have a very similar structure to `people` and `people.json`. `publication.json` needs to follow the time order. The order is reflected on the webpage because I feel it might be a little difficult to automatically sort them while it is not too hard to maintain consistency...

The first object specifies all abbreviations and the respective full names. These will be used to render papers so that the publication venues are consistent. Note that this must be the first object! This is also used to render the statistics (e.g. CHI (x)) on the top of the page.

```json
{
    "CHI": "The ACM Conference on Human Factors in Computing Systems",
    "VIS": "IEEE Visualization and Visual Analytics Conference",
    "TVCG": "IEEE Transactions on Visualization and Computer Graphics",
    "CHI LBW": "CHI Conference Extended Abstracts on Human Factors in Computing Systems",
    "IUI": "The ACM Conference on Intelligent User Interfaces",
    "Ubicomp": "The ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies"
}
```

The second object is a separator like this. 

```json
{
    "separator": "2024" 
}
```

The others are paper entries published falling into the range of `separator`. I think most of them are self-explanatory. 

Please ensure each paper has at least **title**, **people**, **year**, **paper_id** (please follow `yyyy-nickname`, this is used to render the research page), **description** (one sentence pitch), **pdf**, and **abbr**. You should also have at least **doi**. The **repo** field is displayed as supplementary materials. The other fields could be null or `""`.

```json
{
    "title": "In Dice We Trust: Uncertainty Displays for Maintaining Trust in Election Forecasts Over Time",
    "people": "<text class = 'figx-name-style'>Fumeng Yang</text>, Chloe Mortenson, Erik C. Nisbet, Nicholas Diakopoulos, Matthew Kay",
    "year": "2024",
    "thumbnail": "https://raw.githubusercontent.com/fig-x/fig-x-data/main/publication/2024-dice.png",
    "paper_id": "2024-dice",
    "description": "We provide design recommendations for conveying U.S. presidential election forecasts",
    "pdf": "https://osf.io/preprints/osf/9x4nr",
    "video": "https://youtu.be/1pE5yGXHpGU",
    "repo": "https://osf.io/923e7/",
    "doi": "https://doi.org/10.1145/3613904.3642371",
    "demo": "https://forecasts.cs.northwestern.edu/2023-hypothetical-elections/?PROLIFIC_PID=use_testing_or_a_very_long_string",
    "awards": "Best Paper Award (top 1%)",
    "abbr": "CHI"
}
```

To add a paper


- If this is a new venue, please add its abbr and full name to the first object. 

- If we are at a new year, please add a `{
     "separator": "yyyy" 
}`

Otherwise, just copy the paper entry and add one. Remember to upload the thumbnail to the `publication` folder. A thumbnail's aspect ratio should be 16:9. Make sure the resolution is not too small or too large. I've designed the thumbnail to be large to allow for fine details, but make sure it is not too complex. 

- Also, remember to add the `paper_id` into the `research.json` if suitable. And add them to `news.json` (note you might need to follow a specific format for the links.)  

Note: 

- The icon of a paper award is hardcoded. So if there is anything other than Best paper or Honorable mention, we need to add a line in `Publication.js` (`fig-x.github.io`)

- Please use `<text class = 'figx-name-style'> .. </text>` to indicate lab members.

- Equal contribution - the first example is the rethinking paper. 

## artifact.json

This renders [https://fig-x.github.io/artifact](https://fig-x.github.io/artifact).  

Again, this is very similar to `publication.json` and `people.json`. 

The first object is metadata, which specifies the category. Note that everything here has had an icon in the code. 

```json
["dataset", "website", "model", "tool", "library", "package", "interface"]
```


To add one, copy and paste a new entry. **what** is the category above.

```json
{
    "what": "website",
    "title": "Governor Election Forecasts",
    "link": "https://forecasts.cs.northwestern.edu/2022-governors-elections",
    "description": "This site provides our best guess of the outcomes of the 2022 governor elections in the U.S.",
    "people": "Fumeng Yang"
},
```

If the bubbles don't have the same height, it's a little urgily. Please, for now, contact a similar length of sentences...or we can fix the height.

## logo, welcome and work with us

These should be updated in the code repo.
