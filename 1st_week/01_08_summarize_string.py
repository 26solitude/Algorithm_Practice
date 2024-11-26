from collections import Counter


def summarize_string(input_str):
    count = Counter(input_str)
    sorted(count.items(), key=lambda x: x[0])
    ans = ""
    for key, value in count.items():
        ans += key + str(value) + "/"
    ans = ans[:-1]
    return ans


input_str = "acccdeee"

print(summarize_string(input_str))
