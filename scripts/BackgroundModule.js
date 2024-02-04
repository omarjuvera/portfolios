// BackgroundModule.js
const BackgroundModule = (function () {
	// Define array of backgrounds with corresponding URLs
	const backgrounds = [
		{ portfolio: 'Portfolios', url: 'url(https://repository-images.githubusercontent.com/736133296/80d2132b-b291-4b86-a4b6-6b66250785c4)' },
		{ portfolio: 'Cybersecurity', url: 'url(https://raw.githubusercontent.com/omarjuvera/Portfolios/assets/images/backgrounds/cybersecurity/stock-photo.jpg)' },
		{ portfolio: 'Python', url: 'url(path/to/image2.jpg)' },
		// Add more portfolios and corresponding URLs as needed
	];

	function getBackgroundUrl(portfolioUrl) {
		// Check if portfolioUrl is empty or falsy, and return the default background URL
		if (!portfolioUrl) {
			return backgrounds.find(bg => bg.portfolio === 'Portfolios')?.url || '';
		}

		// Check if portfolioUrl is in the available portfolios
		const foundPortfolio = backgrounds.find(bg => bg.portfolio === portfolioUrl);

		// If found, return the background URL associated with the specific portfolio
		if (foundPortfolio) {
			return foundPortfolio.url || '';
		}

		// If not found, return the default background URL for 'Portfolios'
		return backgrounds.find(bg => bg.portfolio === 'Portfolios')?.url || '';
	}

	return {
		getBackgroundUrl,
	};
})();
