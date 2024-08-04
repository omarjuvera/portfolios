/* DOCUMENT INFORMATION
	- Document:	class-canvas-color.js
	- Version:	1.2.4
	- Project:	Santa Monica College - Logo Maker
	- Author:	Omar Juvera

 * Controls the background color
 * Does not depend on external data
 * Must run syncronous (DOMContentLoaded)

*/

class LogoCanvasColor {
	constructor() {
		this.backgroundType = document.getElementById('background-color-type');
		this.color1 = document.getElementById('background-color-1');
		this.color2 = document.getElementById('background-color-2');
		this.canvas = document.getElementById('canvas');
		this.labelColor1 = document.querySelector('label[for="background-color-1"]');
		this.labelColor2 = document.querySelector('label[for="background-color-2"]');
		this.type = "solid";
	}

	init() {
		this.setBackground();
		this.addEventListeners();
	}

	addEventListeners() {
		this.backgroundType.addEventListener('change', () => this.updateLabels());
		this.color1.addEventListener('input', () => this.updateBackgroundColor());
		this.color2.addEventListener('input', () => this.updateBackgroundColor());
	}

	updateLabels() {
		if ( this.backgroundType.value === "solid" && this.type === "gradient" ) {
			this.labelColor1.textContent = "Solid color:";
			this.labelColor2.style.display = "none";
			this.color2.style.display = "none";
			this.setBackground("solid");
		}
		else if ( this.backgroundType.value != "solid" && this.type === "solid") {
			this.labelColor1.textContent = "Gradient color 1:";
			this.labelColor2.style.display = "block";
			this.color2.style.display = "block";
			this.setBackground("gradient");
		}

		//this.updateBackgroundColor();
	}

	setBackground (type) {
		switch (type) {
			case "solid":
				this.type = "solid";
				this.canvas.style.background = this.color1.value;
			case "gradient":
				this.type = "gradient";
				const color2 = this.color2.value;
				const gradient = this.getGradient(colorType, color1, color2);
				this.canvas.style.background = gradient;
			}
	}

	updateBackgroundColor() {
		const colorType = this.backgroundType.value;
		const color1 = this.color1.value;

		if (colorType === 'solid') {
			this.canvas.style.background = color1;
		} else {
			const color2 = this.color2.value;
			const gradient = this.getGradient(colorType, color1, color2);
			this.canvas.style.background = gradient;
		}
	}

	getGradient(type, color1, color2) {
		switch (type) {
			case 'radial':
				return `radial-gradient(circle, ${color1}, ${color2})`;
			case 'conic':
				return `conic-gradient(${color1}, ${color2})`;
			case 'linear':
			default:
				return `linear-gradient(to right, ${color1}, ${color2})`;
		}
	}

	setBackground() {
		this.canvas.style.background = this.color1.value;
		this.labelColor2.style.display = 'none';
		this.color2.style.display = 'none';
	}

	static start() {
		document.addEventListener('DOMContentLoaded', () => {
			const CanvasColor = new LogoCanvasColor();
			CanvasColor.init();
		});
	}
}

LogoCanvasColor.start();
