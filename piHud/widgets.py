import pygal
from pygal.style import Style
from SVGWidget import SVGWidget
from config import defaults


class Gauge(SVGWidget):
    def __init__(self, parent, command, user_config=None):
        super(Gauge, self).__init__(parent, command)
        super(Gauge, self).setFixedWidth(350)
        super(Gauge, self).setFixedHeight(400)

        default_config = defaults[command]

        self.style = Style(
            stroke_width=2.0,
            background='transparent',
            plot_background='transparent',
            foreground='#53B9E8',
            foreground_light='#53B9E8',
            foreground_dark='transparent',
            colors=('#53B9E8', '#53B9E8'))

    def render(self, response):
        """ function called by python-OBD with new data to be rendered """
        
        chart = pygal.Gauge(width=200, height=250)
        
        # styling
        chart.style = self.style
        chart.human_readable = True
        chart.show_legend = False
        chart.title = self.command.name
        chart.range = [0, 8000]

        value = 0
        if isinstance(response.value, float):
            value = response.value

        chart.add(self.command.name, value)

        self.showChart(chart)
