def nhi_phan_thap_phan(s):
    s = s[::-1]
    sum = 0
    for i in range(len(s)):
        sum += int(s[i]) * pow(2,i)
    return sum
if __name__ == "__main__":
    print(nhi_phan_thap_phan(input()))