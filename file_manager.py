class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        uchwyt = open(self.file_name, 'r', encoding ='utf-8')
        return print(uchwyt.read())

    def update_file(self, text_data):
        uchwyt = open(self.file_name, 'a', encoding ='utf-8')
        return uchwyt.write(text_data)


