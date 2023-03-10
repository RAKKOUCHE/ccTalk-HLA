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
    header = {
        255: "Factory set-up and test",
        254: "Simple poll",
        253: "Address poll",
        252: "Address clash",
        251: "Address change",
        250: "Address random",
        249: "Request polling priority",
        248: "Request status",
        247: "Request variable set",
        246: "Request manufacturer id",
        245: "Request equipment category id",
        244: "Request product code",
        243: "Request database version",
        242: "Request serial number",
        241: "Request software revision",
        240: "Test solenoids",
        239: "Operate motors",
        238: "Test output lines",
        237: "Read input lines",
        236: "Read opto states",
        235: "Read DH public key",
        234: "Send DH public key",
        233: "Latch output lines",
        232: "Perform self-check",
        231: "Modify inhibit status",
        230: "Request inhibit status",
        229: "Read buffered credit or error codes",
        228: "Modify master inhibit status",
        227: "Request master inhibit status",
        226: "Request insertion counter",
        225: "Request accept counter",
        224: "Request encrypted product id",
        223: "Modify encrypted inhibit and override registers",
        222: "Modify sorter override status",
        221: "Request sorter override status",
        220: "ACMI encrypted data",
        219: "Enter new PIN number",
        218: "Enter PIN number",
        217: "Request payout high / low status",
        216: "Request data storage availability",
        215: "Read data block",
        214: "Write data block",
        213: "Request option flags",
        212: "Request coin position",
        211: "Power management control",
        210: "Modify sorter paths",
        209: "Request sorter paths",
        208: "Modify payout absolute count",
        207: "Request payout absolute count",
        204: "Meter control",
        203: "Display control",
        202: "Teach mode control ",
        201: "Request teach status",
        200: "ACMI unencrypted product id",
        199: "Configuration to EEPROM",
        198: "Counters to EEPROM",
        197: "Calculate ROM checksum",
        196: "Request creation date",
        195: "Request last modification date",
        194: "Request reject counter",
        193: "Request fraud counter",
        192: "Request build code",
        191: "Keypad control",
        189: "Modify default sorter path",
        188: "Request default sorter path",
        187: "Modify payout capacity",
        186: "Request payout capacity",
        185: "Modify coin id",
        184: "Request coin id",
        183: "Upload window data",
        182: "Download calibration info",
        181: "Modify security setting",
        180: "Request security setting",
        179: "Modify bank select",
        178: "Request bank select",
        177: "Handheld function",
        176: "Request alarm counter",
        175: "Modify payout float",
        174: "Request payout float",
        173: "Request thermistor reading",
        172: "Emergency stop",
        171: "Request hopper coin",
        170: "Request base year",
        169: "Request address mode",
        168: "Request hopper dispense count",
        167: "Dispense hopper coins",
        166: "Request hopper status",
        165: "Modify variable set",
        164: "Enable hopper",
        163: "Test hopper",
        162: "Modify inhibit and override registers",
        161: "Pump RNG",
        160: "Request cipher key",
        159: "Read buffered bill events",
        158: "Modify bill id",
        157: "Request bill id",
        156: "Request country scaling factor",
        155: "Request bill position",
        154: "Route bill",
        153: "Modify bill operating mode",
        152: "Request bill operating mode",
        151: "Test lamps",
        150: "Request individual accept counter",
        149: "Request individual error counter",
        148: "Read opto voltages",
        147: "Perform stacker cycle",
        146: "Operate bi-directional motors",
        145: "Request currency revision",
        144: "Upload bill tables",
        143: "Begin bill table upgrade",
        142: "Finish bill table upgrade",
        141: "Request firmware upgrade capability",
        140: "Upload firmware",
        139: "Begin firmware upgrade",
        138: "Finish firmware upgrade",
        137: "Switch encryption code",
        136: "Store encryption code",
        135: "Set accept limit",
        134: "Dispense hopper value",
        133: "Request hopper polling value",
        132: "Emergency stop value",
        131: "Request hopper coin value",
        130: "Request indexed hopper dispense count",
        129: "Read barcode data",
        128: "Request money in",
        127: "Request money out",
        126: "Clear money counters",
        125: "Pay money out",
        124: "Verify money out",
        123: "Request activity register",
        122: "Request error status",
        121: "Purge hopper",
        120: "Modify hopper balance",
        119: "Request hopper balance",
        118: "Modify cash box value",
        117: "Request cash box value",
        116: "Modify real time clock",
        115: "Request real time clock",
        114: "Request USB id",
        113: "Switch baud rate",
        112: "Read encrypted events",
        111: "Request encryption support",
        110: "Switch encryption key",
        109: "Request encrypted hopper status",
        108: "Request encrypted monetary id",
        107: "Operate escrow",
        106: "Request escrow status",
        105: "Data stream",
        104: "Request service status",
        4: "Request comms revision",
        3: "Clear comms status variables",
        2: "Request comms status variables",
        1: "Reset device",
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
        52: "Microswitch fault",
        53: "RTC fault",
        54: "Firmware error",
        55: "Initialisation error",
        56: "Supply current outside",
        57: "Forced bootloader mode",
        255: "Unspecified fault code",
    }

    code_extra_info = {
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

    teach_status_code = {
        252: "Aborted",
        253: "Error",
        254: "Busy",
        255: "Completed",
    }

    up_window_data = {
        0: "Program coin",
        1: "Modif credit code",
        2: "Delete coin",
        3: "Program token",
        4: "Delete token",
    }

    acknowledge = {
        0: "ACK",
        5: "NAK",
        6: "BUSY",
    }

    route_code = {
        0: "return bill",
        1: "cash box/stacker",
        255: "Extend timeout",
    }

    verif = {
        True: "OK",
        False: "Error"
    }

    error_code = {
        254: "escrow empty",
        255: "failed route",
    }

    error_code_stacker = {
        254: "stacker fault",
        255: "stacker not fitted",
    }

    lamp_control = {
        0: "automatic mode",
        1: "force lamp off",
        2: "force lamp on",
    }

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

    baud_rate_OP = [
        "baud rate in use",
        "switch baud rate",
        "maximum baud rate supported",
        "support for new baud rate"
    ]

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

    operating_status = [
        "idle",
        "operating",
        "fault condition",
    ]

    service_status = [
        "none",
        "servicing recommended",
        "servicing overdue",
    ]

    device_address = NumberSetting(
        label="Slave device address", min_value=2, max_value=255
    )

    str_cv = "Coin validator[chk 8]"
    str_payout = "Payout[chk 8]"
    str_bv = "Bill acceptor[CRC-16]"

    device_category = ChoicesSetting(
        label="Slave device category",
        choices=(str_cv, str_payout, str_bv),
    )

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

    def reset_frame(self):
        """
            Remise à zéro des informations de documentations de la trame
        Returns :
            None

        """
        self.len_data = 0
        self.start_time = None
        self.data = []
        return

    @property
    def _checksum(self):
        """
            Retourne le checksum 8 bits de la trame

        Returns :
            le checksum sur 1 octet de la trame - le dernier octet
        """
        result = loop = 0
        while loop < self.data[1] + 4:
            result += self.data[loop]
            loop += 1
        return 256 - (result % 256)

    @property
    def _crc_16(self):
        """
            Retourne le CRC-16 de la trame
        Returns :
            CRC sur 2 octets
        """
        list_locale = list(self.data)
        list_locale.pop(2)
        list_locale.pop()
        word_crc = i = 0
        while i < len(list_locale):
            word_crc ^= (list_locale[i] << 8)
            j = 0
            while j < 8:
                if word_crc & 0x8000:
                    word_crc = (word_crc << 1) ^ 0x1021
                else:
                    word_crc = word_crc << 1
                j += 1
            i += 1
        word_crc &= 0xFFFF
        return word_crc

    @property
    def _get_param(self):
        """
        Isole les paramètres et les retourne entre crochets
        Returns :
            Une chaine de caractères contenant les paramètres et se finissant par une flèche si une interpretation sera
            affichée

        """
        list_result = []
        position = 4
        while position < (4 + self.data[1]):
            list_result.append(self.data[position])
            position += 1
        str_result = str(list_result)
        if self.data[1] > 0:
            str_result += "->"
        return str_result + ""

    @property
    def _get_ascii(self):
        """
            Convertit les paramètres en chaines de caractères
        Returns :
            Une chaine de caractères contenant les caractères ascii des paramètres
        """
        i = 0
        str_id = " "
        while i < self.data[1]:
            str_id += chr(self.data[i + 4])
            i += 1
        return str_id

    @property
    def _get_int(self):
        """
            Calcule la valeur d'un entier à partir des 3 octets reçus en paramètres
        Returns :
            Un entier
        """
        int_result = self.data[4] + (self.data[5] * 256)
        if self.data[1] > 2:
            int_result += self.data[6] * 65536
        if self.data[1] == 4:
            int_result += self.data[7] * 16777216
        return int_result

    @property
    def _decode_date(self):
        """
            Calcule et interprète une date ccTalk
        Returns :
            Une chaine de caractères contenant la date

        """
        result = self._get_int
        if self.base_year > 0:
            return "{:02d}/{:02d}/{:04d}".format(result & 31, (result >> 5) & 15, 2000 + ((result >> 9) & 31))
        else:
            return "{:02d}/{:02d}/+{:02d}".format(result & 31, (result >> 5) & 15, (result >> 9) & 31)

    @property
    def _decode_buffer_cv(self):
        """
            Analyse le buffer des événements et des errors du monnayeur
        Returns :
            Une chaine de caractères contenant l'interprétation du buffer
        """
        str_events = f"# Events {self.data[4]} "
        str_result = ""
        i = 0
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
    def _decode_buffer_bill(self):
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
    def _master2slave(self):
        """
            Effectue l'interprétation des paramètres contenus dans le message du master

        Returns :
            Une chaine de caractères contenant l'interprétation du message du master
        """
        if ((self.cc_Header == 240) or
                (self.cc_Header == 239) or
                (self.cc_Header == 238) or
                (self.cc_Header == 233) or
                (self.cc_Header == 222)):
            return "Mask [" + bin(self.data[4])[2:].rjust(8, "0") + "]"
        elif self.cc_Header == 231:
            return "Mask [" + bin(self.data[5])[2:].rjust(8, "0") + "|" + bin(self.data[4])[2:].rjust(8, "0") + "]"
        elif self.cc_Header == 228:
            str_result = "Master inh. "
            if (self.data[4]) & 1 == 1:
                return str_result + "enabled"
            else:
                return str_result + "disabled"
        elif (self.cc_Header == 219) or (self.cc_Header == 218):
            if self.data[4] > 47:
                str_pin = "Pin [{:c}][{:c}][{:c}][{:c}]"
            else:
                str_pin = "Pin [{}][{}][{}][{}]"
            return str_pin.format(self.data[4], self.data[5], self.data[6], self.data[7])
        elif self.cc_Header == 215:
            return f"Blk. no. [{self.data[4]}]"
        elif self.cc_Header == 214:
            str_result = f"Blk. no. {self.data[4]} values [ "
            i = 0
            while i < (self.data[1] - 1):
                str_result += f"{self.data[5 + i]} "
                i += 1
            str_result += "]"
            return str_result
        elif self.cc_Header == 211:
            power_option = ["normal", "switch to low",
                            "switch to full", "shutdown"]
            return f"P. opt. {power_option[self.data[4]]}"
        elif self.cc_Header == 210:
            str_result = f"Coin pos.{self.data[4]} Path_1 {self.data[5]} "
            if (self.data[1]) == 5:
                str_result += f"Path_2 {self.data[6]} Path_3 {self.data[7]} Path_4 {self.data[8]}"
            return str_result
        elif self.cc_Header == 209:
            return f"Coin pos. {self.data[4]}"
        elif self.cc_Header == 204:
            str_meter = ["Set", "Inc", "Dec", "Reset", "Read"]
            str_result = str_meter[self.data[4]]
            if self.data[1] == 0:
                str_result += f" {self.data[5] + self.data[6] * 256 + self.data[7] * 65536} "
            return str_result
        elif (self.cc_Header == 217) and (self.data[1] == 1):
            return f"Hopper no. {self.data[4]}"
        elif self.cc_Header == 208:
            if self.data[1] == 2:
                return "Coins {self._get_int}"
            elif self.data[1] == 3:
                return f"Hopper {self.data[4]} - Coins {self.data[5] + self.data[6] + 256}"
            else:
                return ""
        elif (self.cc_Header == 207) and (self.data[1] == 1):
            return f"Hopper {self.data[4]}"
        elif self.cc_Header == 202:
            str_result = f"Pos. {self.data[4]}"
            if self.data[1] == 2:
                str_result += f"Orienta. {self.data[5]}"
            return str_result
        elif self.cc_Header == 201:
            if self.data[4] == 0:
                str_result = "Default "
            else:
                str_result = "Abort "
            return str_result
        elif self.cc_Header == 189:
            return f"Def. path {self.data[4]}"
        elif self.cc_Header == 187:
            if self.data[1] == 2:
                return f"Capacity {self._get_int}"
            else:
                return f"Hopper no. {self.data[4]} Capacity {self.data[5] + (self.data[6] * 256)}"
        elif self.cc_Header == 186:
            if self.data[1] == 1:
                return f"Hopper no. {self.data[4]}"
            else:
                return ""
        elif self.cc_Header == 185:
            return f"Coin pos. {self.data[4]} Id. {chr(self.data[5])}{chr(self.data[6])}_{chr(self.data[7])}\
                    {chr(self.data[8])}{chr(self.data[9])}_{chr(self.data[10])}"
        elif self.cc_Header == 184:
            return f"Pos. {self.data[4]}"
        elif self.cc_Header == 183:
            str_result = f"Pos. {self.data[5]} Cmd {self.up_window_data[self.data[4]]} "
            if (self.data[4] == 0) or (self.data[4] == 3):
                str_result += " var."
                i = 0
                while i < self.data[1]:
                    str_result += f" {self.data[6] + i}"
                    i += 1
            elif self.data[4] == 1:
                str_result += f" Credit code {self.data[6]}"
            return str_result
        elif self.cc_Header == 181:
            return f"Pos. {self.data[4]} setting {self.data[5]}"
        elif self.cc_Header == 180:
            return f"Pos. {self.data[4]}"
        elif self.cc_Header == 179:
            return f"Bank select {self.data[4]} "
        elif self.cc_Header == 175:
            if self.data[1] == 2:
                return f"No. coins {self._get_int} "
            elif self.data[1] == 3:
                return f"Hopper {self.data[4]} No. coins {self.data[5] + (self.data[6] * 256)} "
            else:
                return ""
        elif self.cc_Header == 174:
            if self.data[1] == 1:
                return f"Hopper {self.data[4]}"
            else:
                return ""
        elif self.cc_Header == 167:
            str_result = "Security code "
            i = 0
            while i < (self.data[1] - 1):
                str_result += f" {self.data[4 + i]}"
                i += 1
            str_result += f" No. of coins {self.data[4 + i]}"
            return str_result
        elif self.cc_Header == 164:
            str_result = "Payout {}"
            if self.data[4] == 165:
                return str_result.format("enable")
            else:
                return str_result.format("disable")
        elif self.cc_Header == 162:
            return (" Current (Mask 1 [" + bin(self.data[4])[2:].rjust(8, "0") + "] Mask 2 [" +
                    bin(self.data[5])[2:].rjust(8, "0") + "] Override mask [" + bin(self.data[6])[2:].rjust(8, "0") +
                    "])" + " Next (Mask 1 [" + bin(self.data[7])[2:].rjust(8, "0") + "] Mask 2 [" +
                    bin(self.data[8])[2:].rjust(8, "0") + "] Override mask [" + bin(self.data[9])[2:].rjust(8, "0") +
                    "])")
        elif self.cc_Header == 161:
            str_result = "RNG : "
            i = 0
            while i < self.data[1]:
                str_result += f" {self.data[4 + i]}"
                i += 1
            return str_result
        elif self.cc_Header == 158:
            return f"Bill. type {self.data[4]} Id. {chr(self.data[5])}{chr(self.data[6])}_{chr(self.data[7])}\
                        {chr(self.data[8])}{chr(self.data[9])}_{chr(self.data[10])}_{chr(self.data[11])}"
        elif self.cc_Header == 157:
            return f"Bill type {self.data[4]}"
        elif (self.cc_Header == 156) or (self.cc_Header == 155):
            return "Country {:c}{:c}".format(self.data[4], self.data[5])
        elif self.cc_Header == 154:
            return self.route_code[self.data[4]]
        elif self.cc_Header == 153:
            str_result = " Stacker "
            if self.data[4] & 1:
                str_result += "used"
            else:
                str_result += "non used"
            str_result += " Escrow "
            if self.data[4] & 2:
                str_result += "used "
            else:
                str_result += "non used"
            return str_result
        elif self.cc_Header == 151:
            if self.data[5] < 3:
                return f" Lamp {self.data[4]} control {self.lamp_control[self.data[5]]}"
            elif self.data[5] > 9:
                return f" Lamp {self.data[4]} flash every {self.data[5] * 20} ms"
            else:
                return ""
        elif self.cc_Header == 150:
            return f" Pos. {self.data[4]}"
        elif self.cc_Header == 149:
            return f" Error type {self.data[4]}"
        elif self.cc_Header == 146:
            return "Motor mask [" + bin(self.data[4])[2:].rjust(8, "0") + "]" + \
                "Direction mask [" + bin(self.data[5])[2:].rjust(8, "0") + "]" + "Speed " + str(self.data[6])
        elif (self.cc_Header == 145) and (self.data[1] == 2):
            return "Country {:c}{:c}".format(self.data[4], self.data[5])
        elif (self.cc_Header == 144) or (self.cc_Header == 140):
            str_result = f"Block {self.data[4]} line {self.data[5]}"
            i = 0
            while i < self.data[1] - 2:
                str_result += f" {self.data[6] + i}"
                i += 1
            return str_result
        elif ((self.cc_Header == 141) or (self.cc_Header == 139)) and (self.data[1] == 1):
            return f"Module {self.data[4]} "
        elif self.cc_Header == 137:
            return f"Code [0X{self.data[5]}{self.data[4]}] [0X{self.data[7]}{self.data[6]}] [0X{self.data[9]}\
                    {self.data[8]}]"
        elif self.cc_Header == 135:
            return f"no. coins {self.data[4]}"
        elif self.cc_Header == 134:
            return f"Code [0X{self.data[4]}{self.data[5]}] [0X{self.data[6]}{self.data[7]}] [0X{self.data[8]}\
                    {self.data[9]}] no. of coins {self.data[10] + (self.data[11] * 256)}"
        elif (self.cc_Header == 131) or (self.cc_Header == 130):
            return f"No coin {self.data[4]}"
        elif self.cc_Header == - 125:
            return f"To pay {self.get_dword}"
        elif self.cc_Header == 121:
            return f"Hopper {self.data[4]} no {self.data[5]}"
        elif self.cc_Header == 120:
            return f"Hopper {self.data[4]} no {self.data[5] + (self.data[6] * 256)}"
        elif self.cc_Header == 119:
            return f"Hopper {self.data[4]}"
        elif self.cc_Header == 118:
            return f"Cash box value {self.get_dword}"
        elif self.cc_Header == 116:
            return str(datetime.datetime.fromtimestamp(self._get_int))
        elif self.cc_Header == 113:
            return f"Op. {self.baud_rate_OP[self.data[4]]} {self.baud_rate_code[self.data[5]]}"
        elif self.cc_Header == 107:
            if self.data[4] == 0:
                "Div. accept"
            else:
                "Div. Return"
        elif self.cc_Header == 104:
            if self.data[4] == 0:
                return "Report service status"
            else:
                return "Clear service status"
        else:
            return ""

    @property
    def _slave2master(self):
        """
            Effectue l'interprétation des paramètres contenus dans le message du périphérique

        Returns :
            Une chaine de caractères contenant l'interprétation du message du périphérique
        """
        if self.cc_Header == 253:
            return str(self.data[4])
        elif self.cc_Header == 249:
            if self.data[4] == 0:
                return "Special case"
            elif self.data[4] == 1:
                return f"{self.data[5]}ms"
            elif self.data[4] == 2:
                return f"{self.data[5] * 10}ms"
            elif self.data[4] == 3:
                return f"{self.data[5]}s"
            elif self.data[4] == 4:
                return f"{self.data[5]}m"
            elif self.data[4] == 5:
                return f"{self.data[5]}h"
            elif self.data[4] == 6:
                return f"{self.data[5]}d"
            elif self.data[4] == 7:
                return f"{self.data[5]}w"
            elif self.data[4] == 8:
                return f"{self.data[5]}M"
            elif self.data[4] == 9:
                return f"{self.data[5]}Y"
            else:
                return "Undetermined"
        elif self.cc_Header == 248:
            if self.data[4] == 0:
                return "Status OK"
            elif self.data[4] == 1:
                return "Return activated"
            elif self.data[4] == 1:
                return "C.O.S activated"
        elif ((self.cc_Header == 246) or
              (self.cc_Header == 245) or
              (self.cc_Header == 244) or
              (self.cc_Header == 241) or
              (self.cc_Header == 171) or
              ((self.cc_Header == 129) and (self.data[1] > 0)) or
              (self.cc_Header == 145)):
            return self._get_ascii
        elif self.cc_Header == 243:
            return f"Data base {self.data[4]}"
        elif self.cc_Header == 242:
            return f"S.N. {self._get_int} "
        elif ((self.cc_Header == 237) or
              (self.cc_Header == 236) or
              (self.cc_Header == 221) or
              (self.cc_Header == 217)):
            return "Mask [" + bin(self.data[4])[2:].rjust(8, "0") + "]"
        elif (self.cc_Header == 230) or (self.cc_Header == 212):
            return "Mask [" + bin(self.data[5])[2:].rjust(8, "0") + "|" + bin(self.data[4])[2:].rjust(8, "0") + "]"
        elif self.cc_Header == 229:
            return self._decode_buffer_cv
        elif self.cc_Header == 227:
            str_result = "Master inh. "
            if (self.data[4]) & 1 == 1:
                return str_result + "enabled"
            else:
                return str_result + "disabled"
        elif self.cc_Header == 226:
            return f"Insert counter {self._get_int} "
        elif (self.cc_Header == 225) or (self.cc_Header == 150):
            return f"Accept counter {self._get_int} "
        elif self.cc_Header == 216:
            str_result = [
                "vola. L.O.R",
                "vol. L.O.P.D",
                "perm. limited",
                "perm. unlimited",
            ]
            return str_result[self.data[4]] + \
                ", [rd blocks {} | rd bytes/block {}], [wr blocks {} | wr bytes/block {}]".format(
                    self.data[5], self.data[6], self.data[7], self.data[8]
                )
        elif self.cc_Header == 215:
            i = 0
            str_result = "[ "
            while i < self.data[1]:
                str_result += f"{self.data[i + 4]} "
                i += 1
            return str_result + "]"
        elif self.cc_Header == 213:
            if self.device_category == self.str_cv:
                code_format = {
                    0: "Coin pos.",
                    1: "CVF",
                }
                return f"Code format {code_format[self.data[4] & 1]}"
            else:
                return "Mask [" + self.data[4][2:].rjust(8, "0") + "]"
        elif self.cc_Header == 209:
            str_result = f"Path 1 {self.data[4]}"
            if self.data[1] == 4:
                str_result += f"Path 2 {self.data[5]} Path 3 {self.data[6]} Path 4 {self.data[7]}"
            return str_result
        elif self.cc_Header == 232:
            str_result = f"fault {self.fault_code[self.data[4]]}"
            if self.data[1] == 2:
                str_result += f" info {self.extra_info[self.data[5]]}"
            return str_result
        elif self.cc_Header == 207:
            return f"Coins {self._get_int} "
        elif self.cc_Header == 204:
            return f"Meter {self._get_int} "
        elif self.cc_Header == 201:
            return f"# coins {self.data[4]} status {self.teach_status_code[self.data[5]]}"
        elif self.cc_Header == 197:
            return f"Chk 1 {self.data[4]} Chk 2 {self.data[5]} Chk 3 {self.data[6]} Chk {self.data[7]}"
        elif (self.cc_Header == 196) or (self.cc_Header == 195):
            return self._decode_date
        elif self.cc_Header == 194:
            return f"Rej. counter {self._get_int} "
        elif self.cc_Header == 193:
            return f"Fraud. counter {self._get_int} "
        elif self.cc_Header == 192:
            return f"Build {self._get_ascii}"
        elif self.cc_Header == 188:
            return f"Def. path {self.data[4]} "
        elif self.cc_Header == 186:
            return f"No. coins {self._get_int} "
        elif self.cc_Header == 184:
            i = 4
            while i < 10:
                if (self.data[i] == 123) or (self.data[i] == 125) or (self.data[i] == 91) or (self.data[i] == 93):
                    self.data[i] = 32
                i += 1
            return f"Id. {chr(self.data[4])}{chr(self.data[5])}_{chr(self.data[6])}{chr(self.data[7])}\
                    {chr(self.data[8])}_{chr(self.data[9])}"
        elif self.cc_Header == 182:
            str_result = "Calib. info "
            i = 0
            while i < self.data[1]:
                str_result += f" {self.data[4] + i}"
                i += 1
            return str_result
        elif self.cc_Header == 180:
            return f"Setting {self.data[4]} "
        elif self.cc_Header == 178:
            return f"Bank select {self.data[4]} "
        elif self.cc_Header == 176:
            return f"Alarm counter {self.data[4]}"
        elif self.cc_Header == 174:
            return f"No. coins {self._get_int} "
        elif self.cc_Header == 173:
            if (self.data[4] and 128) == 128:
                return f"Temp. -{self.data[4]} "
            else:
                return f"Temp. {self.data[4]} "
        elif self.cc_Header == 172:
            return f"Remaining {self.data[4]} "
        elif self.cc_Header == 170:
            self.base_year = int(chr(self.data[4]) + chr(self.data[5]) + chr(self.data[6]) + chr(self.data[7]))
            return f"Base year {chr(self.data[4])}{chr(self.data[5])}{chr(self.data[6])}{chr(self.data[7])}"
        elif self.cc_Header == 169:
            return "Mask [" + bin(self.data[4])[2:].rjust(8, "0") + "]"
        elif self.cc_Header == 168:
            return f"Dispensed {self._get_int} "
        elif self.cc_Header == 167:
            if (self.data[1]) == 1:
                return f"Event count. {self.data[4]}"
            else:
                return ""
        elif self.cc_Header == 166:
            return f"Events {self.data[4]} Remaining {self.data[5]} Last paid {self.data[6]} \
                     Last unpaid {self.data[7]} "
        elif self.cc_Header == 163:
            str_result = ""
            i = 0
            while i < self.data[1]:
                str_result += f"Mask {i + 1} " + "[" + bin(self.data[4 + i])[2:].rjust(8, "0") + "] "
                i += 1
            return str_result
        elif self.cc_Header == 160:
            str_result = "KEY :"
            i = 0
            while i < self.data[1]:
                str_result += f" {self.data[4 + i]}"
                i += 1
            return str_result
        elif self.cc_Header == 159:
            return self._decode_buffer_bill
        elif self.cc_Header == 157:
            return (
                    "Id . "
                    + chr(self.data[4])
                    + chr(self.data[5])
                    + "_"
                    + chr(self.data[6])
                    + chr(self.data[7])
                    + chr(self.data[8])
                    + chr(self.data[9])
                    + "_"
                    + chr(self.data[10])
            )
        elif self.cc_Header == 156:
            return f"Scaling factor {self.data[4] + (self.data[5] * 256)} decimal {self.data[6]}"
        elif self.cc_Header == 155:
            return "Mask [" + bin(self.data[5])[2:].rjust(8, "0") + "|" + bin(self.data[4])[2:].rjust(8, "0") + "]"
        elif self.cc_Header == 154:
            return self.error_code[self.data[4]]
        elif self.cc_Header == 152:
            str_result = " Stacker "
            if self.data[4] & 1:
                str_result += "used"
            else:
                str_result += "non used"
            str_result += " Escrow "
            if self.data[4] & 2:
                str_result += "used "
            else:
                str_result += "non used"
            return str_result
        elif self.cc_Header == 149:
            return " Error counter : {} ".format(self._get_int)
        elif self.cc_Header == 148:
            if self.data[1] == 1:
                return f" Opto voltages {self.data[4]}"
            else:
                return f" Opto voltages {self._get_int}"
        elif self.cc_Header == 147:
            if self.data[1] == 1:
                return f"Error {self.error_code_stacker[self.data[4]]}"
            else:
                return ""
        elif self.cc_Header == 141:
            return f"FW option {self.data[4]} "
        elif (self.cc_Header == 134) and (self.data[1] == 1):
            return f"Events {self.data[4]} "
        elif self.cc_Header == 133:
            return f"Events {self.data[4]} remain. {self.data[5] + (self.data[6] * 256)} \
                            paid {self.data[7] + (self.data[8] * 256)} unpaid {self.data[9] + (self.data[10] * 256)} "
        elif self.cc_Header == 132:
            return f"remain. {self._get_int} "
        elif (self.cc_Header == 131) or (self.cc_Header == 119):
            return "Id {:c}{:c}{:c}{:c}{:c}{:c}{}".format(self.data[4], self.data[5], self.data[6], self.data[7],
                                                          self.data[8], self.data[9],
                                                          (self.data[10] + self.data[11] * 256))
        elif self.cc_Header == 130:
            return f"Dispensed {self._get_int} "
        elif (self.cc_Header == 128) and (self.cc_Header == 127):
            return f"Total {self._get_int} "
        elif self.cc_Header == 124:
            return f"Events {self.data[4]} \
                paid {self.data[5] + (self.data[6] * 256) + (self.data[7] * 65536) + (self.data[8] * 16777216)}\
                unpaid {self.data[9] + (self.data[10] * 256) + (self.data[11] * 65536) + (self.data[12] * 16777216)}"
        elif self.cc_Header == 123:
            return "Mask [" + bin(self.data[4])[2:].rjust(8, "0") + "|" + bin(self.data[5])[2:].rjust(8, "0") + "]"
        elif self.cc_Header == 122:
            return f"Device no. {self.data[4]} fault {self.data[5]}"
        elif self.cc_Header == 117:
            return f"Value {self.get_dword} "
        elif self.cc_Header == 115:
            return str(datetime.datetime.fromtimestamp(self.data[4] + (self.data[5] * 256) + (self.data[6] * 65536) +
                                                       (self.data[7] * 16777216)))
        elif self.cc_Header == 114:
            return f"VID_{self.data[4] + (self.data[5] * 256)} PID_{self.data[6] + (self.data[7] * 256)}"
        elif (self.cc_Header == 113) and (self.data[1] == 1):
            return f"Speed {self.baud_rate_code[self.data[4]]} "
        elif self.cc_Header == 106:
            str_result = f"Op. status {self.operating_status[self.data[4]]} "
            if self.data[5] == 0:
                str_result += "empty "
            else:
                str_result += "full "
            str_result += f"fault code {self.data[6]}"
        elif self.cc_Header == 104:
            if self.data[1] == 1:
                return f"Service status {self.service_status[self.data[4]]}"
        elif self.cc_Header == 4:
            if (self.data[4]) > 47:
                return "Release {:c} v{:c}.{:c}".format(self.data[4], self.data[5], self.data[6])
            else:
                return "Release {} v{}.{}".format(self.data[4], self.data[5], self.data[6])
        elif self.cc_Header == 2:
            return f"RX : timeouts {self.data[4]}, bytes ignored {self.data[5]}, bad checksum {self.data[6]}"
        else:
            return ""

    def decode(self, frame: AnalyzerFrame):
        """
            Process a frame from the input analyzer, and optionally return a single `AnalyzerFrame`
            or a list of `AnalyzerFrame`s.

            The type and data values in `frame` will depend on the input analyzer.
        """

        if self.len_data == 0:
            self.reset_frame()

        try:
            self.data += frame.data["data"]
            self.len_data += 1

            if self.len_data == 1:
                self.start_time = frame.start_time
                # Todo MCS header
                if self.data[0] == self.device_address:  # or (self.data[0] == self.broadcast):
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

                    if (self.len_data > 4) and (self.len_data == (5 + self.data[1])):
                        self.isRequest = True
                        self.len_data = self.cc_Header = 0
                        str_header = "unknown"
                        if (self.data[3]) in self.header:
                            str_header = self.header[self.data[3]]
                            self.cc_Header = self.data[3]
                        if self.device_category == self.str_bv:
                            check_result = self._crc_16
                            check_ok = check_result == self.data[2] + (self.data[-1] * 256)
                            if (not check_ok) and (str_header == "unknown"):
                                raise
                            str_frame = ("{}({}) - # param.({}) - LSB CRC({}) - {}({}) - param." +
                                         self._get_param + self._master2slave +
                                         " - MSB CRC({}) ")
                            return AnalyzerFrame(str_frame.format(self.device_category, self.data[0], self.data[1],
                                                                  self.data[2], str_header, self.data[3],
                                                                  self.data[self.data[1] + 4]),
                                                 self.start_time, frame.end_time,
                                                 {"Checksum ": " {} : ".format(self.data[2] +
                                                                               (self.data[
                                                                                    self.data[1] + 4] * 256)) +
                                                               self.verif[check_ok]})
                        else:
                            check_result = self._checksum
                            check_ok = (check_result == self.data[-1])
                            if (not check_ok) and (str_header == "unknown"):
                                raise
                            str_frame = ("{}({}) - # param.({}) - Master({}) - {}({}) - param." +
                                         self._get_param + self._master2slave + " ")
                            return AnalyzerFrame(str_frame.format(self.device_category, self.data[0], self.data[1],
                                                                  self.data[2], str_header, self.data[3],
                                                                  check_result),
                                                 self.start_time, frame.end_time,
                                                 {"Checksum ": " {} : ".format(self.data[- 1]) +
                                                               self.verif[check_ok]})
                else:
                    if (self.len_data == 3) and (self.device_category != self.str_bv) and \
                            (self.data[2] != self.device_address):
                        raise

                    if (self.len_data > 4) and (self.len_data == (5 + self.data[1])):
                        self.len_data = 0
                        self.isRequest = False
                        if self.device_category == self.str_bv:
                            check_result = self._crc_16
                            check_ok = (check_result == self.data[2] + (self.data[self.data[1] + 4] * 256))
                            str_frame = ("Master({}) - # param.({}) - LSB CRC({}) - {}({}) - param." +
                                         self._get_param + self._slave2master +
                                         " - MSB CRC({}) ")
                            return AnalyzerFrame(str_frame.format(self.data[0], self.data[1], self.data[2],
                                                                  self.acknowledge[self.data[3]], self.data[3],
                                                                  self.data[self.data[1] + 4]),
                                                 self.start_time, frame.end_time,
                                                 {"Checksum ": " {} : ".format(self.data[2] +
                                                                               (self.data[self.data[1] + 4] * 256)) +
                                                               self.verif[check_ok]})
                        else:
                            check_result = self._checksum
                            check_ok = (check_result == self.data[- 1])
                            str_frame = ("Master({}) - # param.({}) - {}({}) - {}({}) - param." +
                                         self._get_param + self._slave2master + " ")
                            return AnalyzerFrame(str_frame.format(self.data[0], self.data[1], self.device_category,
                                                                  self.data[2],
                                                                  self.acknowledge[self.data[3]],
                                                                  self.data[3]),
                                                 self.start_time, frame.end_time,
                                                 {"Checksum ": " {} : ".format(self.data[self.len_data - 1]) +
                                                               self.verif[check_ok]}, )
        except (KeyError, RuntimeError, IndexError):
            self.reset_frame()
        return
