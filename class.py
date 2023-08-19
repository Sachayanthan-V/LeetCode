
# class for concate a string

class concate:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2 
    
    # return a concatinated string
    def string_concatination(self):
        return self.str1 + self.str2
    
        
# main

if __name__ == "__main__" :
    strconcate = concate("1","2")
    print(strconcate.string_concatination())

