/* DOCUMENT INFORMATION
	- Document:	data-shapes.js
	- Version:	1.2.4
	- Project:	Santa Monica College - Logo Maker
	- Author:	Omar Juvera

 * Contains all the CSS shape's data

*/

export const shapes = [
	{
		"name": "Badge Ribbon",
		"css-class": "badge-ribbon",
		"class-rules": ".shape-color { background-color: $[color]; } .shape-color:before, .shape-color:after { border-bottom-color: $[color]; }"
	},
	{
		"name": "Base",
		"css-class": "base",
		"class-rules": ".shape-color { background-color: $[color]; } .shape-color:before { border-bottom-color: $[color]; }"
	},
	{
		"name": "Burst: 8 Points",
		"css-class": "burst-8",
		"class-rules": ".shape-color { background-color: $[color]; } .shape-color:before { background-color: $[color]; }"
	},
	{
		"name": "Burst: 12 Points",
		"css-class": "burst-12",
		"class-rules": ".shape-color { background-color: $[color]; } .shape-color:before, .shape-color:after { background-color: $[color]; }"
	},
	{
		"name": "Chevron",
		"css-class": "chevron",
		"class-rules": ".shape-color { } .shape-color:before { background-color: $[color]; } .shape-color:after { background-color: $[color]; }"
	},
	{
		"name": "Circle",
		"css-class": "circle",
		"class-rules": ".shape-color { background-color: $[color]; }"
	},
	{
		"name": "Cone",
		"css-class": "cone",
		"class-rules": ".shape-color { border-top-color: $[color]; }"
	},
	{
		"name": "Cross",
		"css-class": "cross",
		"class-rules": ".shape-color { background-color: $[color]; } .shape-color:after { background-color: $[color]; }"
	},
	{
		"name": "Diamond",
		"css-class": "diamond",
		"class-rules": ".shape-color { border-bottom-color: $[color]; } .shape-color:after { border-top-color: $[color]; }"
	},
	{
		"name": "Diamond: Cut",
		"css-class": "cut-diamond",
		"class-rules": ".shape-color { border-color: transparent transparent $[color] transparent; } .shape-color:after { border-color: $[color] transparent transparent transparent; }"
	},
	{
		"name": "Diamond: Narrow",
		"css-class": "diamond-narrow",
		"class-rules": ".shape-color { border-bottom-color: $[color]; } .shape-color:after { border-top-color: $[color]; }"
	},
	{
		"name": "Diamond: Shield",
		"css-class": "diamond-shield",
		"class-rules": ".shape-color { border-bottom-color: $[color]; } .shape-color:after { border-top-color: $[color]; }"
	},
	{
		"name": "Egg",
		"css-class": "egg",
		"class-rules": ".shape-color { background-color: $[color]; }"
	},
	{
		"name": "Flag",
		"css-class": "flag",
		"class-rules": ".shape-color { background-color: $[color]; }"
	},
	{
		"name": "Heart",
		"css-class": "heart",
		"class-rules": ".shape-color { } .shape-color:before, .shape-color:after { background-color: $[color]; }"
	},
	{
		"name": "Hexagon",
		"css-class": "hexagon",
		"class-rules": ".shape-color { background-color: $[color]; } .shape-color::before { border-bottom-color: $[color]; } .shape-color::after { border-top-color: $[color]; }"
	},
	{
		"name": "Infinity",
		"css-class": "infinity",
		"class-rules": ".shape-color { } .shape-color:before, .shape-color:after { border-color: $[color]; }"
	},
	{
		"name": "Lock",
		"css-class": "lock",
		"class-rules": ".shape-color { border-color: $[color]; } .shape-color:before, .shape-color:after { border-color: $[color]; }"
	},
	{
		"name": "Magnifying Glass",
		"css-class": "magnifying-glass",
		"class-rules": ".shape-color { border-color: $[color]; } .shape-color:before { background-color: $[color]; }"
	},
	{
		"name": "Moon",
		"css-class": "moon",
		"class-rules": ".shape-color { /*box-shadow*/ color: $[color]; }"
	},
	{
		"name": "Oval",
		"css-class": "oval",
		"class-rules": ".shape-color { background-color: $[color]; }"
	},
	{
		"name": "Pacman",
		"css-class": "pacman",
		"class-rules": ".shape-color { border-top-color: $[color]; border-left-color: $[color]; border-bottom-color: $[color]; }"
	},
	{
		"name": "Parallelogram",
		"css-class": "parallelogram",
		"class-rules": ".shape-color { background-color: $[color]; }"
	},
	{
		"name": "Pentagon",
		"css-class": "pentagon",
		"class-rules": ".shape-color { border-color: $[color] transparent; } .shape-color:before { border-color: transparent transparent $[color]; }"
	},
	{
		"name": "Pointer",
		"css-class": "pointer",
		"class-rules": ".shape-color { background-color: $[color]; } .shape-color:before { border-left-color: $[color]; }"
	},
	{
		"name": "Rectangle",
		"css-class": "rectangle",
		"class-rules": ".shape-color { background-color: $[color]; }"
	},
	{
		"name": "Space Invader",
		"css-class": "space-invader",
		"class-rules":	".shape-color { box-shadow: 0 0 0 1em $[color], 0 1em 0 1em $[color], -2.5em 1.5em 0 .5em $[color], 2.5em 1.5em 0 .5em $[color], -3em -3em 0 0 $[color], 3em -3em 0 0 $[color], -2em -2em 0 0 $[color], 2em -2em 0 0 $[color], -3em -1em 0 0 $[color], -2em -1em 0 0 $[color], 2em -1em 0 0 $[color], 3em -1em 0 0 $[color], -4em 0 0 0 $[color], -3em 0 0 0 $[color], 3em 0 0 0 $[color], 4em 0 0 0 $[color], -5em 1em 0 0 $[color], -4em 1em 0 0 $[color], 4em 1em 0 0 $[color], 5em 1em 0 0 $[color], -5em 2em 0 0 $[color], 5em 2em 0 0 $[color], -5em 3em 0 0 $[color], -3em 3em 0 0 $[color], 3em 3em 0 0 $[color], 5em 3em 0 0 $[color], -2em 4em 0 0 $[color], -1em 4em 0 0 $[color], 1em 4em 0 0 $[color], 2em 4em 0 0 $[color]; background-color: $[color]; }"
	},
	{
		"name": "Square",
		"css-class": "square",
		"class-rules": ".shape-color { background-color: $[color]; }"
	},
	{
		"name": "Star: Five Points",
		"css-class": "star-five",
		"class-rules": ".shape-color { color: $[color]; border-bottom-color: $[color]; } .shape-color:before, .shape-color:after { border-bottom-color: $[color]; } .shape-color:after { color: $[color]; }"
	},
	{
		"name": "Star: Six Points",
		"css-class": "star-six",
		"class-rules": ".shape-color { border-bottom-color: $[color]; } .shape-color:after { border-top-color: $[color]; }"
	},
	{
		"name": "Talk Bubble",
		"css-class": "talkbubble",
		"class-rules": ".shape-color { background-color: $[color]; } .shape-color:before { border-right-color: $[color]; }"
	},
	{
		"name": "Trapezoid",
		"css-class": "trapezoid",
		"class-rules": ".shape-color { border-bottom-color: $[color]; }"
	},
	{
		"name": "Triangle: Bottom Left",
		"css-class": "triangle-bottomleft",
		"class-rules": ".shape-color { border-bottom-color: $[color]; }"
	},
	{
		"name": "Triangle: Bottom Right",
		"css-class": "triangle-bottomright",
		"class-rules": ".shape-color { border-bottom-color: $[color]; }"
	},
	{
		"name": "Triangle: Down",
		"css-class": "triangle-down",
		"class-rules": ".shape-color { border-top-color: $[color]; }"
	},
	{
		"name": "Triangle: Left",
		"css-class": "triangle-left",
		"class-rules": ".shape-color { border-right-color: $[color]; }"
	},
	{
		"name": "Triangle: Right",
		"css-class": "triangle-right",
		"class-rules": ".shape-color { border-left-color: $[color]; }"
	},
	{
		"name": "Triangle: Top Left",
		"css-class": "triangle-topleft",
		"class-rules": ".shape-color { border-top-color: $[color]; }"
	},
	{
		"name": "Triangle: Top Right",
		"css-class": "triangle-topright",
		"class-rules": ".shape-color { border-top-color: $[color]; }"
	},
	{
		"name": "Triangle: Up",
		"css-class": "triangle-up",
		"class-rules": ".shape-color { border-bottom-color: $[color]; }"
	},
	{
		"name": "TV",
		"css-class": "tv",
		"class-rules": ".shape-color { background-color: $[color]; }"
	},
	{
		"name": "Yin Yang",
		"css-class": "yin-yang",
		"class-rules": ".shape-color { border-color: $[color]; } .shape-color:before { border-color: $[color]; } .shape-color:after { background-color: $[color]; }"
	}
];