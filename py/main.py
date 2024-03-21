from enum import Enum
import copy


def convert_file_format(filename, target_format):
    valid_extensions = ["docx", "pdf", "txt", "pptx", "ppt", "md"]
    valid_conversions = {
        "docx": ["pdf", "txt", "md"],
        "pdf": ["docx", "txt", "md"],
        "txt": ["docx", "pdf", "md"],
        "pptx": ["ppt", "pdf"],
        "ppt": ["pptx", "pdf"],
        "md": ["docx", "pdf", "txt"],
    }
    current_format = filename.split(".")[-1]
    if (
        current_format in valid_extensions
        and target_format in valid_conversions[current_format]
    ):
        return filename.replace(current_format, target_format)
    return None

# We have a way for Doc2Doc users to set their supported formats in their settings. In memory, we store those settings as a simple dictionary:
#
# settings = {
#     "docx": True,
#     "pdf": True,
#     "txt": False
# }
# Copy icon
# Unfortunately, there is a bug in our code! When a new format is added or removed, it not only updates the new list, but it changes the defaults themselves! That's not good. We want to create a new dictionary with the updates, not change the original.
#
# Fix the bug by making add_format and remove_format pure functions that don't mutate their inputs.
#
# TIP


def add_format(default_formats, new_format):
    default_formats_copy = copy.copy(default_formats)
    default_formats_copy[new_format] = True
    return default_formats_copy


def remove_format(default_formats, old_format):
    default_formats_copy = copy.copy(default_formats)
    default_formats_copy[old_format] = False
    return default_formats_copy

# ASSIGNMENT
# In Doc2Doc we frequently need to change the casing of some text. For example:
#
# TITLECASE
# Every Day Once A Day Give Yourself A Present
#
# LOWERCASE
# every day once a day give yourself a present
#
# UPPERCASE
# EVERY DAY ONCE A DAY GIVE YOURSELF A PRESENT
#
# There is an issue in the convert_case function, our test suite can't test its behavior because it's printing to the console (eww... a side-effect) instead of returning a value. Fix the function so that it returns the correct value instead of printing it.


def convert_case(text, target_format):
    if not text or not target_format:
        raise ValueError(f"No text or target format provided")

    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"Unsupported format: {target_format}")

# ASSIGNMENT
# Complete the markdown_to_text function. It's currently a no-op.
#
# It should:
#
# Remove any # characters from the beginnings of lines. (Headings in markdown)
# Remove any single and double * characters that are at the start or end of a word. (Emphasis in markdown)

# TIPS
# This is a big function, but you can do it! Just thought I'd warn you.
# Feel free to write helper functions to break the problem down into smaller parts.
# I used some of these built-ins:
# str.split
# str.lstrip
# str.strip
# filter
# map
# join
# lambda


def helper(word):
    if len(word) > 1:
        return word.strip("*")
    return word


def remove_asterisks(string):
    return " ".join(map(lambda word: helper(word), string.split(" ")))


def markdown_to_text(doc_content):
    no_hash_char = map(lambda str: str.lstrip("# "), doc_content.split("\n"))
    return "\n".join(map(remove_asterisks, no_hash_char))


def zipmap(keys, values):
    if len(keys) == 0 or len(values) == 0:
        return {}
    res = zipmap(keys[1:], values[1:])
    res[keys[0]] = values[0]
    return res


def list_files(current_node, current_path=""):
    file_paths = []
    for node in current_node:
        node_val = current_node[node]
        if node_val == None:
            file_paths.append(current_path)
        else:
            file_paths.extend(list_files(
                node_val, f"{current_path}/{node_val}"))
    return file_paths


def count_nested_levels_1(nested_documents, target_document_id, level=1):
    for document_id in nested_documents:
        if document_id == target_document_id:
            return level
        found_level = count_nested_levels_1(
            nested_documents[document_id], target_document_id, level + 1
        )
        if found_level != -1:
            return found_level
    return -1


def count_nested_levels(nested_documents, target_document_id, level=1):
    for id in nested_documents:
        if id == target_document_id:
            return level

        found_level = count_nested_levels(
            nested_documents[id], target_document_id, level + 1)

        if found_level != -1:
            return found_level

    return -1


"""
# reverse_string(s) return s
# reverse_string(se) return es
    return 
"""

# MEMOIZATION


def fibonacci(num):
    memo = {}

    def helper(x):
        if x in memo:
            return memo[x]
        else:
            new_ans = 1 if x == 1 or x == 2 else helper(x - 1) + helper(x - 2)
            memo[x] = new_ans
            return new_ans

    return helper(num)


