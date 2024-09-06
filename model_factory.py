
from common import const;
def create_model(model_type):
    """
    create a model_type instance
    :param model_type: bot type code
    :return: bot instance
    """

    if model_type == const.OPEN_AI:
        return 0
    elif model_type == const.QWEN_DASHSCOPE:
        return 1
