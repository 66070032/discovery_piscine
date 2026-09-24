def array_of_names(persons_dict):
    full_names_list = []
    
    for first_name, last_name in persons_dict.items():
        formatted_name = first_name.capitalize() + " " + last_name.capitalize()
        full_names_list.append(formatted_name)

    return full_names_list

persons = { "jean": "valjean", "grace": "hopper", "xavier": "niel", "fifi": "brindacier"}

print(array_of_names(persons))
