from transformers import pipeline
import requests as re

labels = ['toxic', 'racist', 'gender bias', 'religious bias', 'aggressive',
          'personal attacks', 'hate speech', 'offensive language']

# model chosen is fbbart
model = pipeline("zero-shot-classification",
                 model="facebook/bart-large-mnli")


def zero_shot_classifier(text, model=model, labels=labels):
    text = text
    prediction = model(text, labels, multi_label=True)
    if prediction["scores"][0] < 0.75:
        return False
    else:
        return str(prediction["labels"][0])


# catch darkweb links
def dark_web_links(text):
    # Regular expression pattern to match common dark web link formats
    dark_web_pattern = r"(https?://)?[a-z0-9]+\.onion(/[a-zA-Z0-9]*)*"

    # Search for dark web links in the text
    matches = re.findall(dark_web_pattern, text)

    if matches:
        return True
    else:
        return False


# catch adult content links
def adult_content_sites(text):
    # Regular expression pattern to match common adult content websites
    adult_content_pattern = r"(https?://)?(?:www\.)?(pornhub\.com|xnxx\.com|youporn\.com|redtube\.com|etc)\b"

    # Search for adult content sites in the text
    matches = re.findall(adult_content_pattern, text)

    # If any matches are found, flag them
    if matches:
        return True
    else:
        return False


def content_moderator(text, labels=labels, model=model, classifier=zero_shot_classifier, dkweb=dark_web_links, adult=adult_content_sites):
    if dkweb(text):
        return 'Darkweb link'
    elif adult(text):
        return 'Adult content site'
    elif classifier(text):
        return 'Flagged content'
