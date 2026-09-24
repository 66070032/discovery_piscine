def find_the_redheads(family_dict):

    def check_color(name):
        return family_dict[name] == "red"

    redheads_filtered = filter(check_color, family_dict.keys())

    return list(redheads_filtered)

dupont_family = { "florian": "red", "marie": "blond", "virginie": "brunette", "david": "red", "franck": "red" }

print(find_the_redheads(dupont_family))
