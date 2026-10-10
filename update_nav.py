import os
import re

templates_dir = "templates"
mapping = {
    'data-path="dashboard" href="#"': 'data-path="dashboard" href="/"',
    'data-path="risk-analysis" href="#"': 'data-path="risk-analysis" href="/risk"',
    'data-path="citizen-report" href="#"': 'data-path="citizen-report" href="/citizen-report"',
    'data-path="flood-risk-map" href="#"': 'data-path="flood-risk-map" href="/map"',
    'data-path="historical-data" href="#"': 'data-path="historical-data" href="/historical"',
    'data-path="about-project" href="#"': 'data-path="about-project" href="/about"',
}

for filename in os.listdir(templates_dir):
    if filename.endswith(".html"):
        filepath = os.path.join(templates_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        for old, new in mapping.items():
            content = content.replace(old, new)
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
print("Navigation links updated successfully.")
