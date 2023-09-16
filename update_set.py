from pathlib import Path
from typing import NamedTuple

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tabulate import tabulate

class Problem(NamedTuple):
    name: str
    url: str

def normalize(string: str):
    return "_".join(string.lower().replace("-", "_").split())

if __name__ == "__main__":
    # Fetch the problem list page
    response = requests.get("https://cses.fi/problemset/list/")
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract problem types and problem lists
    problem_types = [item.text for item in soup.find_all("h2")]
    problem_list_tags = soup.find_all("ul")
    problems = [
        [
            Problem(item.find("a").text, item.find("a")["href"])
            for item in problem_list_tag.find_all("li")
        ]
        for problem_list_tag in problem_list_tags
    ]

    top_level_readme_table = {"Topic": [], "Solution": []}
    root_path = Path(__file__).parent

    # Loop through problem types and their corresponding problems
    for topic_index, (problem_type, problem_list) in enumerate(
        zip(problem_types[1:], problems[2:]), start=1
    ):
        topic_level_readme_table = {"Problem": [], "Link": [], "Solution": [], "Solved": []}
        problem_type_folder = f"{topic_index:02d}_{normalize(problem_type)}"
        topic_folder_path = root_path / problem_type_folder

        for index, problem in enumerate(problem_list, start=1):
            solution_path = topic_folder_path / f"{index:02d}_{normalize(problem.name)}.py"
            solution_path.parent.mkdir(exist_ok=True, parents=True)
            problem_url = f"https://cses.fi{problem.url}"

            if not solution_path.exists():
                # Create a solution script if it doesn't exist
                solution_path.touch()
                response = requests.get(problem_url)
                soup = BeautifulSoup(response.text, "html.parser")
                content = soup.find("div", {"class": "content"})
                description = f'"""\n{md(content.text)}\n"""'
                solution_path.write_text(description)
                print(f"Successfully written {solution_path}")

            # Populate the topic-level readme table
            topic_level_readme_table["Problem"].append(problem.name)
            topic_level_readme_table["Link"].append(f"[Link]({problem_url})")
            topic_level_readme_table["Solution"].append(f"[Solution](./{solution_path.name})")
            topic_level_readme_table["Solved"].append("__main__" in solution_path.read_text())

        # Populate the top-level readme table
        top_level_readme_table["Topic"].append(problem_type)
        top_level_readme_table["Solution"].append(f"[Link](./{problem_type_folder})")

        # Generate and write the topic-level readme
        readme_path = topic_folder_path / "README.md"
        readme_path.touch()
        readme_path.write_text(tabulate(topic_level_readme_table, headers="keys", tablefmt="github"))

    # Generate and write the top-level readme
    readme_path = root_path / "README.md"
    readme_path.touch()
    readme_content = f"""## How I update this repo?

Most of the things are automated like:

- creating problem solution script.
- generating readme.
- marking a problem as solved.

I generally will solve the problem and then run `python update_set.py` and it should take care of updating all the readme. Even add problems if any new problem is added.

---

{tabulate(top_level_readme_table, headers="keys", tablefmt="github")}

"""
    readme_path.write_text(readme_content)
