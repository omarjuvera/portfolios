class FileLister {
    constructor(username, repository, branch = 'main') {
        this.username = username;
        this.repository = repository;
        this.branch = branch;
    }

    async listFiles() {
        const url = `https://api.github.com/repos/${this.username}/${this.repository}/git/trees/${this.branch}?recursive=1`;

        try {
            const response = await fetch(url);
            const data = await response.json();
            
            if (response.ok && data.tree) {
                const files = data.tree.filter(item => item.type === 'blob').map(item => item.path);
                this.displayFiles(files);
            } else {
                throw new Error("Failed to fetch file list");
            }
        } catch (error) {
            console.error("Error:", error);
            document.getElementById('file-list').textContent = "Failed to load file list.";
        }
    }

    displayFiles(files) {
        const fileList = files.join("\n");
        document.getElementById('file-list').textContent = fileList;
    }
}

// Instantiate the FileLister class with your GitHub username, repository name, and branch
const fileLister = new FileLister('your-username', 'your-repository');
