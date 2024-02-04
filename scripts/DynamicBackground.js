const repoUrl = window.repoUrl || 'https://omarjuvera.github.io/Portfolios/';
const portfolioUrl = getPortfolioUrl(repoUrl);

function getPortfolioUrl(repoUrl) {
	try {
		const sanitizedUrl = window.location.href.replace(repoUrl, '');
		return (sanitizedUrl === repoUrl || sanitizedUrl.startsWith(repoUrl)) ? '' : sanitizedUrl.split('/')[0];
	} catch (error) {
		console.log('Using default portfolio:', error.message);
		return ''; // Set to default (empty string) in case of an issue
	}
}

function setNewBackground() {
	try {
		const backgroundUrl = BackgroundModule.getBackgroundUrl(portfolioUrl);
		document.body.style.backgroundImage = backgroundUrl;
		console.log(`Background changed to ${portfolioUrl}`);
	} catch (error) {
		console.log('Using default background:', error.message);
		document.body.style.backgroundImage = BackgroundModule.getBackgroundUrl(''); // Set to default in case of an issue
	}
}

setNewBackground();