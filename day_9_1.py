# get_group: substring, level
# return points for that group

def get_group(cleaned_input):
    # This assumes a cleaned string
    idx = 0
    stack = []
    score = cscore = 0
    while True:
        if idx >= len(cleaned_input):
            break
        if cleaned_input[idx] == "{":
            cscore += 1
            stack.append(cscore)
        elif cleaned_input[idx] == "}":
            cscore -= 1
            try:
                score += stack.pop()
            except IndexError:
                pass
        idx += 1

    return score


def remove_exclamation_points(input):
    new_str_arr = []
    was_previous_char_exlamation = False
    for char in input:
        if char == "!":
            was_previous_char_exlamation = True
            continue
        elif was_previous_char_exlamation:
            was_previous_char_exlamation = False
            continue
        new_str_arr.append(char)
    new_str = "".join(new_str_arr)
    return new_str

def remove_garbage_between_brackets(input):
    # remove characters only 
    new_str_arr = []
    is_char_between_brackets = False
    for char in input:
        if char == '<':
            is_char_between_brackets = True
            continue
        elif char == '>' and is_char_between_brackets:
            is_char_between_brackets = False
            continue
        elif is_char_between_brackets:
            continue
        new_str_arr.append(char)
    return "".join(new_str_arr)

def main(input):
    # Before we do anything, we loop through to remove all garbage
    # First, remove all exclamation points and subsequent characters
    new_str = remove_exclamation_points(input)
    # Next remove garbage in brackets
    cleaned_str = remove_garbage_between_brackets(new_str)
    print(cleaned_str)
    # Assume that the base string is a group
    points = get_group(cleaned_str) 
    print(points)

if __name__ == '__main__':
    #input = ['{}', '{{{}}}', '{{},{}}', '{{{},{},{{}}}}', '{<{},{},{{}}>}', '{<a>,<a>,<a>,<a>}', '{{<a>},{<a>},{<a>},{<a>}}', '{{<!>},{<!>},{<!>},{<a>}}']
    with open('day_9.txt', 'r') as f:
        input = f.readline()
        main(input)