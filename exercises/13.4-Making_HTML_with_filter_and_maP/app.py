all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

# Your code here
def generate_li(color):
	return f'<li>{color["label"]}</li>'


def filter_colors(color_obj):
	if color_obj["sexy"] == True:
		return color_obj

new_list = list(filter(filter_colors, all_colors))

new_list = list(map(generate_li, new_list))

print(new_list)