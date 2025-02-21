from uuid import UUID


class GenericModel:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        return {
            k: str(v) if isinstance(v, UUID) else v
            for k, v in vars(self).items()
            if not k.startswith("_")
        }
