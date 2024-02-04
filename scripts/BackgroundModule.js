<!-- BackgroundModule.js -->
<script id="background-module">
    const BackgroundModule = (function () {
        const backgrounds = [
            { portfolio: 'Portfolios', url: 'url(https://repository-images.githubusercontent.com/736133296/80d2132b-b291-4b86-a4b6-6b66250785c4)' },
            { portfolio: 'Cybersecurity', url: 'url(https://raw.githubusercontent.com/omarjuvera/Portfolios/assets/images/backgrounds/cybersecurity/stock-photo.jpg)' },
            { portfolio: 'Python', url: 'url(path/to/image2.jpg)' },
            // Add more portfolios and corresponding URLs as needed
        ];

        function getBackgroundUrl(portfolioUrl) {
            const background = backgrounds.find(bg => bg.portfolio === portfolioUrl);
            return background ? background.url : backgrounds[0].url;
        }

        return {
            getBackgroundUrl,
        };
    })();
</script>