def factorial_r(num):
    memo = {}

    def factorial(x):
        if x in memo:
            return memo[x]
        else:
            new_ans = 1 if x > 0 and x == 1 else x * factorial(x - 1)
            memo[x] = new_ans
            return new_ans

    return factorial(num)


def reverse_string(s):
    memo = {}

    def helper(str):
        if str in memo:
            return memo[str]
        else:
            new_ans = str if len(str) == 0 else helper(s[1:]) + str[0]
            memo[str] = new_ans
            return new_ans

    return helper(s)

# Takes a formatter function as parameter
# returns a new function(?)
# The new function PRINTS the formatted inputs using the given formatter function
# this means that we will need two parameters for our inner function and we will use
# that to print the


def get_logger(formatter):
    def print_formatted_inputs(input1, input2):
        print(formatter(input1, input2))
    return print_formatted_inputs

# Don't edit below this line


def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_func(filename, content):
        if filename.split(".")[1] in valid_formats:
            return conversion_function(content)
        raise ValueError("Invalid file format")
    return inner_func


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]


def word_count_aggregator():
    count = 0

    def inner_func(doc):
        number_of_words = len(doc.split())
        nonlocal count
        count += number_of_words
        return count
    return inner_func


def converted_font_size(font_size):
    def inner_func(doc_type):
        if doc_type == "txt":
            return font_size
        if doc_type == "md":
            return font_size * 2
        if doc_type == "docx":
            return font_size * 3
        raise ValueError("Invalid doc type")
    return inner_func


def file_type_aggregator(func_to_wrap):
    # dict of file_type -> count
    counts = {}

    def wrapper(doc, file_type):
        nonlocal counts
        if file_type in counts:
            counts[file_type] += 1
        else:
            counts[file_type] = 1
        result = func_to_wrap(doc, file_type)
        return result, counts

    return wrapper


@file_type_aggregator
def process_doc(doc, file_type):
    return f"Processing doc: {doc} with File Type: {file_type}"


def args_logger(*args, **kwargs):
    for arg in args:
        print(f"* {arg}")
    for kwarg in dict(sorted(kwargs.items())):
        print(f"* {kwarg}: {kwargs[kwarg]}")


# Don't edit below this line


def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
        converted_args = []
        for arg in args:
            converted_args.append(convert_md_to_txt(arg))
        for key, value in kwargs.items():
            kwargs[key] = convert_md_to_txt(value)
        return func(*converted_args, **kwargs)

    return wrapper


def markdown_to_text_decorator_1(func):
    def wrapper(*args, **kwargs):
        converted_args = []
        for arg in args:
            converted_args.append(convert_md_to_txt(arg))
        for key, value in kwargs.items():
            kwargs[key] = convert_md_to_txt(value)
        return func(*converted_args, **kwargs)

    return wrapper


def convert_md_to_txt(doc):
    return "\n".join(doc.split("\n").lstrip("# "))


# Don't edit below this line


@markdown_to_text_decorator
def concat(first_doc, second_doc):
    return f"""First: {first_doc}
Second: {second_doc}
"""


@markdown_to_text_decorator
def format_as_essay(title, body, conclusion):
    return f"""Title: {title}
Body: {body}
Conclusion: {conclusion}
"""


doc_type_pdf = "pdf"
doc_type_txt = "txt"
doc_type_docx = "docx"
doc_type_md = "md"
doc_type_html = "html"


def conversion_type(doc_type):
    if doc_type == "pdf":
        return doc_type_html
    if doc_type == "txt":
        return doc_type_pdf
    if doc_type == "docx":
        return doc_type_md
    if doc_type == "md":
        return doc_type_pdf
    if doc_type == "html":
        return doc_type_txt
    raise Exception("Unknown document type")


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


def convert_format(content, from_format, to_format):
    if from_format == DocFormat.MD and to_format == DocFormat.HTML:
        return f"<h1>{content.lstrip('# ')}</h1>"
    if from_format == DocFormat.TXT and to_format == DocFormat.PDF:
        return f"[PDF] {content} [PDF]"
    if from_format == DocFormat.HTML and to_format == DocFormat.MD:
        converted = content.lstrip("<h1>").rstrip("</h1>")
        return converted
    raise Exception("Invalid type")


def fight_soldiers(soldier_one, soldier_two):
    soldier_one_dps = soldier_one["damage"] * soldier_one["attacks_per_second"]
    soldier_two_dps = soldier_two["damage"] * soldier_two["attacks_per_second"]
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"


def power_set(input_set):
    if len(input_set) == 0:
        return [[]]
    finalsubsets = []
    first = input_set[0]
    remaining = input_set[1:]
    subsets = power_set(remaining)
    for subset in subsets:
        finalsubsets.append([first] + subset)
        finalsubsets.append(subset)

    return finalsubsets
