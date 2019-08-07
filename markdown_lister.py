def markdown_list(text):
    lst = text.split(",")
    for i in range(len(lst)):
        cstr = lst[i].strip()
        print(str(i+1) + ". **" + cstr[0].upper() + cstr[1:] + "**:")

if __name__ == "__main__":
    markdown_list("supervised learning, unsupervised learning, and reinforcement learning")
