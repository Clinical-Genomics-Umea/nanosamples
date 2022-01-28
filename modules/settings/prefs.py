from PySide6.QtCore import QSettings
import yaml
from importlib.resources import path


class SettingsManager:
    def __init__(self):
        self.qs = QSettings("Genomic Medicine Sweden", "nanosamples")
        self.ys = None
        with path(__package__, 'settings.yaml') as prefs_path:
            with prefs_path.open("r") as fh:
                self.ys = yaml.safe_load(fh)
                print(self.ys)
                for key, value in self.ys.items():
                    if not self.qs.value(key):
                        self.qs.setValue(key, value['default_value'])

    def set_value(self, key, value):
        self.qs.setValue(key, value)

    def get_value(self, key):
        return self.qs.value(key)

    def get_settings(self):
        pref_dict = {}
        for key in self.ys:
            pref_dict[key] = {}
            pref_dict[key]['value'] = self.qs.value(key)
            pref_dict[key]['label'] = self.ys[key]['label']
            pref_dict[key]['control'] = self.ys[key]['control']

        return pref_dict




