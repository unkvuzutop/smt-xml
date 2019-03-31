import argparse
import logging

from lxml import etree
from six import StringIO

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
handler.setLevel(logging.INFO)
log.addHandler(handler)


class Analyser(object):
    def __init__(self, orig, other, el_id):
        self.orig = orig
        self.other = other
        self.el_id = el_id
        self.target_el = self.get_target_info(self.el_id)

    def get_row_child_element_class(self, el):
        """
        get first children from  element with class_name=row
        """
        parent = el.getparent()
        if parent is None:
            return parent
        if 'class' in parent.attrib and parent.attrib['class'] == 'row':
            return el.attrib['class']
        return self.get_row_child_element_class(el.getparent())

    def get_target_info(self, el_id):
        """
        get target element from origin file
        with all addition information for searching
        """
        log.info(f'Get info about element with ID = {el_id}')
        data = self.orig.xml.find(f".//a[@id='{el_id}']")
        data.attrib['row_child_el'] = self.get_row_child_element_class(data)

        return data

    def find_by_text(self):
        text = self.target_el.text
        row = self.other.xml.xpath(f'.//a[text()="{text}"]')
        return row

    def find_by_attr_name(self, attr, val):
        data = self.other.xml.find(f".//a[@{attr}='{val}']")
        return data

    def compare_parents(self, result):
        """
        check parents for both elements
        """
        if len(result) > 1:
            parent_class = self.target_el.attrib['row_child_el']
            for row in result:
                if parent_class == \
                        self.get_row_child_element_class(row):
                    log.info(
                        f'Found by parent block class ||==> {parent_class}')
                    return row
            return result
        return result

    def search_similar(self):
        el_class = self.target_el.attrib['class']
        el = self.find_by_attr_name('class', el_class)
        if el is not None:
            log.info(f'Found by class_name ||=>> {el_class}')
            return el
        el = self.find_by_attr_name('id', self.target_el.attrib['id'])
        if el is not None:
            log.info(f'found by id {el.attrib}', el.attrib)
            return el
        el = self.find_by_text()
        if el is not None:
            log.info(f'found by text {el}')
            return el

    def print_report(self, el):
        """
        print result to console
        """
        tree = self.other.xml
        path = tree.getpath(el)
        log.info(f'Path to founded element||=>> {path}')


class Document(object):
    def __init__(self, path):
        self.path = path
        self.data_source = self.load_source()
        self.xml = self.get_xml()

    def load_source(self):
        with open(self.path, 'r') as f:
            source = f.read()
        return source

    def get_xml(self):
        parser = etree.HTMLParser()
        xml = etree.parse(StringIO(self.data_source), parser)
        return xml

    def get_target_info(self, el_id):
        data = self.xml.find(f".//a[@id='{el_id}']")
        return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-orig',
        '--orig',
        help='Path to origin file',
        required=True)
    parser.add_argument(
        '-other',
        '--other',
        help='Path to other file',
        required=True)
    parser.add_argument(
        '-el',
        '--el',
        help='OPTIONAL : Id of the target element',
        required=False,
        default='make-everything-ok-button')
    args = vars(parser.parse_args())
    origin = Document(args['orig'])

    log.info(f'PROCESS file_name {args["other"]}')
    other = Document(args['other'])

    reporter = Analyser(origin, other, args['el'])
    result = reporter.search_similar()
    el = reporter.compare_parents(result)
    reporter.print_report(el)

    log.info('<--END-->')
