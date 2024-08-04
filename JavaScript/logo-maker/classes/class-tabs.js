/* DOCUMENT INFORMATION
	- Document:	class-shapes.js
	- Version:	1.2.4
	- Project:	Santa Monica College - Logo Maker
	- Author:	Omar Juvera

 * Controls the tabs and toggle behavior
 * Does not depend on external data
 * Run syncronous (DOMContentLoaded)

*/

class LogoTabs {
	constructor() {
		this.init();
	}

	init() {
		this.addListenerTabs();
	}

	addListenerTabs() {
		document.querySelectorAll('.tab').forEach(tab => {
			tab.addEventListener('click', function() {
				document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
				document.querySelectorAll('.tab-content').forEach(tc => tc.classList.remove('active'));
				this.classList.add('active');
				document.getElementById(this.getAttribute('data-tab')).classList.add('active');
			});
		});
	}

	static start() {
		document.addEventListener('DOMContentLoaded', () => {
			const Tabs = new LogoTabs();
		});
	}
}

LogoTabs.start();
