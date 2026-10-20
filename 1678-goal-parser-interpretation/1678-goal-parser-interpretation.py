class Solution:
    def interpret(self, command: str) -> str:
        natija = ""
        i = 0
        while i < len(command):
            if command[i] == 'G':
                natija += "G"
                i += 1
            elif command[i:i+2] == '()':
                natija += "o"
                i += 2
            elif command[i:i+4] == '(al)':
                natija += "al"
                i += 4
        return natija 