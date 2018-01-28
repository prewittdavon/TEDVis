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
