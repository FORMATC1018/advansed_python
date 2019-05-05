import yaml

dictinary_to_yaml = {1:[1,2,3], 
                    2: 4, 
                    3: {'5' + u'\u0024': None, '6' + u'\u20AC': None, '7' + u'\u20BD': None}
                    }
with open ("file.yaml", "w", encoding="utf-8") as f:
    yaml.dump(dictinary_to_yaml, f, default_flow_style=False, allow_unicode=True)

with open ("file.yaml", "r", encoding="utf-8") as f:
    f_content = yaml.load(f)
print(f_content)
