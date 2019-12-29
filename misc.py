def reverse_string(i,chars):
    if i>= len(chars) or chars is None:
        return
    reverse_string(i+1,chars)
    print(chars[i])

if __name__ == "__main__":
    reverse_string(0,"manish")