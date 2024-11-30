import re
import json
import os

"""

Not meant to be used as a module. This script is used to obtain recipes from the website allrecipes.com and save them as JSON files.
"""

links_pattern_NODE = r"https:\/\/www\.allrecipes\.com\/recipes/[0-9]{2,5}/.*/"
links_pattern_RECIPE = r"https:\/\/www\.allrecipes\.com\/(recipe\/|.*-recipe-\d+)"

before_json_embed = r'<script id="allrecipes-schema_1-0" class="comp allrecipes-schema mntl-schema-unified" type="application/ld+json">['
after_json_embed = r"]</script>"

urls = [
    "https://www.allrecipes.com/recipe/14522/pizza-on-the-grill-i/",
    "https://www.allrecipes.com/recipe/23600/worlds-best-lasagna/",
    "https://www.allrecipes.com/recipe/229960/shrimp-scampi-with-pasta/",
    "https://www.allrecipes.com/recipe/40399/the-best-meatballs/",
    "https://www.allrecipes.com/recipe/246717/indian-butter-chicken-chicken-makhani/",
    "https://www.allrecipes.com/recipe/45736/chicken-tikka-masala/",
    "https://www.allrecipes.com/recipe/16641/red-lentil-curry/",
    "https://www.allrecipes.com/recipe/8467738/green-onion-garlic-naan-bread/",
    "https://www.allrecipes.com/recipe/257988/traditional-mexican-street-tacos/",
    "https://www.allrecipes.com/recipe/213700/enchiladas-verdes/",
    "https://www.allrecipes.com/recipe/34759/beef-tamales/",
    "https://www.allrecipes.com/recipe/70404/fabulous-wet-burritos/",
    "https://www.allrecipes.com/recipe/72068/chicken-katsu/",
    "https://www.allrecipes.com/recipe/140422/onigiri-japanese-rice-balls/",
    "https://www.allrecipes.com/recipe/190943/spicy-tuna-sushi-roll/",
    "https://www.allrecipes.com/recipe/13107/miso-soup/",
    "https://www.allrecipes.com/recipe/216330/german-pork-chops-and-sauerkraut/",
    "https://www.allrecipes.com/recipe/78117/wienerschnitzel/",
    "https://www.allrecipes.com/recipe/24674/german-zwiebelkuchen-onion-pie/",
    "https://www.allrecipes.com/recipe/24676/german-currywurst/",
]


def get_text_from_web(url):
    # some code to get the text from the web
    import requests

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


while len(urls) < 1000:
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
