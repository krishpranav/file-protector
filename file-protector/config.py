class Config():
    def __init__(self):
        self.suffix = ".file-protector"
        self.invalid = ['.', '..', './', '../']
        self.protect_prefix = 'protect: '
        self.rm_prefix = 'file-p: '