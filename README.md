# TEDVis

Hi guys! Here is our first tutorial of the semester. Breaking away from Twitter Data for a second since our server might be down, I decided to use about 5400 or so TED talks manuscripts forkerd from @saranyan's Ted-Talks repo instead!

The main pursose of this tutorial is to get our feet wet with using data to visualize any insights. At its simplest form, we can create something like a bar graph! 

In our case, we have a large sum of manuscripts from TED talks, why don't we build a bar graph in D3 to show the top ten adjectives that show up in the text. 

The data parsing has already been done and has been condensed into data.json! 

All that is left to do is create the bar chart!

For a finished version of this, go to my personal [website](parlieux.com/TED)!

## Getting Started 

This tutorial will involve picking up Javascript since D3, our Data Visualization library, is written in Javascript. Don't be frightened! It is syntactically different to Python, but remember, all languages follow similar logic so you will be fine!


### Prerequisites

From your terminal/command line, we need to install a few packages

```
python3 -m pip install nltk requests
```


### Steps

Go to the current directory of this project, then run the following command into your terminal/command line:

```
python3 -m http.server
```

This python command creates a server within this directory of this computer! Go to a browser and type in **localhost:8000** You should see our skeleton of the project! Here is our web page. Now we need to write the code for us to generate the bar graph.

####HTML
HTML is a markup language for creating webpages. When we go to **localhost:8000**, we are accessing the **index.html** file within the directory you're in.

First things first, we need to include the tag that 'imports' the D3 package into our webpage. Go to **index.html** and in between the **head** tags, write:

```
<script src="https://d3js.org/d3.v3.min.js"></script>
```


Next, paste this into the commented section:

```
<div class="chart">

</div>
```

Since D3 follows the Document Object Model(DOM), we are able to create what I like to call a placeholder for the bar chart. When we start implementing the JavaScript, we will call this tag to referent the placeholder so that we may fill it in with something more meaningful!

Lastly, lets include this right after chart tags:

```
<script src="index.js"></script>
```

This is the tag that allows us to read in Javascript from a file. We could have totally wrote the code we are about to write in Javascript within the meat of the tag, but that is bad practice! 

Now onto the Javascript

####Javascript

Here is where the meat of our code will be!

Javascript is what animates webpages. In our case, it will create a bar chart for us within our placeholder. Within **index.js**, we will write the rest of our code. 

First, we decide on the size of the chart:

```
var width = 960,
    height = 500;
```


Now is where it gets a bit trickier:

```
d3.json("data.json", function(data) {
	//More code will go here

});
```

This is how we get our data to load into the Javascript. This language use callback functions. WHAT IS THIS? :O

#####Synchronous code
In synchronous programs, if you have two lines of code (L1 followed by L2), then L2 cannot begin running until L1 has finished executing.

You can imagine this as if you are in a line of people waiting to buy train tickets. You can't begin to buy a train ticket until all the people in front of you have finished buying theirs. Similarly, the people behind you can't start buying their tickets until you have bought yours.

#####Asynchronous code
In asynchronous programs, you can have two lines of code (L1 followed by L2), where L1 schedules some task to be run in the future, but L2 runs before that task completes.


Read more at https://www.pluralsight.com/guides/front-end-javascript/introduction-to-asynchronous-javascript#ZXbJUy1fpILuVArh.99

Basically, all we are doing is creating a function to handle the data coming in while it arrives, but in the meantime, we can do other things taht are independent of teh data. It is quite efficent and is a reason why your browser loads pretty fast! If it doesn't sink just yet, it will soon, I promise. 

Within **the more code will go here**, write:
```
	maxVal = data[0].frequency
	d3.select(".chart")

```



The first statement pulls the first data value. It is structured as so: 

```
_{word: fantastic, frequency: 4798}_
```

The frequency is the number of times the word shows up in the 5400 manuscripts.



The second statement is the creation of the chart. Not so bad. The d3 module that we imported using the script tag gave us access to quite a few data representation models to choose from using the **select()** method.


Next, we have to customize our chart. For starters, where do we include the data?

```
d3.select(".chart")
    .attr("width", width)
	.attr("height", height)
	.selectAll("div")
	.data(data) //data being sent in
		.enter() //invokes new data points
		.append("div")
		.style("height", 30)
		.style("width", function(data) {return (data.frequency/maxVal*1.0)*960 + "px"})
		.text(function(data) {return data.word})
```

The **.attr** attributes of the d3 object sets the first parameter's value. 

The **.selectAll** attribute points the chart on the Javascript side to the HTML side.

The **data** attribute loads the data we waited on thereby the chart being dependent on the data loading!

The data's **.enter** attribute says hey, we are about to enter in some data. Listen up.

The data's **.append** attribute sends that data to the HTML to render.

The data's **.style("height", 30)** attributes set the height and width of the bars. Notice that I included asynchronous function in the _width_ style method to make the length of the bar to be dependent on the frequency of the word.

Finally, the data's **.text** attribute just sets every bar graph's text to be the word itself.

That was a lot. For clarity, **index.js** should look like so:

```
var width = 960,
    height = 500;

d3.json("data.json", function(data) {
	maxVal = data[0].frequency
	d3.select(".chart")
	    .attr("width", width)
    	.attr("height", height)
		.selectAll("div")
		.data(data) //data being sent in
			.enter() //invokes new data points
			.append("div")
			.style("height", 30)
			.style("width", function(data) {return (data.frequency/maxVal*1.0)*960 + "px"})
			.text(function(data) {return data.word})

});

```

Baller! Now we are finally done with the JavaScript implementation.

Now we can see the graph! You might need to restart the server, but refresh the webpage **localhost:8000** and you should see the graphs!


We are mostly done! Congrats!

####Bonus: CSS

CSS is responsible for the style of the website. Its what will make our drab webpage and stock chart fit the needs of our problem! Within data viz especially, the represemntstion matters. In the link tag at the top of the HTML file, use _ted.css_ instead of _index.css_





## Authors

* **@prewittdavon** - *Initial work* - [Profile](https://github.com/prewittdavon)

* **@saranyan** - *TED-Talks* - [TED-Talks](https://github.com/saranyan/TED-Talks)




