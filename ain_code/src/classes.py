import queue


class Individual:
    """
    _summary_

    Attributes:
        id (int): Bytes individual as decimal number.
        score (int): AVG of total payoff function.
        prehistory (int): Bytes prehistory as decimal number. Do not change!
    """
    id = 0
    score = 0
    prehistory = 0

    def __init__(self, id, prehistory):
        self.id = id
        self.prehistory = prehistory

    def choice(history) -> int:
        # prehistory to bytes
        # ind_history = queue.Queue()
        # ind_history = prehistory

        # for i in history:
        #     ind_history.drop(0)
        #     ind_history.append(i)

        # dec_hist = whole ind_history to decimal
        # binary_id_list = id to binary (ex. list of 0 and 1)
        # return binary_id_list(dec_hist)
        pass
