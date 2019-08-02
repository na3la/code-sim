from driveropen import create_token_dict


def _dict_builder():
    uuid_list, obj_matrix = [], []
    return dict(create_token_dict(uuid_list, obj_matrix))


if __name__ == "__main__":
    _dict_builder()
