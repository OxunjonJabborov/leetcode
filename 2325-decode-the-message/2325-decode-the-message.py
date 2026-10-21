class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        new_key = ""
        for i in key:
            if i not in new_key and i != " ":
                new_key += i
        dictionary = {" ": " "}
        for i in range(26):
            dictionary[new_key[i]] = chr(ord('a') + i)
        new_message = ""
        for i in message:
            new_message += dictionary[i]
        return new_message
        