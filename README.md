
# GitSight

GitSight is a command-line tool that fetches insightful details about a GitHub repository. It provides information such as contributors, issues, labels, and the programming languages used in the repository. Additionally, it allows users to save this data for further analysis.

## Features

1. **Repository Details**: Fetches the description, stars, forks, and open issues of a repository.
2. **Contributors Insights**: Lists the top contributors along with their contribution counts.
3. **Issues Analysis**: Breaks down open issues by labels, providing a detailed overview.
4. **Language Usage**: Shows the percentage of code written in each programming language.
5. **Save to File**: Optionally saves all fetched data in JSON format for further use.

## Installation

To use GitSight, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/valkarinc/GitSight.git
   cd GitSight
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. Then install the required dependencies using pip:
   ```bash
   pip install requests
   ```

3. **Set Up a GitHub Personal Access Token** (Optional):
   - If you want to fetch private repository details or avoid rate limits, create a GitHub Personal Access Token:
     - Go to your GitHub profile > Settings > Developer settings > Personal Access Tokens > Tokens (classic).
     - Generate a token and copy it.
   - Use the token with the `--token` argument when running the tool.

## Usage

Run the tool using Python and provide the required arguments:

### Basic Usage
```bash
python github_repo_insights.py <owner> <repo>
```

- `<owner>`: The username or organization name of the repository owner.
- `<repo>`: The name of the repository.

### Example:
```bash
python github_repo_insights.py torvalds linux
```

### Optional Arguments:
- `--token`: Use your GitHub Personal Access Token for authenticated requests.
- `--save`: Save the output data to a JSON file.

### Example with Token and Save:
```bash
python github_repo_insights.py torvalds linux --token <your-token> --save output.json
```

## Output

1. **Repository Information**:
   ```
   Repository: torvalds/linux
   Description: Linux kernel source tree
   Stars: 150000
   Forks: 70000
   Open Issues: 300
   ```

2. **Top Contributors**:
   ```
   Top Contributors:
   - LinusTorvalds (5000 contributions)
   - Developer1 (3000 contributions)
   - Developer2 (1500 contributions)
   ```

3. **Issues by Label**:
   ```
   Open Issues by Label:
   - bug: 50
   - enhancement: 20
   - question: 10
   ```

4. **Language Usage**:
   ```
   Languages Used:
   - C: 85.00%
   - Assembly: 10.00%
   - Python: 5.00%
   ```

5. **Saved Output**:
   If the `--save` argument is used, the data is saved in JSON format:
   ```json
   {
       "repository": { ... },
       "contributors": [ ... ],
       "issues": { "by_label": { ... } },
       "languages": { ... }
   }
   ```

## Error Handling

- If required arguments (`owner` and `repo`) are missing, the program displays usage instructions.
- If the GitHub API rate limit is reached, use a Personal Access Token with the `--token` argument.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to enhance GitSight.
