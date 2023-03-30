# High Level Analyzer
""" For more information and documentation,
please go to https://support.saleae.com/extensions/high-level-analyzer-extensions"""
import datetime

from saleae.analyzers import (
    AnalyzerFrame,
    ChoicesSetting,
    HighLevelAnalyzer,
    NumberSetting,
)


# High level analyzers must subclass the HighLevelAnalyzer class.
class Hla(HighLevelAnalyzer):
    """
    Hla Class Hla ccTalk

    sous-class de HighLevelAnalyzer gérant l'analyse des trames ccTalk

    Args:
        HighLevelAnalyzer: class mère

    Returns :
        AnalyzerFrame: description de la  trame
    """
    # header = {
    #     255: "Factory set-up and test",
    #     254: "Simple poll",
    #     253: "Address poll",
    #     252: "Address clash",
    #     251: "Address change",
    #     250: "Address random",
    #     249: "Request polling priority",
    #     248: "Request status",
    #     247: "Request variable set",
    #     246: "Request manufacturer id",
    #     245: "Request equipment category id",
    #     244: "Request product code",
    #     243: "Request database version",
    #     242: "Request serial number",
    #     241: "Request software revision",
    #     240: "Test solenoids",
    #     239: "Operate motors",
    #     238: "Test output lines",
    #     237: "Read input lines",
    #     236: "Read opto states",
    #     235: "Read DH public key",
    #     234: "Send DH public key",
    #     233: "Latch output lines",
    #     232: "Perform self-check",
    #     231: "Modify inhibit status",
    #     230: "Request inhibit status",
    #     229: "Read buffered credit or error codes",
    #     228: "Modify master inhibit status",
    #     227: "Request master inhibit status",
    #     226: "Request insertion counter",
    #     225: "Request accept counter",
    #     224: "Request encrypted product id",
    #     223: "Modify encrypted inhibit and override registers",
    #     222: "Modify sorter override status",
    #     221: "Request sorter override status",
    #     220: "ACMI encrypted data",
    #     219: "Enter new PIN number",
    #     218: "Enter PIN number",
    #     217: "Request payout high / low status",
    #     216: "Request data storage availability",
    #     215: "Read data block",
    #     214: "Write data block",
    #     213: "Request option flags",
    #     212: "Request coin position",
    #     211: "Power management control",
    #     210: "Modify sorter paths",
    #     209: "Request sorter paths",
    #     208: "Modify payout absolute count",
    #     207: "Request payout absolute count",
    #     204: "Meter control",
    #     203: "Display control",
    #     202: "Teach mode control ",
    #     201: "Request teach status",
    #     200: "ACMI unencrypted product id",
    #     199: "Configuration to EEPROM",
    #     198: "Counters to EEPROM",
    #     197: "Calculate ROM checksum",
    #     196: "Request creation date",
    #     195: "Request last modification date",
    #     194: "Request reject counter",
    #     193: "Request fraud counter",
    #     192: "Request build code",
    #     191: "Keypad control",
    #     189: "Modify default sorter path",
    #     188: "Request default sorter path",
    #     187: "Modify payout capacity",
    #     186: "Request payout capacity",
    #     185: "Modify coin id",
    #     184: "Request coin id",
    #     183: "Upload window data",
    #     182: "Download calibration info",
    #     181: "Modify security setting",
    #     180: "Request security setting",
    #     179: "Modify bank select",
    #     178: "Request bank select",
    #     177: "Handheld function",
    #     176: "Request alarm counter",
    #     175: "Modify payout float",
    #     174: "Request payout float",
    #     173: "Request thermistor reading",
    #     172: "Emergency stop",
    #     171: "Request hopper coin",
    #     170: "Request base year",
    #     169: "Request address mode",
    #     168: "Request hopper dispense count",
    #     167: "Dispense hopper coins",
    #     166: "Request hopper status",
    #     165: "Modify variable set",
    #     164: "Enable hopper",
    #     163: "Test hopper",
    #     162: "Modify inhibit and override registers",
    #     161: "Pump RNG",
    #     160: "Request cipher key",
    #     159: "Read buffered bill events",
    #     158: "Modify bill id",
    #     157: "Request bill id",
    #     156: "Request country scaling factor",
    #     155: "Request bill position",
    #     154: "Route bill",
    #     153: "Modify bill operating mode",
    #     152: "Request bill operating mode",
    #     151: "Test lamps",
    #     150: "Request individual accept counter",
    #     149: "Request individual error counter",
    #     148: "Read opto voltages",
    #     147: "Perform stacker cycle",
    #     146: "Operate bi-directional motors",
    #     145: "Request currency revision",
    #     144: "Upload bill tables",
    #     143: "Begin bill table upgrade",
    #     142: "Finish bill table upgrade",
    #     141: "Request firmware upgrade capability",
    #     140: "Upload firmware",
    #     139: "Begin firmware upgrade",
    #     138: "Finish firmware upgrade",
    #     137: "Switch encryption code",
    #     136: "Store encryption code",
    #     135: "Set accept limit",
    #     134: "Dispense hopper value",
    #     133: "Request hopper polling value",
    #     132: "Emergency stop value",
    #     131: "Request hopper coin value",
    #     130: "Request indexed hopper dispense count",
    #     129: "Read barcode data",
    #     128: "Request money in",
    #     127: "Request money out",
    #     126: "Clear money counters",
    #     125: "Pay money out",
    #     124: "Verify money out",
    #     123: "Request activity register",
    #     122: "Request error status",
    #     121: "Purge hopper",
    #     120: "Modify hopper balance",
    #     119: "Request hopper balance",
    #     118: "Modify cash box value",
    #     117: "Request cash box value",
    #     116: "Modify real time clock",
    #     115: "Request real time clock",
    #     114: "Request USB id",
    #     113: "Switch baud rate",
    #     112: "Read encrypted events",
    #     111: "Request encryption support",
    #     110: "Switch encryption key",
    #     109: "Request encrypted hopper status",
    #     108: "Request encrypted monetary id",
    #     107: "Operate escrow",
    #     106: "Request escrow status",
    #     105: "Data stream",
    #     104: "Request service status",
    #     4: "Request comms revision",
    #     3: "Clear comms status variables",
    #     2: "Request comms status variables",
    #     1: "Reset device",
    # }

    header = {
        255: ["Factory set-up and test", 255, 255, ],
        254: ["Simple poll", 0, 0, ],
        253: ["Address poll", 0, 255, ],
        252: ["Address clash", 0, 255, ],
        251: ["Address change", 1, 0, ],
        250: ["Address random", 0, 0, ],
        249: ["Request polling priority", 0, 2, ],
        248: ["Request status", 0, 1, ],
        247: ["Request variable set", 0, 1, ],
        246: ["Request manufacturer id", 0, 255, ],
        245: ["Request equipment category id", 0, 255, ],
        244: ["Request product code", 0, 255, ],
        243: ["Request database version", 0, 1, ],
        242: ["Request serial number", 0, 3, ],
        241: ["Request software revision", 0, 255, ],
        240: ["Test solenoids", 1, 0, ],
        239: ["Operate motors", 1, 0, ],
        238: ["Test output lines", 1, 0, ],
        237: ["Read input lines", 0, 255, ],
        236: ["Read opto states", 0, 1, ],
        235: ["Read DH public key", 1, 255, ],
        234: ["Send DH public key", 3, 0, ],
        233: ["Latch output lines", 1, 0, ],
        232: ["Perform self-check", 0, 255, ],
        231: ["Modify inhibit status", 2, 0, ],
        230: ["Request inhibit status", 0, 2, ],
        229: ["Read buffered credit or error codes", 0, 11, ],
        228: ["Modify master inhibit status", 1, 0, ],
        227: ["Request master inhibit status", 0, 1, ],
        226: ["Request insertion counter", 0, 3, ],
        225: ["Request accept counter", 0, 3, ],
        224: ["Request encrypted product id", 2, 32, ],
        223: ["Modify encrypted inhibit and override registers", 13, 0, ],
        222: ["Modify sorter override status", 1, 0, ],
        221: ["Request sorter override status", 0, 1, ],
        220: ["ACMI encrypted data", 255, 255, ],
        219: ["Enter new PIN number", 4, 0, ],
        218: ["Enter PIN number", 4, 0, ],
        217: ["Request payout high / low status", 255, 1, ],
        216: ["Request data storage availability", 0, 5, ],
        215: ["Read data block", 1, 255, ],
        214: ["Write data block", 255, 0, ],
        213: ["Request option flags", 0, 1, ],
        212: ["Request coin position", 1, 2, ],
        211: ["Power management control", 1, 0, ],
        210: ["Modify sorter paths", 255, 0, ],
        209: ["Request sorter paths", 1, 255, ],
        208: ["Modify payout absolute count", 255, 0, ],
        207: ["Request payout absolute count", 255, 2, ],
        204: ["Meter control", 255, 255, ],
        203: ["Display control", 255, 255, ],
        202: ["Teach mode control ", 255, 0, ],
        201: ["Request teach status", 1, 2, ],
        200: ["ACMI unencrypted product id", 1, 40, ],
        199: ["Configuration to EEPROM", 0, 0, ],
        198: ["Counters to EEPROM", 0, 0, ],
        197: ["Calculate ROM checksum", 0, 4, ],
        196: ["Request creation date", 0, 2, ],
        195: ["Request last modification date", 0, 2, ],
        194: ["Request reject counter", 0, 3, ],
        193: ["Request fraud counter", 0, 3, ],
        192: ["Request build code", 0, 255, ],
        191: ["Keypad control", 1, 255, ],
        189: ["Modify default sorter path", 1, 0, ],
        188: ["Request default sorter path", 0, 1, ],
        187: ["Modify payout capacity", 255, 0, ],
        186: ["Request payout capacity", 1, 2, ],
        185: ["Modify coin id", 7, 0, ],
        184: ["Request coin id", 1, 6, ],
        183: ["Upload window data", 255, 0, ],
        182: ["Download calibration info", 0, 255, ],
        181: ["Modify security setting", 2, 255, ],
        180: ["Request security setting", 1, 1, ],
        179: ["Modify bank select", 1, 0, ],
        178: ["Request bank select", 0, 1, ],
        177: ["Handheld function", 255, 255, ],
        176: ["Request alarm counter", 0, 1, ],
        175: ["Modify payout float", 255, 0, ],
        174: ["Request payout float", 255, 2, ],
        173: ["Request thermistor reading", 0, 1, ],
        172: ["Emergency stop", 0, 1, ],
        171: ["Request hopper coin", 0, 255, ],
        170: ["Request base year", 0, 4, ],
        169: ["Request address mode", 0, 1, ],
        168: ["Request hopper dispense count", 0, 3, ],
        167: ["Dispense hopper coins", 255, 255, ],
        166: ["Request hopper status", 0, 4, ],
        165: ["Modify variable set", 255, 0, ],
        164: ["Enable hopper", 1, 0, ],
        163: ["Test hopper", 0, 255, ],
        162: ["Modify inhibit and override registers", 6, 0, ],
        161: ["Pump RNG", 255, 0, ],
        160: ["Request cipher key", 0, 255, ],
        159: ["Read buffered bill events", 0, 11, ],
        158: ["Modify bill id", 8, 0, ],
        157: ["Request bill id", 1, 7, ],
        156: ["Request country scaling factor", 2, 3, ],
        155: ["Request bill position", 2, 255, ],
        154: ["Route bill", 1, 255, ],
        153: ["Modify bill operating mode", 1, 0, ],
        152: ["Request bill operating mode", 0, 1, ],
        151: ["Test lamps", 2, 0, ],
        150: ["Request individual accept counter", 1, 3, ],
        149: ["Request individual error counter", 1, 3, ],
        148: ["Read opto voltages", 0, 255, ],
        147: ["Perform stacker cycle", 0, 255, ],
        146: ["Operate bi-directional motors", 3, 0, ],
        145: ["Request currency revision", 255, 255, ],
        144: ["Upload bill tables", 255, 0, ],
        143: ["Begin bill table upgrade", 0, 0, ],
        142: ["Finish bill table upgrade", 0, 0, ],
        141: ["Request firmware upgrade capability", 255, 1, ],
        140: ["Upload firmware", 255, 0, ],
        139: ["Begin firmware upgrade", 255, 0, ],
        138: ["Finish firmware upgrade", 0, 0, ],
        137: ["Switch encryption code", 3, 0, ],
        136: ["Store encryption code", 0, 0, ],
        135: ["Set accept limit", 1, 0, ],
        134: ["Dispense hopper value", 255, 255, ],
        133: ["Request hopper polling value", 0, 7, ],
        132: ["Emergency stop value", 0, 2, ],
        131: ["Request hopper coin value", 1, 8, ],
        130: ["Request indexed hopper dispense count", 1, 3, ],
        129: ["Read barcode data", 0, 255, ],
        128: ["Request money in", 0, 4, ],
        127: ["Request money out", 0, 4, ],
        126: ["Clear money counters", 0, 0, ],
        125: ["Pay money out", 4, 0, ],
        124: ["Verify money out", 0, 9, ],
        123: ["Request activity register", 0, 2, ],
        122: ["Request error status", 0, 2, ],
        121: ["Purge hopper", 2, 0, ],
        120: ["Modify hopper balance", 3, 0, ],
        119: ["Request hopper balance", 1, 8, ],
        118: ["Modify cash box value", 4, 0, ],
        117: ["Request cash box value", 0, 4, ],
        116: ["Modify real time clock", 4, 0, ],
        115: ["Request real time clock", 0, 4, ],
        114: ["Request USB id", 0, 4, ],
        113: ["Switch baud rate", 2, 255, ],
        112: ["Read encrypted events", 1, 16, ],
        111: ["Request encryption support", 6, 20, ],
        110: ["Switch encryption key", 16, 0, ],
        109: ["Request encrypted hopper status", 3, 16, ],
        108: ["Request encrypted monetary id", 2, 16, ],
        107: ["Operate escrow", 1, 0, ],
        106: ["Request escrow status", 0, 3, ],
        105: ["Data stream", 255, 255, ],
        104: ["Request service status", 1, 255, ],
        4: ["Request comms revision", 0, 3, ],
        3: ["Clear comms status variables", 0, 0, ],
        2: ["Request comms status variables", 0, 3, ],
        1: ["Reset device", 0, 0, ],
        0: ["Unknown", 255, 255, ],
    }

    fault_code = {
        0: "None",
        1: "EEPROM checksum corrupted",
        2: "Fault on inductive coils Coil number",
        3: "Fault on credit sensor",
        4: "Fault on piezo sensor",
        5: "Fault on reflective sensor",
        6: "Fault on diameter sensor",
        7: "Fault on wake-up sensor",
        8: "Fault on sorter exit sensors",
        9: "NVRAM checksum corrupted",
        10: "Coin dispensing error",
        11: "Low level sensor error",
        12: "High level sensor error",
        13: "Coin counting error",
        14: "Keypad error",
        15: "Button error",
        16: "Display error",
        17: "Coin auditing error",
        18: "Fault on reject sensor",
        19: "Fault on coin return mechanism",
        20: "Fault on C.O.S. mechanism",
        21: "Fault on rim sensor",
        22: "Fault on thermistor",
        23: "Payout motor fault",
        24: "Payout timeout",
        25: "Payout jammed",
        26: "Payout sensor fault",
        27: "Level sensor error",
        28: "Personality module not fitted",
        29: "Personality checksum corrupted",
        30: "ROM checksum mismatch",
        31: "Missing slave device",
        32: "Internal comms bad",
        33: "Supply voltage outside",
        34: "Temperature outside",
        35: "D.C.E. fault",
        36: "Fault on bill validation sensor",
        37: "Fault on bill transport motor",
        38: "Fault on stacker",
        39: "Bill jammed",
        40: "RAM test fail",
        41: "Fault on string sensor",
        42: "Accept gate failed open",
        43: "Accept gate failed closed",
        44: "Stacker missing",
        45: "Stacker full",
        46: "Flash memory erase fail",
        47: "Flash memory write fail",
        48: "Slave device not responding",
        49: "Fault on opto sensor",
        50: "Battery fault",
        51: "Door open",
        52: "Micro-switch fault",
        53: "RTC fault",
        54: "Firmware error",
        55: "Initialisation error",
        56: "Supply current outside",
        57: "Forced bootloader mode",
        255: "Unspecified fault code",
    }

    extra_info = {
        2: "Coil number",
        8: "Sensor number",
        11: "Hopper or tube number",
        12: "Hopper or tube number",
        14: "Key number",
        23: "Hopper number",
        24: "Hopper or tube number",
        25: "Hopper or tube number",
        26: "Hopper or tube number",
        27: "Hopper or tube number",
        31: "Slave address",
        32: "Slave address",
        35: "1 = coin, 2 = token",
        36: "Sensor number",
        48: "Device number",
        49: "Opto number",
        255: "Further information",
    }

    acknowledge = {0: "ACK", 5: "NAK", 6: "BUSY", }

    verif = {True: "OK", False: "Error"}

    error_code = {254: "escrow empty", 255: "failed route", }

    error_code_stacker = {254: "stacker fault", 255: "stacker not fitted", }

    CV_Error_Code = {
        0: "Null event",
        1: "Reject coin",
        2: "Inhibited coin",
        3: "Multiple window",
        4: "Wake-up timeout",
        5: "Validation timeout",
        6: "Credit sensor timeout",
        7: "Sorter opto timeout",
        8: "2nd close coin error",
        9: "Accept gate not ready",
        10: "Credit sensor not ready",
        11: "Sorter not ready",
        12: "Reject coin not cleared",
        13: "Validation sensor not ready",
        14: "Credit sensor blocked",
        15: "Sorter opto blocked",
        16: "Credit sequence error",
        17: "Coin going backwards",
        18: "Coin too fast",
        19: "Coin too slow",
        20: "C.O.S. mechanism activated",
        21: "DCE opto timeout",
        22: "DCE opto not seen",
        23: "Credit sensor reached too early",
        24: "Reject coin",
        25: "Reject slug",
        26: "Reject sensor blocked",
        27: "Games overload",
        28: "Max. coin meter pulses exceeded",
        29: "Accept gate open not closed",
        30: "Accept gate closed not open",
        31: "Manifold opto timeout",
        32: "Manifold opto blocked",
        33: "Manifold not ready",
        34: "Security status changed",
        35: "Motor exception",
        36: "Swallowed coin",
        37: "Coin too fast",
        38: "Coin too slow",
        39: "Coin incorrectly sorted",
        40: "External light attack",
        253: "Data block request",
        254: "Coin return mechanism activated",
        255: "Unspecified alarm code",
    }

    BILL_Error_Code = {
        0: "Master inhibit active",
        1: "Bill returned from escrow",
        2: "Invalid bill",
        3: "Invalid bill",
        4: "Inhibited bill",
        5: "Inhibited bill",
        6: "Bill jammed in transport",
        7: "Bill jammed in stacker",
        8: "Bill pulled backwards",
        9: "Bill tamper",
        10: "Stacker OK",
        11: "Stacker removed",
        12: "Stacker inserted",
        13: "Stacker faulty",
        14: "Stacker full",
        15: "Stacker jammed",
        16: "Bill jammed in transport",
        17: "Opto fraud detected",
        18: "String fraud detected",
        19: "Anti-string mechanism faulty",
        20: "Barcode detected",
        21: "Unknown bill type stacked",
    }

    baud_rate_code = {
        0: "4800",
        1: "9600",
        2: "19200",
        3: "38400",
        4: "57600",
        5: "115200",
        6: "230400",
        7: "460800",
        8: "512000",
        9: "921600",
        10: "1000000",
        18: "1843200",
        20: "2000000",
        30: "3000000",
    }

    device_address = NumberSetting(label = "Slave device address", min_value = 2, max_value = 255)

    str_cv = "Coin validator[chk 8]"
    str_payout = "Payout[chk 8]"
    str_bv = "Bill acceptor[CRC-16]"

    device_category = ChoicesSetting(label = "Slave device category", choices = (str_cv, str_payout, str_bv))

    address_in_progress = 0

    """ An optional list of types this analyzer produces, 
    providing a way to customize the way frames are displayed in Logic 2."""

    # result_types = {
    #     "mytype": {"format": "Output type: {{type}}, Input type: {{data.input_type}}"}
    # }

    def __init__(self):
        self.data = []
        self.len_data = self.cc_Header = self.broadcast = 0
        self.start_time = None
        self.isMaster2Slave = True
        self.isRequest = False
        self.base_year = 0

        """       
        Initialize HLA.

        Settings can be accessed using the same name used above.
        """
        # print(
        #     "\nSetting : \n - Adresse périphérique : {} \n - Catégorie : {}".format(
        #         self.device_address, self.device_category
        #     )
        # )

    def __reset_frame(self):
        """
            Remise à zéro des informations de documentations de la trame
        """
        self.len_data = 0
        self.start_time = None
        self.data = []
        Hla.address_in_progress = 0
        return

    def __get_int(self, index = 4, length = 2):
        """
            Calcule un nombre entier à partir des données contenues dans data
        Args :
            index : Position du MSB
            length : Nombre d'octets à considérer

        Returns :
            Un nombre entier
        """

        int_result = self.data[index] + (self.data[index + 1] * 256)
        if length > 2:
            int_result += self.data[index + 2] * 65536
        if length == 4:
            int_result += self.data[index + 3] * 16777216
        return int_result

    @property
    def __get_device_address(self):
        """
            Getter de l'adresse du périphérique

        Returns :
            Adresse du périphérique
        """
        return self.device_address

    @property
    def __checksum(self):
        """
            Retourne le checksum 8 bits de la trame

        Returns :
            le checksum sur 1 octet de la trame - le dernier octet
        """
        result = 0
        for value in self.data[0:-1]:
            result += value
        return 256 - (result % 256)

    @property
    def __crc_16(self):
        """
            Retourne le CRC-16 de la trame
        Returns :
            CRC sur 2 octets
        """

        list_locale = self.data[0:2] + self.data[3:-1]
        word_crc = i = 0
        while i < len(list_locale):
            word_crc ^= (list_locale[i] << 8)
            j = 0
            while j < 8:
                if word_crc & 0x8000:
                    word_crc = (word_crc << 1) ^ 0x1021
                else:
                    word_crc <<= 1
                j += 1
            i += 1
        word_crc &= 0xFFFF
        return word_crc

    @property
    def __get_param(self):
        """
        Isole les paramètres et les retourne entre crochets
        Returns :
            Une chaine de caractères contenant les paramètres et se finissant par une flèche si une interpretation sera
            affichée

        """
        str_result = str(self.data[4:-1])
        if self.data[1] > 0:
            str_result += "->"
        return str_result + " "

    @property
    def __get_ascii(self):
        """
            Convertit les paramètres en chaines de caractères
        Returns :
            Une chaine de caractères contenant les caractères ascii des paramètres

        """

        str_ascii = ""
        for c in self.data[4:-1]:
            str_ascii += chr(c)
        return str_ascii

    @property
    def __decode_date(self):
        """
            Calcule et interprète une date ccTalk
        Returns :
            Une chaine de caractères contenant la date

        """
        result = self.__get_int()
        if self.base_year > 0:
            return "{:02d}/{:02d}/{:04d}".format(result & 31, (result >> 5) & 15, 2000 + ((result >> 9) & 31))
        else:
            return "{:02d}/{:02d}/+{:02d}".format(result & 31, (result >> 5) & 15, (result >> 9) & 31)

    @property
    def __decode_buffer_cv(self):
        """
            Analyse le buffer des événements et des errors du monnayeur
        Returns :
            Une chaine de caractères contenant l'interprétation du buffer
        """

        str_events = f"# Events {self.data[4]} "
        i = 0
        str_result = ""
        while i < 5:
            str_result += f" - Result {i + 1} : "
            if self.data[5 + (i * 2)] > 0:
                # Coin accepted
                str_result += f"Coin {self.data[5 + (i * 2)]} Sort. {self.data[6 + (i * 2)]}"
            else:
                # Erreur
                str_result += f"Err. #{self.data[6 + (i * 2)]} "
                # Erreur inhibited
                if (self.data[6 + (i * 2)] > 127) and (self.data[6 + (i * 2)] < 160):
                    str_result += f"Inhibited ch. {self.data[6 + (i * 2)] - 127}"
                    # Erreur reserved
                elif (self.data[6 + (i * 2)] > 159) and (self.data[6 + (i * 2)] < 191):
                    str_result += f" Err. #{self.data[6 + (i * 2)]} Reserved"
                    # Erreur
                elif self.data[6 + (i * 2)] < 41:
                    str_result += f"{self.CV_Error_Code[self.data[6 + (i * 2)]]} "
                else:
                    str_result += "unidentified"
            i += 1
        return str_events + str_result

    @property
    def __decode_buffer_bill(self):
        """
            Analyse le buffer des événements et des errors du monnayeur

        Returns :
            Une chaine de caractères contenant l'interprétation du buffer
        """
        str_events = f"# Events {self.data[4]} "
        i = 0
        str_result = ""
        while i < 5:
            str_result += f" - Result {i + 1} : "
            if self.data[5 + (i * 2)] > 0:
                # bill accepted
                if self.data[6 + (i * 2)] == 1:
                    str_result += f"Bill {self.data[5 + (i * 2)]} in escrow"
                else:
                    str_result += f"Bill {self.data[5 + (i * 2)]} in cash box"
            else:
                if self.data[6 + (i * 2)] < 22:
                    str_result += f"Code {self.data[6 + (i * 2)]} : {self.BILL_Error_Code[self.data[6 + (i * 2)]]}"
                else:
                    str_result += f"Code {self.data[6 + (i * 2)]} : inconnu"
            i += 1
        return str_events + str_result

    @property
    def __master_inhibit(self):
        return f"Master inh. {('activated', 'norm. op.')[self.data[4] & 1]}"

    @property
    def __stacker_escrow(self):
        use = ('non used', 'used')
        return f"Stacker {use[self.data[4] & 1]} Escrow {use[self.data[4] & 2]}"

    @property
    def __get_country(self):
        return f"{chr(self.data[4])}{chr(self.data[5])}"

    def __get_mask(self, index = 4, length = 1):
        if length == 1:
            return f"Mask [{bin(self.data[index])[2:].rjust(8, '0')}]"
        else:
            return f"Mask [{bin(self.data[index + 1])[2:].rjust(8, '0')} / {bin(self.data[index])[2:].rjust(8, '0')}]"

    @property
    def __master2slave(self):
        """
            Effectue l'interprétation des paramètres contenus dans le message du master

        Returns :
            Une chaine de caractères contenant l'interprétation du message du master
        """
        # 240 Test solenoid, 239 Operate motors, 238 Test output lines, 233 Latch out lines, 222 Modify sorter
        # override status
        if self.cc_Header in (240, 239, 238, 233, 222):
            return self.__get_mask()

        # Modify inhibit status
        elif self.cc_Header == 231:
            return self.__get_mask(length = 2)

        # Modify master inhibit status
        elif self.cc_Header == 228:
            return self.__master_inhibit

        # 219 Enter new PIN, 218 Enter PIN
        elif self.cc_Header in (219, 218):
            if self.data[4] > 47:
                str_pin = "Pin [{:c}][{:c}][{:c}][{:c}]"
            else:
                str_pin = "Pin [{}][{}][{}][{}]"
            return str_pin.format(self.data[4], self.data[5], self.data[6], self.data[7])

        # Request payout high / low status
        elif (self.cc_Header == 217) and (self.data[1] == 1):
            return f"Hopper no. {self.data[4]}"

        # Read data block
        elif self.cc_Header == 215:
            return f"Blk. no. {self.data[4]}"

        # Write data block
        elif self.cc_Header == 214:
            return f"Blk. no. {self.data[4]} values {str(self.data[5:-1])} "

        # Request coin position
        elif self.cc_Header == 212:
            return f"coin {self.data[4]}"

        # Power management control
        elif self.cc_Header == 211:
            return f"Pow. opt. : {('normal', 'switch to low', 'switch to full', 'shutdown')[self.data[4]]}"

        # Modify sorter paths
        elif self.cc_Header == 210:
            str_result = f"Coin pos.{self.data[4]} Path_1 {self.data[5]} "
            if (self.data[1]) == 5:
                str_result += f"Path_2 {self.data[6]} Path_3 {self.data[7]} Path_4 {self.data[8]}"
            return str_result

        # Request sorter paths
        elif self.cc_Header == 209:
            return f"Coin pos. {self.data[4]}"

        # Modify payout absolute count
        elif self.cc_Header == 208:
            if self.data[1] == 2:
                return f"Coins {self.__get_int()}"
            elif self.data[1] == 3:
                return f"Hopper {self.data[4]} - Coins {self.__get_int(5)}"

        # Request payout absolute count
        elif (self.cc_Header == 207) and (self.data[1] == 1):
            return f"Hopper {self.data[4]}"

        # Meter control
        elif self.cc_Header == 204:
            str_result = f"{('Set', 'Inc.', 'Dec.', 'Reset', 'Read')[self.data[4]]} meter"
            if self.data[4] == 0:
                str_result += f"{self.__get_int(5, 3)}"
            return str_result

        # TODO display control
        elif self.cc_Header == 203:
            pass

        # Teach mode control
        elif self.cc_Header == 202:
            str_result = f"Pos. {self.data[4]}"
            if self.data[1] == 2:
                str_result += f" Orienta. {self.data[5]} "
            return str_result

        # Request teach status
        elif self.cc_Header == 201:
            return ('Default', 'Abort')[self.data[4]]

        # Modify default sorter path
        elif self.cc_Header == 189:
            return f"Def. path {self.data[4]}"

        # Modify payout capacity
        elif self.cc_Header == 187:
            if self.data[1] == 2:
                return f"Capacity {self.__get_int()}"
            else:
                return f"Hopper no. {self.data[4]} Capacity {self.__get_int(5)}"

        # Request payout capacity
        elif (self.cc_Header == 186) and (self.data[1] == 1):
            return f"Hopper no. {self.data[4]}"

        # Modify coin id
        elif self.cc_Header == 185:
            return "Coin pos. {} Id. {:c}{:c}_{:c}{:c}{:c}_{:c}".format(self.data[4], self.data[5], self.data[6],
                                                                        self.data[7], self.data[8], self.data[9],
                                                                        self.data[10], )

        # Request coin id
        elif self.cc_Header == 184:
            return f"Pos. {self.data[4]}"

        # Upload window data
        elif self.cc_Header == 183:
            str_op = ("Program coin", "Modif credit code", "Delete coin", "Program token", "Delete token")
            str_result = f"Pos. {self.data[5]} {str_op[self.data[4]]}"
            if self.data[4] == 1:
                str_result += f" Credit code {self.data[6]}"
            elif self.data[4] in [0, 3]:
                str_result += f" {self.data[6:-1]}"
            return str_result

        # Modify security setting
        elif self.cc_Header == 181:
            return f"Pos. {self.data[4]} setting {self.data[5]}"

        # Request security setting
        elif self.cc_Header == 180:
            return f"Pos. {self.data[4]}"

        # Modify bank select
        elif self.cc_Header == 179:
            return f"Bank no. {self.data[4]}"

        # Modify payout float
        elif self.cc_Header == 175:
            if self.data[1] == 2:
                return f"float {self.__get_int()}"
            elif self.data[1] == 3:
                return f"Hopper {self.data[4]} float {self.__get_int(5)}"

        # Request payout float
        elif (self.cc_Header == 174) and (self.data[1] == 1):
            return f"Hopper {self.data[4]}"

        # Dispense hopper coins
        elif self.cc_Header == 167:
            return f"Secur. code {self.data[4: -2]} no. coins {self.data[-2]}"

        # Enable hopper
        elif self.cc_Header == 164:
            return f"Payout {('disable', 'enable')[int(self.data[4] == 165)]}"

        # Modify inhibit and override registers
        elif self.cc_Header == 162:
            return f"Current (inh. [{bin(self.data[5])[2:].rjust(8, '0')}/{bin(self.data[4])[2:].rjust(8, '0')}]" \
                   f" overr. sorter [{bin(self.data[6])[2:].rjust(8, '0')}]) - " \
                   f"Next (inh. [{bin(self.data[8])[2:].rjust(8, '0')}/{bin(self.data[7])[2:].rjust(8, '0')}] " \
                   f"overr. sorter [{bin(self.data[9])[2:].rjust(8, '0')}])"

        # Pump RNG
        elif self.cc_Header == 161:
            return f"RNG : {self.data[4: -1]}"

        # Modify bill id
        elif self.cc_Header == 158:
            return "Bill pos. {} {:c}{:c}_{:c}{:c}{:c}{:c}_{:c}".format(self.data[4], self.data[5], self.data[6],
                                                                        self.data[7], self.data[8], self.data[9],
                                                                        self.data[10], self.data[11])

        # Request bill id
        elif self.cc_Header == 157:
            return f"Bill type {self.data[4]}"

        # Request country scaling factor
        elif self.cc_Header in [156, 155]:
            return self.__get_country

        # Route bill
        elif self.cc_Header == 154:
            return {0: "return bill", 1: "send cash box/stacker", 255: "Extend timeout", }[self.data[4]]

        # Modify bill operating mode
        elif self.cc_Header == 153:
            return self.__stacker_escrow

        # Test lamps
        elif self.cc_Header == 151:
            if self.data[5] < 3:
                return f"Lamp {self.data[4]} " \
                       f"control {('automatic mode', 'force lamp off', 'force lamp on',)[self.data[5]]}"
            elif self.data[5] > 9:
                return f" Lamp {self.data[4]} flash every {self.data[5] * 20} ms"

        # Request individual accept counter
        elif self.cc_Header == 150:
            return f" Type {self.data[4]}"

        #  Request individual error counter
        elif self.cc_Header == 149:
            return f" Error type {self.CV_Error_Code[self.data[4]]}"

        # Operate bi-directional motors
        elif self.cc_Header == 146:
            return f"Mot. {self.__get_mask()} Dir. {self.__get_mask(5)} Speed {self.data[6]}"

        # Request currency revision
        elif (self.cc_Header == 145) and (self.data[1] == 2):
            return self.__get_country

        # 144 Upload bill tables, 140 Upload firmware
        elif self.cc_Header in (144, 140):
            return f"Block {self.data[4]} line {self.data[5]} data {self.data[6:-1]}"

        # 141 Request firmware upgrade capability, 139 Begin firmware upgrade
        elif self.cc_Header in (141, 139) and (self.data[1] == 1):
            return f"Module {self.data[4]} "

        # Switch encryption code
        elif self.cc_Header == 137:
            return f"Code [0X{self.data[5]}{self.data[4]}] [0X{self.data[7]}{self.data[6]}] [0X{self.data[9]}\
                    {self.data[8]}]"

        # Set accept_ limit
        elif self.cc_Header == 135:
            return f"No. coins {self.data[4]}"

        # Dispense hopper value
        elif self.cc_Header == 134:
            return f"Code [0X{self.data[4]}{self.data[5]}] [0X{self.data[6]}{self.data[7]}] [0X{self.data[8]}\
                    {self.data[9]}] no. of coins {self.__get_int(10)}"

        # 131 Request hopper coin value, 130 Request indexed hopper dispense count
        elif self.cc_Header in (131, 130):
            return f"No coin {self.data[4]}"

        # Pay money out
        elif self.cc_Header == - 125:
            return f"To pay {self.__get_int()}"

        # Purge hopper
        elif self.cc_Header == 121:
            return f"Hopper {self.data[4]} no {self.data[5]}"

        # Modify hopper balance
        elif self.cc_Header == 120:
            return f"Hopper {self.data[4]} no {self.__get_int(5)}"

        # Request hopper balance
        elif self.cc_Header == 119:
            return f"Hopper {self.data[4]}"

        # Modify cash box value
        elif self.cc_Header == 118:
            return f"Cash box value {self.__get_int()}"

        # Request cash box value
        elif self.cc_Header == 116:
            return str(datetime.datetime.fromtimestamp(self.__get_int()()))

        # Switch baud rate
        elif self.cc_Header == 113:
            baud_rate_op = ("baud rate in use", "switch baud rate", "maximum baud rate supported",
                            "support for new baud rate",)
            return f"Op. {baud_rate_op[self.data[4]]} {self.baud_rate_code[self.data[5]]}"

        # Operate escrow
        elif self.cc_Header == 107:
            return ('Div. accept', 'Div. return')[self.data[4]]

        # Request service status
        elif self.cc_Header == 104:
            return ('Report', 'Clear')[self.data[4]]
        else:
            return ""

    @property
    def __slave2master(self):
        """
            Effectue l'interprétation des paramètres contenus dans le message du périphérique

        Returns :
            Une chaine de caractères contenant l'interprétation du message du périphérique
        """
        # Request polling priority
        if self.cc_Header == 249:
            units = {1: 'ms', 3: 'sec.', 4: 'min.', 5: 'hours', 6: 'day', 7: 'weeks', 8: 'month', 9: 'years'}
            if self.data[4] == 0:
                return "Special case"
            elif self.data[4] == 2:
                return f"{self.data[5] * 10}ms"
            else:
                return f"{self.data[4]} {units[self.data[5]]}"

        # Request status
        elif self.cc_Header == 248:
            return f"{('Status OK', 'Return activated', 'C.O.S.')[self.data[4]]}"

        # Request variable set
        elif self.cc_Header == 247:
            if self.device_category == self.str_bv:
                return f"No. bill types {self.data[4]} No. banks {self.data[5]}"
            else:
                return f"Var. {self.data[4:-1]}"

        # 246 Request manufacturer id, 245 Request equipment category id, 244 Request product code,
        # 241 Request software revision, 171 Request hopper coin, 145 Request currency revision,
        # 129 Read barcode data
        elif self.cc_Header in (246, 245, 244, 241, 171, 145, 129) and (self.data[1] > 0):
            return self.__get_ascii

        # Request database version
        elif self.cc_Header == 243:
            return f"Data base {self.data[4]}"

        # Request serial number
        elif self.cc_Header == 242:
            return f"S.N. {self.__get_int()} "

        # 237 Read input lines, 236 Read opto states, 221 Request sorter override status,
        # 217 Request payout high / low status, 169 Request address mode
        elif self.cc_Header in (237, 236, 221, 217, 169):
            return self.__get_mask()

        # Perform self-check
        elif self.cc_Header == 232:
            str_result = f"fault {self.fault_code[self.data[4]]}"
            if self.data[1] == 2:
                str_result += f" info {self.extra_info[self.data[5]]}"
            return str_result

        # 230 Request inhibit status, 212 Request coin position, 155 Request bill position,
        # 123 Request activity register
        elif self.cc_Header in (230, 212, 155, 123):
            return self.__get_mask(length = 2)

        # Read buffered credit or error codes
        elif self.cc_Header == 229:
            return self.__decode_buffer_cv

        # Request master inhibit status
        elif self.cc_Header == 227:
            return self.__master_inhibit

        # Request insertion counter
        elif self.cc_Header == 226:
            return f"Insert counter {self.__get_int()}"

        # 225 Request accept counter, 150 Request individual accept counter
        elif self.cc_Header in (225, 150):
            return f"Accept counter {self.__get_int()}"

        # Request data storage availability
        elif self.cc_Header == 216:
            return f"{('vola. L.O.R', 'vol. L.O.P.D', 'perm. limited', 'perm. unlimited')[self.data[4]]} " \
                   f"[rd blocks {self.data[5]} | rd bytes/block {self.data[6]}] " \
                   f"[wr blocks {self.data[7]} | wr bytes/block {self.data[8]}]"

        # Read data block
        elif self.cc_Header == 215:
            return f"Values {self.data[4:-1]}"

        # Request option flags
        elif self.cc_Header == 213:
            if self.device_category == self.str_cv:
                return f"Code format {('Coin pos.', 'CVF')[self.data[4] & 1]}"
            else:
                return self.__get_mask()

        # Request sorter paths
        elif self.cc_Header == 209:
            str_result = f"Path 1 {self.data[4]}"
            if self.data[1] == 4:
                str_result += f" Path 2 {self.data[5]} Path 3 {self.data[6]} Path 4 {self.data[7]}"
            return str_result

        # Request payout absolute count
        elif self.cc_Header == 207:
            return f"Coins {self.__get_int()}"

        # Meter control
        elif (self.cc_Header == 204) and (self.data[1] > 0):
            return f"Meter {self.__get_int()}"

        # Request payout absolute count
        elif self.cc_Header == 201:
            teach_status_code = {
                252: "aborted",
                253: "error",
                254: "busy",
                255: "completed",
            }
            return f"# Coins {self.data[4]} Status {teach_status_code[self.data[5]]}"

        # Calculate ROM checksum
        elif self.cc_Header == 197:
            return f"Chk_1 {self.data[4]} Chk_2 {self.data[5]} Chk_3 {self.data[6]} Chk_4 {self.data[7]}"

        # 196 Request creation date, 195 Request last modification date
        elif (self.cc_Header == 196) or (self.cc_Header == 195):
            return self.__decode_date

        # Request reject counter
        elif self.cc_Header == 194:
            return f"Rej. counter {self.__get_int()}"

        # Request fraud counter
        elif self.cc_Header == 193:
            return f"Fraud. counter {self.__get_int()}"

        # Request build code
        elif self.cc_Header == 192:
            return f"Build {self.__get_ascii}"

        # Request default sorter path
        elif self.cc_Header == 188:
            return f"Def. path {self.data[4]}"

        # Request payout capacity
        elif self.cc_Header == 186:
            return f"No. coins {self.__get_int()}"

        # Request coin id
        elif self.cc_Header == 184:
            i = 4
            while i < 10:
                if self.data[i] in (123, 125, 91, 93):
                    self.data[i] = 32
                i += 1
            return "{:c}{:c}_{:c}{:c}{:c}_{:c}".format(self.data[4], self.data[5], self.data[6], self.data[7],
                                                       self.data[8], self.data[9])

        # Download calibration info
        elif self.cc_Header == 182:
            return f"Calib. info. {self.data[4:-1]}"

        # Request security setting
        elif self.cc_Header == 180:
            return f"Setting {self.data[4]}"

        # Request bank select
        elif self.cc_Header == 178:
            return f"Bank select {self.data[4]}"

        # Request alarm counter
        elif self.cc_Header == 176:
            return f"Alarm count {self.data[4]}"

        # Request payout float
        elif self.cc_Header == 174:
            return f"No. coins {self.__get_int()}"

        # Request thermistor reading
        elif self.cc_Header == 173:
            if (self.data[4] and 128) == 128:
                return f"Temp. -{self.data[4]}"
            else:
                return f"Temp. {self.data[4]}"

        # Emergency stop
        elif self.cc_Header == 172:
            return f"Remaining {self.data[4]}"

        # Request base year
        elif self.cc_Header == 170:
            self.base_year = int(chr(self.data[4]) + chr(self.data[5]) + chr(self.data[6]) + chr(self.data[7]))
            return f"Base year {self.base_year}"

        # Request hopper dispense count
        elif self.cc_Header == 168:
            return f"Dispensed {self.__get_int()}"

        # Dispense hopper coins
        elif (self.cc_Header == 167) and (self.data[1] > 0):
            return f"Event count. {self.data[4]}"

        # Request hopper status
        elif self.cc_Header == 166:
            return f"Events {self.data[4]} Remaining {self.data[5]} Last paid {self.data[6]} " \
                   f"Last unpaid {self.data[7]}"

        # Test hopper
        elif self.cc_Header == 163:
            i = 0
            str_result = ""
            while i < self.data[1]:
                str_result += f" Mask {i + 1} [{bin(self.data[4 + i])[2:].rjust(8, '0')}]"
                i += 1
            return str_result

        # Request cipher key
        elif self.cc_Header == 160:
            return f"Key : {self.data[4:-1]}"

        # Read buffered bill events
        elif self.cc_Header == 159:
            return self.__decode_buffer_bill

        # Request bill id
        elif self.cc_Header == 157:
            return "Id. {:c}{:c}_{:c}{:c}{:c}{:c}_{:c}".format(self.data[4], self.data[5], self.data[6], self.data[7],
                                                               self.data[8], self.data[9], self.data[10])

        # Request country scaling factor
        elif self.cc_Header == 156:
            return f"Scaling factor {self.__get_int()} decimal {self.data[6]}"

        # Route bill
        elif (self.cc_Header == 154) and (self.data[1] == 1):
            return self.error_code[self.data[4]]

        # Request bill operating mode
        elif self.cc_Header == 152:
            return self.__stacker_escrow

        # Request individual error counter
        elif self.cc_Header == 149:
            return " Error counter : {} ".format(self.__get_int())

        # Read opto voltages
        elif self.cc_Header == 148:
            str_result = " Opto voltages {}"
            if self.data[1] == 1:
                return str_result.format(self.data[4])
            else:
                return str_result.format(self.__get_int())

        # Perform stacker cycle
        elif (self.cc_Header == 147) and (self.data[1] == 1):
            return f"Error {self.error_code_stacker[self.data[4]]}"

        # Request firmware upgrade capability
        elif self.cc_Header == 141:
            return f"FW option {self.data[4]}"

        # Dispense hopper value
        elif (self.cc_Header == 134) and (self.data[1] == 1):
            return f"Events {self.data[4]}"

        # Request hopper polling value
        elif self.cc_Header == 133:
            return f"Events {self.data[4]} remain. {self.__get_int(5)} paid {self.__get_int(7)} " \
                   f"unpaid {self.__get_int(9)} "

        # Emergency stop value
        elif self.cc_Header == 132:
            return f"remain. {self.__get_int()}"

        # 131 Request hopper coin value_, 119 Request hopper balance
        elif (self.cc_Header == 131) or (self.cc_Header == 119):
            return "Id. {:c}{:c}{:c}{:c}{:c}{:c}{}".format(self.data[4], self.data[5], self.data[6], self.data[7],
                                                           self.data[8], self.data[9], self.__get_int(10))

        # Request indexed hopper dispense count
        elif self.cc_Header == 130:
            return f"Dispensed {self.__get_int()} "

        # 128 Request money in, 127 Request money out
        elif (self.cc_Header == 128) and (self.cc_Header == 127):
            return f"Total {self.__get_int()} "

        elif self.cc_Header == 124:
            return f"Events {self.data[4]} paid {self.__get_int(5, 4)} unpaid {self.__get_int(9, 4)}"

        # Request error status
        elif self.cc_Header == 122:
            device = {100: "Coin acceptor", 250: "Cash box", 255: "System"}
            fault_code_status = {
                1: "hopper empty(requires",
                2: "hopper jam",
                3: "hopper fraud",
                4: "hopper fault",
                101: "coin acceptor jam",
                102: "coin acceptor fraud",
                103: "coin acceptor fault",
                104: "coin acceptor opto fault",
                251: "cash box full",
                252: "cash box missing",
                255: "other",
            }
            str_device = ""
            if (self.data[4] == 0) and (self.data[5] == 0):
                return "No error"
            elif (self.data[5] == 255) and self.data[5] == 255:
                return "General fault"

            elif (self.data[4] > 0) and (self.data[4] < 9):
                str_device = f"Hopper {self.data[4]}"
            elif self.data[4] in device:
                str_device = device[self.data[4]]
            return f"{str_device} {fault_code_status[self.data[5]]}"

        # Request cash box value
        elif self.cc_Header == 117:
            return f"Value {self.__get_int()} "

        # Request real time clock
        elif self.cc_Header == 115:
            return str(datetime.datetime.fromtimestamp(self.__get_int()))

        # Request USB id
        elif self.cc_Header == 114:
            return f"VID_{self.__get_int()} PID_{self.__get_int(6)}"

        # Switch baud rate
        elif (self.cc_Header == 113) and (self.data[1] == 1):
            return f"Speed {self.baud_rate_code[self.data[4]]}"

        # Request escrow status
        elif self.cc_Header == 106:
            str_result = f"Op. status {('idle', 'operating', 'fault condition',)[self.data[4]]}"
            if self.data[5] == 0:
                str_result += "empty "
            else:
                str_result += "full "
            str_result += f"fault code {self.data[6]}"
            return str_result

        # Request service status
        elif (self.cc_Header == 104) and (self.data[1] == 1):
            service_status = ('none', 'servicing recommended', 'servicing overdue',)
            return f"Service status {service_status[self.data[4]]}"

        # Request comm revision
        elif self.cc_Header == 4:
            if (self.data[4]) > 47:
                return "Release {:c} v{:c}.{:c}".format(self.data[4], self.data[5], self.data[6])
            else:
                return "Release {} v{}.{}".format(self.data[4], self.data[5], self.data[6])

        # Request comm status variables
        elif self.cc_Header == 2:
            return f"RX : timeouts {self.data[4]}, bytes ignored {self.data[5]}, bad checksum {self.data[6]}"

        # Nothing to return
        else:
            return ""

    def decode(self, frame: AnalyzerFrame):
        """
            Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame`
            or a list of `AnalyzerFrame`s.

            The type and data values in `frame` will depend on the input analyzer.
        """

        try:
            if (Hla.address_in_progress == 0) or (Hla.address_in_progress == self.__get_device_address):
                if self.len_data == 0:
                    self.__reset_frame()

                self.data += frame.data["data"]
                self.len_data += 1

                if self.len_data == 1:
                    self.start_time = frame.start_time
                    # Todo MCS header
                    Hla.address_in_progress = self.__get_device_address
                    if self.data[0] == self.__get_device_address:  # or (self.data[0] == self.broadcast):
                        self.isMaster2Slave = True
                    elif self.isRequest and self.data[0] == 1:
                        self.isMaster2Slave = False
                    else:
                        raise

                elif self.len_data == 2:
                    return

                if self.len_data > 2:
                    if self.isMaster2Slave:
                        if (self.len_data == 3) and (self.device_category != self.str_bv) and (self.data[2] != 1):
                            raise
                        if (self.len_data == 4) and ((Hla.header[self.data[3]][1] != 255) and
                                                     (Hla.header[self.data[3]][1] != self.data[1])):
                            raise

                        if (self.len_data > 4) and (self.len_data == (5 + self.data[1])):
                            self.isRequest = True
                            self.len_data = self.cc_Header = 0
                            str_header = "unknown"
                            if (self.data[3]) in Hla.header:
                                str_header = Hla.header[self.data[3]][0]
                                self.cc_Header = self.data[3]

                            if self.device_category == self.str_bv:
                                check_result = self.__crc_16
                                check_ok = (check_result == self.data[2] + (self.data[-1] * 256))
                                if (not check_ok) and (str_header == "unknown"):
                                    raise

                                return AnalyzerFrame(f"{self.device_category}({self.data[0]}) -"
                                                     f" # param.({self.data[1]}) - "
                                                     f"LSB CRC({self.data[2]}) - {str_header}({self.data[3]}) - "
                                                     f"param.{self.__get_param}{self.__master2slave} - "
                                                     f"MSB CRC({self.data[-1]}) ", self.start_time, frame.end_time,
                                                     {"Checksum ": f" {self.data[2] + (self.data[-1] * 256)} "
                                                                   f"{self.verif[check_ok]}"})
                            else:
                                check_result = self.__checksum
                                check_ok = (check_result == self.data[-1])
                                if (not check_ok) and (str_header == "unknown"):
                                    raise
                                return AnalyzerFrame(f"{self.device_category}({self.data[0]}) - "
                                                     f"# param.({self.data[1]}) - "
                                                     f"Master({self.data[2]}) - {str_header}({self.data[3]}) - param. "
                                                     f"{self.__get_param}{self.__master2slave} ", self.start_time,
                                                     frame.end_time,
                                                     {"Checksum ": f" {self.data[-1]} {self.verif[check_ok]}"})
                    else:
                        if (self.len_data == 3) and (self.device_category != self.str_bv) and \
                                (self.data[2] != self.__get_device_address):
                            raise

                        if (self.len_data > 4) and (self.len_data == (5 + self.data[1])):
                            self.len_data = 0
                            self.isRequest = False
                            if self.device_category == self.str_bv:
                                check_result = self.__crc_16
                                check_ok = (check_result == self.data[2] + (self.data[-1] * 256))

                                return AnalyzerFrame(f"Master({self.data[0]}) - # param.({self.data[1]}) - "
                                                     f"LSB CRC({self.data[2]}) - {self.acknowledge[self.data[3]]}"
                                                     f"({self.data[3]}) - "
                                                     f"param. {self.__get_param}{self.__slave2master} - "
                                                     f"MSB CRC({self.data[-1]}) ",
                                                     self.start_time, frame.end_time,
                                                     {"Checksum ": f" {self.data[2] + self.data[-1] * 256} "
                                                                   f"{self.verif[check_ok]}"})
                            else:
                                check_result = self.__checksum
                                check_ok = (check_result == self.data[- 1])
                                return AnalyzerFrame(f"Master({self.data[0]}) - # param.({self.data[1]}) - "
                                                     f"{self.device_category}({self.data[2]}) - "
                                                     f"{self.acknowledge[self.data[3]]}({self.data[3]}) - param. "
                                                     f"{self.__get_param}{self.__slave2master} ",
                                                     self.start_time, frame.end_time,
                                                     {"Checksum ": f" {self.data[-1]} {self.verif[check_ok]}"})
            else:
                raise
        except:
            print()
            self.__reset_frame()
        return
