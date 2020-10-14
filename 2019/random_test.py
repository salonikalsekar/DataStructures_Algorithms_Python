

def string_manipulation(s):

        res= []

        start_idx, end_idx, idx = 0,0,0
        while idx < len(s):

            if s[idx].isalpha():
                start_idx = idx
                end_idx = idx
                while end_idx < len(s) and s[end_idx].isalpha():
                    end_idx+=1

                res.append(string_format(s[start_idx:end_idx]))
                idx = end_idx

            else:
                res.append(s[idx])
                idx += 1
        return "".join(res)

def string_format(s):
    return s[0]+ str(len(set(s[1:-1]))) +s[-1]
test_cases = "a98779079745092740"
# test_cases = ["Automotive","ldefabc1 cb!a %%%def1123","a hot character","at","x","tipu-is-smart","1234567890","a98779079745092740","98779079745092740a"]
print(string_manipulation(test_cases))

