# Daily Logbook for Noah LIsin

## Date: Topic(s) of the day

Your daily log book should include the following contents:
* Questions you were asking/tasks you needed to complete
* Details on your approach to those questions/task
* A summary of outcomes (e.g. answers, numbers, graphs, intermediate products)
* Your next steps
* Questions you have for your peer(s) and/or instructor(s) 

*each of the topics below should contain a complete summary as detailed above*

This is a [markdown syntax](https://www.markdownguide.org/basic-syntax). Thanks for learning this!

### Topic/question/task 1
Summary of question/task
details of approach
summary of outcomes
next steps
questions

## 7/10/2023 Mt. Baker Climate

### Summary
My main objective for today was to educate myself on the climate of the Pacific Northwest and specifically, Mt. Baker. 

### Approach
Using the resources provided in the README file in this repository, I gained a solid understanding of Mt. Baker and its climate. I then furthered my knowledge through some more curated searches to answer some specific questions I had.

### Outcome
Significant points I discovered through my research:
* The pacific northwest is subject to mild to cold climates due to the cold ocean wind that settles to the west of the Cascades and the Rockies.
* Glacial runoff from the snow on Mt. Baker is extremely important for the preservation of wildlife, crops, and to temper [wildfires].
* By 2070, there may be no snowpack on Mt. Baker due to climate change.
* Lapse rate can be utilized by meteorologists to predict the weather; for instance, precipitation and snowfall.
* Evergreen trees are used as inexpensive cosmic radiation shields in order to obtain accurate temperature measurements.
* The IButton temperature sensors can additionally be used to calculate snowfall.
* Lapse rate can be positive during nighttime when the ground is cooler than the atmosphere. (The ground radiates energy toward space)
* Lapse rate is higher when it's dry around summer.
* Buried IButtons give 0C when snow is melting since that is the melting point. (The ground and air is heating it)

### Next Steps
Begin to analyze data on the lapse rate, sunlight, and snowfall on [Mt. Baker.]

### Questions
N/a
[wildfires]: # (also the source of our electricity from the skagit river.)
[less snowmelt]: # (less than what? be specific here about what you are comparing to)
[Mt. Baker]: # (sounds like you are ready to start asking questions of the data. I will coach you all into the data set and where to start.) 

## 7/11/2023 Schrieber's Meadow Sunniness

### Summary
My main objective for today was to continue educating myself on the climate of the Pacific Northwest and specifically, Mt. Baker. 

### Approach
I began to focus my attention on a specific question: How sunny is it at Schrieber's Meadow (the lowest instrument site)? Has this changed over the instrument record? I used the scientific papers in the README file, specifically the one on using evergreen trees as radiation shields to begin to understand how I should parse my data.

### Outcome
<<<<<<< HEAD
I updated my notes on Mt. Baker from yesterday, using points noted in the teaching session with Dr. Town. (See my notes from yesterday)
I began to write a program that will parse data from all 5 years and take the difference between the sensors in the open and the sensors under the trees to find the "sunniness" without radiation interference. Then graph that as a function of average daily radiation and see how well linear regression will fit (r^2). The better the fit, the better trees will block solar radiation. Making it less "sunny". (Question - If I want to answer the question (How sunny is it at Schrieber's Meadow?), what does it mean by "sunny", and how should I calculate it? Or should I not be taking these questions at face value and just use them for [inspiration]?) 
=======
I updated my notes on Mt. Baker from yesterday, using points noted in the teaching session with Dr. Town.
I began to write a program that will parse data from all 5 years and take the difference between the sensors in the open and the sensors under the trees to find the "sunniness" without radiation interference. Then graph that as a function of average daily radiation and see how well linear regression will fit (r^2). The better the fit, the better trees will block solar radiation. Making it less "sunny". (Question - If I want to answer the question (How sunny is it at Schrieber's Meadow?), what does it mean by "sunny", and how should I calculate it? Or should I not be taking these questions at face value and just use them for inspiration?) 
>>>>>>> 988beffee00f8dce3d32cb3986b657b203eeda02

### Next Steps
Finish my program, and make conclusions about the results.

### Questions
N/a

<<<<<<< HEAD
[inspiration]: # (Can you link to your code here to make it easier for me to find? Good entry today.)
=======
## 7/12/2023 iButtons

### Summary
My main objective for today was to organize the iButton's locations/conditions/surroundings into easily readable and accessible charts and maps.

### Approach
We used Google Sheets to make a chart of all the button conditions and site locations. We then used Google Maps to map the locations for each year.

### Outcome
We have a well-organized chart that will be super useful for making sure our data parsing is correct. 

### Next Steps
Finish maps for iButtons. Log locations for each. Double-check our work. Translate the Logbooks into easy-to-read [charts].

### Questions
N/a

[charts]: # (this is a good update. Can you link your code in the logbook so that I can see the link next time? Also input the map image, at least intermediate products, here.) 
>>>>>>> 988beffee00f8dce3d32cb3986b657b203eeda02

# 7/13/2023 More iButtons
### Summary
Continued to update our charts on iButton data. [iButton Locations, Descriptions, and More](https://docs.google.com/spreadsheets/d/1rYSfCRtbOYoHYn_85mbR3-nh_1uO19BrHjO-JNV4u0A/edit#gid=0)

### Approach
We worked as a group to complete our charts, maps, and notes.


### Outcome
A practically complete chart with all the data on iButtons. Added a dir called ESR-LSRI with my program and data. [programs](https://github.com/ESR-LSRI/2023_NoahL/tree/main/ESR_LSRI)

### Next Steps
Think about how I am going to handle all these csv's in a [single program].

### Questions
N/a

[single program]: # (what are your questions here? what is the task, or tasks, that are implicit in the work handle?)


## I hope you are well, Noah. When you get a chance, please up me on Friday and whatever else you've been able to do - DT

# 7/17/2023 Programming

### Summary
I communicated with my group, and worked on some programs.

### Approach
Talked to my group over email and then did some programming work.


### Outcome
I now have a program that can graph data in a range: [program zip](https://github.com/ESR-LSRI/2023_NoahL/blob/main/ESR_LSRI-programs%20(2).zip) \ [raw program](https://github.com/ESR-LSRI/2023_NoahL/blob/main/ESR_LSRI/mtbakerparser.py) \
I started on a program that can concatenate [data].

### Next Steps
Continue to work on concatenating data. Think more about my question on snow depth, how I'm going to present it, what data I'm going to use, etc.

### Questions
N/a

[data]: # (Very strong work, Noah. I'm excited to see your concatenation work. Let's also think about where to spend your time so that you can get a good graph or two of your work. How will you identify when the sensors are buried? Please use relative path names for figures and files here. Thanks!)

# 7/19/2023 Snow Depth / A Bit Of Research

### Summary
I worked on a program that will graph the temperature of exposed sensors side-by-side so I can see when each got buried and will also calculate how much it snowed over a period of time, and how high the snow is.

I spent a lot of time debugging issues with pandas, unfortunately.

Did some research on how to calculate snow depth.

I'm a little behind since I was sick and spent a lot of time working on calculating sunniness. I'm going to do a lot of catchup work tonight and hopefully finish my graph and my poster. (git will probably be updated a little late since i have practice)

**UPDATE:** I realized some files were out of date, some had weird formatting, and some more issues. It's all fixed and I have graphs in my esr-lsri folder. Also a function that can get the days when it was buried by just checking if temp is close to 0. A graph of that is soon or some other way to present that data? 
Poster drafted.

### Outcome
I'm almost done, my program will be finished by tomorrow.

### Next Steps
Poster draft.

### Questions
N/a

