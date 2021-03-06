from disp_base import DisplayBase


class Large7SegDisplay(DisplayBase):

    SEG_LENGTH = 18
    SEG_WIDTH = 3
    
    COLON_SIZE = 3
    COLON_COLOR = 8

    PM_X = (SEG_LENGTH + SEG_LENGTH + 10) * 2 + 27
    PM_Y = SEG_LENGTH * 2 - 5
    
    DIGIT_OFS = [
        [0, 0],
        [SEG_LENGTH + 10, 0],
        [(SEG_LENGTH + 10) * 2 + 9, 0],
        [(SEG_LENGTH + 10) * 3 + 9, 0]
    ]

    COLON_OFS = [
        [(SEG_LENGTH + 8) * 2 + 4, int(SEG_LENGTH / 2) + 2],
        [(SEG_LENGTH + 8) * 2 + 4, SEG_LENGTH + int(SEG_LENGTH / 2)]
    ]

    SEVEN_SEGS = [
        'abcdef',  # 0
        'bc',  # 1
        'abdeg',  # 2
        'abcdg',  # 3
        'bcfg',  # 4
        'acdfg',  # 5
        'acdefg',  # 6
        'abc',  # 7
        'abcdefg',  # 8
        'abcdfg',  # 9
    ]

    def __init__(self, window):
        self._window = window
        
    def _draw_colon(self, xofs, yofs,config):
        for num in range(2):
            x = Large7SegDisplay.COLON_OFS[num][0]
            y = Large7SegDisplay.COLON_OFS[num][1]
            self._window.DrawBox(x + xofs, y + yofs, Large7SegDisplay.COLON_SIZE,
                                 Large7SegDisplay.COLON_SIZE,
                                 config['brightness'])

    def _draw_digit(self, xofs, yofs, num, value,config):

        # clockwise from top: a,b,c,d,e,f, and g in middle

        segs = Large7SegDisplay.SEVEN_SEGS[value]

        x = Large7SegDisplay.DIGIT_OFS[num][0]
        y = Large7SegDisplay.DIGIT_OFS[num][1]

        if 'a' in segs:
            self._window.DrawBox(x + xofs + 1, y + yofs + 0, Large7SegDisplay.SEG_LENGTH, Large7SegDisplay.SEG_WIDTH, config['brightness'])  # a
        if 'b' in segs:
            self._window.DrawBox(x + xofs + Large7SegDisplay.SEG_LENGTH - 1, y + yofs + 1, Large7SegDisplay.SEG_WIDTH, Large7SegDisplay.SEG_LENGTH, config['brightness'])  # b
        if 'c' in segs:
            self._window.DrawBox(x + xofs + Large7SegDisplay.SEG_LENGTH - 1, y + yofs + Large7SegDisplay.SEG_LENGTH + 2, Large7SegDisplay.SEG_WIDTH, Large7SegDisplay.SEG_LENGTH, config['brightness'])  # c
        if 'd' in segs:
            self._window.DrawBox(x + xofs + 1, y + yofs + Large7SegDisplay.SEG_LENGTH * 2, Large7SegDisplay.SEG_LENGTH, Large7SegDisplay.SEG_WIDTH, config['brightness'])  # d
        if 'e' in segs:
            self._window.DrawBox(x + xofs + 0, y + yofs + Large7SegDisplay.SEG_LENGTH + 2, Large7SegDisplay.SEG_WIDTH, Large7SegDisplay.SEG_LENGTH, config['brightness'])  # e
        if 'f' in segs:
            self._window.DrawBox(x + xofs + 0, y + yofs + 1, Large7SegDisplay.SEG_WIDTH, Large7SegDisplay.SEG_LENGTH, config['brightness'])  # f
        if 'g' in segs:
            self._window.DrawBox(x + xofs + 1, y + yofs + Large7SegDisplay.SEG_LENGTH, Large7SegDisplay.SEG_LENGTH, Large7SegDisplay.SEG_WIDTH, config['brightness'])  # g

    def get_window_size(self):
        return (132, 40)

    def make_time(self, xofs, yofs, hours, minutes, _seconds, config):

        self._draw_colon(xofs, yofs,config)
                        
        if config['am_pm']:
            pm = (hours>=12)
            if hours > 12:
                hours = hours - 12                

        hours_a = int(hours / 10)
        hours_b = int(hours % 10)
        mins_a = int(minutes / 10)
        mins_b = int(minutes % 10)

        if config['am_pm']:
            if pm:
                self._window.draw_text(Large7SegDisplay.PM_X + xofs, Large7SegDisplay.PM_Y + yofs, 'PM', config['brightness'])
            if hours_a > 0:
                self._draw_digit(xofs, yofs, 0, hours_a,config)
        else:
            self._draw_digit(xofs, yofs, 0, hours_a,config)

        self._draw_digit(xofs, yofs, 1, hours_b,config)
        self._draw_digit(xofs, yofs, 2, mins_a,config)
        self._draw_digit(xofs, yofs, 3, mins_b,config)
