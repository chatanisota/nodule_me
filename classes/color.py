class Color:

    # 0 - 255 8bit
    r = 0
    g = 0
    b = 0

    def __init__(self, r=0, g=0, b=0):
        self.r = r
        self.g = g
        self.b = b

    def get_color(self):
        return (self.r , self.g, self.b)


    @staticmethod
    def white():
    	return Color(255,255,255)

    @staticmethod
    def olive():
    	return Color(128,128,0)

    @staticmethod
    def yellow():
    	return Color(255,255,0)

    @staticmethod
    def fuchsia():
    	return Color(255,0,255)

    @staticmethod
    def silver():
    	return Color(192,192,192)

    @staticmethod
    def aqua():
    	return Color(0,255,255)

    @staticmethod
    def lime():
    	return Color(0,255,0)

    @staticmethod
    def red():
    	return Color(255,0,0)

    @staticmethod
    def gray():
    	return Color(128,128,128)

    @staticmethod
    def blue():
    	return Color(0,0,255)

    @staticmethod
    def green():
    	return Color(0,128,0)

    @staticmethod
    def purple():
    	return Color(128,0,128)

    @staticmethod
    def black():
    	return Color(0,0,0)

    @staticmethod
    def navy():
    	return Color(0,0,128)

    @staticmethod
    def teal():
    	return Color(0,128,128)

    @staticmethod
    def maroon():
        return Color(128,0,0)
