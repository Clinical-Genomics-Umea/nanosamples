import yaml
from importlib.resources import path
import xml.etree.ElementTree as ET
from pathlib import Path


class PlateSvg:
    def __init__(self):
        self.type2color = {
            'pos_ctrl': '#99ff99',
            'neg_ctrl': '#ff99ff',
            'sample': '#ffffff',
            'unused': '#dcdcdcff'
        }
        self.ns = {'': 'http://www.w3.org/2000/svg'}

        with path(__package__, '96-plate-template2.svg') as svg_path:
            self.tree = ET.parse(svg_path)
            self.root = self.tree.getroot()

        with path(__package__, 'config.yaml') as conf_path:
            with conf_path.open("r") as fh:
                self.config = yaml.safe_load(fh)

        coord_list = self.config['pos2coord'].values()
        self._remove_coord_texts(coord_list)

    def get_svg(self):
        return ET.tostring(self.root, encoding='unicode', method='xml')

    def _remove_coord_texts(self, coord_list):
        if all([self.root, coord_list]):
            text_id_list = ["text_" + coord for coord in coord_list]
            for t_element in self.root[2].findall('text', self.ns):
                tid = t_element.get('id')
                if tid in text_id_list:
                    t_element[0].text = ''

    def _set_coord_texts(self, coord2text: dict):
        if self.root:
            for t_element in self.root[2].findall('text', self.ns):
                tid = t_element.get('id')
                if tid in coord2text:
                    t_element[0].text = coord2text[tid]

    def _set_coord_colors(self, coord2col: dict):
        if self.root:
            for r_element in self.root[2].findall('rect', self.ns):
                rid = r_element.get('id')
                if rid in coord2col:
                    style = r_element.get('style')
                    style_dict = dict(item.split(":") for item in style.split(";"))
                    style_dict['fill'] = coord2col[rid]
                    style_dict['font-size'] = '6px'
                    new_style = ";".join([f"{k}:{v}" for k, v in style_dict.items()])
                    r_element.set('style', new_style)

    def set_props(self, proplist: list):
        """

        :param input: list of dicts, e.g. [{'position': '1', 'text': 'POSITIVE-1'}]
        :return: [{'position': '1', 'text': 'POSITIVE-1', 'coord': 'a1', 'color': '#99ff99'}]
        """
        for p in proplist:
            p['coord'] = self.config['pos2coord'][str(p['position'])]  # add coordinate
            p['color'] = self.color_from_text(p['text'])  # add color

        self._set_svg_values(proplist)

    def color_from_text(self, text):
        if "POSITIVE" in text:
            return self.type2color['pos_ctrl']
        elif "NEGATIVE" in text:
            return self.type2color['neg_ctrl']
        elif len(text) > 0:
            return self.type2color['sample']

        return self.type2color['unused']

    def _set_svg_values(self, propslist):
        """

        :param propslist: list of dicts, e.g. [{'coord': 'a1', 'color': '#99ff99', 'text': 'pos-ctrl-1'}]
        :return: None
        """

        coord2text = {'text_'+d['coord']: d['text'] for d in propslist}
        coord2col = {'rect_' + d['coord']: d['color'] for d in propslist}

        self._set_coord_colors(coord2col)
        self._set_coord_texts(coord2text)


    # def set_props(self, propslist):
    #     def _coord_texts(self, coord_list):
    #         if all([self.root, coord_list]):
    #             text_id_list = ["text_" + coord for coord in coord_list]
    #             for t_element in self.root[2].findall('text', self.ns):
    #                 tid = t_element.get('id')
    #                 if tid in text_id_list:
    #                     t_element[0].text = ''
    #
    #
    # def set_well_props(self, coord=None, text=None, well_color=None):
    #     if all([self.root, coord, well_color]):
    #         text_id = "text_" + coord
    #         rect_id = "rect_" + coord
    #
    #         for t_element in self.root[2].findall('text', self.ns):
    #             tid = t_element.get('id')
    #             if tid == text_id:
    #                 t_element[0].text = text
    #                 break
    #
    #         for r_element in self.root[2].findall('rect', self.ns):
    #             rid = r_element.get('id')
    #             if rid == rect_id:
    #                 style = r_element.get('style')
    #                 style_dict = dict(item.split(":") for item in style.split(";"))
    #                 style_dict['fill'] = self.type2color[well_color]
    #                 style_dict['font-size'] = '6px'
    #                 new_style = ";".join([f"{k}:{v}" for k, v in style_dict.items()])
    #                 r_element.set('style', new_style)
    #                 break
