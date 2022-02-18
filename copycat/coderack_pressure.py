import logging

from .formulas import Temperature
from .slipnet import slipnet


class CoderackPressure:
    def __init__(self, name):
        self.name = name

    def reset(self):
        self.unmodifed_values = []
        self.values = []
        self.codelets = []


def _codelet_index(codelet):
    name_indices = {
        "bottom-up-bond-scout": 0,
        "top-down-bond-scout--category": {
            slipnet.successor: 1,
            slipnet.predecessor: 2,
            None: 3,
        },
        "top-down-bond-scout--direction": {
            slipnet.left: 4,
            slipnet.right: 5,
            None: 3,
        },
        "top-down-group-scout--category": {
            slipnet.successor_group: 6,
            slipnet.predecessor_group: 7,
            None: 8,
        },
        "top-down-group-scout--direction": {
            slipnet.left: 9,
            slipnet.right: 10,
            None: -1,
        },
        "group-scout--whole-string": 11,
        "replacement-finder": 12,
        "rule-scout": 13,
        "rule-translator": 14,
        "bottom-up-correspondence-scout": 15,
        "important-object-correspondence-scout": 16,
        "breaker": 17,
    }
    name_index = name_indices.get(codelet.name, -1)
    try:
        return int(name_index)
    except (TypeError, ValueError):
        try:
            node = codelet.arguments[0]
            return name_index[node]
        except KeyError:
            return name_index[None]


class CoderackPressures:
    def __init__(self):
        self.initialise_pressures()
        self.reset()

    def initialise_pressures(self):
        self.pressures = []
        self.pressures += [CoderackPressure("Bottom Up Bonds")]
        self.pressures += [CoderackPressure("Top Down Successor Bonds")]
        self.pressures += [CoderackPressure("Top Down Predecessor Bonds")]
        self.pressures += [CoderackPressure("Top Down Sameness Bonds")]
        self.pressures += [CoderackPressure("Top Down Left Bonds")]
        self.pressures += [CoderackPressure("Top Down Right Bonds")]
        self.pressures += [CoderackPressure("Top Down Successor Group")]
        self.pressures += [CoderackPressure("Top Down Predecessor Group")]
        self.pressures += [CoderackPressure("Top Down Sameness Group")]
        self.pressures += [CoderackPressure("Top Down Left Group")]
        self.pressures += [CoderackPressure("Top Down Right Group")]
        self.pressures += [CoderackPressure("Bottom Up Whole Group")]
        self.pressures += [CoderackPressure("Replacement Finder")]
        self.pressures += [CoderackPressure("Rule Codelets")]
        self.pressures += [CoderackPressure("Rule Translator")]
        self.pressures += [CoderackPressure("Bottom Up Correspondences")]
        self.pressures += [CoderackPressure("Important Object Correspondences")]
        self.pressures += [CoderackPressure("Breakers")]

    def calculate_pressures(self):
        scale = (100.0 - Temperature + 10.0) / 15.0
        values = []
        for pressure in self.pressures:
            value = sum(_.urgency**scale for _ in pressure.codelets)
            values += [value]
        total_value = sum(values)
        if not total_value:
            total_value = 1.0
        values = [value / total_value for value in values]
        self.max_value = max(values)
        for pressure, value in zip(self.pressures, values):
            pressure.values += [value * 100.0]
        for codelet in self.removed_codelets:
            if codelet.pressure:
                codelet.pressure.codelets.remove_element(codelet)
        self.removed_codelets = []

    def reset(self):
        self.max_value = 0.001
        for pressure in self.pressures:
            pressure.reset()
        self.removed_codelets = []

    def add_codelet(self, codelet):
        node = None
        index = _codelet_index(codelet)
        if index >= 0:
            self.pressures[index].codelets += [codelet]
        if codelet.pressure:
            codelet.pressure.codelets += [codelet]
        if index >= 0:
            codelet.pressure = self.pressures[index]
        logging.info(f"Add {codelet.name}: {index}")
        if node:
            logging.info(f"Node: {node.name}")

    def remove_codelet(self, codelet):
        self.removed_codelets += [codelet]

    def number_of_pressures(self):
        return len(self.pressures)


coderack_pressures = CoderackPressures()
