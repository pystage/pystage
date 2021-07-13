import importlib
import inspect
import dis

def get_translated_function(corefunc, language, stage=False):
    """Get translated API function for a core function name.

    Use the function metadata to determine the correct translated API
    function based on a given core function name.

    Parameters
    ----------
    corefunc : str
        A core function name, i.e. a method from CoreSprite or CoreStage
    language : str
        The language of the target API
    stage : bool
        True, if the stage API is to be used, otherwise defaults to sprite.
    """
    if language=="core":
        return corefunc
    lang = importlib.import_module(f"pystage.{language}")
    cls = lang.stage_class if stage else lang.sprite_class
    for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
        for i in dis.Bytecode(func):
            if (i.opname=="LOAD_METHOD" or i.opname=="LOAD_ATTR") and i.argval==corefunc:
                # print(f"Translated: {name}")
                return name
    # print(f"No translated API method found for {corefunc}")
    return None


def get_core_function(translated, language, stage=False):
    """Get core API function for a translated function name.

    Use the function metadata to determine the correct translated API
    function based on a given core function name.

    Parameters
    ----------
    translated : str
        A translated function name, i.e. a method from a sprite or stage class
    language : str
        The language of the source API
    stage : bool
        True, if the stage API is to be used, otherwise defaults to sprite.
    """
    if language=="core":
        return translated
    lang = importlib.import_module(f"pystage.{language}")
    cls = lang.stage_class if stage else lang.sprite_class
    for name, func in inspect.getmembers(cls, predicate=inspect.isfunction):
        for i in dis.Bytecode(func):
            if (i.opname=="LOAD_METHOD" or i.opname=="LOAD_ATTR") and name==translated:
                # print(f"Translated: {name}")
                # TODO: This is most likely not sufficient...
                return i.argval
    # print(f"No core API method found for {name}")
    return None

