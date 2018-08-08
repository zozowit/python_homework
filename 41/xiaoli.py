class FileObject:
    def __init__(self):
        self.f = None

    def openFile(self, path, parameter):
        self.f = open(path, parameter)

    def closeFile(self):
        self.f.close()

    def __del__(self):
        if self.f is not None:
            self.f.close()
