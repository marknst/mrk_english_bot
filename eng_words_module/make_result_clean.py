
def clean_result_ukr(string: str):
    start_index = string.find('t="')
    end_index = string.rfind('" data-url=')
    new_string = string[start_index:end_index]
    result_string = new_string.replace('t="', '').replace(
        '&lt;em&gt;', '*').replace('&lt;/em&gt;', '*')
    return result_string
