stat_str= "hello, Good day!"
keyword = "hello"

start_index = stat_str.rfind(keyword)

if start_index != -1:
    end_index = start_index + len(keyword) - 1
    print(f"Pattern: '{keyword}' starts at index {start_index} and ends at index {end_index}.")
else:
    print(f"Pattern: '{keyword}' not found in the string '{stat_str}'.")
