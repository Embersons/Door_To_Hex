class Card:
    # Constructor, parms facility code, code name
    # AWID-26 Class atributes, sets the AWID bit to 26 

    awid_bit = 26

    def __init__(self, fc_code, cn_code):
        if not (0 <= cn_code <= 65535):
            raise ValueError("Invalid CN code. Must be between 0 and 65535.")

        if not (0 <= fc_code <= 255):
            raise ValueError("Invalid FC code. Must be between 0 and 255.")

        self.fc_code = fc_code
        self.cn_code = cn_code

        



