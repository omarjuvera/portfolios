/* DOCUMENT INFORMATION
	- Document:	class-shapes.js
	- Version:	1.2.4
	- Project:	Santa Monica College - Logo Maker
	- Author:	Omar Juvera

 * Controls the shapes of the Logo app
 * Depends on data-shapes.js
 * Run syncronous (DOMContentLoaded)

*/

import { shapes } from '../data/data-shapes.js';

class LogoShapes {
	constructor() {
		this.shape = document.getElementById("shape");
		this.dropdown = document.getElementById("shape-menu");
		this.size = document.getElementById("shape-size");
		this.color = document.getElementById("shape-color");
		this.left = document.getElementById("shape-position-left");
		this.top = document.getElementById("shape-position-top");
		this.rotation = document.getElementById("shape-rotate");
		this.zIndexToggle = document.getElementById("shape-z-index");
		this.colorValue = "red";
	}

	init() {
		this.populateDropdown();
		this.setEventListeners();
		this.startupShape();
	}

	populateDropdown() {
		shapes.forEach(shape => {
			const option = document.createElement('option');
			option.value = shape['css-class'];
			option.textContent = shape.name;
			this.dropdown.appendChild(option);
		});
	}

	setEventListeners() {
		this.addListenerShapes();
		this.addListenerShapeSize();
		this.addListenerShapeColor();
		this.addListenerShapePosition();
		this.addListenerRotate();
		this.addListenerShapeZIndex();
	}

	startupShape() {
		const newDefaultShape = "space-invader";
		this.dropdown.value = newDefaultShape;
		this.shape.className = newDefaultShape;
	}

	addListenerShapes() {
		this.dropdown.addEventListener('change', (event) => {
			//const selectedClass = this.dropdown.value; Had some errors. Also falling back to [event] for moudularity
			const selectedClass = event.target.value;
			this.shape.className = selectedClass;
			this.applyColorStyle(selectedClass, this.color.value);
		});
	}

	addListenerShapeSize() {
		this.size.addEventListener('input', (event) => {
			const size = event.target.value;
			this.shape.style.scale = size / 100;
		});
	}

	addListenerShapeColor() {
		this.color.addEventListener('input', () => {
			const selectedShapeClass = this.dropdown.value;
			const selectedColor = this.color.value;
			this.applyColorStyle(selectedShapeClass, selectedColor);
		});
	}

	addListenerShapePosition() {
		this.left.addEventListener('input', (event) => {
			const left = event.target.value;
			this.shape.style.left = `${left}%`;
		});

		this.top.addEventListener('input', (event) => {
			const top = event.target.value;
			this.shape.style.top = `${top}%`;
		});
	}

	addListenerRotate() {
		this.rotation.addEventListener('input', (event) => {
			const rotation = event.target.value;
		this.shape.style.rotate = `${rotation}deg`;
		});
	}

	addListenerShapeZIndex() {
		this.zIndexToggle.addEventListener('change', (event) => {
			const isOnTop = event.target.checked;
			this.shape.style.zIndex = isOnTop ? 3 : 1;
		});
	}

	applyColorStyle(shapeClass, color) {
		const selectedShape = shapes.find(shape => shape["css-class"] === shapeClass);
		if (!selectedShape) return;

		const styleRules = selectedShape["class-rules"].replace(/\$\[color\]/g, color);
		let styleSheet = document.getElementById("dynamic-styles");

		if (!styleSheet) {
			styleSheet = document.createElement("style");
			styleSheet.id = "dynamic-styles";
			document.head.appendChild(styleSheet);
		}

		styleSheet.textContent = styleRules;
		this.shape.className = `shape-color ${shapeClass}`;
	}

	static start() {
		document.addEventListener('DOMContentLoaded', () => {
			const Shape = new LogoShapes();
			Shape.init();
		});
	}
}

LogoShapes.start();
