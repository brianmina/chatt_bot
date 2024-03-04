import re


def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus


def remove_chat_metadata(chat_export_file):
    date_time_am_pm_dash = r"\d+\/\d+\/\d+,\s\d+:\d+\s\w\w\s-\s"  #"9/16/22 am/pm,  " - "
    username = r"[\w\s]+.[\s\w]+"  # Brian and Erwin name
    metadata_end = r":\s"  # ": "
    pattern = date_time_am_pm_dash + username + metadata_end

    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content)
    return tuple(cleaned_corpus.split("\n"))


def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]

    filter_out_msgs = ("<Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))


file_test = clean_corpus("chat_brother.txt")
print(file_test)
