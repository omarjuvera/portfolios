/* DOCUMENT INFORMATION
	- Document:	class-fonts-samples.js
	- Version:	1.2.4
	- Project:	Santa Monica College - Logo Maker
	- Author:	Omar Juvera

 * Controls the content of the tab: Font Samples
 * Depends on data-fonts.js
 * Run hibrid, asyncronous (code loaded) + syncronous (DOMContentLoaded)

*/

import { fonts } from '../data/data-fonts.js';

class FontSamples {
	constructor() {
		//this.fonts = fonts;
		this.masonry = null;
		this.size = null;
		this.weight = null;
		this.color = null;
	}

	init() {
		this.masonry = this.getElement('masonry');
		this.size = this.getElement('fontSize');
		this.weight = this.getElement('fontWeight');
		this.color = this.getElement('fontColor');

		this.makeFontSampleItems();
		this.addListenerStyleTools();
	}

	getElement(id) {
		return document.getElementById(id);
	}

	makeFontSampleItems() {
		this.masonry.innerHTML = ''; // Clear existing content

		fonts.forEach(font => {
			const item = document.createElement('div');
			item.className = 'masonry-item';
			item.style.fontFamily = `${font.name}, sans-serif`;
			item.innerHTML = `
				<p class="font-name">• ${font.name}:</p>
				<p>Sample text</p>
			`;
			this.masonry.appendChild(item);
		});
	}

	addListenerStyleTools() {
		const updateStyles = () => {
			const fontSize = this.size.value + 'px';
			const fontWeight = this.weight.value;
			const fontColor = this.color.value;

			this.masonry.style.fontSize = fontSize;
			this.masonry.style.fontWeight = fontWeight;
			this.masonry.style.color = fontColor;
		};

		this.size.addEventListener('input', updateStyles);
		this.weight.addEventListener('change', updateStyles);
		this.color.addEventListener('input', updateStyles);
	}

	static start() {
		document.addEventListener('DOMContentLoaded', () => {
			const FontSamplesTabContent = new FontSamples();
			FontSamplesTabContent.init();
		});
	}
}

FontSamples.start();
