import pystache


class PystacheTest(object):
    def __init__(self, template, mapping):
        self.template = template
        self.mapping = mapping

    def run(self):
        return pystache.render(self.template, self.mapping)


class TestView(pystache.View):
    def person(self):
        return 'Peter'

    def colors(self):
        return [
            {'color': 'red'},
            {'color': 'green'},
            {'color': 'blue'},
            {'color': 'yellow'},
            {'color': 'purple'},
            {'color': 'orange'},
            {'color': 'brown'},
            {'color': 'pink'},
            ]

    def cars(self):
        def print_this(text):
            return '<b>' + str(text) + '</b>'

        return {
            'name': 'Willy',
            'wrapped': print_this('something'),
            }


if __name__ == '__main__':
    # # Without view
    # template = 'Hello, {{person}}!'
    # mapping = {
    #     'person': 'Peter',
    #     }

    # test = PystacheTest(template, mapping)
    # print test.run()

    # With view
    print TestView().render()
