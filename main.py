from parser import convert_yaml_to_sexpr

if __name__ == "__main__":
    with open("sample.yaml", "r") as f:
        yaml_input = f.read()
    print(convert_yaml_to_sexpr(yaml_input))
