import re
import json
import os
import threading
import requests

"""

Not meant to be used as a module. This script is used to obtain recipes from the website allrecipes.com and save them as JSON files.
"""

links_pattern_NODE = r"https:\/\/www\.allrecipes\.com\/recipes/[0-9]{2,5}/.*/"
links_pattern_RECIPE = r"https:\/\/www\.allrecipes\.com\/(recipe\/[0-9]*\/[a-zA-Z\-]*\/|[a-zA-Z\-]*recipe-\d+)"

before_json_embed = r'<script id="allrecipes-schema_1-0" class="comp allrecipes-schema mntl-schema-unified" type="application/ld+json">['
after_json_embed = r"]</script>"

urls = [
    "https://www.allrecipes.com/recipe/14522/pizza-on-the-grill-i/",
]


def get_text_from_web(url):
    # some code to get the text from the web
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Error"


def delete_match(regex, text):
    regex = re.escape(regex)
    return re.sub(regex, "", text)


def delete_before_match(regex, text):
    regex = re.escape(regex)
    return re.sub(f"^.*?{regex}", "", text, flags=re.DOTALL)


def delete_after_match(regex, text):
    return re.sub(f"{regex}.*?$", "", text, flags=re.DOTALL)


def cut_match(regex, text):

    return re.findall(regex, text)


def clean_file(file):

    with open(file, "r+", encoding="utf-8") as f:
        text = f.read()

    text = delete_match(links_pattern, text)

    with open(file, "w", encoding="utf-8") as f:
        f.seek(0)
        f.truncate()
        f.write(text)

def recursive_recipe_search(url, urls, visited_nodes=set(), visited_recipes=set(), depth=0, max_depth=10):
    
    if depth > max_depth:
        return 

    text = get_text_from_web(url)
    new_links = cut_match(links_pattern_NODE, text)
    recipe_links = cut_match(links_pattern_RECIPE, text)
    
    threads = []
    for link in recipe_links:
        if link not in visited_recipes:
            link = f"https://www.allrecipes.com/{link}"
            threads.insert(0, threading.Thread(target=make_json, args=(link,)))
            threads[0].start()
            visited_recipes.add(link)
            urls.append(link)

    for thread in threads:
        thread.join()
    
    for link in new_links:
        if link not in visited_nodes:
            visited_nodes.add(link)
            urls.append(link)
            recursive_recipe_search(link, urls, visited_nodes, visited_recipes, depth + 1, max_depth)

def make_json(url):
    text: str = get_text_from_web(url)

    text = delete_before_match(before_json_embed, text)
    text = delete_after_match(after_json_embed, text)
    

    
    text = re.sub("&#39;", "'", text)
    # Load JSON data from the string
    data = json.loads(text)

    # Extract the keys you want
    desired_keys = [
        "headline",
        "name",
        "description",
        "recipeCuisine",
        "totalTime",
        "cookTime",
        "nutrition",
        "prepTime",
        "recipeCategory",
        "recipeIngredient",
        "recipeInstructions",
        "recipeYield",
    ]
    filtered_data = {key: data[key] for key in desired_keys if key in data}

    headline = data["headline"]

    first_cuisine = data["recipeCuisine"][0]
    if " " in first_cuisine:
        first_cuisine = first_cuisine.split(" ")[0]

    output_dir = f"recipes/{first_cuisine}"
    os.makedirs(output_dir, exist_ok=True)

    # Write the filtered data to the output file
    with open(f"{output_dir}/{headline}.json", "w", encoding="utf-8") as f:
        json.dump(filtered_data, f, indent=4)

recipes_urls = set()
recursive_recipe_search(urls[0], urls, visited_recipes=recipes_urls )
print(recipes_urls)