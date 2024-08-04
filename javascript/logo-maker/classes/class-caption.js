/* DOCUMENT INFORMATION
	- Document:	class-caption.js
	- Version:	1.2.4
	- Project:	Santa Monica College - Logo Maker
	- Author:	Omar Juvera

 * Controls the text of the log's caption
 * Depends on data-fonts.js
 * Run hibrid, asyncronous (code loaded) + syncronous (DOMContentLoaded)

*/

import { fonts } from '../data/data-fonts.js';

class Caption {
	constructor() {
		this.text = document.getElementById("logo-text");
		this.logo = document.getElementById("logo");
		this.fontFamily = document.getElementById("logo-font");
		this.weight = document.getElementById("logo-font-weight");
		this.size = document.getElementById("logo-size");
		this.color = document.getElementById("logo-color");
		this.left = document.getElementById("logo-position-left");
		this.top = document.getElementById("logo-position-top");
	}

	init() {
		this.setEventListeners();
		this.populateFonts();
	}

	populateFonts() {
		fonts.forEach(font => {
			const option = document.createElement("option");
			//option.value = font.name;
			option.value = `'${font.name}', sans-serif`;
			option.textContent = font.name;
			this.fontFamily.appendChild(option);
		});
	}

	sanitizeInput(input) {
		const element = document.createElement("div");
		element.innerText = input; // `innerText` automatically escapes special characters
		return element.innerHTML;
	}

	updateText() {
		const sanitizedText = this.sanitizeInput(this.text.value);
		this.logo.textContent = sanitizedText;
	}

	setFontFamily() {
		const selectedFont = this.fontFamily.value || "Arial, sans-serif";
		// Preformated in populateFonts(): option.value = `'${font.name}', sans-serif`;
		this.logo.style.fontFamily =  selectedFont;
	}

	setFontWeight() {
		const selectedWeight = this.weight.value;
		this.logo.style.fontWeight = selectedWeight;
	}

	setFontSize() {
		const selectedSize = this.size.value + "px";
		this.logo.style.fontSize = selectedSize;
	}

	setFontColor() {
		const selectedColor = this.color.value;
		this.logo.style.color = selectedColor;
	}

	setPosition() {
		const leftPosition = this.left.value + "%";
		const topPosition = this.top.value + "%";
		this.logo.style.left = leftPosition;
		this.logo.style.top = topPosition;
		this.logo.style.position = 'absolute'; // Ensure positioning is applied
	}

	updateCaption() {
		this.setFontFamily();
		this.setFontWeight();
		this.setFontSize();
		this.setFontColor();
		this.setPosition();
	}

	addListenerText() {
		this.text.addEventListener("input", () => this.updateText());
	}

	addListenerFontFamily() {
		this.fontFamily.addEventListener("change", () => this.updateCaption());
	}

	addListenerFontWeight() {
		this.weight.addEventListener("change", () => this.updateCaption());
	}

	addListenerFontSize() {
		this.size.addEventListener("input", () => this.updateCaption());
	}

	addListenerFontColor() {
		this.color.addEventListener("input", () => this.updateCaption());
	}

	addListenerPositionLeft() {
		this.left.addEventListener("input", () => this.updateCaption());
	}

	addListenerPositionTop() {
		this.top.addEventListener("input", () => this.updateCaption());
	}

	setEventListeners() {
		this.addListenerText();
		this.addListenerFontFamily();
		this.addListenerFontWeight();
		this.addListenerFontSize();
		this.addListenerFontColor();
		this.addListenerPositionLeft();
		this.addListenerPositionTop();
	}

	static start() {
		document.addEventListener("DOMContentLoaded", () => {
			const LogoCaption = new Caption();
			LogoCaption.init();
		});
	}
}

// Start the Caption class
Caption.start();
