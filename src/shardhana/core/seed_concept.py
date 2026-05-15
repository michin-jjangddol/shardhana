"""
Shardhana HEM Core - Seed

Seed is the first observation unit of HEM.

Nature is one(HAN).
Humans cannot perceive the whole nature directly.
Humans divide nature into what can be perceived
and what cannot be perceived.

Seed is not a 1D / 2D / 3D element.
Dimension is only a simplified human view of Seed.

Seed may contain condensed matter-like behavior.
Seed may become space-like.
Space may become seed-like.
Face is the contact / transfer surface between Seed and outside world.

This file is an early draft.
It is intentionally flexible and editable.
"""


class Seed:
    """
    Flexible Seed class for early Shardhana HEM development.
    """

    def __init__(self, seed_id=None, name="seed"):
        self.id = seed_id
        self.name = name

        # 인간이 느낄 수 있는 자연
        self.human_perceivable = {
            "geometry": {
                "x": None,
                "y": None,
                "z": None,
                "length": None,
                "area": None,
                "volume": None,
                "shape": None,
            },
            "motion": {
                "displacement": None,
                "velocity": None,
                "acceleration": None,
            },
            "sense": {
                "visible": None,
                "color": None,
                "sound": None,
                "temperature_feel": None,
                "pressure_feel": None,
                "smell": None,
                "taste": None,
            },
            "surface": {
                "crack": None,
                "opening": None,
                "slip": None,
                "surface_damage": None,
            },
        }

        # 인간이 직접 느끼기 어려운 자연
        self.human_imperceivable = {
            "internal_state": {
                "strain": None,
                "stress": None,
                "damage": None,
                "temperature": None,
                "pressure": None,
                "density": None,
                "moisture": None,
            },
            "flow": {
                "stress_flow": None,
                "heat_flow": None,
                "fluid_flow": None,
                "energy_flow": None,
            },
            "potential": {
                "fracture": None,
                "localization": None,
                "instability": None,
                "growth": None,
            },
            "uncertainty": {
                "noise": None,
                "variation": None,
                "probability": {},
            },
        }

        # Seed가 외부와 만나는 면
        # Space 자체가 아니라, Seed의 접촉/전달 면
        self.face = {
            "left": {},
            "right": {},
            "top": {},
            "bottom": {},
            "front": {},
            "back": {},
        }

        # Seed와 주변의 관계
        self.relation = {
            "neighbors": [],
            "contact": {},
            "bond": {},
            "constraint": {},
        }

        # Seed를 통해 오고 가는 것
        self.transfer = {
            "force": None,
            "heat": None,
            "mass": None,
            "momentum": None,
            "information": None,
        }

        # Seed가 Space처럼 변하거나,
        # Space와 연결되는 상태를 임시로 기록
        self.space_like = {
            "void": None,
            "gap": None,
            "opening": None,
            "separation": None,
            "space_state": None,
        }

        # 개발 중 새 개념을 임시로 넣는 공간
        self.extra = {}

        # 변화 기록
        self.history = []

    def set_value(self, group, category, key, value):
        target = self._get_group(group)

        if category not in target:
            target[category] = {}

        target[category][key] = value
        self._record("set", group, category, key, value)

    def get_value(self, group, category, key, default=None):
        target = self._get_group(group)
        return target.get(category, {}).get(key, default)

    def delete_value(self, group, category, key):
        target = self._get_group(group)

        if category in target and key in target[category]:
            old_value = target[category].pop(key)
            self._record("delete", group, category, key, old_value)

    def set_extra(self, category, key, value):
        if category not in self.extra:
            self.extra[category] = {}

        self.extra[category][key] = value
        self._record("set_extra", "extra", category, key, value)

    def view_1d(self):
        """
        1D simplified view.
        1D is not Seed itself.
        It is only a human simplification.
        """

        g = self.human_perceivable["geometry"]
        m = self.human_perceivable["motion"]
        s = self.human_imperceivable["internal_state"]

        return {
            "id": self.id,
            "name": self.name,
            "x": g.get("x"),
            "length": g.get("length"),
            "area": g.get("area"),
            "displacement": m.get("displacement"),
            "velocity": m.get("velocity"),
            "strain": s.get("strain"),
            "stress": s.get("stress"),
            "damage": s.get("damage"),
            "face_left": self.face.get("left"),
            "face_right": self.face.get("right"),
        }

    def view_full(self):
        return {
            "id": self.id,
            "name": self.name,
            "human_perceivable": self.human_perceivable,
            "human_imperceivable": self.human_imperceivable,
            "face": self.face,
            "relation": self.relation,
            "transfer": self.transfer,
            "space_like": self.space_like,
            "extra": self.extra,
            "history": self.history,
        }

    def _get_group(self, group):
        if group == "perceivable":
            return self.human_perceivable

        if group == "imperceivable":
            return self.human_imperceivable

        if group == "face":
            return self.face

        if group == "relation":
            return self.relation

        if group == "transfer":
            return self.transfer

        if group == "space_like":
            return self.space_like

        if group == "extra":
            return self.extra

        raise ValueError(
            "group must be one of: "
            "perceivable, imperceivable, face, relation, "
            "transfer, space_like, extra"
        )

    def _record(self, action, group, category, key, value):
        self.history.append(
            {
                "action": action,
                "group": group,
                "category": category,
                "key": key,
                "value": value,
            }
        )


if __name__ == "__main__":
    seed = Seed(seed_id=1, name="first_seed")

    seed.set_value("perceivable", "geometry", "x", 0.0)
    seed.set_value("perceivable", "geometry", "length", 1.0)
    seed.set_value("perceivable", "geometry", "area", 0.01)

    seed.set_value("imperceivable", "internal_state", "stress", 0.0)
    seed.set_value("imperceivable", "internal_state", "damage", 0.0)

    seed.set_value("face", "left", "contact", True)
    seed.set_value("face", "right", "contact", True)

    print(seed.view_1d())