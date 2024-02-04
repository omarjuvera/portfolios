// DynamicContent.js
//-- GitHub API Script --
const username = 'omarjuvera';
const repo = 'Portfolios';

const scriptElement = document.currentScript;

const scriptPath = window.location.pathname.replace(/\/index\.html$/, '');
const directoryPath = window.location.pathname.replace(/^\//, '').replace(/\/index\.html$/, '');

const apiUrl = `https://api.github.com/repos/${username}/${repo}/contents/${directoryPath}`;

fetch(apiUrl)
	.then(response => response.json())
	.then(data => {
		const directoryList = document.getElementById('directory-list');

		data.forEach(item => {
			if (item.type === 'file') {
				const listItem = document.createElement('li');
				const link = document.createElement('a');
				link.href = `https://${username}.github.io/${repo}${directoryPath}/${item.name}`;
				link.textContent = item.name;
				listItem.appendChild(link);
				directoryList.appendChild(listItem);
			} else if (item.type === 'dir') {
				const listItem = document.createElement('li');
				const link = document.createElement('a');
				link.href = `https://${username}.github.io/${repo}${directoryPath}/${item.name}/`;
				link.textContent = item.name + '/';
				listItem.appendChild(link);
				directoryList.appendChild(listItem);
			}
		});
	})
	.catch(error => console.error('Error fetching directory content:', error));
